# GINR Payment Failure Monitor — Architecture

> **System:** ERCOT RIOO-IS / RARF  
> **Version:** 1.0.0  
> **Last Updated:** 2026-05-31

---

## 1. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    GINR Payment Monitor System                      │
│                    (ERCOT RIOO-IS / RARF)                           │
└─────────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │  daily_scheduler  │  ← Entry Point
                    │   (APScheduler)   │
                    │  BlockingScheduler│
                    │  Every day 7AM CST│
                    └────────┬──────────┘
                             │ triggers
              ┌──────────────▼───────────────┐
              │     run_daily_payment_check() │
              └──────┬───────────────────┬───┘
                     │                   │
          ┌──────────▼──────┐   ┌────────▼──────────┐
          │ payment_failure │   │   email_service    │
          │   _analyzer     │   │                   │
          │  run_analysis() │   │  send_email()     │
          └──────┬──────────┘   └────────┬──────────┘
                 │                       │
    ┌────────────▼──────────┐   ┌────────▼──────────────────┐
    │     Data Layer        │   │     Notification Layer     │
    │   load_data()         │   │                           │
    │  CSV (dev) /          │   │  build_html_email()       │
    │  Oracle DB (prod)     │   │  build_csv_attachment()   │
    └────────────┬──────────┘   │  SMTP → Office 365        │
                 │              └───────────────────────────┘
    ┌────────────▼──────────────────────────────────────────┐
    │              7 Detection Rules (pandas)               │
    │  1. detect_fis_fee_unpaid()      → CRITICAL           │
    │  2. detect_ss_fee_unpaid()       → CRITICAL           │
    │  3. detect_analysis_fee_unpaid() → HIGH               │
    │  4. detect_payment_sync_errors() → HIGH               │
    │  5. detect_amount_mismatch()     → HIGH               │
    │  6. detect_duplicate_payments()  → MEDIUM             │
    │  7. detect_stale_pending()       → MEDIUM             │
    └───────────────────────────────────────────────────────┘
```

---

## 2. Component Breakdown

| Module | Role |
|---|---|
| `daily_scheduler.py` | **Orchestrator** — APScheduler (cron), event listeners, graceful shutdown |
| `payment_failure_analyzer.py` | **Business Logic** — runs 7 detection rules, produces structured report |
| `email_service.py` | **Notification** — builds HTML email + CSV attachment, sends via SMTP |
| `config.py` | **Configuration** — DB, SMTP, schedule, business rule thresholds |
| `generate_payment_data.py` | **Test Data Generator** — synthetic CSV replicating Oracle DB schema |

---

## 3. Data Flow (End-to-End)

```
[Oracle DB / CSV]
       │
       ▼
  load_data()          ← pandas DataFrame (payment records)
       │
       ▼
  7 Detection Rules    ← each rule returns failing rows + failure_type
       │
       ▼
  run_analysis()       ← aggregates into structured report dict:
  {                       total_failures, critical_count,
    summary_by_type,      total_at_risk, records[]
    failure_meta
  }
       │
       ▼
  send_email()         ← builds HTML + CSV
       │
       ├── saves  reports/payment_report_<date>.html
       ├── saves  reports/GINR_Payment_Failures_<date>.csv
       └── SMTP → manager@ercot.com + CC list
       │
       ▼
  _write_audit_log()   ← appends to logs/audit.csv (trend tracking)
```

---

## 4. Scheduler Design

```
BlockingScheduler (APScheduler)
├── Trigger      : CronTrigger  — daily at 07:00 America/Chicago (CST)
├── misfire_grace: 3600s        — runs late if server was down (up to 1h)
├── coalesce     : True         — never double-runs missed jobs
├── max_instances: 1            — prevents overlap
└── Event Listeners
    ├── EVENT_JOB_EXECUTED  → logs ✅ success
    ├── EVENT_JOB_ERROR     → logs ❌ failure + traceback
    └── EVENT_JOB_MISSED    → logs ⚠️ warning with scheduled time
