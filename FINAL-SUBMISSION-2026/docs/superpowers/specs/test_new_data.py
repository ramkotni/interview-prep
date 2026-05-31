"""Quick end-to-end test for new GINR data predictions."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ginr_model_pipeline import load_latest_model, predict_single

pipeline, metadata = load_latest_model()
print(f"Model loaded: v{metadata['version']}  ROC-AUC={metadata['roc_auc']}")

scenarios = [
    {"label": "PASS — Clean 200MW Solar 345kV CenterPoint",
     "resource_type": "SOLAR",        "project_mw": 200,
     "poi_voltage_kv": 345,           "inr_type": "SS",
     "nameplate_to_maxgen_ratio": 1.10,"lead_tdsp": "CENTERPOINT",
     "crez_flag": 0,                  "months_to_cod": 42,
     "resubmission_count": 0,
     "fis_fee_paid": 1, "ss_fee_paid": 1, "payment_made_flag": 1,
     "missing_poib_flag": 0, "poi_voltage_mismatch_flag": 0,
     "duplicate_substation_flag": 0,  "null_connectivity_node_flag": 0,
     "orphan_node_flag": 0,           "thermal_margin_mw": 450,
     "project_exceeds_thermal_flag": 0, "cmz_name": "LZ_NORTH"},

    {"label": "FAIL — 800MW Wind CREZ 138kV exceeds thermal + 3 returns",
     "resource_type": "WIND",         "project_mw": 800,
     "poi_voltage_kv": 138,           "inr_type": "FIS",
     "nameplate_to_maxgen_ratio": 1.40,"lead_tdsp": "ONCOR",
     "crez_flag": 1,                  "months_to_cod": 18,
     "resubmission_count": 3,
     "fis_fee_paid": 1, "ss_fee_paid": 1, "payment_made_flag": 1,
     "missing_poib_flag": 0, "poi_voltage_mismatch_flag": 1,
     "duplicate_substation_flag": 0,  "null_connectivity_node_flag": 0,
     "orphan_node_flag": 0,           "thermal_margin_mw": 350,
     "project_exceeds_thermal_flag": 1, "cmz_name": "LZ_WEST"},

    {"label": "FAIL — ESR 150MW fees unpaid missing POIB orphan node",
     "resource_type": "ESR",          "project_mw": 150,
     "poi_voltage_kv": 115,           "inr_type": "FIS_SS",
     "nameplate_to_maxgen_ratio": 1.05,"lead_tdsp": "AEP",
     "crez_flag": 0,                  "months_to_cod": 30,
     "resubmission_count": 1,
     "fis_fee_paid": 0, "ss_fee_paid": 0, "payment_made_flag": 0,
     "missing_poib_flag": 1, "poi_voltage_mismatch_flag": 0,
     "duplicate_substation_flag": 0,  "null_connectivity_node_flag": 0,
     "orphan_node_flag": 1,           "thermal_margin_mw": 200,
     "project_exceeds_thermal_flag": 0, "cmz_name": "LZ_SOUTH"},

    {"label": "PASS — 50MW Gas 230kV TNMP all clean",
     "resource_type": "CONVENTIONAL", "project_mw": 50,
     "poi_voltage_kv": 230,           "inr_type": "FIS",
     "nameplate_to_maxgen_ratio": 1.02,"lead_tdsp": "TNMP",
     "crez_flag": 0,                  "months_to_cod": 48,
     "resubmission_count": 0,
     "fis_fee_paid": 1, "ss_fee_paid": 1, "payment_made_flag": 1,
     "missing_poib_flag": 0, "poi_voltage_mismatch_flag": 0,
     "duplicate_substation_flag": 0,  "null_connectivity_node_flag": 0,
     "orphan_node_flag": 0,           "thermal_margin_mw": 300,
     "project_exceeds_thermal_flag": 0, "cmz_name": "LZ_HOUSTON"},

    {"label": "MEDIUM RISK — 400MW Battery CREZ 345kV 1 prior return",
     "resource_type": "BATTERY",      "project_mw": 400,
     "poi_voltage_kv": 345,           "inr_type": "FIS",
     "nameplate_to_maxgen_ratio": 1.20,"lead_tdsp": "ONCOR",
     "crez_flag": 1,                  "months_to_cod": 36,
     "resubmission_count": 1,
     "fis_fee_paid": 1, "ss_fee_paid": 1, "payment_made_flag": 1,
     "missing_poib_flag": 0, "poi_voltage_mismatch_flag": 0,
     "duplicate_substation_flag": 1,  "null_connectivity_node_flag": 0,
     "orphan_node_flag": 0,           "thermal_margin_mw": 500,
     "project_exceeds_thermal_flag": 0, "cmz_name": "LZ_WEST"},

    {"label": "FAIL — CRITICAL 600MW Solar duplicate sub null nodes no fees",
     "resource_type": "SOLAR",        "project_mw": 600,
     "poi_voltage_kv": 69,            "inr_type": "FIS_SS",
     "nameplate_to_maxgen_ratio": 1.55,"lead_tdsp": "AEP",
     "crez_flag": 1,                  "months_to_cod": 12,
     "resubmission_count": 4,
     "fis_fee_paid": 0, "ss_fee_paid": 0, "payment_made_flag": 0,
     "missing_poib_flag": 1, "poi_voltage_mismatch_flag": 1,
     "duplicate_substation_flag": 1,  "null_connectivity_node_flag": 1,
     "orphan_node_flag": 1,           "thermal_margin_mw": 80,
     "project_exceeds_thermal_flag": 1, "cmz_name": "LZ_WEST"},
]

print()
print("=" * 65)
print("END-TO-END TEST — NEW DATA PREDICTIONS")
print("=" * 65)

for i, s in enumerate(scenarios, 1):
    lbl = s.pop("label")
    s["ginr_request_id"] = 9000 + i
    s["inr_id"] = f"INR26-{9000+i}"
    r = predict_single(s, pipeline, metadata)

    prob = r["pass_probability"]
    pred = r["predicted_label"]
    risk = r["risk_level"]
    icon = r["risk_icon"]
    action = r["action"]

    print(f"\n[{i}] {lbl}")
    print(f"     Pass Probability : {prob:.1%}")
    print(f"     Prediction       : {'✅ PASS' if pred == 'PASS' else '❌ FAIL'}")
    print(f"     Risk Level       : {icon} {risk}")
    print(f"     ERCOT Action     : {action}")

print()
print("=" * 65)
print("Prediction log written to: prediction_log.csv")
print("Model version            : " + metadata["version"])
print("=" * 65)

