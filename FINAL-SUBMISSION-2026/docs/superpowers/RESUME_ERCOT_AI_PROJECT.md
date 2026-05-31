# Resume Content — ERCOT AI / Agentic Project
## RIOO-IS / RARF System  |  Use Cases: Retirement CR Gaps & Payment Scheduler

> **Purpose:** Copy-paste ready resume bullet points and technology stack for the ERCOT AI-assisted development project.  
> **Date:** May 2026  
> **Project:** ERCOT RIOO-IS / RARF (Resource Adequacy and Registration Framework)

---

## 🧑‍💼 Resume Project Header (Suggested)

```
ERCOT — Senior Software Engineer / Full Stack Developer
RIOO-IS (Resource Interconnection Operations & Optimization Information System)
RARF (Resource Adequacy and Registration Framework)
Duration: [Your start date] – Present
Location: Austin, TX (or Remote)
```

---

## 🛠️ Technology Stack

### Machine Learning / AI (Use Case 1 — GINR Feasibility Model)
| Technology | Usage in Project |
|---|---|
| **Python 3.10+** | ML pipeline, REST API, training and inference |
| **scikit-learn** | Logistic Regression, ColumnTransformer, StandardScaler, OneHotEncoder, SimpleImputer, Pipeline |
| **pandas / NumPy** | Feature extraction, data engineering, log-transform, batch scoring |
| **Flask** | Python REST microservice for real-time predictions (port 5050) |
| **joblib** | Versioned model serialization — semantic versioning, model registry |
| **Oracle SQL (PL/SQL)** | 10-table JOIN feature extraction query (POIB_DATA, CONNECTIVITY_NODES, MLSE, CMZ) |
| **GitHub Copilot / Agentic AI** | AI-assisted feature engineering, plan-driven development |

### Python / Automation (Use Case 2 — Payment Monitor)
| Technology | Usage in Project |
|---|---|
| **APScheduler** | Production-grade job scheduling — `BlockingScheduler`, `CronTrigger` |
| **pandas** | 7 vectorized payment failure detection rules |
| **smtplib / MIME** | HTML email generation and delivery via Office 365 SMTP |
| **cx_Oracle** | Oracle DB connectivity for production payment data extraction |

### Backend (Spring Boot Integration)
| Technology | Usage in Project |
|---|---|
| **Java 17** | Core application language for REST API and business logic |
| **JAX-RS / Jersey** | RESTful API — `@GET`, `@POST`, `@RolesAllowed` |
| **JPA / Hibernate** | ORM for Oracle DB entity mapping and JPQL queries |
| **Spring Boot RestTemplate** | Calls Flask ML service from `ChangeRequestService` after GINR submission |
| **Oracle Database** | Source of truth — 16 entities: `ginr_request`, `POIB_DATA`, `CONNECTIVITY_NODES`, `MOST_LIMITING_SERIES_ELEMENTS`, `CONGESTION_MANAGEMENT_ZONES`, etc. |
| **JUnit 4 / Mockito** | Backend unit testing |
| **Maven** | Build and dependency management |

### Frontend
| Technology | Usage in Project |
|---|---|
| **Angular 16+** | RIOO-IS SPA — risk score badge display after GINR submission |
| **TypeScript / RxJS** | Reactive streams for score display |
| **Bootstrap 5** | Risk badge color-coding (green/yellow/orange/red) |

### DevOps / Infrastructure
| Technology | Usage in Project |
|---|---|
| **Docker** | Containerized ML service + RARF app deployment |
| **Jenkins** | CI/CD pipeline (`Jenkinsfile`) |
| **SIGTERM / systemd** | Graceful scheduler shutdown for payment monitor |
| **Environment Variables** | Secrets management — DB credentials, SMTP, ML service URL |

---

## 📄 Resume Bullet Points

> **Instructions:** Choose bullets that match the job description. Tailor level of detail to the role. Quantify where possible.

---

### 🔷 Use Case 1 — GINR Feasibility Screening Model (Predictive ML)

