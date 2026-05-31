"""
GINR Feasibility Screening — Prediction REST API (Enterprise Service)
=====================================================================
Flask microservice that serves real-time feasibility scores.
Integrated with the existing Spring Boot RARF application.

Endpoints:
  POST /api/v1/score          → score a single GINR submission
  POST /api/v1/score/batch    → score multiple GINRs at once
  GET  /api/v1/score/{id}     → retrieve stored score for a GINR
  GET  /api/v1/health         → liveness + model version info
  GET  /api/v1/model/info     → model metadata and training metrics
  GET  /api/v1/drift          → current drift status

Usage:
  pip install flask
  python ginr_prediction_api.py

Spring Boot calls this at: http://localhost:5050/api/v1/score
"""

from flask import Flask, request, jsonify, abort
import pandas as pd
import numpy as np
import json
import logging
import datetime
from pathlib import Path

# Import pipeline functions
import sys
sys.path.insert(0, str(Path(__file__).parent))
from ginr_model_pipeline import (
    load_latest_model, predict_single, predict_batch,
    check_drift, engineer_features,
    NUMERIC_FEATURES, BINARY_FEATURES, CATEGORICAL_FEATURES,
    PRED_LOG, BASE_DIR
)

# ─────────────────────────────────────────────────────────────────────────────
# App Setup
# ─────────────────────────────────────────────────────────────────────────────

app = Flask(__name__)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
LOG = logging.getLogger("GINRPredictionAPI")

# Load model at startup (cached in memory)
_pipeline = None
_metadata = None

def get_model():
    global _pipeline, _metadata
    if _pipeline is None:
        _pipeline, _metadata = load_latest_model()
    return _pipeline, _metadata


# ─────────────────────────────────────────────────────────────────────────────
# Input Validation
# ─────────────────────────────────────────────────────────────────────────────

REQUIRED_FIELDS = NUMERIC_FEATURES + BINARY_FEATURES + CATEGORICAL_FEATURES

def validate_request(data: dict) -> list[str]:
    """Return list of missing or invalid fields."""
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")
    # Numeric range checks
    if "project_mw" in data and float(data["project_mw"]) <= 0:
        errors.append("project_mw must be > 0")
    if "poi_voltage_kv" in data and int(data["poi_voltage_kv"]) not in [69, 115, 138, 230, 345, 500]:
        errors.append("poi_voltage_kv must be one of: 69, 115, 138, 230, 345, 500")
    if "resource_type" in data and data["resource_type"] not in ["SOLAR","WIND","CONVENTIONAL","ESR","BATTERY"]:
        errors.append("resource_type must be one of: SOLAR, WIND, CONVENTIONAL, ESR, BATTERY")
    return errors


