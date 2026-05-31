"""
GINR Payment Failure Analyzer
==============================
Detects 7 categories of payment failures from GINR/RARF data.
Each failure maps directly to actual database entities.

Failure Types:
  1. FIS_FEE_UNPAID       — FIS study fee required but not paid
  2. SS_FEE_UNPAID        — Scoping Study fee not paid
  3. ANALYSIS_FEE_UNPAID  — CR analysis fee outstanding
  4. PAYMENT_SYNC_ERROR   — Authorize.net paid but system flag not updated
  5. AMOUNT_MISMATCH      — Payment amount < required fee amount
  6. DUPLICATE_PAYMENT    — Same GINR has multiple payment records
  7. STALE_PENDING        — CR in PENDING_REVIEW > N days with no payment
"""

import pandas as pd
import datetime
import logging
from pathlib import Path
from config import BASE_DIR, DATA_FILE, AUDIT_LOG, RULES

LOG = logging.getLogger("PaymentAnalyzer")

# ─────────────────────────────────────────────────────────────────────────────
# Severity levels and display metadata
# ─────────────────────────────────────────────────────────────────────────────

FAILURE_META = {
    "FIS_FEE_UNPAID": {
        "severity":    "CRITICAL",
        "color":       "#C0392B",
        "icon":        "🔴",
        "description": "FIS Study Fee Not Paid",
        "impact":      "Full Interconnection Study CANNOT start. Queue position at risk.",
        "action":      "Contact developer immediately. Fee must be received before study begins.",
        "source":      "ginr.ginr_request.FIS_FEE_PAID / FIS_FEE",
    },
    "SS_FEE_UNPAID": {
        "severity":    "CRITICAL",
        "color":       "#C0392B",
        "icon":        "🔴",
        "description": "Scoping Study Fee Not Paid",
        "impact":      "Scoping Study CANNOT begin. CR blocked in queue.",
        "action":      "Contact developer. SS fee required before study assignment.",
        "source":      "ginr.ginr_request.SS_FEE_PAID / SS_FEE",
    },
    "ANALYSIS_FEE_UNPAID": {
        "severity":    "HIGH",
        "color":       "#E67E22",
        "icon":        "🟠",
        "description": "Analysis Fee Outstanding",
        "impact":      "Change Request blocked from progressing to READY_FOR_MODELING.",
        "action":      "Send fee reminder to developer. Escalate if > 15 days outstanding.",
        "source":      "CHANGE_REQUESTS.ANALYSIS_FEE_PAID / ANALYSIS_FEE",
    },
    "PAYMENT_SYNC_ERROR": {
        "severity":    "HIGH",
        "color":       "#E67E22",
        "icon":        "🟠",
        "description": "Payment Gateway Sync Error",
        "impact":      "Authorize.net shows payment received but RIOO fee_paid flag = FALSE. "
                       "Study is blocked even though developer paid.",
        "action":      "URGENT: Update fee_paid flag in RIOO. Contact developer to confirm payment.",
        "source":      "GINR_PAYMENT_DATA_VW.DATE_PAID vs ginr_request.FIS_FEE_PAID",
    },
    "AMOUNT_MISMATCH": {
        "severity":    "HIGH",
        "color":       "#E67E22",
        "icon":        "🟠",
        "description": "Payment Amount Mismatch",
        "impact":      "Amount received is less than required fee. Balance outstanding.",
        "action":      "Invoice developer for balance. Do not start study until full amount received.",
        "source":      "GINR_PAYMENT_DATA_VW.TOTAL_AMOUNT vs ginr_request.FIS_FEE + SS_FEE",
    },
    "DUPLICATE_PAYMENT": {
        "severity":    "MEDIUM",
        "color":       "#F39C12",
        "icon":        "🟡",
        "description": "Duplicate Payment Detected",
        "impact":      "Developer may have been double-charged via Authorize.net. Refund risk.",
        "action":      "Review GINR_PAYMENT_DATA_VW for duplicate TRANS_IDs. Issue refund if confirmed.",
        "source":      "GINR_PAYMENT_DATA_VW — multiple rows per ID_CHANGE_REQUEST",
    },
    "STALE_PENDING": {
        "severity":    "MEDIUM",
        "color":       "#F39C12",
        "icon":        "🟡",
        "description": f"Stale Pending > {RULES['stale_pending_days']} Days",
        "impact":      "CR has been in PENDING_REVIEW with no fee or activity for extended period.",
        "action":      "Contact developer to confirm intent. Consider withdrawing abandoned submissions.",
        "source":      "CHANGE_REQUEST_STATUS.PENDING_REVIEW(2) + CHANGE_REQUESTS.created",
    },
}

