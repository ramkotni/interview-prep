# GINR Feasibility Screening Model — Enterprise Architecture
## End-to-End System Design

**Date:** May 31, 2026  
**Stack:** Oracle DB · Spring Boot (existing RARF) · Python · Flask · scikit-learn  

---

## System Architecture Diagram

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    ERCOT RIOO-IS / RARF ECOSYSTEM                           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ┌─────────────────────┐    ┌──────────────────────────────────────────┐    ║
║  │  IE / DEVELOPER     │    │        ORACLE DATABASE                   │    ║
║  │  (Web Browser)      │    │  ┌──────────────┐  ┌────────────────┐   │    ║
║  │                     │    │  │ ginr.ginr_   │  │ CHANGE_        │   │    ║
║  │  1. Submit GINR     │    │  │ request      │  │ REQUESTS       │   │    ║
║  │  2. See risk score  │    │  ├──────────────┤  ├────────────────┤   │    ║
║  └────────┬────────────┘    │  │ POIB_DATA    │  │ CONNECTIVITY_  │   │    ║
║           │                 │  ├──────────────┤  │ NODES          │   │    ║
║           ▼                 │  │ MOST_LIMIT_  │  ├────────────────┤   │    ║
║  ┌─────────────────────┐    │  │ SERIES_ELEM  │  │ SUBSTATIONS    │   │    ║
║  │  RARF / RIOO-IS     │    │  └──────────────┘  └────────────────┘   │    ║
║  │  Spring Boot API    │    └──────────────────────┬───────────────────┘    ║
║  │  (existing)         │◄─────── reads/writes ─────┘                        ║
║  │                     │                                                     ║
║  │  POST /ginr/{id}/   │──── calls ────►  ┌──────────────────────────────┐  ║
║  │    submit           │                  │  PYTHON ML SERVICE           │  ║
║  │                     │◄── risk score ── │  (ginr_prediction_api.py)    │  ║
║  │  GET  /ginr/{id}/   │                  │                              │  ║
║  │    feasibility-score│                  │  Port: 5050                  │  ║
║  └─────────────────────┘                  │  /api/v1/score               │  ║
║                                           │  /api/v1/score/batch         │  ║
║                                           │  /api/v1/health              │  ║
║                                           └──────────────────────────────┘  ║
╚══════════════════════════════════════════════════════════════════════════════╝

═══════════════════════  ML SYSTEM INTERNALS  ═══════════════════════════════

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                    TRAINING PIPELINE (Batch / Scheduled)                │
  │                                                                         │
  │  Oracle DB                                                              │
  │     │                                                                   │
  │     ▼ (feature_extraction.sql → pandas)                                 │
  │  Raw Features  ──► Feature Engineering ──► Preprocessing ──► Train     │
  │     │               (log-transform,          (StandardScaler,    │      │
  │     │                derived flags)            OneHotEncoder)    │      │
  │     │                                                            ▼      │
  │     │                                                    Model Registry │
  │     │                                                    /models/       │
  │     │                                                    v1.0/          │
  │     │                                                    v1.1/ (latest) │
  │     └──► Prediction Logs ──► Drift Monitor ──► Retrain Trigger         │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                    PREDICTION FLOW (Real-Time)                          │
  │                                                                         │
  │  GINR Submitted                                                         │
  │       │                                                                 │
  │       ▼                                                                 │
  │  Feature Extractor  ──► Load Model (from registry) ──► Predict         │
  │  (SQL or Python)                                           │            │
  │                                                            ▼            │
  │                                              {                          │
  │                                                "ginr_id": 1234,        │
  │                                                "pass_prob": 0.87,      │
  │                                                "risk_level": "LOW",    │
  │                                                "top_risks": [          │
  │                                                  "missing_poib_flag",  │
  │                                                  "crez_flag"           │
  │                                                ],                      │
  │                                                "model_version": "1.1"  │
  │                                              }                         │
  └─────────────────────────────────────────────────────────────────────────┘

═══════════════════════  DATA FLOW  ══════════════════════════════════════════

  [Training Time]
  Oracle → SQL Extract → CSV/Pandas → Feature Eng. → Train → joblib → Registry

  [Prediction Time]
  GINR Submit Event → Spring Boot → HTTP POST /api/v1/score → Flask ML API
       → Load model from Registry → Compute features → Predict → JSON Response
       → Spring Boot stores score → UI displays risk badge

  [Feedback Loop - Daily]
  Oracle (CR status changes: SENT_BACK / READY_FOR_MODELING)
       → Append labeled rows to training data
       → Retrain if N new labeled rows accumulated
       → Deploy new model version to Registry

═══════════════════════  COMPONENT INVENTORY  ════════════════════════════════

  File                              Purpose
  ─────────────────────────────── ─────────────────────────────────────────
  generate_ginr_synthetic_data.py  Generate training data (dev/test)
  ginr_model_pipeline.py           Train → save → version → monitor
  ginr_prediction_api.py           Flask REST API (prediction service)
  ginr_logistic_regression.py      Exploratory model + evaluation
  models/                          Model registry (versioned joblib files)
  prediction_log.csv               Audit trail of all predictions made
  training_data/                   Historical labeled training data

═══════════════════════  SPRING BOOT INTEGRATION  ════════════════════════════

  In existing ChangeRequestService.java or GinrRequestService.java:

  // After GINR submission succeeds, call ML service
  @Value("${ml.service.url:http://localhost:5050}")
  private String mlServiceUrl;

  public FeasibilityScore scoreFeasibility(Long ginrRequestId) {
      String url = mlServiceUrl + "/api/v1/score";
      FeasibilityRequest req = buildFeaturePayload(ginrRequestId);
      return restTemplate.postForObject(url, req, FeasibilityScore.class);
  }
```

---

## Component Responsibilities

| Component | Technology | Responsibility |
|---|---|---|
| **Oracle DB** | Oracle 19c | Source of truth for all GINR/RARF data |
| **Spring Boot API** | Java 11, existing RARF app | Orchestrates GINR workflow, calls ML service |
| **Python ML Service** | Flask + scikit-learn | Serves predictions, loads versioned models |
| **Model Pipeline** | Python, joblib | Train, version, save, monitor models |
| **Model Registry** | Local filesystem / S3 | Stores versioned model artifacts |
| **Prediction Log** | CSV / Oracle table | Audit trail of all predictions for drift detection |

---

## Risk Score Interpretation

| Pass Probability | Risk Level | Badge Color | Action |
|---|---|---|---|
| 85% – 100% | 🟢 LOW | Green | Proceed to study queue |
| 60% – 84% | 🟡 MEDIUM | Yellow | Planner review recommended |
| 40% – 59% | 🟠 HIGH | Orange | Developer notified of specific gaps |
| 0% – 39% | 🔴 CRITICAL | Red | Likely SENT_BACK; auto-flag for triage |
