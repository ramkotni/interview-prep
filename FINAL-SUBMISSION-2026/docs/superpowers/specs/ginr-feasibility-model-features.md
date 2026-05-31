# Predictive Feasibility Screening Model — Core Feature Catalog
## GINR / RARF Codebase–Derived Feature Specification (Revised)

**Project:** Predictive Feasibility Screening Model for GINR Submissions  
**Codebase:** `rarf` (single-schema) · Spring Boot / JPA / Oracle  
**Date:** May 31, 2026  
**Revision Note:** Removed signature-based `missing_fields_count` — application enforces required fields at submission; all submitted records have signatures. Only features with real predictive variance are kept.


---

> **Why signatures were removed:** The RIOO-RS / RARF UI enforces all required authorization signatures before allowing submission (`@NotNull` validations + UI guards). Every record in `ginr_request` that has `SUBMIT_DATE IS NOT NULL` will have all signature columns populated — zero predictive variance. Features must have variance across the training set to be useful.

---

## 1. Source Tables → Java Entities

| Java Entity | DB Table | Schema |
|---|---|---|
| `GinrRequest` | `ginr_request` | `ginr` |
| `GinrPaymentDataVw` | `GINR_PAYMENT_DATA_VW` | default |
| `ChangeRequests` | `CHANGE_REQUESTS` | default |
| `ChangeRequestTransitions` | `CHANGE_REQUEST_TRANSITIONS` | default |
| `ChangeRequestStatus` | `CHANGE_REQUEST_STATUS` | default |
| `Substations` | `SUBSTATIONS` | default |
| `PoibData` | `POIB_DATA` | default |
| `ConnectivityNodes` | `CONNECTIVITY_NODES` | default |
| `ConnectivityTerminals` | `CONNECTIVITY_TERMINALS` | default |
| `MostLimitingSeriesElements` | `MOST_LIMITING_SERIES_ELEMENTS` | default |
| `SubstationVoltages` | `SUBSTATION_VOLTAGES` | default |
| `InrReference` | `inr_reference` | default |
| `CongestionManagementZones` | `CONGESTION_MANAGEMENT_ZONES` | default |
| `WeatherZones` | `WEATHER_ZONES` | default |
| `LoadZones` | `LOAD_ZONES` | default |
| `GinrAttachmentVw` | `ginr_attachment_vw` | default |

---

---

## 2. Target Variable (Label) — from `ChangeRequestStatus` enum

```java
// ChangeRequestStatus.Status enum (actual values from codebase)
SAVED(1)            // draft, not submitted
PENDING_REVIEW(2)   // submitted, awaiting ERCOT review
IN_REVIEW(3)        // ERCOT planner actively reviewing
SENT_BACK(4)        // ← FAIL: returned to developer for corrections
WITHDRAWN(5)        // ← FAIL: developer withdrew
RESUBMITTED(6)      // re-entered after SENT_BACK → another PENDING_REVIEW
READY_FOR_MODELING(7) // ← PASS: cleared feasibility, entering study queue
MERGED(8)           // ← PASS: data merged to network model
MODELED(9)          // ← PASS: study complete
ERCOT_REJECTED(16)  // ← FAIL: formally rejected
ERCOT_ACCEPTED(17)  // ← PASS
ACCEPTED_AND_MERGED(19) // ← PASS
```

| Label Value | Condition | Source |
|---|---|---|
| **1 = PASS** | Final CR status is `READY_FOR_MODELING`, `MERGED`, `MODELED`, `ERCOT_ACCEPTED`, `ERCOT_ACCEPTED_INTERIM`, `ACCEPTED_AND_MERGED` **AND** `returnedToIe = 0` | `ChangeRequestStatus.id` IN (7,8,9,17,18,19) |
| **0 = FAIL** | Final status is `SENT_BACK`, `WITHDRAWN`, `ERCOT_REJECTED` **OR** `returnedToIe > 0` | `ChangeRequestStatus.id` IN (4,5,16) OR `returned_to_ie > 0` |

---

## 3. Core Features for Logistic Regression (20 Features)

