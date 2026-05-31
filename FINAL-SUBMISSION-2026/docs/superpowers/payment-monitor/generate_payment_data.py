"""
GINR Payment Data Generator — Synthetic Data
=============================================
Generates realistic synthetic payment records based on actual RARF/GINR entities:

  GinrPaymentDataVw   → GINR_PAYMENT_DATA_VW  (payment transactions)
  GinrRequest         → ginr.ginr_request      (fis_fee_paid, ss_fee_paid, fis_fee, ss_fee)
  ChangeRequests      → CHANGE_REQUESTS        (analysis_fee, analysis_fee_paid)
  ChangeRequestStatus → CHANGE_REQUEST_STATUS  (status: PENDING_REVIEW=2, IN_REVIEW=3, etc.)
  Companies           → COMPANIES              (company name, DUNS)

Run: python generate_payment_data.py
Output: payment_data.csv
"""

import csv
import random
import datetime
from pathlib import Path

random.seed(99)

# ── Lookup data matching actual ERCOT entities ──────────────────────────────
COMPANIES = [
    ("NextEra Energy Resources",       "00-789-4561"), ("Luminant Generation",    "00-123-9876"),
    ("Calpine Corporation",            "00-456-1234"), ("EDF Renewables",         "00-321-6549"),
    ("Invenergy",                      "00-654-3217"), ("Orion Energy LLC",       "00-147-8523"),
    ("SunPower Development",           "00-258-9630"), ("Pattern Energy Group",   "00-369-7410"),
    ("Apex Clean Energy",              "00-741-8520"), ("Clearway Energy Group",  "00-852-9630"),
    ("8minutenergy",                   "00-963-7410"), ("AES Clean Energy",       "00-159-8520"),
    ("Terraform Power",                "00-357-9510"), ("Vesper Energy",          "00-486-1230"),
    ("sPower",                         "00-753-9870"),
]

RESOURCE_TYPES  = ["SOLAR", "WIND", "CONVENTIONAL", "ESR", "BATTERY"]
CR_STATUSES     = {
    2: "PENDING_REVIEW", 3: "IN_REVIEW", 4: "SENT_BACK",
    6: "RESUBMITTED",    7: "READY_FOR_MODELING"
}
FEE_SCHEDULE    = {"FIS": 10000.00, "SS": 5000.00, "FIS_SS": 15000.00, "ANALYSIS": 7500.00}


def rand_date(days_back_min=1, days_back_max=180):
    today = datetime.date.today()
    delta = random.randint(days_back_min, days_back_max)
    return (today - datetime.timedelta(days=delta)).strftime("%Y-%m-%d")


def rand_trans_id():
    return f"AUTH-{random.randint(10000000, 99999999)}"


