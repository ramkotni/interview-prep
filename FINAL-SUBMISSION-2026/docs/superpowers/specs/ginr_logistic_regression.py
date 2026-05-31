"""
GINR Feasibility Screening — Logistic Regression Model
=======================================================
Trains and evaluates a logistic regression model on the synthetic dataset.
Load the CSV, preprocess, train, evaluate, and explain predictions.

Usage:
    python ginr_logistic_regression.py

Requirements:
    pip install pandas scikit-learn shap matplotlib
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# ─────────────────────────────────────────────
# 1. Load Data
# ─────────────────────────────────────────────

df = pd.read_csv("ginr_feasibility_training_data.csv")

print("=" * 65)
print("GINR FEASIBILITY SCREENING — LOGISTIC REGRESSION")
print("=" * 65)
print(f"\n📄 Dataset: {len(df)} rows, {len(df.columns)} columns")
print(f"   PASS (1): {df['feasibility_pass'].sum()} rows")
print(f"   FAIL (0): {(df['feasibility_pass']==0).sum()} rows")
print()

# ─────────────────────────────────────────────
# 2. Feature / Label Split
# ─────────────────────────────────────────────

# Drop identifiers (not predictive)
DROP_COLS = ["ginr_request_id", "inr_id", "feasibility_pass"]

X = df.drop(columns=DROP_COLS)
y = df["feasibility_pass"]

# ─────────────────────────────────────────────
# 3. Feature Groups
#    (match exactly to GINR/RARF codebase fields)
# ─────────────────────────────────────────────

# Continuous numeric — apply log-transform + StandardScaler
NUMERIC_FEATURES = [
    "project_mw",               # MAX_GEN_MW         → log-scaled
    "poi_voltage_kv",           # POI_VOLTAGE
    "nameplate_to_maxgen_ratio",# MAX_NAMEPLATE_MW_GEN / MAX_GEN_MW
    "months_to_cod",            # COMMERCIAL_OPERATION_DATE - SUBMIT_DATE
    "resubmission_count",       # RETURNED_TO_IE
    "thermal_margin_mw",        # MIN(MOST_LIMITING_SERIES_ELEMENTS.RATING_NORMAL)
]

# Binary flags — fill missing with 0, no scaling
BINARY_FEATURES = [
    "crez_flag",                    # Derived: COUNTY/LATITUDE/LONGITUDE
    "fis_fee_paid",                 # FIS_FEE_PAID
    "ss_fee_paid",                  # SS_FEE_PAID
    "payment_made_flag",            # GINR_PAYMENT_DATA_VW.DATE_PAID IS NOT NULL
    "missing_poib_flag",            # COUNT(POIB_DATA via INR_REFERENCE) = 0
    "poi_voltage_mismatch_flag",    # POIB_DATA.VOLTAGE != ginr.POI_VOLTAGE
    "duplicate_substation_flag",    # duplicate POIB_SUBSTATION_ID
    "null_connectivity_node_flag",  # COUNT(CONNECTIVITY_NODES) = 0
    "orphan_node_flag",             # CONNECTIVITY_NODES with 0 CONNECTIVITY_TERMINALS
    "project_exceeds_thermal_flag", # project_mw > thermal_margin_mw
]

# Categorical — OneHotEncoder
CATEGORICAL_FEATURES = [
    "resource_type",  # ID_TECHNOLOGY_TYPE
    "inr_type",       # ID_INR_TYPE
    "lead_tdsp",      # ID_LEAD_TDSP
    "cmz_name",       # CONGESTION_MANAGEMENT_ZONES.NAME
]

print("📋 Feature Summary:")
print(f"   Numeric    : {len(NUMERIC_FEATURES)} features")
print(f"   Binary     : {len(BINARY_FEATURES)} features")
print(f"   Categorical: {len(CATEGORICAL_FEATURES)} features  (will expand via OHE)")
print()

# ─────────────────────────────────────────────
# 4. Log-transform skewed numeric features
# ─────────────────────────────────────────────

# project_mw ranges 10–2000, highly right-skewed — log1p compresses it
X = X.copy()
X["project_mw"]        = np.log1p(X["project_mw"])
X["thermal_margin_mw"] = np.log1p(X["thermal_margin_mw"])

# ─────────────────────────────────────────────
# 5. Preprocessing Pipeline
# ─────────────────────────────────────────────

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
    ("num", numeric_transformer,         NUMERIC_FEATURES),
    ("bin", binary_transformer,          BINARY_FEATURES),
    ("cat", categorical_transformer,     CATEGORICAL_FEATURES),
])

# ─────────────────────────────────────────────
# 6. Full Model Pipeline
# ─────────────────────────────────────────────

model = Pipeline([
    ("prep", preprocessor),
    ("clf",  LogisticRegression(
                 class_weight="balanced",  # handles 60/40 imbalance
                 C=1.0,
                 solver="lbfgs",
                 max_iter=1000,
                 random_state=42
             ))
])

# ─────────────────────────────────────────────
# 7. Train / Test Split (80/20)
# ─────────────────────────────────────────────

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"🔀 Train/Test Split: {len(X_train)} train / {len(X_test)} test")
print()

# ─────────────────────────────────────────────
# 8. Train
# ─────────────────────────────────────────────

model.fit(X_train, y_train)
print("✅ Model trained successfully\n")

# ─────────────────────────────────────────────
# 9. Evaluate
# ─────────────────────────────────────────────

y_pred      = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]

print("=" * 65)
print("MODEL EVALUATION")
print("=" * 65)

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=["FAIL (0)", "PASS (1)"]))

auc = roc_auc_score(y_test, y_pred_prob)
print(f"🎯 ROC-AUC Score: {auc:.4f}")

# Cross-validation AUC (5-fold)
cv_scores = cross_val_score(model, X, y, cv=5, scoring="roc_auc")
print(f"📈 5-Fold CV AUC:  {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

print("\n📊 Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"               Predicted FAIL  Predicted PASS")
print(f"  Actual FAIL       {cm[0,0]:5d}          {cm[0,1]:5d}")
print(f"  Actual PASS       {cm[1,0]:5d}          {cm[1,1]:5d}")

# ─────────────────────────────────────────────
# 10. Feature Importance (Logistic Regression Coefficients)
# ─────────────────────────────────────────────

print("\n" + "=" * 65)
print("FEATURE IMPORTANCE — Logistic Regression Coefficients")
print("(Positive = increases PASS probability, Negative = increases FAIL)")
print("=" * 65)

# Get feature names after OHE expansion
ohe_feature_names = (
    model.named_steps["prep"]
        .named_transformers_["cat"]
        .named_steps["ohe"]
        .get_feature_names_out(CATEGORICAL_FEATURES)
    .tolist()
)

all_feature_names = NUMERIC_FEATURES + BINARY_FEATURES + ohe_feature_names
coefficients      = model.named_steps["clf"].coef_[0]

coef_df = pd.DataFrame({
    "feature":     all_feature_names,
    "coefficient": coefficients
}).sort_values("coefficient", ascending=False)

print("\n🔼 Top 10 Features → INCREASE Pass Probability:")
print(coef_df.head(10).to_string(index=False))

print("\n🔽 Top 10 Features → INCREASE Fail Probability:")
print(coef_df.tail(10).sort_values("coefficient").to_string(index=False))

# ─────────────────────────────────────────────
# 11. Predict on New Scenarios
# ─────────────────────────────────────────────

print("\n" + "=" * 65)
print("REAL-TIME PREDICTION — Example Scenarios")
print("=" * 65)

scenarios = [
    {
        "scenario": "✅ SCENARIO A — Clean 200 MW Solar, 345kV, paid fees, good RARF",
        "resource_type": "SOLAR",     "project_mw": np.log1p(200),
        "poi_voltage_kv": 345,        "inr_type": "SS",
        "nameplate_to_maxgen_ratio": 1.10,  "lead_tdsp": "CENTERPOINT",
        "crez_flag": 0,               "months_to_cod": 42,
        "resubmission_count": 0,
        "fis_fee_paid": 1,            "ss_fee_paid": 1,    "payment_made_flag": 1,
        "missing_poib_flag": 0,       "poi_voltage_mismatch_flag": 0,
        "duplicate_substation_flag": 0, "null_connectivity_node_flag": 0,
        "orphan_node_flag": 0,
        "thermal_margin_mw": np.log1p(450),
        "project_exceeds_thermal_flag": 0,  "cmz_name": "LZ_NORTH"
    },
    {
        "scenario": "❌ SCENARIO B — 800 MW Wind in CREZ, exceeds thermal margin, 3 prior returns",
        "resource_type": "WIND",       "project_mw": np.log1p(800),
        "poi_voltage_kv": 138,         "inr_type": "FIS",
        "nameplate_to_maxgen_ratio": 1.40,  "lead_tdsp": "ONCOR",
        "crez_flag": 1,                "months_to_cod": 18,
        "resubmission_count": 3,
        "fis_fee_paid": 1,             "ss_fee_paid": 1,   "payment_made_flag": 1,
        "missing_poib_flag": 0,        "poi_voltage_mismatch_flag": 1,
        "duplicate_substation_flag": 0, "null_connectivity_node_flag": 0,
        "orphan_node_flag": 0,
        "thermal_margin_mw": np.log1p(350),
        "project_exceeds_thermal_flag": 1,  "cmz_name": "LZ_WEST"
    },
    {
        "scenario": "❌ SCENARIO C — 150 MW ESR, fees NOT paid, missing POIB, orphan node",
        "resource_type": "ESR",        "project_mw": np.log1p(150),
        "poi_voltage_kv": 115,         "inr_type": "FIS_SS",
        "nameplate_to_maxgen_ratio": 1.05,  "lead_tdsp": "AEP",
        "crez_flag": 0,                "months_to_cod": 30,
        "resubmission_count": 1,
        "fis_fee_paid": 0,             "ss_fee_paid": 0,   "payment_made_flag": 0,
        "missing_poib_flag": 1,        "poi_voltage_mismatch_flag": 0,
        "duplicate_substation_flag": 0, "null_connectivity_node_flag": 0,
        "orphan_node_flag": 1,
        "thermal_margin_mw": np.log1p(200),
        "project_exceeds_thermal_flag": 0,  "cmz_name": "LZ_SOUTH"
    },
    {
        "scenario": "✅ SCENARIO D — 50 MW Conventional gas, 230kV, all clean, FIS",
        "resource_type": "CONVENTIONAL", "project_mw": np.log1p(50),
        "poi_voltage_kv": 230,           "inr_type": "FIS",
        "nameplate_to_maxgen_ratio": 1.02, "lead_tdsp": "TNMP",
        "crez_flag": 0,                  "months_to_cod": 48,
        "resubmission_count": 0,
        "fis_fee_paid": 1,               "ss_fee_paid": 1,  "payment_made_flag": 1,
        "missing_poib_flag": 0,          "poi_voltage_mismatch_flag": 0,
        "duplicate_substation_flag": 0,  "null_connectivity_node_flag": 0,
        "orphan_node_flag": 0,
        "thermal_margin_mw": np.log1p(300),
        "project_exceeds_thermal_flag": 0,  "cmz_name": "LZ_HOUSTON"
    },
]

for s in scenarios:
    label = s.pop("scenario")
    s_df  = pd.DataFrame([s])
    prob  = model.predict_proba(s_df)[0][1]
    pred  = "PASS ✅" if prob >= 0.5 else "FAIL ❌"
    print(f"\n{label}")
    print(f"   → Predicted: {pred}   (Pass probability: {prob:.1%})")

print("\n" + "=" * 65)
print("Files generated:")
print("  ginr_feasibility_training_data.csv  — 300-row training dataset")
print("  ginr_logistic_regression.py          — this model script")
print("=" * 65)