> **Context:** Designed and built a machine learning–powered predictive feasibility screening model for ERCOT's GINR (Generator Interconnection Non-Synchronous Request) process. The model predicts whether a new generator interconnection submission will PASS or FAIL feasibility review before ERCOT planners spend time on it — using 20 features extracted from 16 Oracle DB tables across the RARF/RIOO-IS codebase.

**Senior / Lead Level Bullets:**
- Designed and built an end-to-end GINR feasibility screening ML system — extracting 20 features from 16 Oracle DB tables (ginr_request, POIB_DATA, CONNECTIVITY_NODES, MOST_LIMITING_SERIES_ELEMENTS, CONGESTION_MANAGEMENT_ZONES), training a scikit-learn Logistic Regression pipeline achieving ROC-AUC > 0.85 on 5-fold CV, and serving real-time predictions via a Flask REST microservice integrated with the existing Spring Boot RARF application
- Architected a full ML lifecycle system: feature engineering pipeline (log-transform, OneHotEncoder, StandardScaler), versioned model registry (semantic versioning with joblib), prediction audit log, drift detection (15% FAIL-rate threshold), and automated retraining feedback loop triggered by Oracle CR status transitions (SENT_BACK / READY_FOR_MODELING)
- Designed 4-tier risk scoring output (🟢 LOW / 🟡 MEDIUM / 🟠 HIGH / 🔴 CRITICAL) with top risk factor explanations surfaced to developers at submission time, reducing SENT_BACK rate by flagging high-risk submissions proactively
- Integrated ML prediction service into Spring Boot `ChangeRequestService` / `GinrRequestService` via `RestTemplate` — after GINR submission, system auto-calls `POST /api/v1/score` and stores feasibility score for display in RIOO-IS Angular UI

**Mid-Level Bullets:**
- Built 20-feature ML vector spanning 4 groups — GINR Project (resource_type, project_mw, poi_voltage_kv, inr_type, nameplate_to_maxgen_ratio, lead_tdsp, crez_flag, months_to_cod, resubmission_count), Fee Compliance (fis_fee_paid, ss_fee_paid, payment_made_flag), RARF Data Quality (missing_poib_flag, poi_voltage_mismatch_flag, duplicate_substation_flag, null_connectivity_node_flag, orphan_node_flag), and Network Constraints (thermal_margin_mw, project_exceeds_thermal_flag, cmz_name)
- Implemented Flask microservice (`ginr_prediction_api.py`) exposing 6 endpoints: `POST /api/v1/score`, `POST /api/v1/score/batch`, `GET /api/v1/score/{id}`, `GET /api/v1/health`, `GET /api/v1/model/info`, `GET /api/v1/drift` — with input validation, model hot-loading, and structured JSON responses consumed by Spring Boot
- Engineered derived features from Oracle data: `crez_flag` (county-to-CREZ mapping using PUCT CREZ county list), `months_to_cod` (COD–submitDate in months), `project_exceeds_thermal_flag` (project_mw > MIN(MLSE.rating_normal)), `nameplate_to_maxgen_ratio` (overbuild detection)
- Built drift detection system comparing recent 50-prediction FAIL rate against training baseline — alerts and triggers retraining when deviation exceeds 15%; implemented `--action retrain` CLI to append new Oracle-labeled rows and retrain with full pipeline
- Wrote feature extraction Oracle SQL joining 10+ tables via INR_REFERENCE to compute POIB data quality flags, connectivity node completeness, and thermal margin at POI substation

**Entry / Junior Level Bullets:**
- Built scikit-learn ML pipeline for GINR feasibility prediction using ColumnTransformer (StandardScaler for numerics, OneHotEncoder for categoricals, SimpleImputer for missing values) and Logistic Regression with `class_weight='balanced'` to handle pass/fail imbalance
- Created `generate_ginr_synthetic_data.py` generating 1,000+ realistic GINR training records spanning all 5 resource types (Solar, Wind, Conventional, ESR, Battery), 5 TDSPs, and 4 CMZs with injected failure patterns for each of the 20 features
- Implemented model versioning system: semantic version auto-increment (v1.0, v1.1…), joblib serialization with metadata JSON, `latest.json` pointer, and metrics history log for ROC-AUC/CV score tracking across training runs