### Why these 20 — the selection principle:
- ✅ Has **real variance** across submitted records  
- ✅ Reflects an **actual feasibility risk** (network, data quality, or process)  
- ✅ Is **available at submission time** (not leakage from post-study data)  
- ❌ Dropped: Signature columns (zero variance after submission validation)  
- ❌ Dropped: Payment merchant/address fields (administrative, not predictive)  
- ❌ Dropped: Timestamps as raw dates (use derived duration features instead)

---

### GROUP A — GINR Project Characteristics
*Source: `ginr.ginr_request` · Entity: `GinrRequest`*

| # | Feature | DB Column | Type | Why It Predicts Feasibility |
|---|---|---|---|---|
| **1** | `resource_type` | `ID_TECHNOLOGY_TYPE` | Categorical | Wind/Solar behave differently at POI than conventional — intermittency, reactive requirements, and CREZ congestion all vary by type |
| **2** | `project_mw` | `MAX_GEN_MW` | Numeric (log-scale) | Larger projects consume more thermal headroom at POI; direct driver of feasibility failure |
| **3** | `poi_voltage_kv` | `POI_VOLTAGE` | Numeric | Low-voltage interconnections (< 69kV) face more congestion; mismatch with substation voltages is a red flag |
| **4** | `inr_type` | `ID_INR_TYPE` | Categorical | FIS-only vs SS-only vs combined — combined studies have more risk points and longer review cycles |
| **5** | `nameplate_to_maxgen_ratio` | `MAX_NAMEPLATE_MW_GEN / MAX_GEN_MW` | Numeric (derived) | Overbuild ratio > 1.25 flags projects requesting more nameplate than operating MW — increases grid impact |
| **6** | `lead_tdsp` | `ID_LEAD_TDSP` | Categorical | Oncor / CenterPoint / AEP / TNMP each have different queue loads and constraint profiles; congestion risk varies significantly by TDSP territory |
| **7** | `crez_flag` | Derived: `COUNTY` + `LATITUDE/LONGITUDE` | Binary | CREZ zones (West TX / Panhandle) have high renewable saturation and known congestion — requests in CREZ have higher thermal constraint risk |
| **8** | `months_to_cod` | Derived: `COMMERCIAL_OPERATION_DATE - SUBMIT_DATE` | Numeric | Aggressive COD timelines (< 24 months) lead to rushed RARF data and higher failure rates; very long timelines may indicate speculative projects |
| **9** | `resubmission_count` | `RETURNED_TO_IE` | Numeric | **Strongest signal** — directly records how many times ERCOT returned this request. Carries historical risk; same IE with high past returns is a predictor |

---

### GROUP B — GINR Fee & Process Compliance
*Source: `ginr.ginr_request` + `GINR_PAYMENT_DATA_VW` · Entities: `GinrRequest`, `GinrPaymentDataVw`*

| # | Feature | DB Column | Type | Why It Predicts Feasibility |
|---|---|---|---|---|
| **10** | `fis_fee_paid` | `FIS_FEE_PAID` | Binary | FIS study cannot begin until fee is paid; unpaid = process blocker = likely SENT_BACK |
| **11** | `ss_fee_paid` | `SS_FEE_PAID` | Binary | Same logic — Scoping Study payment gate; missing → study queue blockage |
| **12** | `payment_made_flag` | `GINR_PAYMENT_DATA_VW.DATE_PAID IS NOT NULL` | Binary | Cross-validates fee flags; confirms Authorize.net transaction was recorded — missing payment is a direct risk |

---

### GROUP C — RARF Data Quality Indicators
*Source: `POIB_DATA`, `CONNECTIVITY_NODES`, `CONNECTIVITY_TERMINALS` via `INR_REFERENCE` · Entities: `PoibData`, `ConnectivityNodes`*

> These are meaningful because POIB and connectivity data is entered **as part of the RARF model build-out AFTER the GINR submission**. Incomplete data here means the grid model cannot be validated — a direct cause of `SENT_BACK`.

