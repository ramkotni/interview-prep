# GINR Feasibility Screening Model - Operations Runbook

**Project Name:** Predictive Feasibility Screening Model for GINR Submissions  
**Service Name:** GINR Feasibility ML Service (Flask)  
**Location:** `C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\specs`  
**Primary Port:** `5050`

---

## 1) Purpose and Scope

This runbook explains how to operate, verify, retrain, deploy, and recover the Python feasibility scoring service used by RARF/Spring Boot.

It covers:
- model training and versioning
- API startup and health checks
- batch/single scoring
- drift checks and retraining
- rollback and incident actions

---

## 2) System Components

- `ginr_model_pipeline.py` - train/evaluate/score/drift/retrain CLI
- `ginr_prediction_api.py` - Flask API service (`/api/v1/score`, `/api/v1/health`, `/api/v1/drift`)
- `generate_ginr_synthetic_data.py` - synthetic training data generator
- `ginr_feasibility_training_data.csv` - training dataset
- `models/` - model registry (`ginr_model_v*.joblib`, metadata, `latest.json`)
- `prediction_log.csv` - audit trail for scored records
- `model_metrics_history.json` - historical model metrics

---

## 3) Prerequisites

- Python 3.9+
- Required packages: `pandas`, `numpy`, `scikit-learn`, `flask`, `joblib`
- Access to this folder path and write permission to `models/`

Install dependencies (if needed):

```powershell
cd "C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\specs"
pip install pandas numpy scikit-learn flask joblib
```

---

## 4) Quick Start (Local Ops)

### 4.1 Generate sample data (if training file is missing)

```powershell
cd "C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\specs"
python generate_ginr_synthetic_data.py
```

### 4.2 Train model

```powershell
python ginr_model_pipeline.py --action train
```

Expected outcomes:
- new artifact in `models/` (example `ginr_model_v1.2.joblib`)
- matching metadata file (example `ginr_model_v1.2_metadata.json`)
- `models/latest.json` updated to new version
- `model_metrics_history.json` appended

### 4.3 Start API service

```powershell
python ginr_prediction_api.py
```

Optional (run API in background from PowerShell):

```powershell
Start-Process -FilePath python -ArgumentList "ginr_prediction_api.py" -WorkingDirectory "C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\specs"
```

### 4.4 End-to-end command flow (train -> start API -> REST calls)

```powershell
cd "C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\specs"

# 1) Optional: generate sample training data
python generate_ginr_synthetic_data.py

# 2) Train model and update latest pointer
python ginr_model_pipeline.py --action train

# 3) Start API (keep this terminal running)
python ginr_prediction_api.py
```

Use a second terminal for REST calls:

```powershell
# 4) Health check
Invoke-RestMethod -Uri "http://localhost:5050/api/v1/health" -Method Get | ConvertTo-Json -Depth 5

# 5) Model metadata
Invoke-RestMethod -Uri "http://localhost:5050/api/v1/model/info" -Method Get | ConvertTo-Json -Depth 8

# 6) Score one request
$body = @{
  ginr_request_id = 1234
  inr_id = "INR26-1234"
  resource_type = "SOLAR"
  project_mw = 250
  poi_voltage_kv = 345
  inr_type = "SS"
  nameplate_to_maxgen_ratio = 1.10
  lead_tdsp = "ONCOR"
  crez_flag = 0
  months_to_cod = 40
  resubmission_count = 0
  fis_fee_paid = 1
  ss_fee_paid = 1
  payment_made_flag = 1
  missing_poib_flag = 0
  poi_voltage_mismatch_flag = 0
  duplicate_substation_flag = 0
  null_connectivity_node_flag = 0
  orphan_node_flag = 0
  thermal_margin_mw = 400
  project_exceeds_thermal_flag = 0
  cmz_name = "LZ_NORTH"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5050/api/v1/score" -Method Post -ContentType "application/json" -Body $body | ConvertTo-Json -Depth 8

# 7) Read last stored score by GINR ID
Invoke-RestMethod -Uri "http://localhost:5050/api/v1/score/1234" -Method Get | ConvertTo-Json -Depth 8

# 8) Drift status
Invoke-RestMethod -Uri "http://localhost:5050/api/v1/drift" -Method Get | ConvertTo-Json -Depth 5
```

