"""
GINR Feasibility Screening — Model Pipeline (Enterprise Grade)
==============================================================
Responsibilities:
  1. Load & validate training data
  2. Train logistic regression model
  3. Evaluate and log metrics
  4. Save versioned model artifact to ./models/
  5. Detect model drift from prediction logs
  6. Retrain trigger when new labeled data arrives

Usage:
    python ginr_model_pipeline.py --action train
    python ginr_model_pipeline.py --action evaluate
    python ginr_model_pipeline.py --action retrain --new-data new_labels.csv
"""

import os
import json
import argparse
import logging
import warnings
import datetime
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, precision_recall_curve, average_precision_score
)

# ─────────────────────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────────────────────

BASE_DIR        = Path(__file__).parent
MODELS_DIR      = BASE_DIR / "models"
TRAINING_DATA   = BASE_DIR / "ginr_feasibility_training_data.csv"
PRED_LOG        = BASE_DIR / "prediction_log.csv"
METRICS_LOG     = BASE_DIR / "model_metrics_history.json"

MODELS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
LOG = logging.getLogger("GINRModelPipeline")

# ─────────────────────────────────────────────────────────────────────────────
# Feature Groups  (mapped from GINR/RARF codebase entities)
# ─────────────────────────────────────────────────────────────────────────────

NUMERIC_FEATURES = [
    "project_mw",                # GinrRequest.maxGenMw          → log1p
    "poi_voltage_kv",            # GinrRequest.poiVoltage
    "nameplate_to_maxgen_ratio", # maxNameplateMwGen / maxGenMw
    "months_to_cod",             # commercialOperationDate - submitDate
    "resubmission_count",        # GinrRequest.returnedToIe
    "thermal_margin_mw",         # MostLimitingSeriesElements.ratingNormal → log1p
]

BINARY_FEATURES = [
    "crez_flag",                    # Derived: county / lat / lon
    "fis_fee_paid",                 # GinrRequest.fisFeePaid
    "ss_fee_paid",                  # GinrRequest.ssFeePaid
    "payment_made_flag",            # GinrPaymentDataVw.datePaid IS NOT NULL
    "missing_poib_flag",            # POIB_DATA count = 0 via INR_REFERENCE
    "poi_voltage_mismatch_flag",    # POIB_DATA.VOLTAGE != GinrRequest.poiVoltage
    "duplicate_substation_flag",    # duplicate POIB_DATA.POIB_SUBSTATION_ID
    "null_connectivity_node_flag",  # CONNECTIVITY_NODES count = 0
    "orphan_node_flag",             # CONNECTIVITY_NODES with 0 terminals
    "project_exceeds_thermal_flag", # project_mw > thermal_margin_mw
]

CATEGORICAL_FEATURES = [
    "resource_type",  # GinrRequest.idTechnologyType
    "inr_type",       # GinrRequest.idInrType
    "lead_tdsp",      # GinrRequest.idLeadTdsp
    "cmz_name",       # CongestionManagementZones.name
]

LABEL_COL = "feasibility_pass"
ID_COLS   = ["ginr_request_id", "inr_id"]