# ─────────────────────────────────────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/api/v1/health", methods=["GET"])
def health():
    """
    Liveness check. Returns model version and status.
    Called by Spring Boot on startup to verify ML service is up.
    """
    try:
        pipeline, metadata = get_model()
        return jsonify({
            "status":        "UP",
            "service":       "GINR Feasibility ML Service",
            "model_version": metadata.get("version"),
            "trained_at":    metadata.get("trained_at"),
            "roc_auc":       metadata.get("roc_auc"),
            "timestamp":     datetime.datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({"status": "DOWN", "error": str(e)}), 503


@app.route("/api/v1/model/info", methods=["GET"])
def model_info():
    """Full model metadata — training metrics, feature list, version history."""
    _, metadata = get_model()
    return jsonify(metadata), 200


@app.route("/api/v1/score", methods=["POST"])
def score_single():
    """
    Score a single GINR submission.

    Request body (JSON):
    {
        "ginr_request_id": 1234,
        "inr_id": "INR26-1234",
        "resource_type": "SOLAR",
        "project_mw": 250,
        "poi_voltage_kv": 345,
        "inr_type": "SS",
        "nameplate_to_maxgen_ratio": 1.10,
        "lead_tdsp": "ONCOR",
        "crez_flag": 0,
        "months_to_cod": 40,
        "resubmission_count": 0,
        "fis_fee_paid": 1,
        "ss_fee_paid": 1,
        "payment_made_flag": 1,
        "missing_poib_flag": 0,
        "poi_voltage_mismatch_flag": 0,
        "duplicate_substation_flag": 0,
        "null_connectivity_node_flag": 0,
        "orphan_node_flag": 0,
        "thermal_margin_mw": 400,
        "project_exceeds_thermal_flag": 0,
        "cmz_name": "LZ_NORTH"
    }

    Response:
    {
        "ginr_request_id": 1234,
        "inr_id": "INR26-1234",
        "pass_probability": 0.9234,
        "predicted_label": "PASS",
        "risk_level": "LOW",
        "risk_icon": "🟢",
        "action": "Proceed to study queue",
        "top_risk_factors": [],
        "model_version": "1.1",
        "scored_at": "2026-05-31T10:23:45"
    }
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    errors = validate_request(data)
    if errors:
        return jsonify({"error": "Validation failed", "details": errors}), 422

    try:
        pipeline, metadata = get_model()
        result = predict_single(data, pipeline, metadata)
        LOG.info(f"Scored GINR {data.get('ginr_request_id')} → "
                 f"{result['predicted_label']} ({result['pass_probability']:.1%}) "
                 f"[{result['risk_level']}]")
        return jsonify(result), 200
    except Exception as e:
        LOG.error(f"Prediction error: {e}", exc_info=True)
        return jsonify({"error": "Internal scoring error", "detail": str(e)}), 500


@app.route("/api/v1/score/batch", methods=["POST"])
def score_batch():
    """
    Score multiple GINR records at once.

    Request body: { "records": [ {...}, {...}, ... ] }
    Response:     { "results": [ {...}, {...}, ... ], "total": N }
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    body = request.get_json()
    records = body.get("records", [])
    if not records:
        return jsonify({"error": "No records provided"}), 400

    pipeline, metadata = get_model()
    results = []
    errors  = []

    for i, rec in enumerate(records):
        validation_errors = validate_request(rec)
        if validation_errors:
            errors.append({"index": i, "ginr_request_id": rec.get("ginr_request_id"), "errors": validation_errors})
            continue
        try:
            result = predict_single(rec, pipeline, metadata)
            results.append(result)
        except Exception as e:
            errors.append({"index": i, "ginr_request_id": rec.get("ginr_request_id"), "error": str(e)})

    LOG.info(f"Batch scored {len(results)} records, {len(errors)} errors")
    return jsonify({
        "results":      results,
        "total_scored": len(results),
        "total_errors": len(errors),
        "errors":       errors
    }), 200


@app.route("/api/v1/score/<int:ginr_request_id>", methods=["GET"])
def get_stored_score(ginr_request_id: int):
    """
    Retrieve the last stored prediction for a specific GINR request ID.
    Useful for Spring Boot to display score without re-scoring.
    """
    if not PRED_LOG.exists():
        abort(404, description="No prediction log found")

    log_df = pd.read_csv(PRED_LOG)
    match  = log_df[log_df["ginr_request_id"] == ginr_request_id]

    if match.empty:
        return jsonify({"error": f"No score found for ginr_request_id={ginr_request_id}"}), 404

    last = match.iloc[-1].to_dict()
    # Return key fields only
    return jsonify({
        "ginr_request_id":  int(last.get("ginr_request_id", ginr_request_id)),
        "inr_id":           last.get("inr_id"),
        "pass_probability": float(last.get("pass_probability", 0)),
        "predicted_label":  last.get("predicted_label"),
        "risk_level":       last.get("risk_level"),
        "risk_icon":        last.get("risk_icon"),
        "action":           last.get("action"),
        "model_version":    last.get("model_version"),
        "scored_at":        last.get("scored_at"),
    }), 200


@app.route("/api/v1/drift", methods=["GET"])
def drift_status():
    """
    Current model drift status.
    Called by monitoring jobs to decide if retraining is needed.
    """
    result = check_drift()
    http_status = 200 if result.get("status") in ("OK", "insufficient_data") else 206
    return jsonify(result), http_status


@app.route("/api/v1/score/test", methods=["GET"])
def test_scenarios():
    """
    Run 4 built-in test scenarios and return predictions.
    Used to verify the ML service is working after deployment.
    """
    pipeline, metadata = get_model()

    test_cases = [
        {
            "label": "PASS — Clean Solar 345kV CENTERPOINT",
            "resource_type": "SOLAR",      "project_mw": 200,
            "poi_voltage_kv": 345,          "inr_type": "SS",
            "nameplate_to_maxgen_ratio": 1.10, "lead_tdsp": "CENTERPOINT",
            "crez_flag": 0,                 "months_to_cod": 42,
            "resubmission_count": 0,
            "fis_fee_paid": 1, "ss_fee_paid": 1, "payment_made_flag": 1,
            "missing_poib_flag": 0, "poi_voltage_mismatch_flag": 0,
            "duplicate_substation_flag": 0, "null_connectivity_node_flag": 0,
            "orphan_node_flag": 0,
            "thermal_margin_mw": 450, "project_exceeds_thermal_flag": 0,
            "cmz_name": "LZ_NORTH"
        },
        {
            "label": "FAIL — 800MW Wind CREZ exceeds thermal",
            "resource_type": "WIND",       "project_mw": 800,
            "poi_voltage_kv": 138,          "inr_type": "FIS",
            "nameplate_to_maxgen_ratio": 1.40, "lead_tdsp": "ONCOR",
            "crez_flag": 1,                 "months_to_cod": 18,
            "resubmission_count": 3,
            "fis_fee_paid": 1, "ss_fee_paid": 1, "payment_made_flag": 1,
            "missing_poib_flag": 0, "poi_voltage_mismatch_flag": 1,
            "duplicate_substation_flag": 0, "null_connectivity_node_flag": 0,
            "orphan_node_flag": 0,
            "thermal_margin_mw": 350, "project_exceeds_thermal_flag": 1,
            "cmz_name": "LZ_WEST"
        },
        {
            "label": "FAIL — ESR fees unpaid missing POIB",
            "resource_type": "ESR",        "project_mw": 150,
            "poi_voltage_kv": 115,          "inr_type": "FIS_SS",
            "nameplate_to_maxgen_ratio": 1.05, "lead_tdsp": "AEP",
            "crez_flag": 0,                 "months_to_cod": 30,
            "resubmission_count": 1,
            "fis_fee_paid": 0, "ss_fee_paid": 0, "payment_made_flag": 0,
            "missing_poib_flag": 1, "poi_voltage_mismatch_flag": 0,
            "duplicate_substation_flag": 0, "null_connectivity_node_flag": 0,
            "orphan_node_flag": 1,
            "thermal_margin_mw": 200, "project_exceeds_thermal_flag": 0,
            "cmz_name": "LZ_SOUTH"
        },
        {
            "label": "PASS — 50MW Gas 230kV TNMP all clean",
            "resource_type": "CONVENTIONAL", "project_mw": 50,
            "poi_voltage_kv": 230,            "inr_type": "FIS",
            "nameplate_to_maxgen_ratio": 1.02, "lead_tdsp": "TNMP",
            "crez_flag": 0,                   "months_to_cod": 48,
            "resubmission_count": 0,
            "fis_fee_paid": 1, "ss_fee_paid": 1, "payment_made_flag": 1,
            "missing_poib_flag": 0, "poi_voltage_mismatch_flag": 0,
            "duplicate_substation_flag": 0, "null_connectivity_node_flag": 0,
            "orphan_node_flag": 0,
            "thermal_margin_mw": 300, "project_exceeds_thermal_flag": 0,
            "cmz_name": "LZ_HOUSTON"
        }
    ]

    results = []
    for tc in test_cases:
        test_label = tc.pop("label")
        result = predict_single(tc, pipeline, metadata)
        result["test_scenario"] = test_label
        results.append(result)

    return jsonify({"test_results": results, "model_version": metadata.get("version")}), 200


# ─────────────────────────────────────────────────────────────────────────────
# Error Handlers
# ─────────────────────────────────────────────────────────────────────────────

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found", "detail": str(e)}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error", "detail": str(e)}), 500


# ─────────────────────────────────────────────────────────────────────────────
# Startup
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("GINR FEASIBILITY ML SERVICE  — Starting on port 5050")
    print("=" * 65)
    print("Endpoints:")
    print("  POST /api/v1/score          → score single GINR")
    print("  POST /api/v1/score/batch    → score multiple GINRs")
    print("  GET  /api/v1/score/<id>     → get stored score")
    print("  GET  /api/v1/score/test     → run built-in test scenarios")
    print("  GET  /api/v1/health         → liveness check")
    print("  GET  /api/v1/model/info     → model metadata")
    print("  GET  /api/v1/drift          → drift detection")
    print("=" * 65)
    # Pre-load model
    get_model()
    app.run(host="0.0.0.0", port=5050, debug=False)

