# Payment Monitor - Step-by-Step Execution Runbook

**Project:** GINR Payment Failure Monitor  
**Path:** `C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\payment-monitor`  
**Main entrypoint:** `daily_scheduler.py`

---

## 0) 5-Minute Smoke Test (Post-Deploy Quick Validation)

Run this block end-to-end to confirm setup, data pipeline, report generation, and dry-run email path.

```powershell
Set-Location "C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\payment-monitor"
pip install -r requirements.txt
python generate_payment_data.py
python daily_scheduler.py --dry-run
Get-Content .\logs\scheduler.log -Tail 25
Get-Content .\logs\audit.csv -Tail 3
Get-ChildItem .\reports | Sort-Object LastWriteTime -Descending | Select-Object -First 3 Name, LastWriteTime
```

Expected in under 5 minutes:
- `payment_data.csv` regenerated
- one new row in `logs\\audit.csv`
- fresh report files in `reports\\`
- no unhandled exceptions in `logs\\scheduler.log`

For one-shot live email verification after smoke test:

```powershell
python daily_scheduler.py --now
```

---

## 1) What This Project Does

This service scans GINR payment records, applies 7 failure-detection rules, builds an HTML + CSV report, and emails stakeholders.

Main modules:
- `generate_payment_data.py` -> creates synthetic `payment_data.csv` for dev/testing
- `payment_failure_analyzer.py` -> loads data and runs 7 detection rules
- `email_service.py` -> creates report outputs and sends SMTP email (or dry-run)
- `daily_scheduler.py` -> one-shot run or daily scheduled run (APScheduler)
- `config.py` -> environment-driven config for DB, SMTP, schedule, thresholds

---

## 2) Prerequisites

- Python 3.10+ (3.11 also works)
- Access to project folder
- Pip packages:
  - `pandas`
  - `apscheduler`
  - `ollama` (for AI summary in email)
  - `cx_Oracle` (only when Oracle integration is enabled)

Install dependencies:

```powershell
Set-Location "C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\payment-monitor"
pip install pandas apscheduler ollama
```

Optional for Oracle production mode:

```powershell
pip install cx_Oracle
```

---

## 3) Configure Environment Variables (Optional for Local, Required for Live Email/Prod)

The app has defaults in `config.py`, but set real values before live email/prod.

### 3.1 Gmail + Ollama demo mode (recommended for demo)

```powershell
$env:EMAIL_PROVIDER = "gmail"
$env:SMTP_HOST = "smtp.gmail.com"
$env:SMTP_PORT = "587"
$env:SMTP_USER = "yourgmail@gmail.com"
$env:SMTP_PASSWORD = "<gmail-app-password>"
$env:FROM_ADDRESS = "yourgmail@gmail.com"
$env:MANAGER_EMAIL = "yourgmail@gmail.com"
$env:CC_EMAILS = ""

$env:ENABLE_OLLAMA_SUMMARY = "true"
$env:OLLAMA_MODEL = "gemma3:1b"

$env:SCHEDULE_HOUR = "7"
$env:SCHEDULE_MINUTE = "0"
$env:STALE_PENDING_DAYS = "30"
$env:MIN_FEE_THRESHOLD = "1.00"
$env:AMOUNT_VARIANCE_PCT = "0.05"
```

Start Ollama before running scheduler:

```powershell
ollama pull gemma3:1b
```

### 3.2 Office365 mode (existing/default)

```powershell
$env:EMAIL_PROVIDER = "office365"
$env:SMTP_HOST = "smtp.office365.com"
$env:SMTP_PORT = "587"
$env:SMTP_USER = "rioo-alerts@ercot.com"
$env:SMTP_PASSWORD = "<secure-password>"
$env:MANAGER_EMAIL = "manager@ercot.com"
$env:CC_EMAILS = "planner1@ercot.com,planner2@ercot.com"

$env:ENABLE_OLLAMA_SUMMARY = "false"
```

---

## 4) End-to-End Local Execution (Recommended First)

### 4.1 End-to-end execution flow (at a glance)

```text
[generate_payment_data.py or Oracle load]
              |
              v
[payment_failure_analyzer.run_analysis()]
  - load data
  - apply 7 rules
  - aggregate risk + counts
              |
              v
[email_service.send_email()]
  - build HTML
  - (optional) add Ollama executive summary
  - build CSV attachment
  - save reports locally
  - send via Gmail/Office365 SMTP (or skip in dry-run)
              |
              v
[daily_scheduler.py]
  - one-shot (--dry-run / --now) OR
  - scheduled daily run
              |
              v
[artifacts + observability]
  - reports/*.html, reports/*.csv
  - logs/scheduler.log
  - logs/audit.csv
```

### 4.2 Demo end-to-end (Gmail + Ollama)

1. Configure Gmail + Ollama env vars (Section 3.1)
2. Pull Ollama model
3. Generate synthetic data
4. Run dry-run to validate report generation + AI summary
5. Run live one-shot to send test email
6. Review logs and report files

### Step 0 (Demo only): ensure Ollama model is ready

```powershell
ollama pull gemma3:1b
```

### Step 1: Go to project folder

```powershell
Set-Location "C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\payment-monitor"
```

### Step 2: Generate synthetic data

```powershell
python generate_payment_data.py
```

Expected:
- `payment_data.csv` created
- Console prints clean/failure counts