def make_record(ginr_id, failure_type=None):
    company_name, duns = random.choice(COMPANIES)
    resource_type       = random.choice(RESOURCE_TYPES)
    inr_type            = random.choice(["FIS", "SS", "FIS_SS"])
    cr_id               = ginr_id * 10 + random.randint(1, 9)
    submit_date         = rand_date(30, 180)

    fis_fee = FEE_SCHEDULE["FIS"] if inr_type in ["FIS", "FIS_SS"] else 0.0
    ss_fee  = FEE_SCHEDULE["SS"]  if inr_type in ["SS",  "FIS_SS"] else 0.0
    analysis_fee        = FEE_SCHEDULE["ANALYSIS"]

    # Default: clean record (PASS)
    fis_fee_paid        = True  if fis_fee  > 0 else False
    ss_fee_paid         = True  if ss_fee   > 0 else False
    analysis_fee_paid   = True
    payment_trans_id    = rand_trans_id()
    payment_total       = fis_fee + ss_fee
    payment_date        = rand_date(1, 30)
    payment_amount_paid = payment_total
    cr_status_id        = random.choice([3, 7])  # IN_REVIEW or READY_FOR_MODELING
    days_in_pending     = random.randint(1, 20)
    duplicate_payment   = False
    authorization       = rand_trans_id()
    account_type        = random.choice(["Visa", "Mastercard", "ACH"])
    account_last4       = str(random.randint(1000, 9999))
    first_name          = random.choice(["James","Sarah","Michael","Emily","Robert","Lisa"])
    last_name           = random.choice(["Johnson","Smith","Williams","Brown","Davis","Wilson"])
    failure_reason      = ""

    # ── Inject failure patterns ──────────────────────────────────────────────
    if failure_type == "FIS_FEE_UNPAID":
        fis_fee_paid      = False
        payment_trans_id  = ""
        payment_date      = ""
        payment_total     = 0.0
        payment_amount_paid = 0.0
        cr_status_id      = 2  # PENDING_REVIEW — stuck
        days_in_pending   = random.randint(5, 90)
        failure_reason    = f"FIS fee ${fis_fee:,.0f} required but not paid. Study cannot begin."

    elif failure_type == "SS_FEE_UNPAID":
        ss_fee_paid       = False
        payment_trans_id  = ""
        payment_date      = ""
        payment_total     = 0.0
        payment_amount_paid = 0.0
        cr_status_id      = 2  # PENDING_REVIEW — stuck
        days_in_pending   = random.randint(5, 60)
        failure_reason    = f"Scoping Study fee ${ss_fee:,.0f} required but not paid."

    elif failure_type == "ANALYSIS_FEE_UNPAID":
        analysis_fee_paid = False
        payment_trans_id  = ""
        payment_date      = ""
        payment_total     = 0.0
        payment_amount_paid = 0.0
        cr_status_id      = 2
        days_in_pending   = random.randint(3, 45)
        failure_reason    = f"Analysis fee ${analysis_fee:,.0f} outstanding. CR blocked."

    elif failure_type == "PAYMENT_SYNC_ERROR":
        # Authorize.net shows paid but system flag not updated
        fis_fee_paid      = False   # ← system flag wrong
        payment_trans_id  = rand_trans_id()
        payment_date      = rand_date(1, 10)
        payment_amount_paid = fis_fee + ss_fee
        cr_status_id      = 2
        days_in_pending   = random.randint(1, 15)
        failure_reason    = (f"Authorize.net transaction {payment_trans_id} recorded "
                             f"on {payment_date} but fis_fee_paid flag = FALSE. "
                             "Possible sync failure between payment gateway and RIOO.")

    elif failure_type == "AMOUNT_MISMATCH":
        # Paid amount doesn't match required fee
        discount          = random.uniform(0.10, 0.40)
        payment_amount_paid = round(payment_total * (1 - discount), 2)
        cr_status_id      = 3
        days_in_pending   = random.randint(1, 20)
        failure_reason    = (f"Payment recorded: ${payment_amount_paid:,.2f}. "
                             f"Required: ${payment_total:,.2f}. "
                             f"Underpayment of ${payment_total - payment_amount_paid:,.2f}.")

    elif failure_type == "DUPLICATE_PAYMENT":
        duplicate_payment = True
        payment_trans_id  = rand_trans_id()
        payment_date      = rand_date(1, 5)
        payment_amount_paid = payment_total
        cr_status_id      = 3
        failure_reason    = (f"Two payment transactions found for same GINR. "
                             f"Possible double-charge to payer. "
                             f"Second trans: {rand_trans_id()} on {rand_date(1,3)}.")

    elif failure_type == "STALE_PENDING":
        fis_fee_paid      = False
        ss_fee_paid       = False
        payment_trans_id  = ""
        payment_date      = ""
        payment_total     = 0.0
        payment_amount_paid = 0.0
        cr_status_id      = 2
        days_in_pending   = random.randint(31, 120)
        failure_reason    = (f"CR in PENDING_REVIEW for {days_in_pending} days "
                             "with no payment or activity. Potential abandoned submission.")

    return {
        # ── Identifiers ──────────────────────────────────────────────────────
        "ginr_request_id":    ginr_id,
        "inr_id":             f"INR24-{ginr_id:04d}",
        "cr_id":              cr_id,
        "company_name":       company_name,
        "company_duns":       duns,
        "resource_type":      resource_type,
        "inr_type":           inr_type,
        "submit_date":        submit_date,

        # ── GinrRequest fields ────────────────────────────────────────────────
        # Source: ginr.ginr_request  (GinrRequest.java)
        "fis_fee":            fis_fee,            # FIS_FEE
        "fis_fee_paid":       fis_fee_paid,        # FIS_FEE_PAID
        "ss_fee":             ss_fee,             # SS_FEE
        "ss_fee_paid":        ss_fee_paid,         # SS_FEE_PAID

        # ── ChangeRequests fields ─────────────────────────────────────────────
        # Source: CHANGE_REQUESTS  (ChangeRequests.java)
        "analysis_fee":       analysis_fee,       # ANALYSIS_FEE
        "analysis_fee_paid":  analysis_fee_paid,  # ANALYSIS_FEE_PAID
        "cr_status_id":       cr_status_id,
        "cr_status_name":     CR_STATUSES.get(cr_status_id, "UNKNOWN"),
        "days_in_pending":    days_in_pending,

        # ── GinrPaymentDataVw fields ──────────────────────────────────────────
        # Source: GINR_PAYMENT_DATA_VW  (GinrPaymentDataVw.java)
        "payment_trans_id":   payment_trans_id,   # TRANS_ID
        "authorization":      authorization,      # AUTHORIZATION
        "payment_total":      payment_total,      # TOTAL_AMOUNT
        "payment_amount_paid": payment_amount_paid,
        "payment_date":       payment_date,       # DATE_PAID
        "account_type":       account_type,       # ACCOUNT_TYPE
        "account_last4":      account_last4,      # ACCOUNT_NUMBER (masked)
        "first_name":         first_name,         # FIRST_NAME
        "last_name":          last_name,          # LAST_NAME
        "duplicate_payment":  duplicate_payment,

        # ── Failure metadata ──────────────────────────────────────────────────
        "failure_type":   failure_type or "NONE",
        "failure_reason": failure_reason,
        "is_failure":     failure_type is not None,
        "detected_date":  datetime.date.today().strftime("%Y-%m-%d"),
    }


# ── Build dataset ─────────────────────────────────────────────────────────────

rows = []

# Clean records (no failures) — 60 records
for i in range(1001, 1061):
    rows.append(make_record(i, failure_type=None))

# Failure records — 7 types × multiple instances
failure_pool = [
    ("FIS_FEE_UNPAID",      12),
    ("SS_FEE_UNPAID",       8),
    ("ANALYSIS_FEE_UNPAID", 7),
    ("PAYMENT_SYNC_ERROR",  6),
    ("AMOUNT_MISMATCH",     5),
    ("DUPLICATE_PAYMENT",   4),
    ("STALE_PENDING",       8),
]

ginr_id = 2001
for ftype, count in failure_pool:
    for _ in range(count):
        rows.append(make_record(ginr_id, failure_type=ftype))
        ginr_id += 1

random.shuffle(rows)

output = Path(__file__).parent / "payment_data.csv"
fieldnames = list(rows[0].keys())
with open(output, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

total_failures = sum(1 for r in rows if r["is_failure"])
print(f"Generated {len(rows)} records → {output}")
print(f"  Clean    : {len(rows) - total_failures}")
print(f"  Failures : {total_failures}")
for ftype, count in failure_pool:
    print(f"    {ftype:30s}: {count}")