# ─────────────────────────────────────────────────────────────────────────────
# Feature Engineering
# ─────────────────────────────────────────────────────────────────────────────

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Apply transformations consistent with training-time feature engineering."""
    df = df.copy()
    # Log-transform right-skewed numerics
    df["project_mw"]        = np.log1p(df["project_mw"])
    df["thermal_margin_mw"] = np.log1p(df["thermal_margin_mw"].fillna(0))
    return df


# ─────────────────────────────────────────────────────────────────────────────
# Build sklearn Pipeline
# ─────────────────────────────────────────────────────────────────────────────

def build_model_pipeline() -> Pipeline:
    numeric_transformer = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale",  StandardScaler()),
    ])
    binary_transformer = Pipeline([
        ("impute", SimpleImputer(strategy="constant", fill_value=0)),
    ])
    categorical_transformer = Pipeline([
        ("impute", SimpleImputer(strategy="constant", fill_value="UNKNOWN")),
        ("ohe",    OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])
    preprocessor = ColumnTransformer([
        ("num", numeric_transformer,     NUMERIC_FEATURES),
        ("bin", binary_transformer,      BINARY_FEATURES),
        ("cat", categorical_transformer, CATEGORICAL_FEATURES),
    ])
    return Pipeline([
        ("prep", preprocessor),
        ("clf",  LogisticRegression(
                     class_weight="balanced",
                     C=1.0,
                     solver="lbfgs",
                     max_iter=1000,
                     random_state=42
                 ))
    ])


# ─────────────────────────────────────────────────────────────────────────────
# Model Versioning
# ─────────────────────────────────────────────────────────────────────────────

def next_version() -> str:
    """Determine next semantic version based on existing model files."""
    existing = sorted(MODELS_DIR.glob("ginr_model_v*.joblib"))
    if not existing:
        return "1.0"
    last = existing[-1].stem.split("_v")[-1]
    major, minor = last.split(".")
    return f"{major}.{int(minor)+1}"


def save_model(pipeline: Pipeline, version: str, metrics: dict) -> Path:
    """Save model + metadata. Also update 'latest' symlink equivalent."""
    model_path    = MODELS_DIR / f"ginr_model_v{version}.joblib"
    metadata_path = MODELS_DIR / f"ginr_model_v{version}_metadata.json"

    joblib.dump(pipeline, model_path, compress=3)

    metadata = {
        "version":           version,
        "trained_at":        datetime.datetime.now().isoformat(),
        "roc_auc":           metrics.get("roc_auc"),
        "cv_auc_mean":       metrics.get("cv_auc_mean"),
        "cv_auc_std":        metrics.get("cv_auc_std"),
        "train_rows":        metrics.get("train_rows"),
        "feature_groups": {
            "numeric":     NUMERIC_FEATURES,
            "binary":      BINARY_FEATURES,
            "categorical": CATEGORICAL_FEATURES,
        },
        "label_distribution": metrics.get("label_distribution"),
        "status": "active"
    }
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

    # Write pointer to latest model
    latest_ptr = MODELS_DIR / "latest.json"
    with open(latest_ptr, "w") as f:
        json.dump({"version": version, "path": str(model_path)}, f, indent=2)

    LOG.info(f"✅ Model saved: {model_path}")
    LOG.info(f"   Metadata  : {metadata_path}")
    return model_path


def load_latest_model() -> tuple[Pipeline, dict]:
    """Load the most recently trained model from the registry."""
    latest_ptr = MODELS_DIR / "latest.json"
    if not latest_ptr.exists():
        raise FileNotFoundError("No trained model found. Run: python ginr_model_pipeline.py --action train")
    with open(latest_ptr) as f:
        info = json.load(f)
    model_path    = Path(info["path"])
    metadata_path = model_path.with_suffix("").parent / (model_path.stem + "_metadata.json")
    pipeline  = joblib.load(model_path)
    with open(metadata_path) as f:
        metadata = json.load(f)
    LOG.info(f"✅ Loaded model v{info['version']} from {model_path}")
    return pipeline, metadata


# ─────────────────────────────────────────────────────────────────────────────
# Training
# ─────────────────────────────────────────────────────────────────────────────

def train(data_path: Path = TRAINING_DATA) -> dict:
    LOG.info(f"Loading training data from: {data_path}")
    df = pd.read_csv(data_path)
    LOG.info(f"Loaded {len(df)} rows | Label distribution: {df[LABEL_COL].value_counts().to_dict()}")

    df = engineer_features(df)

    X = df[NUMERIC_FEATURES + BINARY_FEATURES + CATEGORICAL_FEATURES]
    y = df[LABEL_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    pipeline = build_model_pipeline()
    pipeline.fit(X_train, y_train)

    # Evaluation
    y_pred      = pipeline.predict(X_test)
    y_pred_prob = pipeline.predict_proba(X_test)[:, 1]
    roc_auc     = roc_auc_score(y_test, y_pred_prob)
    avg_prec    = average_precision_score(y_test, y_pred_prob)

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(pipeline, X, y, cv=cv, scoring="roc_auc")

    metrics = {
        "roc_auc":            round(roc_auc, 4),
        "avg_precision":      round(avg_prec, 4),
        "cv_auc_mean":        round(cv_scores.mean(), 4),
        "cv_auc_std":         round(cv_scores.std(), 4),
        "train_rows":         len(X_train),
        "test_rows":          len(X_test),
        "label_distribution": df[LABEL_COL].value_counts().to_dict(),
    }

    LOG.info(f"  ROC-AUC       : {metrics['roc_auc']}")
    LOG.info(f"  Avg Precision : {metrics['avg_precision']}")
    LOG.info(f"  5-Fold CV AUC : {metrics['cv_auc_mean']} ± {metrics['cv_auc_std']}")
    LOG.info(f"\n{classification_report(y_test, y_pred, target_names=['FAIL','PASS'])}")

    # Feature importance
    ohe_names = (pipeline.named_steps["prep"]
                         .named_transformers_["cat"]
                         .named_steps["ohe"]
                         .get_feature_names_out(CATEGORICAL_FEATURES).tolist())
    all_names = NUMERIC_FEATURES + BINARY_FEATURES + ohe_names
    coef_df   = pd.DataFrame({"feature": all_names, "coef": pipeline.named_steps["clf"].coef_[0]})
    coef_df   = coef_df.reindex(coef_df["coef"].abs().sort_values(ascending=False).index)

    LOG.info("\n📊 Top 10 Most Important Features:")
    for _, row in coef_df.head(10).iterrows():
        direction = "→ PASS +" if row["coef"] > 0 else "→ FAIL -"
        LOG.info(f"   {direction}  {row['feature']:40s}  coef={row['coef']:+.4f}")

    version    = next_version()
    model_path = save_model(pipeline, version, metrics)

    # Append to metrics history
    history_entry = {"version": version, "trained_at": datetime.datetime.now().isoformat(), **metrics}
    history = []
    if METRICS_LOG.exists():
        with open(METRICS_LOG) as f:
            history = json.load(f)
    history.append(history_entry)
    with open(METRICS_LOG, "w") as f:
        json.dump(history, f, indent=2)

    LOG.info(f"🏁 Training complete. Model version: {version}")
    return {"version": version, "model_path": str(model_path), **metrics}


# ─────────────────────────────────────────────────────────────────────────────
# Prediction (single record)
# ─────────────────────────────────────────────────────────────────────────────

RISK_THRESHOLDS = [
    (0.85, "LOW",      "🟢", "Proceed to study queue"),
    (0.60, "MEDIUM",   "🟡", "Planner review recommended"),
    (0.40, "HIGH",     "🟠", "Developer notified of specific gaps"),
    (0.00, "CRITICAL", "🔴", "Likely SENT_BACK — auto-flag for triage"),
]


def classify_risk(prob: float) -> dict:
    for threshold, level, icon, action in RISK_THRESHOLDS:
        if prob >= threshold:
            return {"level": level, "icon": icon, "action": action}
    return {"level": "CRITICAL", "icon": "🔴", "action": "Flag for triage"}


def explain_top_risks(row: dict, pipeline: Pipeline) -> list[str]:
    """Return top risk factors from the coefficient × feature value signal."""
    ohe_names = (pipeline.named_steps["prep"]
                         .named_transformers_["cat"]
                         .named_steps["ohe"]
                         .get_feature_names_out(CATEGORICAL_FEATURES).tolist())
    all_names = NUMERIC_FEATURES + BINARY_FEATURES + ohe_names
    coefs     = pipeline.named_steps["clf"].coef_[0]

    # Build risk signals: negative coef × positive binary flag = risk
    risks = []
    for name, coef in zip(all_names, coefs):
        if coef < -0.4:  # meaningful negative coefficient = fail driver
            # Map back to original feature name
            base = name.split("_")[0] if "__" not in name else name
            risks.append((abs(coef), name))
    risks.sort(reverse=True)
    return [r[1] for r in risks[:5]]


def predict_single(features: dict, pipeline: Pipeline, metadata: dict) -> dict:
    """Score a single GINR record. Input features match CSV column names."""
    df = pd.DataFrame([features])
    df = engineer_features(df)
    X  = df[NUMERIC_FEATURES + BINARY_FEATURES + CATEGORICAL_FEATURES]

    pass_prob = float(pipeline.predict_proba(X)[0][1])
    risk      = classify_risk(pass_prob)
    top_risks = explain_top_risks(features, pipeline)

    result = {
        "ginr_request_id":  features.get("ginr_request_id"),
        "inr_id":           features.get("inr_id"),
        "pass_probability": round(pass_prob, 4),
        "predicted_label":  "PASS" if pass_prob >= 0.5 else "FAIL",
        "risk_level":       risk["level"],
        "risk_icon":        risk["icon"],
        "action":           risk["action"],
        "top_risk_factors": top_risks,
        "model_version":    metadata.get("version"),
        "scored_at":        datetime.datetime.now().isoformat(),
    }

    # Append to prediction log (audit trail)
    log_row = {**features, **result}
    log_df  = pd.DataFrame([log_row])
    write_header = not PRED_LOG.exists()
    log_df.to_csv(PRED_LOG, mode="a", header=write_header, index=False)

    return result


# ─────────────────────────────────────────────────────────────────────────────
# Batch Prediction (new CSV)
# ─────────────────────────────────────────────────────────────────────────────

def predict_batch(input_csv: Path) -> pd.DataFrame:
    LOG.info(f"Batch scoring: {input_csv}")
    pipeline, metadata = load_latest_model()
    df = pd.read_csv(input_csv)
    results = []
    for _, row in df.iterrows():
        result = predict_single(row.to_dict(), pipeline, metadata)
        results.append(result)
    results_df = pd.DataFrame(results)
    output_path = input_csv.parent / (input_csv.stem + "_scored.csv")
    results_df.to_csv(output_path, index=False)
    LOG.info(f"✅ Batch results saved: {output_path}")
    return results_df


# ─────────────────────────────────────────────────────────────────────────────
# Drift Detection
# ─────────────────────────────────────────────────────────────────────────────

def check_drift() -> dict:
    """
    Compare recent prediction distribution to training distribution.
    Alert if FAIL rate in last 50 predictions deviates > 15% from baseline.
    """
    if not PRED_LOG.exists() or not METRICS_LOG.exists():
        return {"status": "insufficient_data"}

    pred_log = pd.read_csv(PRED_LOG)
    if len(pred_log) < 20:
        return {"status": "insufficient_data", "rows": len(pred_log)}

    recent = pred_log.tail(50)
    recent_fail_rate = (recent["predicted_label"] == "FAIL").mean()

    with open(METRICS_LOG) as f:
        history = json.load(f)
    latest = history[-1]
    label_dist = latest.get("label_distribution", {})
    total = sum(label_dist.values())
    baseline_fail_rate = label_dist.get(0, 0) / total if total > 0 else 0.40

    drift    = abs(recent_fail_rate - baseline_fail_rate)
    drifted  = drift > 0.15

    result = {
        "status":              "DRIFT_DETECTED" if drifted else "OK",
        "recent_fail_rate":    round(recent_fail_rate, 3),
        "baseline_fail_rate":  round(baseline_fail_rate, 3),
        "drift_magnitude":     round(drift, 3),
        "sample_size":         len(recent),
        "recommendation":      "Retrain model with recent labeled data" if drifted else "No action needed"
    }
    LOG.info(f"📈 Drift check: {result['status']}  (recent={recent_fail_rate:.1%}  baseline={baseline_fail_rate:.1%})")
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Retrain with new labeled data (feedback loop)
# ─────────────────────────────────────────────────────────────────────────────

def retrain_with_feedback(new_data_path: Path) -> dict:
    """
    Append new labeled rows (from Oracle: CR status transitions → labels)
    to training data, then retrain.
    """
    LOG.info(f"Loading new labeled data: {new_data_path}")
    existing = pd.read_csv(TRAINING_DATA)
    new_data = pd.read_csv(new_data_path)

    required_cols = NUMERIC_FEATURES + BINARY_FEATURES + CATEGORICAL_FEATURES + [LABEL_COL]
    missing = [c for c in required_cols if c not in new_data.columns]
    if missing:
        raise ValueError(f"New data missing required columns: {missing}")

    combined = pd.concat([existing, new_data], ignore_index=True).drop_duplicates()
    combined.to_csv(TRAINING_DATA, index=False)
    LOG.info(f"Training data updated: {len(existing)} → {len(combined)} rows (+{len(new_data)} new)")

    return train(TRAINING_DATA)


# ─────────────────────────────────────────────────────────────────────────────
# CLI Entry Point
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="GINR Feasibility Model Pipeline")
    parser.add_argument("--action", choices=["train", "evaluate", "score", "batch", "drift", "retrain"],
                        default="train", help="Pipeline action")
    parser.add_argument("--input",  type=str, help="Input CSV for batch scoring or retrain")
    parser.add_argument("--ginr-id", type=int, help="GINR request ID for single score")
    args = parser.parse_args()

    print("=" * 65)
    print(f"GINR ML PIPELINE  |  Action: {args.action.upper()}")
    print("=" * 65)

    if args.action == "train":
        train()

    elif args.action == "evaluate":
        pipeline, metadata = load_latest_model()
        LOG.info(f"Model v{metadata['version']} — ROC-AUC: {metadata['roc_auc']}  "
                 f"CV: {metadata['cv_auc_mean']} ± {metadata['cv_auc_std']}")

    elif args.action == "score":
        pipeline, metadata = load_latest_model()
        # Example: score a sample GINR (replace with real feature extraction from Oracle)
        sample = {
            "ginr_request_id": args.ginr_id or 9999,
            "inr_id": f"INR26-{args.ginr_id or 9999:04d}",
            "resource_type": "SOLAR",  "project_mw": 250,
            "poi_voltage_kv": 345,     "inr_type": "SS",
            "nameplate_to_maxgen_ratio": 1.10, "lead_tdsp": "ONCOR",
            "crez_flag": 0,            "months_to_cod": 40,
            "resubmission_count": 0,
            "fis_fee_paid": 1,         "ss_fee_paid": 1,   "payment_made_flag": 1,
            "missing_poib_flag": 0,    "poi_voltage_mismatch_flag": 0,
            "duplicate_substation_flag": 0, "null_connectivity_node_flag": 0,
            "orphan_node_flag": 0,
            "thermal_margin_mw": 400,
            "project_exceeds_thermal_flag": 0, "cmz_name": "LZ_NORTH"
        }
        result = predict_single(sample, pipeline, metadata)
        print(json.dumps(result, indent=2))

    elif args.action == "batch":
        if not args.input:
            parser.error("--input required for batch action")
        predict_batch(Path(args.input))

    elif args.action == "drift":
        result = check_drift()
        print(json.dumps(result, indent=2))

    elif args.action == "retrain":
        if not args.input:
            parser.error("--input required for retrain action")
        retrain_with_feedback(Path(args.input))


if __name__ == "__main__":
    main()