SEVERITY_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}


# ─────────────────────────────────────────────────────────────────────────────
# Load Data  (CSV for dev/test; swap with Oracle cx_Oracle query in production)
# ─────────────────────────────────────────────────────────────────────────────

def load_data() -> pd.DataFrame:
    """
    Load payment data.
    In production this runs the Oracle SQL from payment_queries.sql.
    For dev/test, reads the synthetic CSV.
    """
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Data file not found: {DATA_FILE}\n"
            "Run: python generate_payment_data.py"
        )
    df = pd.read_csv(DATA_FILE)
    LOG.info(f"Loaded {len(df)} payment records from {DATA_FILE.name}")
    return df


# ─────────────────────────────────────────────────────────────────────────────
# Detection Rules  (one function per failure type)
# ─────────────────────────────────────────────────────────────────────────────

def detect_fis_fee_unpaid(df: pd.DataFrame) -> pd.DataFrame:
    """
    FIS fee is required (fis_fee > threshold) but fis_fee_paid = False.
    Maps to: ginr.ginr_request.FIS_FEE > 0 AND FIS_FEE_PAID = 0
    """
    mask = (
        (df["fis_fee"] > RULES["min_fee_threshold"]) &
        (df["fis_fee_paid"] == False) &
        (df["cr_status_id"].isin([2, 3]))  # PENDING_REVIEW or IN_REVIEW
    )
    result = df[mask].copy()
    result["failure_type"]   = "FIS_FEE_UNPAID"
    result["amount_at_risk"] = result["fis_fee"]
    return result


def detect_ss_fee_unpaid(df: pd.DataFrame) -> pd.DataFrame:
    """
    SS fee required but not paid.
    Maps to: ginr.ginr_request.SS_FEE > 0 AND SS_FEE_PAID = 0
    """
    mask = (
        (df["ss_fee"] > RULES["min_fee_threshold"]) &
        (df["ss_fee_paid"] == False) &
        (df["cr_status_id"].isin([2, 3]))
    )
    result = df[mask].copy()
    result["failure_type"]   = "SS_FEE_UNPAID"
    result["amount_at_risk"] = result["ss_fee"]
    return result