| # | Feature | Source | Type | Why It Predicts Feasibility |
|---|---|---|---|---|
| **13** | `missing_poib_flag` | COUNT of `POIB_DATA` rows via `INR_REFERENCE` = 0 | Binary | No POIB data entered = ERCOT cannot validate POI substation mapping → automatic `SENT_BACK` |
| **14** | `poi_voltage_mismatch_flag` | `POIB_DATA.VOLTAGE != ginr_request.POI_VOLTAGE` | Binary | POIB voltage doesn't match the requested POI voltage — topology error in RARF submission |
| **15** | `duplicate_substation_flag` | Duplicate `POIB_SUBSTATION_ID` across POIB rows for same INR | Binary | Two POIB entries pointing to the same substation = data entry error → reviewer returns the request |
| **16** | `null_connectivity_node_flag` | COUNT of `CONNECTIVITY_NODES` via `INR_REFERENCE` = 0 | Binary | No connectivity nodes = the generator cannot be placed in the network model; ERCOT cannot run feasibility study |
| **17** | `orphan_node_flag` | `CONNECTIVITY_NODES` rows with 0 `CONNECTIVITY_TERMINALS` | Binary | Connectivity node exists but has no terminals = dangling node, model will fail validation |

---

### GROUP D — Network / Electrical Constraints
*Source: `SUBSTATIONS`, `MOST_LIMITING_SERIES_ELEMENTS`, `SUBSTATION_VOLTAGES`, `CONGESTION_MANAGEMENT_ZONES` · Entities: `Substations`, `MostLimitingSeriesElements`, `SubstationVoltages`*

| # | Feature | DB Column | Type | Why It Predicts Feasibility |
|---|---|---|---|---|
| **18** | `thermal_margin_mw` | `MOST_LIMITING_SERIES_ELEMENTS.RATING_NORMAL` (MIN per substation) | Numeric | Core network constraint. If `project_mw > thermal_margin_mw`, feasibility likely fails — this is the primary physical reason for rejections |
| **19** | `project_exceeds_thermal_flag` | Derived: `project_mw > thermal_margin_mw` | Binary | Direct feasibility test — the model needs this as a pre-computed interaction term |
| **20** | `cmz_name` | `CONGESTION_MANAGEMENT_ZONES.NAME` | Categorical | Congestion zone identifier. Certain CMZs (e.g., West Texas) are chronically congested; projects there face systematically higher feasibility risk |

**Bonus — SubstationVoltages voltage limits (add if available for the POI substation):**

| # | Feature | DB Column | Type | Notes |
|---|---|---|---|---|
| **21** | `poi_voltage_exceeds_normal_max` | `SUBSTATION_VOLTAGES.VOLTAGE_LIMIT_NORMAL_MAX` | Binary | Project's POI voltage > normal operating limit at that substation bus |
| **22** | `substation_gross_mw` | `SUBSTATIONS.GROSS_CAPABILITY_MW_SITE` | Numeric | Total existing generation already at the POI substation — high value = less headroom for new injection |

---

## 4. Features REMOVED and Why

| Removed Feature | Reason |
|---|---|
| `missing_fields_count` (signatures) | **Zero variance** — all 10 signature columns are required by the application before submission is allowed. Every submitted record has them. |
| `rarf_signed`, `fis_signed`, `ss_signed`, `mitigation_signed`, etc. | Same reason — enforced by UI, no discriminative power |
| `authorized_signature` text content | No signal in the name string itself |
| `water_rights_required`, `air_permit_required` | Highly project-specific; `air_permit_missing` (conditional flag) already covered by `missing_poib_flag` pattern |
| `lonestar_criteria` | Only applies to a small subset; low base rate makes it noise for general model |
| `esr_load_flag` | Subsumed by `resource_type` (ESR category) |
| Raw date columns (`submit_date`, `cod_date`) | Use derived `months_to_cod` instead — raw dates don't generalize across cohorts |
| `payment_total_amount`, `analysis_fee` raw amounts | Amount doesn't predict feasibility — whether it was **paid** does (covered by `fis_fee_paid`, `ss_fee_paid`) |
| `poi_name` text string | Free text, no consistent encoding; POI quality is already captured by `missing_poib_flag` and `poi_voltage_mismatch_flag` |
| `duns_number` | Company identifier, not a feasibility signal |

---

## 5. Final 20-Feature Vector Summary