---

## 5) Health and Readiness Checks

### 5.1 Liveness

```powershell
Invoke-RestMethod -Uri "http://localhost:5050/api/v1/health" -Method Get | ConvertTo-Json -Depth 5
```

Expected fields:
- `status = UP`
- `model_version`
- `trained_at`
- `roc_auc`

### 5.2 Model info

```powershell
Invoke-RestMethod -Uri "http://localhost:5050/api/v1/model/info" -Method Get | ConvertTo-Json -Depth 8
```

### 5.3 Built-in scenario tests

```powershell
Invoke-RestMethod -Uri "http://localhost:5050/api/v1/score/test" -Method Get | ConvertTo-Json -Depth 8
```

---

## 6) Scoring Operations

### 6.1 Single-record scoring API

```powershell
$body = @{
  ginr_request_id = 1234
  inr_id = "INR26-1234"
  resource_type = "SOLAR"
  project_mw = 250
  poi_voltage_kv = 345
  inr_type = "SS"
  nameplate_to_maxgen_ratio = 1.10
  lead_tdsp = "ONCOR"
  crez_flag = 0
  months_to_cod = 40
  resubmission_count = 0
  fis_fee_paid = 1
  ss_fee_paid = 1
  payment_made_flag = 1
  missing_poib_flag = 0
  poi_voltage_mismatch_flag = 0
  duplicate_substation_flag = 0
  null_connectivity_node_flag = 0
  orphan_node_flag = 0
  thermal_margin_mw = 400
  project_exceeds_thermal_flag = 0
  cmz_name = "LZ_NORTH"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5050/api/v1/score" -Method Post -ContentType "application/json" -Body $body | ConvertTo-Json -Depth 8
```

### 6.2 Batch scoring via pipeline CLI

```powershell
python ginr_model_pipeline.py --action batch --input ".\input_batch.csv"
```

Output file: `input_batch_scored.csv`

### 6.3 Batch scoring via REST API

```powershell
$batch = @{
  records = @(
    @{
      ginr_request_id = 2001
      inr_id = "INR26-2001"
      resource_type = "SOLAR"
      project_mw = 120
      poi_voltage_kv = 138
      inr_type = "SS"
      nameplate_to_maxgen_ratio = 1.08
      lead_tdsp = "ONCOR"
      crez_flag = 0
      months_to_cod = 36
      resubmission_count = 0
      fis_fee_paid = 1
      ss_fee_paid = 1
      payment_made_flag = 1
      missing_poib_flag = 0
      poi_voltage_mismatch_flag = 0
      duplicate_substation_flag = 0
      null_connectivity_node_flag = 0
      orphan_node_flag = 0
      thermal_margin_mw = 260
      project_exceeds_thermal_flag = 0
      cmz_name = "LZ_NORTH"
    },
    @{
      ginr_request_id = 2002
      inr_id = "INR26-2002"
      resource_type = "WIND"
      project_mw = 650
      poi_voltage_kv = 138
      inr_type = "FIS"
      nameplate_to_maxgen_ratio = 1.35
      lead_tdsp = "ONCOR"
      crez_flag = 1
      months_to_cod = 20
      resubmission_count = 2
      fis_fee_paid = 1
      ss_fee_paid = 1
      payment_made_flag = 1
      missing_poib_flag = 0
      poi_voltage_mismatch_flag = 1
      duplicate_substation_flag = 0
      null_connectivity_node_flag = 0
      orphan_node_flag = 0
      thermal_margin_mw = 300
      project_exceeds_thermal_flag = 1
      cmz_name = "LZ_WEST"
    }
  )
} | ConvertTo-Json -Depth 8

Invoke-RestMethod -Uri "http://localhost:5050/api/v1/score/batch" -Method Post -ContentType "application/json" -Body $batch | ConvertTo-Json -Depth 8
```

