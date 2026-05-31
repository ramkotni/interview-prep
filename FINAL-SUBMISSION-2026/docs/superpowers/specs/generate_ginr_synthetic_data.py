"""
GINR Feasibility Screening — Synthetic Training Data Generator
==============================================================
Generates 300 realistic records (180 PASS / 120 FAIL) directly usable
for Logistic Regression training.

All values are based on actual ERCOT GINR/RARF codebase entity fields:
  - ginr.ginr_request  (GinrRequest.java)
  - POIB_DATA          (PoibData.java)
  - CONNECTIVITY_NODES (ConnectivityNodes.java)
  - MOST_LIMITING_SERIES_ELEMENTS (MostLimitingSeriesElements.java)
  - SUBSTATIONS        (Substations.java)
  - GINR_PAYMENT_DATA_VW (GinrPaymentDataVw.java)
  - CHANGE_REQUEST_STATUS enum: SENT_BACK=4, WITHDRAWN=5, READY_FOR_MODELING=7

Run:
    python generate_ginr_synthetic_data.py

Output:
    ginr_feasibility_training_data.csv   (300 rows, ready for sklearn)
"""

import random
import math
import csv
import os

random.seed(42)

# ─────────────────────────────────────────────
# Lookup value pools  (matches actual codebase)
# ─────────────────────────────────────────────
RESOURCE_TYPES = ["SOLAR", "WIND", "CONVENTIONAL", "ESR", "BATTERY"]
INR_TYPES      = ["FIS", "SS", "FIS_SS"]
LEAD_TDSPS     = ["ONCOR", "CENTERPOINT", "TNMP", "AEP", "SHARYLAND"]
CMZ_NAMES      = ["LZ_WEST", "LZ_NORTH", "LZ_HOUSTON", "LZ_SOUTH"]

# Voltage levels actually used in ERCOT (kilovolts)
VOLTAGE_LEVELS = [69, 115, 138, 230, 345, 500]

# ─────────────────────────────────────────────
# Helper functions
# ─────────────────────────────────────────────

def weighted_choice(choices, weights):
    total = sum(weights)
    r = random.uniform(0, total)
    cumulative = 0
    for choice, weight in zip(choices, weights):
        cumulative += weight
        if r <= cumulative:
            return choice
    return choices[-1]


def clamp(val, lo, hi):
    return max(lo, min(hi, val))


# ─────────────────────────────────────────────
# Core row generation
# ─────────────────────────────────────────────

def make_pass_record(ginr_id):
    """
    SUCCESS scenario — project clears all feasibility gates.
    Based on real patterns: reasonable MW, good RARF data,
    fees paid, no prior returns, non-CREZ or ample thermal margin.
    Label: feasibility_pass = 1
    """
    # ── GROUP A: GINR Project ──────────────────────────────────────────
    resource_type = weighted_choice(
        RESOURCE_TYPES, [30, 25, 20, 15, 10]  # all types can pass
    )

    # Voltage level: higher voltage = more capacity = easier to pass
    poi_voltage_kv = weighted_choice(
        VOLTAGE_LEVELS, [5, 15, 25, 25, 20, 10]
    )

    # Project MW: sized appropriately for voltage
    voltage_mw_cap = {69: 80, 115: 200, 138: 300, 230: 600, 345: 900, 500: 1500}
    max_mw = voltage_mw_cap[poi_voltage_kv]
    project_mw = round(random.uniform(20, max_mw * 0.75), 1)

    # Nameplate slightly above operating (realistic overbuild 1.0–1.2)
    nameplate_to_maxgen_ratio = round(random.uniform(1.0, 1.20), 3)

    # INR type: SS-only projects have simpler reviews → more pass
    inr_type = weighted_choice(INR_TYPES, [35, 45, 20])

    # TDSP: CenterPoint/Sharyland slightly fewer pass issues
    lead_tdsp = weighted_choice(LEAD_TDSPS, [22, 25, 18, 20, 15])

    # CREZ: pass scenarios lean toward non-CREZ
    crez_flag = weighted_choice([0, 1], [70, 30])

    # Months to COD: realistic 30–60 months
    months_to_cod = round(random.uniform(28, 62), 1)

    # Zero or very low resubmission count for pass
    resubmission_count = weighted_choice([0, 1], [90, 10])

    # ── GROUP B: Fee / Process ─────────────────────────────────────────
    fis_fee_paid      = 1
    ss_fee_paid       = 1
    payment_made_flag = 1

    # ── GROUP C: RARF Data Quality ─────────────────────────────────────
    missing_poib_flag          = 0
    poi_voltage_mismatch_flag  = 0  # POIB voltage matches POI voltage
    duplicate_substation_flag  = 0
    null_connectivity_node_flag = 0
    orphan_node_flag            = 0

    # ── GROUP D: Network Constraints ───────────────────────────────────
    # Thermal margin well above project MW for pass
    thermal_margin_mw = round(project_mw * random.uniform(1.25, 2.80), 1)
    project_exceeds_thermal_flag = 0  # PASS: project < thermal margin

    # CMZ: passes lean away from congested LZ_WEST
    cmz_name = weighted_choice(CMZ_NAMES, [15, 35, 30, 20])

    return build_row(
        ginr_id, resource_type, project_mw, poi_voltage_kv, inr_type,
        nameplate_to_maxgen_ratio, lead_tdsp, crez_flag, months_to_cod,
        resubmission_count, fis_fee_paid, ss_fee_paid, payment_made_flag,
        missing_poib_flag, poi_voltage_mismatch_flag, duplicate_substation_flag,
        null_connectivity_node_flag, orphan_node_flag,
        thermal_margin_mw, project_exceeds_thermal_flag, cmz_name,
        label=1
    )