```

---

## 5. Payment Failure Detection Rules

| # | Rule | Severity | Oracle Source | Condition |
|---|---|---|---|---|
| 1 | `FIS_FEE_UNPAID` | 🔴 CRITICAL | `ginr.ginr_request.FIS_FEE_PAID` | `fis_fee > 0` AND `fis_fee_paid = FALSE` AND `status IN (2,3)` |
| 2 | `SS_FEE_UNPAID` | 🔴 CRITICAL | `ginr.ginr_request.SS_FEE_PAID` | `ss_fee > 0` AND `ss_fee_paid = FALSE` AND `status IN (2,3)` |
| 3 | `ANALYSIS_FEE_UNPAID` | 🟠 HIGH | `CHANGE_REQUESTS.ANALYSIS_FEE_PAID` | `analysis_fee > 0` AND `analysis_fee_paid = FALSE` AND `status IN (2,3)` |
| 4 | `PAYMENT_SYNC_ERROR` | 🟠 HIGH | `GINR_PAYMENT_DATA_VW.DATE_PAID` vs `FIS_FEE_PAID` | Transaction exists in gateway but `fis_fee_paid = FALSE` |
| 5 | `AMOUNT_MISMATCH` | 🟠 HIGH | `GINR_PAYMENT_DATA_VW.TOTAL_AMOUNT` | `amount_paid < (fis_fee + ss_fee)` beyond 5% variance |
| 6 | `DUPLICATE_PAYMENT` | 🟡 MEDIUM | `GINR_PAYMENT_DATA_VW` | `COUNT(*) > 1` per `ID_CHANGE_REQUEST` |
| 7 | `STALE_PENDING` | 🟡 MEDIUM | `CHANGE_REQUEST_STATUS` | Status = `PENDING_REVIEW(2)` AND `days_in_pending > 30` AND no payment |

---

## 6. Data Sources (Oracle DB Entities)

| Table / View | Java Entity | Fields Used |
|---|---|---|
| `ginr.ginr_request` | `GinrRequest.java` | `fis_fee`, `fis_fee_paid`, `ss_fee`, `ss_fee_paid` |
| `CHANGE_REQUESTS` | `ChangeRequests.java` | `analysis_fee`, `analysis_fee_paid`, `cr_status_id` |
| `GINR_PAYMENT_DATA_VW` | `GinrPaymentDataVw.java` | `trans_id`, `date_paid`, `total_amount`, `authorization` |
| `CHANGE_REQUEST_STATUS` | — | `PENDING_REVIEW=2`, `IN_REVIEW=3`, `READY_FOR_MODELING=7` |
| `COMPANIES` | — | `company_name`, `duns` |

---

## 7. Email Notification Design

```
┌─────────────────── HTML Email ─────────────────────┐
│ Header: ERCOT RIOO-IS | GINR Payment Monitor        │
│ Alert Banner: 🔴 CRITICAL / 🟠 HIGH / ✅ ALL CLEAR  │
│ Summary Cards: Total Failures | Critical | High     │
│                $ At Risk | Records Scanned          │
│                                                     │
│ Per-Failure Sections (sorted by severity):          │
│  ├── Section header (color-coded)                   │
│  ├── Impact + Required Action + Data Source         │
│  └── Detail table (up to 25 rows; rest in CSV)     │
│                                                     │
│ Oracle Verification Queries (embedded SQL)          │
│ Footer: Dashboard link | Support email              │
└─────────────────────────────────────────────────────┘
      + Attached: GINR_Payment_Failures_<date>.csv
```

### Email Subject Lines (Auto-determined by Severity)

| Condition | Subject Prefix |
|---|---|
| Any CRITICAL failures | `🔴 CRITICAL: N GINR Payment Failures — $X At Risk [date]` |
| HIGH or MEDIUM failures | `⚠️ GINR Payment Report: N Issues Detected [date]` |
| No failures | `✅ GINR Payment Monitor: All Clear [date]` |

---

## 8. Run Modes

| Command | Behavior |
|---|---|
| `python daily_scheduler.py` | Starts persistent scheduler (runs every day 7 AM CST) |
| `python daily_scheduler.py --now` | One-shot run immediately, then exits |
| `python daily_scheduler.py --dry-run` | Analyzes & saves report, **skips** SMTP send |

---

## 9. File System Layout

```
payment-monitor/
├── ARCHITECTURE.md                    ← This document
├── config.py                          ← All settings (env-var driven)
├── daily_scheduler.py                 ← Scheduler + entry point
├── payment_failure_analyzer.py        ← 7 detection rules
├── email_service.py                   ← HTML email + SMTP
├── generate_payment_data.py           ← Synthetic test data generator
├── payment_data.csv                   ← Data source (dev/test)
├── logs/
│   ├── scheduler.log                  ← Scheduler run log
│   └── audit.csv                      ← Trend tracking (every run appended)
└── reports/
    ├── payment_report_<date>.html     ← HTML email preview
    └── GINR_Payment_Failures_<date>.csv  ← Full failure details
```

---

## 10. Configuration (All via Environment Variables)

| Environment Variable | Default | Purpose |
|---|---|---|
| `ORACLE_HOST` | `localhost` | Oracle DB hostname |
| `ORACLE_PORT` | `1521` | Oracle DB port |
| `ORACLE_SERVICE` | `RIOO` | Oracle service name |
| `ORACLE_USER` | `rarf_user` | Oracle DB username |
| `ORACLE_PASSWORD` | `change_me` | Oracle DB password |
| `SMTP_HOST` | `smtp.office365.com` | SMTP relay server |
| `SMTP_PORT` | `587` | SMTP port (STARTTLS) |
| `SMTP_USER` | `rioo-alerts@ercot.com` | SMTP login user |
| `SMTP_PASSWORD` | `change_me` | SMTP password |
| `MANAGER_EMAIL` | `manager@ercot.com` | Primary report recipient |
| `CC_EMAILS` | `planner1@ercot.com,...` | CC recipients (comma-separated) |
| `SCHEDULE_HOUR` | `7` | Hour to run (24h, CST) |
| `SCHEDULE_MINUTE` | `0` | Minute to run |
| `STALE_PENDING_DAYS` | `30` | Days threshold for STALE_PENDING rule |
| `MIN_FEE_THRESHOLD` | `1.00` | Minimum fee amount to consider |
| `AMOUNT_VARIANCE_PCT` | `0.05` | Allowed underpayment variance (5%) |

---

## 11. Audit & Observability

| Output | Location | Purpose |
|---|---|---|
| Scheduler log | `logs/scheduler.log` | Every job start/end, errors, misfire warnings |
| Audit CSV | `logs/audit.csv` | Row per run: date, total_failures, critical, high, at_risk — for trend tracking |
| HTML report | `reports/payment_report_<date>.html` | Visual inspection without email client |
| CSV report | `reports/GINR_Payment_Failures_<date>.csv` | Full failure detail for manager/analyst |

---

## 12. Deployment Notes

- **Production:** Replace `payment_data.csv` with live Oracle `cx_Oracle` queries in `load_data()`.
- **Docker / systemd:** The scheduler handles `SIGTERM` gracefully — it shuts down cleanly without killing in-flight jobs.
- **Dependencies:** `pip install apscheduler pandas cx_Oracle`
- **Python:** 3.10+