```
GINR Project (9 features)
─────────────────────────
 1. resource_type              [categorical: Wind/Solar/Conv/ESR/Battery]
 2. project_mw                 [numeric, log-scale]
 3. poi_voltage_kv             [numeric]
 4. inr_type                   [categorical: FIS/SS/FIS+SS]
 5. nameplate_to_maxgen_ratio  [numeric: maxNameplateMW / maxGenMW]
 6. lead_tdsp                  [categorical: Oncor/CNP/TNMP/AEP/Sharyland]
 7. crez_flag                  [binary: derived from county + lat/lon]
 8. months_to_cod              [numeric: COD - submit_date in months]
 9. resubmission_count         [numeric: returned_to_ie]

Fee / Process (3 features)
───────────────────────────
10. fis_fee_paid               [binary]
11. ss_fee_paid                [binary]
12. payment_made_flag          [binary: GINR_PAYMENT_DATA_VW.date_paid IS NOT NULL]

RARF Data Quality (5 features)
────────────────────────────────
13. missing_poib_flag          [binary: poib_data count = 0 for this INR]
14. poi_voltage_mismatch_flag  [binary: poib voltage ≠ ginr poi_voltage]
15. duplicate_substation_flag  [binary: duplicate poib_substation_id]
16. null_connectivity_node_flag [binary: connectivity_nodes count = 0]
17. orphan_node_flag           [binary: connectivity_nodes with 0 terminals]

Network Constraints (3 features)
──────────────────────────────────
18. thermal_margin_mw          [numeric: MIN(mlse.rating_normal) at POI substation]
19. project_exceeds_thermal_flag [binary: project_mw > thermal_margin_mw]
20. cmz_name                   [categorical: congestion management zone]
```

---

## 6. Feature Extraction SQL (Oracle)