def make_fail_record(ginr_id):
    """
    FAILURE scenario — project is Sent Back or Withdrawn.
    Based on real ERCOT failure patterns grouped into 4 failure archetypes.
    Label: feasibility_pass = 0
    """

    # Pick a failure archetype (real-world failure categories)
    archetype = weighted_choice(
        ["thermal_overload", "rarf_incomplete", "fee_unpaid", "chronic_resubmit"],
        [35, 35, 15, 15]
    )

    # ── GROUP A: GINR Project ──────────────────────────────────────────
    resource_type = weighted_choice(
        RESOURCE_TYPES, [35, 30, 10, 15, 10]  # solar/wind dominate failures
    )

    poi_voltage_kv = weighted_choice(
        VOLTAGE_LEVELS, [20, 25, 25, 15, 10, 5]  # lower voltage → more failures
    )

    voltage_mw_cap = {69: 80, 115: 200, 138: 300, 230: 600, 345: 900, 500: 1500}
    max_mw = voltage_mw_cap[poi_voltage_kv]

    inr_type = weighted_choice(INR_TYPES, [40, 20, 40])  # FIS and FIS+SS fail more
    lead_tdsp = weighted_choice(LEAD_TDSPS, [28, 18, 22, 25, 7])  # Oncor/AEP higher fail
    crez_flag = weighted_choice([0, 1], [40, 60])  # CREZ heavy for fails
    months_to_cod = round(random.uniform(10, 72), 1)

    # ── Set archetype-specific values ─────────────────────────────────

    if archetype == "thermal_overload":
        # Project too big for the transmission wire
        project_mw               = round(random.uniform(max_mw * 0.9, max_mw * 1.8), 1)
        nameplate_to_maxgen_ratio = round(random.uniform(1.1, 1.6), 3)
        resubmission_count        = weighted_choice([0, 1, 2], [50, 30, 20])
        fis_fee_paid              = 1
        ss_fee_paid               = 1
        payment_made_flag         = 1
        missing_poib_flag          = 0
        poi_voltage_mismatch_flag  = weighted_choice([0, 1], [60, 40])
        duplicate_substation_flag  = 0
        null_connectivity_node_flag = 0
        orphan_node_flag            = 0
        thermal_margin_mw          = round(project_mw * random.uniform(0.40, 0.85), 1)
        project_exceeds_thermal_flag = 1

    elif archetype == "rarf_incomplete":
        # POIB or connectivity data missing / wrong
        project_mw               = round(random.uniform(20, max_mw * 0.70), 1)
        nameplate_to_maxgen_ratio = round(random.uniform(1.0, 1.25), 3)
        resubmission_count        = weighted_choice([0, 1, 2, 3], [30, 30, 25, 15])
        fis_fee_paid              = 1
        ss_fee_paid               = 1
        payment_made_flag         = 1
        # RARF data quality issues
        missing_poib_flag          = weighted_choice([0, 1], [30, 70])
        poi_voltage_mismatch_flag  = weighted_choice([0, 1], [40, 60])
        duplicate_substation_flag  = weighted_choice([0, 1], [50, 50])
        null_connectivity_node_flag = weighted_choice([0, 1], [35, 65])
        orphan_node_flag            = weighted_choice([0, 1], [45, 55])
        # Thermal margin might be OK — the issue is data quality
        thermal_margin_mw          = round(project_mw * random.uniform(1.1, 2.5), 1)
        project_exceeds_thermal_flag = 0

    elif archetype == "fee_unpaid":
        # Fees not paid — study cannot start
        project_mw               = round(random.uniform(30, max_mw * 0.65), 1)
        nameplate_to_maxgen_ratio = round(random.uniform(1.0, 1.15), 3)
        resubmission_count        = weighted_choice([0, 1], [70, 30])
        fis_fee_paid              = weighted_choice([0, 1], [75, 25])
        ss_fee_paid               = weighted_choice([0, 1], [70, 30])
        payment_made_flag         = 0  # No Authorize.net record
        missing_poib_flag          = weighted_choice([0, 1], [60, 40])
        poi_voltage_mismatch_flag  = 0
        duplicate_substation_flag  = 0
        null_connectivity_node_flag = weighted_choice([0, 1], [65, 35])
        orphan_node_flag            = 0
        thermal_margin_mw          = round(project_mw * random.uniform(1.2, 2.0), 1)
        project_exceeds_thermal_flag = 0

    else:  # chronic_resubmit
        # Developer keeps getting sent back — systemic issues
        project_mw               = round(random.uniform(50, max_mw), 1)
        nameplate_to_maxgen_ratio = round(random.uniform(1.15, 1.50), 3)
        resubmission_count        = weighted_choice([2, 3, 4, 5], [35, 30, 20, 15])
        fis_fee_paid              = 1
        ss_fee_paid               = 1
        payment_made_flag         = 1
        missing_poib_flag          = weighted_choice([0, 1], [40, 60])
        poi_voltage_mismatch_flag  = weighted_choice([0, 1], [45, 55])
        duplicate_substation_flag  = weighted_choice([0, 1], [55, 45])
        null_connectivity_node_flag = weighted_choice([0, 1], [50, 50])
        orphan_node_flag            = weighted_choice([0, 1], [50, 50])
        thermal_margin_mw          = round(project_mw * random.uniform(0.80, 1.30), 1)
        project_exceeds_thermal_flag = 1 if project_mw > thermal_margin_mw else 0

    # CMZ: failures heavily skew toward congested zones
    cmz_name = weighted_choice(CMZ_NAMES, [40, 25, 20, 15])
    months_to_cod = clamp(months_to_cod, 6, 120)

    return build_row(
        ginr_id, resource_type, project_mw, poi_voltage_kv, inr_type,
        nameplate_to_maxgen_ratio, lead_tdsp, crez_flag, months_to_cod,
        resubmission_count, fis_fee_paid, ss_fee_paid, payment_made_flag,
        missing_poib_flag, poi_voltage_mismatch_flag, duplicate_substation_flag,
        null_connectivity_node_flag, orphan_node_flag,
        thermal_margin_mw, project_exceeds_thermal_flag, cmz_name,
        label=0
    )