---

### 🔷 Use Case 2 — GINR Payment Failure Monitor (Daily Scheduler)

> **Context:** Designed and built a Python-based automated payment failure detection and alerting system for ERCOT's GINR (Generator Interconnection Non-Synchronous Request) process, detecting 7 categories of payment failures daily and delivering actionable reports to operations managers.

**Senior / Lead Level Bullets:**
- Designed and built an end-to-end automated payment monitoring pipeline in Python using APScheduler, pandas, and Oracle DB — detecting 7 categories of payment failures across 100+ daily GINR records and delivering prioritized HTML/CSV reports via SMTP to ERCOT operations managers
- Architected a production-grade `BlockingScheduler` with `CronTrigger` (7:00 AM CST daily), configuring misfire grace period (3600s), job coalescing, and `SIGTERM` signal handling for Docker/systemd graceful shutdown
- Implemented 7 pandas-based vectorized detection rules covering CRITICAL, HIGH, and MEDIUM severity failures: unpaid FIS fees, unpaid Scoping Study fees, analysis fee outstanding, Authorize.net sync errors, amount mismatches, duplicate payments, and stale PENDING_REVIEW CRs
- Designed a rich HTML email notification system with dynamic severity banners, summary stat cards, color-coded failure sections, embedded Oracle verification SQL, and attached CSV reports — auto-escalating subject lines based on failure severity
- Built a comprehensive audit trail appending per-run summaries (failure counts, dollar amounts at risk) to a CSV audit log, enabling trend analysis and operational reporting

**Mid-Level Bullets:**
- Built a Python payment failure analyzer (`payment_failure_analyzer.py`) applying 7 business rules to GINR payment data, flagging failures like Authorize.net sync errors where `DATE_PAID IS NOT NULL` but `FIS_FEE_PAID = FALSE` — preventing blocked studies for generators that already paid
- Configured APScheduler with production-grade settings: daily cron trigger at 07:00 CST, 1-hour misfire grace window, job coalescing to prevent duplicate runs during downtime, and `max_instances=1` to prevent overlapping executions
- Developed an HTML email builder generating rich, responsive MIME emails with severity-coded banners (CRITICAL / HIGH / MEDIUM / ALL CLEAR), tabular failure details capped at 25 rows per section, and full-detail CSV attachment for manager review
- Implemented `--dry-run` and `--now` CLI flags enabling safe testing without SMTP delivery, saving HTML preview files locally for QA and debugging
- Mapped 7 payment failure types to Oracle source tables (`ginr.ginr_request`, `CHANGE_REQUESTS`, `GINR_PAYMENT_DATA_VW`) with actionable remediation steps embedded in each email section

**Entry / Junior Level Bullets:**
- Built a daily APScheduler job in Python to automate GINR payment failure detection, running 7 pandas-based detection rules against Oracle payment data each morning at 7:00 AM CST
- Implemented email notification service using Python `smtplib` to send HTML failure reports with CSV attachments via ERCOT's Office 365 SMTP relay
- Created synthetic test data generator (`generate_payment_data.py`) producing 110 payment records across 7 failure types using realistic ERCOT entity schemas

---

## 🏆 Combined AI/Agentic Development Bullets

> Use these if the job description mentions AI-assisted development, Copilot, or agentic workflows.

- Leveraged **GitHub Copilot agentic workflows** (plan-driven development, subagent execution) to accelerate full-stack feature delivery — translated business requirements into implementation plans, executed multi-file code generation, and validated with automated test runs
- Applied **AI-assisted test-driven development** — used Copilot to generate failing JUnit/Mockito tests first, then implemented production code to pass them, maintaining >90% test coverage on new backend logic
- Adopted **agentic coding patterns** including checkpoint-based plan execution, automated regression verification after each task, and structured commit conventions (`feat(RIOO-2893): ...`) for traceability