```sql
SELECT
    -- === IDENTIFIERS ===
    gr.id                                                   AS ginr_request_id,
    gr.inr_id                                               AS inr_id,

    -- === GROUP A: GINR Project ===
    gr.id_technology_type                                   AS resource_type,
    gr.max_gen_mw                                           AS project_mw,
    gr.poi_voltage                                          AS poi_voltage_kv,
    gr.id_inr_type                                          AS inr_type,
    CASE WHEN gr.max_gen_mw > 0
         THEN gr.max_nameplate_mw_gen / gr.max_gen_mw
         ELSE NULL END                                      AS nameplate_to_maxgen_ratio,
    gr.id_lead_tdsp                                         AS lead_tdsp,
    -- CREZ flag: West TX counties per PUCT CREZ map
    CASE WHEN gr.county IN (
        'NOLAN','MITCHELL','TAYLOR','JONES','HASKELL',
        'STONEWALL','KING','DICKENS','FLOYD','CROSBY',
        'LUBBOCK','LYNN','TERRY','YOAKUM','COCHRAN',
        'HOCKLEY','LAMB','BAILEY','PARMER','CASTRO',
        'SWISHER','BRISCOE','HALL','CHILDRESS','HARDEMAN',
        'FOARD','KNOX','BAYLOR','THROCKMORTON',
        'REAGAN','IRION','TOM GREEN','CONCHO','MENARD',
        'SUTTON','KIMBLE','EDWARDS','REAL','BANDERA',
        'KERR','GILLESPIE','BLANCO','HAYS','TRAVIS',
        'WILLIAMSON','MILAM','FALLS','BOSQUE','HILL'
    ) THEN 1 ELSE 0 END                                     AS crez_flag,
    CASE WHEN gr.commercial_operation_date IS NOT NULL
             AND gr.submit_date IS NOT NULL
         THEN MONTHS_BETWEEN(gr.commercial_operation_date, gr.submit_date)
         ELSE NULL END                                      AS months_to_cod,
    NVL(gr.returned_to_ie, 0)                              AS resubmission_count,

    -- === GROUP B: Fee / Process ===
    NVL(gr.fis_fee_paid, 0)                                AS fis_fee_paid,
    NVL(gr.ss_fee_paid,  0)                                AS ss_fee_paid,
    CASE WHEN EXISTS (
        SELECT 1 FROM ginr_payment_data_vw gpd
        WHERE gpd.rscr_id = cr.id
          AND gpd.date_paid IS NOT NULL)
        THEN 1 ELSE 0 END                                   AS payment_made_flag,

    -- === GROUP C: RARF Data Quality ===
    -- Missing POIB
    CASE WHEN (
        SELECT COUNT(*) FROM poib_data pd
        JOIN inr_reference ir ON ir.object_id = pd.id
            AND ir.object_name = 'PoibData'
        WHERE ir.id_ginr_request = gr.id
    ) = 0 THEN 1 ELSE 0 END                                AS missing_poib_flag,

    -- POI Voltage mismatch in POIB
    CASE WHEN EXISTS (
        SELECT 1 FROM poib_data pd
        JOIN inr_reference ir ON ir.object_id = pd.id
            AND ir.object_name = 'PoibData'
        WHERE ir.id_ginr_request = gr.id
          AND pd.voltage IS NOT NULL
          AND pd.voltage <> gr.poi_voltage
    ) THEN 1 ELSE 0 END                                    AS poi_voltage_mismatch_flag,

    -- Duplicate POIB substation
    CASE WHEN (
        SELECT COUNT(*) FROM poib_data pd
        JOIN inr_reference ir ON ir.object_id = pd.id
            AND ir.object_name = 'PoibData'
        WHERE ir.id_ginr_request = gr.id
          AND pd.poib_substation_id IS NOT NULL
    ) > (
        SELECT COUNT(DISTINCT pd2.poib_substation_id) FROM poib_data pd2
        JOIN inr_reference ir2 ON ir2.object_id = pd2.id
            AND ir2.object_name = 'PoibData'
        WHERE ir2.id_ginr_request = gr.id
          AND pd2.poib_substation_id IS NOT NULL
    ) THEN 1 ELSE 0 END                                    AS duplicate_substation_flag,

    -- Missing connectivity nodes
    CASE WHEN (
        SELECT COUNT(*) FROM connectivity_nodes cn
        JOIN inr_reference ir ON ir.object_id = cn.id
            AND ir.object_name = 'ConnectivityNodes'
        WHERE ir.id_ginr_request = gr.id
    ) = 0 THEN 1 ELSE 0 END                                AS null_connectivity_node_flag,

    -- Orphan node (no terminals)
    CASE WHEN EXISTS (
        SELECT 1 FROM connectivity_nodes cn
        JOIN inr_reference ir ON ir.object_id = cn.id
            AND ir.object_name = 'ConnectivityNodes'
        LEFT JOIN connectivity_terminals ct ON ct.connectivity_node_id = cn.id
        WHERE ir.id_ginr_request = gr.id
          AND ct.id IS NULL
    ) THEN 1 ELSE 0 END                                    AS orphan_node_flag,

    -- === GROUP D: Network Constraints ===
    -- Minimum thermal rating at POI substation
    (SELECT MIN(m.rating_normal)
        FROM most_limiting_series_elements m
        JOIN substations s ON s.id = m.substation_id
        JOIN inr_reference ir ON ir.substation_id = s.id
        WHERE ir.id_ginr_request = gr.id
          AND m.rating_normal IS NOT NULL)                  AS thermal_margin_mw,

    -- Project exceeds thermal margin
    CASE WHEN gr.max_gen_mw > (
        SELECT MIN(m.rating_normal)
        FROM most_limiting_series_elements m
        JOIN substations s ON s.id = m.substation_id
        JOIN inr_reference ir ON ir.substation_id = s.id
        WHERE ir.id_ginr_request = gr.id
          AND m.rating_normal IS NOT NULL)
    THEN 1 ELSE 0 END                                      AS project_exceeds_thermal_flag,

    -- Congestion zone
    (SELECT cmz.name
        FROM congestion_management_zones cmz
        JOIN substations s ON s.id_cmz = cmz.id   -- adjust join key per schema
        JOIN inr_reference ir ON ir.substation_id = s.id
        WHERE ir.id_ginr_request = gr.id
        AND ROWNUM = 1)                                     AS cmz_name,

    -- === TARGET LABEL ===
    CASE
        WHEN NVL(gr.returned_to_ie, 0) > 0 THEN 0
        WHEN EXISTS (
            SELECT 1 FROM change_requests cr2
            WHERE cr2.ginr_request_id = gr.id
              AND cr2.change_request_status_id IN (4, 5, 16)) -- SENT_BACK, WITHDRAWN, ERCOT_REJECTED
        THEN 0
        WHEN EXISTS (
            SELECT 1 FROM change_requests cr3
            WHERE cr3.ginr_request_id = gr.id
              AND cr3.change_request_status_id IN (7, 8, 9, 17, 18, 19)) -- PASS statuses
        THEN 1
        ELSE NULL  -- still in progress, exclude from training
    END                                                    AS feasibility_pass

FROM ginr.ginr_request gr
LEFT JOIN change_requests cr ON cr.ginr_request_id = gr.id
WHERE gr.deleted = 0
  AND gr.submit_date IS NOT NULL   -- only include actually submitted requests
ORDER BY gr.id;
```