def build_row(ginr_id, resource_type, project_mw, poi_voltage_kv, inr_type,
              nameplate_to_maxgen_ratio, lead_tdsp, crez_flag, months_to_cod,
              resubmission_count, fis_fee_paid, ss_fee_paid, payment_made_flag,
              missing_poib_flag, poi_voltage_mismatch_flag, duplicate_substation_flag,
              null_connectivity_node_flag, orphan_node_flag,
              thermal_margin_mw, project_exceeds_thermal_flag, cmz_name,
              label):
    return {
        # ── Identifiers ──────────────────────────────────────────────────
        "ginr_request_id": ginr_id,
        "inr_id": f"INR24-{ginr_id:04d}",

        # ── GROUP A: GINR Project ────────────────────────────────────────
        # Source: ginr.ginr_request columns
        "resource_type":            resource_type,          # ID_TECHNOLOGY_TYPE
        "project_mw":               project_mw,             # MAX_GEN_MW
        "poi_voltage_kv":           poi_voltage_kv,         # POI_VOLTAGE
        "inr_type":                 inr_type,               # ID_INR_TYPE
        "nameplate_to_maxgen_ratio": nameplate_to_maxgen_ratio,  # MAX_NAMEPLATE_MW_GEN/MAX_GEN_MW
        "lead_tdsp":                lead_tdsp,              # ID_LEAD_TDSP
        "crez_flag":                crez_flag,              # Derived: COUNTY/LATITUDE/LONGITUDE
        "months_to_cod":            months_to_cod,          # COMMERCIAL_OPERATION_DATE - SUBMIT_DATE
        "resubmission_count":       resubmission_count,     # RETURNED_TO_IE

        # ── GROUP B: Fee / Process ────────────────────────────────────────
        # Source: ginr_request + GINR_PAYMENT_DATA_VW
        "fis_fee_paid":             fis_fee_paid,           # FIS_FEE_PAID
        "ss_fee_paid":              ss_fee_paid,            # SS_FEE_PAID
        "payment_made_flag":        payment_made_flag,      # GINR_PAYMENT_DATA_VW.DATE_PAID IS NOT NULL

        # ── GROUP C: RARF Data Quality ────────────────────────────────────
        # Source: POIB_DATA + CONNECTIVITY_NODES + CONNECTIVITY_TERMINALS via INR_REFERENCE
        "missing_poib_flag":           missing_poib_flag,          # COUNT(POIB_DATA via INR_REF) = 0
        "poi_voltage_mismatch_flag":   poi_voltage_mismatch_flag,  # POIB_DATA.VOLTAGE != ginr.POI_VOLTAGE
        "duplicate_substation_flag":   duplicate_substation_flag,  # duplicate POIB_SUBSTATION_ID
        "null_connectivity_node_flag": null_connectivity_node_flag, # COUNT(CONNECTIVITY_NODES) = 0
        "orphan_node_flag":            orphan_node_flag,            # CONNECTIVITY_NODES with 0 TERMINALS

        # ── GROUP D: Network / Electrical Constraints ─────────────────────
        # Source: MOST_LIMITING_SERIES_ELEMENTS + CONGESTION_MANAGEMENT_ZONES
        "thermal_margin_mw":           thermal_margin_mw,           # MIN(RATING_NORMAL) at POI substation
        "project_exceeds_thermal_flag": project_exceeds_thermal_flag, # project_mw > thermal_margin_mw
        "cmz_name":                    cmz_name,                     # CONGESTION_MANAGEMENT_ZONES.NAME

        # ── TARGET LABEL ──────────────────────────────────────────────────
        # 1 = PASS (READY_FOR_MODELING/MERGED/MODELED/ERCOT_ACCEPTED)
        # 0 = FAIL (SENT_BACK/WITHDRAWN/ERCOT_REJECTED or returnedToIe > 0)
        "feasibility_pass": label
    }