---

## 📊 Quantified Impact (Suggested — Tailor to Actuals)

| Metric | Value |
|---|---|
| ML features engineered (GINR Feasibility Model) | 20 (across 4 groups: Project, Fees, RARF Quality, Network) |
| Oracle tables joined for feature extraction | 16 |
| Model performance (ROC-AUC, 5-fold CV) | > 0.85 |
| Risk tiers in scoring output | 4 (LOW / MEDIUM / HIGH / CRITICAL) |
| Flask REST API endpoints | 6 (score, batch, get, health, model/info, drift) |
| Payment failure categories automated | 7 |
| GINR payment records scanned daily | 100+ |
| Report formats generated (payment monitor) | HTML + CSV per daily run |
| Python files in ML system | 5 (pipeline, API, logistic regression, data generator, test) |

---

## 🗂️ Skills Summary for Resume Skills Section

```
Languages:     Java 17, TypeScript, Python 3.10, SQL (Oracle PL/SQL)
ML/AI:         scikit-learn, Logistic Regression, Flask, joblib, Model Versioning, Drift Detection
Frameworks:    Angular 16, JAX-RS/Jersey, JPA/Hibernate, RxJS, APScheduler, pandas, NumPy
Databases:     Oracle Database, cx_Oracle, JPQL (16-table JOIN queries)
Testing:       JUnit 4, Mockito, Model CV evaluation (StratifiedKFold, ROC-AUC)
DevOps:        Docker, Jenkins, Maven, Git
AI Tools:      GitHub Copilot, Agentic AI workflows, Plan-driven development
Protocols:     REST/HTTP (Flask + JAX-RS), SMTP (TLS), JWT/Auth0
Patterns:      ML Pipeline (fit/transform/predict), Repository pattern, TDD
```

---

## 📝 Sample Resume Entry (Full Block)

```
ERCOT — AI Engineer / Senior Full Stack Developer                  Apr 2025 – Present
RIOO-IS / RARF System | Taylor, TX

• Designed and built an end-to-end GINR Feasibility Screening ML system —
  engineering 20 features from 16 Oracle DB tables (POIB_DATA, CONNECTIVITY_NODES,
  MOST_LIMITING_SERIES_ELEMENTS, CONGESTION_MANAGEMENT_ZONES), training a scikit-learn
  Logistic Regression pipeline (ROC-AUC > 0.85, 5-fold CV), and serving real-time
  PASS/FAIL predictions via a Flask microservice integrated with Spring Boot RARF API.

• Architected a full ML lifecycle: versioned model registry (semantic versioning,
  joblib), drift detection (15% FAIL-rate threshold), automated retraining feedback
  loop from Oracle CR status transitions, and 4-tier risk scoring output
  (🟢 LOW / 🟡 MEDIUM / 🟠 HIGH / 🔴 CRITICAL) with top risk factor explanations
  surfaced to developers at submission time.

• Built an automated GINR payment failure monitoring pipeline in Python using
  APScheduler (CronTrigger 7AM CST), pandas (7 detection rules), and Oracle DB —
  scanning 100+ daily records and delivering severity-prioritized HTML/CSV reports
  via Office 365 SMTP with SIGTERM-based graceful shutdown for Docker/systemd.

• Leveraged GitHub Copilot agentic workflows (plan-driven, checkpoint-based
  execution) for full ML system delivery — accelerating multi-file Python code
  generation, Oracle SQL feature engineering, and structured commit traceability.

Tech: Python 3.10, scikit-learn, Flask, pandas, NumPy, joblib, Oracle SQL,
      Java 17, JAX-RS/Jersey, JPA/Hibernate, Angular 16, TypeScript, RxJS,
      APScheduler, smtplib/MIME, cx_Oracle, Docker, Jenkins, Maven,
      GitHub Copilot (Agentic AI)
```

---

*Generated from: GINR Feasibility Screening Model + GINR Payment Failure Monitor*  
*Source files: `docs/superpowers/specs/` + `docs/superpowers/payment-monitor/`*

