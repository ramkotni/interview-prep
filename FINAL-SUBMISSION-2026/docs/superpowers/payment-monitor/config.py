"""
GINR Payment Failure Monitor — Configuration
=============================================
All tunable settings in one place.
For production: load from environment variables or a secrets manager.
"""

import os
from pathlib import Path

# ─────────────────────────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────────────────────────
BASE_DIR    = Path(__file__).parent
LOG_DIR     = BASE_DIR / "logs"
REPORT_DIR  = BASE_DIR / "reports"
DATA_FILE   = BASE_DIR / "payment_data.csv"        # synthetic or Oracle extract
AUDIT_LOG   = BASE_DIR / "logs" / "audit.csv"      # every run recorded here

LOG_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

# ─────────────────────────────────────────────────────────────────
# Oracle Database  (swap in real credentials for production)
# ─────────────────────────────────────────────────────────────────
DB_CONFIG = {
    "host":     os.getenv("ORACLE_HOST",     "localhost"),
    "port":     int(os.getenv("ORACLE_PORT", "1521")),
    "service":  os.getenv("ORACLE_SERVICE",  "RIOO"),
    "user":     os.getenv("ORACLE_USER",     "rarf_user"),
    "password": os.getenv("ORACLE_PASSWORD", "change_me"),
}

# ─────────────────────────────────────────────────────────────────
# Email Configuration
# ─────────────────────────────────────────────────────────────────
EMAIL_PROVIDER = os.getenv("EMAIL_PROVIDER", "office365").lower()
DEFAULT_SMTP_HOST = "smtp.gmail.com" if EMAIL_PROVIDER == "gmail" else "smtp.office365.com"
DEFAULT_FROM = os.getenv("SMTP_USER", "rioo-alerts@ercot.com")

EMAIL_CONFIG = {
    # Provider settings: gmail or office365
    "provider":      EMAIL_PROVIDER,
    "smtp_host":     os.getenv("SMTP_HOST", DEFAULT_SMTP_HOST),
    "smtp_port":     int(os.getenv("SMTP_PORT", "587")),
    "smtp_user":     os.getenv("SMTP_USER", DEFAULT_FROM),
    "smtp_password": os.getenv("SMTP_PASSWORD", "change_me"),
    "use_tls":       os.getenv("SMTP_USE_TLS", "true").lower() == "true",

    # Sender / Recipients
    "from_address":  os.getenv("FROM_ADDRESS", DEFAULT_FROM),
    "manager_email": os.getenv("MANAGER_EMAIL", "manager@ercot.com"),
    "cc_emails":     os.getenv("CC_EMAILS", "planner1@ercot.com,planner2@ercot.com").split(","),
    "reply_to":      os.getenv("REPLY_TO", DEFAULT_FROM),
}

# Optional AI summary using local Ollama
OLLAMA_CONFIG = {
    "enabled": os.getenv("ENABLE_OLLAMA_SUMMARY", "false").lower() == "true",
    "model": os.getenv("OLLAMA_MODEL", "gemma3:1b"),
}

# ─────────────────────────────────────────────────────────────────
# Scheduler Settings
# ─────────────────────────────────────────────────────────────────
SCHEDULE_CONFIG = {
    "run_hour":   int(os.getenv("SCHEDULE_HOUR",   "7")),    # 7:00 AM CST
    "run_minute": int(os.getenv("SCHEDULE_MINUTE", "0")),
    "timezone":   "America/Chicago",
}

# ─────────────────────────────────────────────────────────────────
# Business Rules — Payment Failure Thresholds
# ─────────────────────────────────────────────────────────────────
RULES = {
    # How many days a CR can be in PENDING_REVIEW without payment before alerting
    "stale_pending_days": int(os.getenv("STALE_PENDING_DAYS", "30")),

    # Minimum fee amount to consider a failure (ignore $0 fees)
    "min_fee_threshold": float(os.getenv("MIN_FEE_THRESHOLD", "1.00")),

    # Max payment amount variance before flagging as amount mismatch (%)
    "amount_variance_pct": float(os.getenv("AMOUNT_VARIANCE_PCT", "0.05")),
}

# ─────────────────────────────────────────────────────────────────
# Application Info  (shown in email header)
# ─────────────────────────────────────────────────────────────────
APP_INFO = {
    "name":        "GINR Payment Failure Monitor",
    "version":     "1.0.0",
    "system":      "ERCOT RIOO-IS / RARF",
    "dashboard":   "https://rioo.ercot.com/ginr/payments",
    "support":     "rioo-support@ercot.com",
}