# ─────────────────────────────────────────────
# Generate dataset: 180 PASS + 120 FAIL = 300 rows
# ─────────────────────────────────────────────

rows = []
ginr_id = 1001

# 180 PASS records
for _ in range(180):
    rows.append(make_pass_record(ginr_id))
    ginr_id += 1

# 120 FAIL records
for _ in range(120):
    rows.append(make_fail_record(ginr_id))
    ginr_id += 1

# Shuffle so PASS/FAIL are mixed
random.shuffle(rows)

# ─────────────────────────────────────────────
# Write CSV
# ─────────────────────────────────────────────

output_file = os.path.join(os.path.dirname(__file__), "ginr_feasibility_training_data.csv")

fieldnames = [
    "ginr_request_id", "inr_id",
    # GROUP A
    "resource_type", "project_mw", "poi_voltage_kv", "inr_type",
    "nameplate_to_maxgen_ratio", "lead_tdsp", "crez_flag",
    "months_to_cod", "resubmission_count",
    # GROUP B
    "fis_fee_paid", "ss_fee_paid", "payment_made_flag",
    # GROUP C
    "missing_poib_flag", "poi_voltage_mismatch_flag",
    "duplicate_substation_flag", "null_connectivity_node_flag", "orphan_node_flag",
    # GROUP D
    "thermal_margin_mw", "project_exceeds_thermal_flag", "cmz_name",
    # TARGET
    "feasibility_pass"
]

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ Generated {len(rows)} rows → {output_file}")

# ─────────────────────────────────────────────
# Quick distribution summary
# ─────────────────────────────────────────────

pass_count = sum(1 for r in rows if r["feasibility_pass"] == 1)
fail_count = len(rows) - pass_count

print(f"\n📊 Label Distribution:")
print(f"   PASS (1): {pass_count} rows ({100*pass_count//len(rows)}%)")
print(f"   FAIL (0): {fail_count} rows ({100*fail_count//len(rows)}%)")

print(f"\n📊 Resource Type Distribution:")
from collections import Counter
rt_counts = Counter(r["resource_type"] for r in rows)
for k, v in sorted(rt_counts.items()):
    print(f"   {k:15s}: {v}")

print(f"\n📊 CMZ Distribution:")
cmz_counts = Counter(r["cmz_name"] for r in rows)
for k, v in sorted(cmz_counts.items()):
    print(f"   {k:15s}: {v}")

print(f"\n📊 FAIL Breakdown by key flags:")
fail_rows = [r for r in rows if r["feasibility_pass"] == 0]
print(f"   thermal_overload (project_exceeds_thermal=1):   {sum(1 for r in fail_rows if r['project_exceeds_thermal_flag']==1)}")
print(f"   missing_poib_flag = 1:                          {sum(1 for r in fail_rows if r['missing_poib_flag']==1)}")
print(f"   null_connectivity_node_flag = 1:                {sum(1 for r in fail_rows if r['null_connectivity_node_flag']==1)}")
print(f"   resubmission_count >= 2:                        {sum(1 for r in fail_rows if r['resubmission_count']>=2)}")
print(f"   payment_made_flag = 0:                          {sum(1 for r in fail_rows if r['payment_made_flag']==0)}")