### 6.4 Fetch stored score by request id

```powershell
Invoke-RestMethod -Uri "http://localhost:5050/api/v1/score/1234" -Method Get | ConvertTo-Json -Depth 8
```

---

## 7) Drift Monitoring and Retraining

### 7.1 Drift check

```powershell
python ginr_model_pipeline.py --action drift
```

or

```powershell
Invoke-RestMethod -Uri "http://localhost:5050/api/v1/drift" -Method Get | ConvertTo-Json -Depth 5
```

Drift rule in current code:
- compares recent fail-rate (last 50 predictions) against baseline
- `DRIFT_DETECTED` when deviation > `0.15`

### 7.2 Retrain with new labeled feedback

```powershell
python ginr_model_pipeline.py --action retrain --input ".\new_labeled_rows.csv"
```

Expected behavior:
- merges new rows into `ginr_feasibility_training_data.csv`
- trains new model version
- updates `models/latest.json`
- appends metrics history

---

## 8) Deployment and Rollback

### 8.1 Deploy a newly trained model

1. Train model with `--action train` or `--action retrain`.
2. Confirm `models/latest.json` points to desired model path.
3. Restart API process so model cache reloads.
4. Run health + test endpoint checks.

### 8.2 Rollback procedure

If predictions degrade or API errors occur after model update:

1. Stop API process.
2. Edit `models/latest.json` and set `version` and `path` to previous stable model.
3. Restart API process.
4. Verify with `/api/v1/health` and `/api/v1/score/test`.

Example `latest.json` shape:

```json
{
  "version": "1.1",
  "path": "C:\\...\\models\\ginr_model_v1.1.joblib"
}
```

---

## 9) Incident Response

### P1: API down (`/health` fails)

1. Confirm process is running.
2. Restart `ginr_prediction_api.py`.
3. Check model pointer file exists: `models/latest.json`.
4. Check model path in pointer exists on disk.

### P1: Scoring endpoint returns 500

1. Validate request payload includes all required features.
2. Verify categorical values (`resource_type`, `poi_voltage_kv`) are valid.
3. Verify model artifact and metadata files both exist.
4. If needed, rollback to prior model.

### P2: Sudden quality drop / drift

1. Run drift endpoint.
2. Pull latest labeled outcomes.
3. Retrain with `--action retrain`.
4. Re-run smoke tests and compare metrics before promotion.

---

## 10) Troubleshooting Matrix

| Symptom | Likely Cause | Action |
|---|---|---|
| `No trained model found` | `models/latest.json` missing | Run training and regenerate pointer |
| `/score` returns validation errors | Missing/invalid fields in payload | Fix payload based on API response details |
| Drift repeatedly detected | Data distribution changed | Retrain with recent labeled records |
| Predictions logged but no metrics updates | Training not executed | Run `--action train` and verify metrics file |
| `/score/<id>` returns 404 | No matching row in `prediction_log.csv` | Score that request first or verify ID |

---

## 11) Operational Cadence

### Daily
- Verify `/api/v1/health`
- Check recent errors in service console/logs
- Review last lines of `prediction_log.csv`

### Weekly
- Run drift check
- Compare recent prediction distribution vs baseline
- Review any repeated validation failures from callers

### Monthly
- Retrain using recent labeled outcomes (if available)
- Compare new vs prior ROC-AUC and average precision
- Promote only if metrics are stable or improved

---

## 12) Useful Commands Reference

```powershell
cd "C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\specs"
python ginr_model_pipeline.py --action train
python ginr_model_pipeline.py --action evaluate
python ginr_model_pipeline.py --action drift
python ginr_model_pipeline.py --action retrain --input ".\new_labeled_rows.csv"
python ginr_prediction_api.py
```

---

## 13) Change Log Template

Use this section to track operational changes.

- `YYYY-MM-DD` - Model promoted to `vX.Y` - reason, metrics, owner
- `YYYY-MM-DD` - Rollback to `vX.Y` - reason, impact, owner
- `YYYY-MM-DD` - Runbook updated - sections changed, owner