### Step 3: Run one-shot dry-run (no real email send)

```powershell
python daily_scheduler.py --dry-run
```

Expected outputs:
- `reports\payment_report_<date>.html`
- `reports\GINR_Payment_Failures_<date>.csv`
- `logs\audit.csv` appended
- `logs\scheduler.log` updated
- If `ENABLE_OLLAMA_SUMMARY=true`, HTML includes **AI Executive Summary (Ollama)**

### Step 4: Validate outputs

```powershell
Get-ChildItem .\reports
Get-Content .\logs\scheduler.log -Tail 50
Get-Content .\logs\audit.csv -Tail 5
```

### Step 5: Run one-shot live email test (Gmail)

```powershell
python daily_scheduler.py --now
```

Expected:
- Gmail email received by `MANAGER_EMAIL` (and CC recipients if configured)
- Subject reflects detected severity (critical/high/all clear)
- Same HTML/CSV files available under `reports\`

### Step 6: Start daily schedule (continuous mode)

```powershell
python daily_scheduler.py
```

Expected:
- Scheduler starts and waits for next configured cron time
- Every run appends one row to `logs\audit.csv`

---

## 5) Live Execution Modes

### A) One-shot live execution now (sends email)

```powershell
python daily_scheduler.py --now
```

Use when you want to manually trigger one complete cycle immediately.

### B) Persistent daily scheduler mode

```powershell
python daily_scheduler.py
```

Behavior:
- Schedules daily at `SCHEDULE_HOUR:SCHEDULE_MINUTE` in `America/Chicago`
- Uses misfire/coalesce/max_instances controls from `daily_scheduler.py`

---

## 6) Safe Stop / Shutdown

- Foreground mode: press `Ctrl+C`
- For service-managed shutdown (`SIGTERM`), scheduler performs graceful stop

If process needs force termination, identify Python process and stop it:

```powershell
Get-Process python
Stop-Process -Id <PID>
```

---

## 7) Operations Verification Checklist

After each run verify:
- `logs\scheduler.log` has job start + completion
- `logs\audit.csv` has a new row for the run date
- `reports\payment_report_<date>.html` exists
- `reports\GINR_Payment_Failures_<date>.csv` exists
- Email status is `sent` (live) or `dry_run` (test)

---

## 8) Common Troubleshooting

### Error: `ModuleNotFoundError: No module named 'apscheduler'`

```powershell
pip install apscheduler
```

### Error: `Data file not found ... payment_data.csv`

```powershell
python generate_payment_data.py
```

### SMTP auth failure / cannot send email
- Verify `$env:SMTP_USER` and `$env:SMTP_PASSWORD`
- Verify SMTP host/port and TLS connectivity
- Run dry-run to validate report generation without SMTP

```powershell
python daily_scheduler.py --dry-run
```

### Unexpected high/low failures
- Inspect `payment_data.csv`
- Validate threshold variables: `STALE_PENDING_DAYS`, `MIN_FEE_THRESHOLD`, `AMOUNT_VARIANCE_PCT`

### Ollama summary not visible in report
- Confirm env var: `$env:ENABLE_OLLAMA_SUMMARY = "true"`
- Confirm package: `pip install ollama`
- Confirm model is available: `ollama pull gemma3:1b`
- If Ollama is unavailable, report still sends without AI block

### Gmail authentication failed
- Use **Google App Password**, not your regular Gmail password
- Confirm account allows app-password based SMTP access
- Validate settings:

```powershell
$env:EMAIL_PROVIDER = "gmail"
$env:SMTP_HOST = "smtp.gmail.com"
$env:SMTP_PORT = "587"
```

---

## 9) Production Cutover Notes

1. Keep scheduler in dry-run for 1-3 days and validate outputs.
2. Replace CSV `load_data()` path in `payment_failure_analyzer.py` with Oracle query logic.
3. Validate Oracle row counts vs expected daily volume.
4. Switch to live email (`--now` once), verify recipients/subject/content.
5. Start persistent mode and monitor first 3 scheduled runs.

---

## 10) Daily/Weekly Runbook Activities

### Daily
- Check latest `scheduler.log` entry
- Confirm report files generated
- Confirm no SMTP failures

### Weekly
- Review `audit.csv` trend (failures, critical count, amount at risk)
- Tune thresholds if needed

### Monthly
- Review detection quality with operations team
- Update recipient list, schedule, and thresholds in env/config

---

## 11) Quick Command Block

```powershell
Set-Location "C:\RamKotni\Personal\interview-prep\FINAL-SUBMISSION-2026\docs\superpowers\payment-monitor"
pip install pandas apscheduler ollama
$env:EMAIL_PROVIDER = "gmail"
$env:SMTP_HOST = "smtp.gmail.com"
$env:SMTP_PORT = "587"
$env:SMTP_USER = "yourgmail@gmail.com"
$env:SMTP_PASSWORD = "<gmail-app-password>"
$env:FROM_ADDRESS = "yourgmail@gmail.com"
$env:MANAGER_EMAIL = "yourgmail@gmail.com"
$env:CC_EMAILS = ""
$env:ENABLE_OLLAMA_SUMMARY = "true"
$env:OLLAMA_MODEL = "gemma3:1b"
ollama pull gemma3:1b
python generate_payment_data.py
python daily_scheduler.py --dry-run
python daily_scheduler.py --now
python daily_scheduler.py
```