def detect_analysis_fee_unpaid(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analysis fee on Change Request not paid.
    Maps to: CHANGE_REQUESTS.ANALYSIS_FEE > 0 AND ANALYSIS_FEE_PAID = 0
    """
    mask = (
        (df["analysis_fee"] > RULES["min_fee_threshold"]) &
        (df["analysis_fee_paid"] == False) &
        (df["cr_status_id"].isin([2, 3]))
    )
    result = df[mask].copy()
    result["failure_type"]   = "ANALYSIS_FEE_UNPAID"
    result["amount_at_risk"] = result["analysis_fee"]
    return result


def detect_payment_sync_errors(df: pd.DataFrame) -> pd.DataFrame:
    """
    A payment transaction exists in GINR_PAYMENT_DATA_VW
    but the fee_paid flag in ginr_request is still FALSE.
    """
    mask = (
        (df["payment_trans_id"].notna()) &
        (df["payment_trans_id"] != "") &
        (df["payment_date"].notna()) &
        (df["payment_date"] != "") &
        (df["fis_fee_paid"] == False) &
        (df["fis_fee"] > RULES["min_fee_threshold"])
    )
    result = df[mask].copy()
    result["failure_type"]   = "PAYMENT_SYNC_ERROR"
    result["amount_at_risk"] = result["payment_total"]
    return result


def detect_amount_mismatch(df: pd.DataFrame) -> pd.DataFrame:
    """
    Payment amount received differs from required fee by more than variance threshold.
    Maps to: GINR_PAYMENT_DATA_VW.TOTAL_AMOUNT != (FIS_FEE + SS_FEE)
    """
    required = df["fis_fee"] + df["ss_fee"]
    paid     = df["payment_amount_paid"]
    allowed_variance = required * RULES["amount_variance_pct"]

    mask = (
        (required > RULES["min_fee_threshold"]) &
        (paid > 0) &
        ((required - paid).abs() > allowed_variance) &
        (paid < required)  # only underpayment — overpayment is separate workflow
    )
    result = df[mask].copy()
    result["failure_type"]   = "AMOUNT_MISMATCH"
    result["amount_at_risk"] = required[mask] - paid[mask]
    result["amount_at_risk"] = result["amount_at_risk"].round(2)
    return result


def detect_duplicate_payments(df: pd.DataFrame) -> pd.DataFrame:
    """
    Same CR has multiple payment records in GINR_PAYMENT_DATA_VW.
    Maps to: COUNT(*) > 1 per ID_CHANGE_REQUEST in GINR_PAYMENT_DATA_VW
    """
    mask = df["duplicate_payment"] == True
    result = df[mask].copy()
    result["failure_type"]   = "DUPLICATE_PAYMENT"
    result["amount_at_risk"] = result["payment_amount_paid"]
    return result


def detect_stale_pending(df: pd.DataFrame) -> pd.DataFrame:
    """
    CR has been in PENDING_REVIEW (status=2) for more than N days
    with no payment recorded.
    Maps to: CHANGE_REQUEST_STATUS_ID = 2 AND CREATED < SYSDATE - N
    """
    mask = (
        (df["cr_status_id"] == 2) &
        (df["days_in_pending"] > RULES["stale_pending_days"]) &
        ((df["payment_date"].isna()) | (df["payment_date"] == ""))
    )
    result = df[mask].copy()
    result["failure_type"]   = "STALE_PENDING"
    result["amount_at_risk"] = result["fis_fee"] + result["ss_fee"]
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Main Analysis Orchestrator
# ─────────────────────────────────────────────────────────────────────────────

def run_analysis() -> dict:
    """
    Run all 7 detection rules. Returns structured report dict.
    """
    LOG.info("=" * 60)
    LOG.info("GINR PAYMENT FAILURE ANALYSIS — Starting")
    LOG.info(f"Run date: {datetime.date.today()}")
    LOG.info("=" * 60)

    df = load_data()

    detectors = [
        detect_fis_fee_unpaid,
        detect_ss_fee_unpaid,
        detect_analysis_fee_unpaid,
        detect_payment_sync_errors,
        detect_amount_mismatch,
        detect_duplicate_payments,
        detect_stale_pending,
    ]

    all_failures = []
    summary_by_type = {}

    for detector in detectors:
        result = detector(df)
        if not result.empty:
            ftype = result["failure_type"].iloc[0]
            count = len(result)
            total_at_risk = result["amount_at_risk"].sum()
            all_failures.append(result)
            summary_by_type[ftype] = {
                "count":        count,
                "amount_at_risk": round(total_at_risk, 2),
                "severity":     FAILURE_META[ftype]["severity"],
                "records":      result.to_dict("records"),
            }
            LOG.info(f"  {FAILURE_META[ftype]['icon']}  {ftype:30s}: {count:3d} records  ${total_at_risk:>12,.2f} at risk")
        else:
            ftype_name = detector.__name__.replace("detect_", "").upper()
            LOG.info(f"  ✅  {ftype_name:30s}: 0 records  — clean")

    combined = pd.concat(all_failures, ignore_index=True) if all_failures else pd.DataFrame()

    total_failures   = len(combined)
    total_at_risk    = combined["amount_at_risk"].sum() if not combined.empty else 0.0
    critical_count   = sum(v["count"] for v in summary_by_type.values() if v["severity"] == "CRITICAL")
    high_count       = sum(v["count"] for v in summary_by_type.values() if v["severity"] == "HIGH")

    report = {
        "run_date":         datetime.date.today().isoformat(),
        "run_timestamp":    datetime.datetime.now().isoformat(),
        "total_records":    len(df),
        "total_failures":   total_failures,
        "total_at_risk":    round(total_at_risk, 2),
        "critical_count":   critical_count,
        "high_count":       high_count,
        "summary_by_type":  summary_by_type,
        "failure_meta":     FAILURE_META,
        "has_failures":     total_failures > 0,
    }

    LOG.info("-" * 60)
    LOG.info(f"TOTAL FAILURES  : {total_failures}")
    LOG.info(f"CRITICAL        : {critical_count}")
    LOG.info(f"HIGH            : {high_count}")
    LOG.info(f"TOTAL AT RISK   : ${total_at_risk:,.2f}")
    LOG.info("=" * 60)

    _write_audit_log(report)
    return report


def _write_audit_log(report: dict):
    """Append summary to audit log CSV for trend tracking."""
    import csv
    write_header = not AUDIT_LOG.exists()
    with open(AUDIT_LOG, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["run_date", "run_timestamp", "total_records",
                             "total_failures", "critical_count", "high_count", "total_at_risk"])
        writer.writerow([
            report["run_date"], report["run_timestamp"],
            report["total_records"], report["total_failures"],
            report["critical_count"], report["high_count"],
            report["total_at_risk"]
        ])