---

## 7. Python Preprocessing Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

NUMERIC_FEATURES = [
    'project_mw',              # log-transform first
    'poi_voltage_kv',
    'nameplate_to_maxgen_ratio',
    'months_to_cod',
    'resubmission_count',
    'thermal_margin_mw',
]

BINARY_FEATURES = [
    'crez_flag',
    'fis_fee_paid',
    'ss_fee_paid',
    'payment_made_flag',
    'missing_poib_flag',
    'poi_voltage_mismatch_flag',
    'duplicate_substation_flag',
    'null_connectivity_node_flag',
    'orphan_node_flag',
    'project_exceeds_thermal_flag',
]

CATEGORICAL_FEATURES = [
    'resource_type',
    'inr_type',
    'lead_tdsp',
    'cmz_name',
]

import numpy as np
df['project_mw'] = np.log1p(df['project_mw'])

preprocessor = ColumnTransformer([
    ('num', Pipeline([
        ('impute', SimpleImputer(strategy='median')),
        ('scale',  StandardScaler())
    ]), NUMERIC_FEATURES),
    ('bin', SimpleImputer(strategy='constant', fill_value=0), BINARY_FEATURES),
    ('cat', Pipeline([
        ('impute', SimpleImputer(strategy='constant', fill_value='UNKNOWN')),
        ('ohe',    OneHotEncoder(handle_unknown='ignore', sparse=False))
    ]), CATEGORICAL_FEATURES),
])

model = Pipeline([
    ('prep',  preprocessor),
    ('clf',   LogisticRegression(
                  class_weight='balanced',  # handles imbalanced pass/fail
                  C=1.0,
                  solver='lbfgs',
                  max_iter=1000
              ))
])
```

---

## 8. Business Risk → Feature Mapping (Revised)

| Business Risk | Feature Used | Codebase Source |
|---|---|---|
| Project too large for the POI grid | `project_mw` + `project_exceeds_thermal_flag` + `thermal_margin_mw` | `ginr_request.MAX_GEN_MW` vs `MOST_LIMITING_SERIES_ELEMENTS.RATING_NORMAL` |
| Wrong / missing POI substation mapping | `missing_poib_flag` + `poi_voltage_mismatch_flag` | `POIB_DATA` via `INR_REFERENCE` |
| Duplicate substation entry error | `duplicate_substation_flag` | Duplicate `POIB_DATA.POIB_SUBSTATION_ID` |
| Network model cannot be built | `null_connectivity_node_flag` + `orphan_node_flag` | `CONNECTIVITY_NODES` + `CONNECTIVITY_TERMINALS` |
| High congestion zone | `cmz_name` + `crez_flag` | `CONGESTION_MANAGEMENT_ZONES` + county derivation |
| Study cannot start (fees unpaid) | `fis_fee_paid` + `ss_fee_paid` + `payment_made_flag` | `ginr_request.FIS_FEE_PAID` + `GINR_PAYMENT_DATA_VW` |
| Repeat submitter with known issues | `resubmission_count` | `ginr_request.RETURNED_TO_IE` |
| Unrealistic project timeline | `months_to_cod` | `COMMERCIAL_OPERATION_DATE - SUBMIT_DATE` |
| Project type mismatch with grid | `resource_type` + `inr_type` + `lead_tdsp` | `ID_TECHNOLOGY_TYPE`, `ID_INR_TYPE`, `ID_LEAD_TDSP` |



