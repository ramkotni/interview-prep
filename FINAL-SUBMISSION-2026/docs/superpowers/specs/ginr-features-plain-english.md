# GINR Feasibility Model — Features in Plain English
## What Each Feature Means in Real Life (ERCOT Interconnection Context)

**Date:** May 31, 2026

---

## The Big Picture First

Think of a GINR submission like a **permit application** to connect a new power plant to the Texas grid.  
ERCOT acts like the building inspector. They check:
- Is the plant the right size for that neighborhood's electrical wiring? (network capacity)  
- Did the developer fill out all the right paperwork? (RARF data quality)  
- Did they pay the required study fees? (process compliance)  
- Have they had problems before? (history)  

If any check fails → the application is **Sent Back (FAIL)**.  
If all checks pass → it moves to the study queue **(PASS)**.

---

## GROUP A — GINR Project Features (What kind of project is this?)

---

### Feature 1: `resource_type`
**What it is:** The type of power plant — Solar, Wind, Conventional (gas/coal), ESR (battery storage), etc.  
**Why it matters for feasibility:**  
- **Solar and Wind** are intermittent — they generate power only when the sun shines or wind blows. ERCOT must study how this unpredictability impacts the grid. They also need reactive power compensation studies.  
- **Conventional generators** (natural gas) are dispatchable — ERCOT studies are simpler but they still need to check thermal limits.  
- **Battery/ESR** have both charge and discharge modes — the most complex feasibility study because they act as both generator and load.  
- In CREZ-heavy West Texas, most new submissions are Solar or Wind → those areas are more congested → higher fail rate for those types.

**Real example:** A 500 MW solar farm trying to interconnect at a 69 kV substation that was built for 100 MW — almost certain to fail thermal margin.

---

### Feature 2: `project_mw`
**What it is:** How many megawatts the project wants to put on the grid. Pulled from `MAX_GEN_MW` in `ginr_request`.  
**Why it matters:**  
This is the single most direct driver of congestion impact. Think of the grid's power lines like water pipes — they can only carry so much water. A 1,000 MW project is like trying to pour a firehose through a garden hose.  
- Small projects (< 100 MW) usually fit within existing headroom at a substation.  
- Large projects (> 500 MW) almost always require expensive network upgrades.  
- We **log-transform** this because project sizes range from 10 MW to 3,000 MW — a straight scale would make small projects invisible.

**Real example:** A 200 MW solar project at a 345 kV substation with 300 MW thermal margin → feasible. The same project at a 115 kV substation with 180 MW thermal margin → likely FAIL.

---

### Feature 3: `poi_voltage_kv`
**What it is:** The voltage level (in kilovolts) where the project wants to connect to the grid. From `POI_VOLTAGE` in `ginr_request`.  
**Why it matters:**  
Lower voltage = smaller pipes = less capacity.
- **500 kV / 345 kV** — high-voltage transmission backbone. Can handle very large projects.  
- **138 kV / 115 kV** — sub-transmission. Medium projects only.  
- **69 kV** — distribution-level. Small projects only (< 100 MW usually).  
A 500 MW project trying to connect at 69 kV is like plugging a factory into a household outlet — it won't pass.

**Real example:** A 750 MW wind farm requests connection at 115 kV. ERCOT studies show thermal limit is 400 MW → Sent Back.

---

### Feature 4: `inr_type`
**What it is:** The type of study requested — FIS (Full Interconnection Study), SS (Scoping Study), or both. From `ID_INR_TYPE`.  
**Why it matters:**  
- **SS only** = quick scoping study, fewer data requirements → lower fail rate.  
- **FIS only** = full detailed power flow study → strict data requirements for RARF submission.  
- **FIS + SS combined** = most complex, most data needed, most checkpoints → highest fail rate.  
ERCOT planners verify more data for FIS, so any gaps in RARF data (missing POIB, connectivity nodes) immediately trigger a "Sent Back."

---

### Feature 5: `nameplate_to_maxgen_ratio`
**What it is:** Nameplate MW ÷ Operating MW. For example, a wind farm with 600 MW of turbines but an operating limit of 500 MW has a ratio of 1.20.  
**Why it matters:**  
- Ratio > 1.25 = the developer is "over-building" — they want more physical equipment than their requested grid capacity.  
- Very high ratios (> 1.5) signal a speculative project — developers padding capacity hoping to sell unused capacity later.  
- ERCOT planners scrutinize these more heavily because the impact on the grid could be larger than declared.  
- Ratio exactly 1.0 = clean, straightforward project → lower risk.

---

### Feature 6: `lead_tdsp`
**What it is:** The Transmission & Distribution Service Provider (utility company) responsible for the territory where the project sits. From `ID_LEAD_TDSP`.  
**Values:** Oncor, CenterPoint Energy, TNMP, AEP Texas, Sharyland Utilities.  
**Why it matters:**  
Each TDSP manages a different part of Texas with different congestion profiles:
- **Oncor** covers North and West Texas → high queue volume, many CREZ-adjacent projects.  
- **CenterPoint** covers Houston metro → high load growth, newer grid infrastructure.  
- **TNMP** covers smaller areas in West Texas → common for wind projects, sometimes strained.  
- **AEP Texas** covers South/West Texas → large renewable project pipeline, frequent congestion.  
The TDSP also does their own review of the RARF data — each TDSP has different technical standards, so the failure rate varies by territory.

---

### Feature 7: `crez_flag`
**What it is:** Binary flag — is the project in a CREZ (Competitive Renewable Energy Zone) county? Derived from the `COUNTY` field in `ginr_request`.  
**Why it matters:**  
CREZ zones in West Texas and the Panhandle were originally designed for wind energy in the 2000s. By 2026 they are **saturated with renewable generation**. New projects trying to connect there face:
- Heavily loaded transmission lines already at or near their thermal limits.  
- Long queue of existing projects ahead of them.  
- Higher probability that the thermal margin check fails.

**Real example:** A 300 MW solar project in Nolan County (CREZ) vs. the same project near Houston (non-CREZ) → the CREZ project has 3× higher chance of thermal constraint issues.

---

### Feature 8: `months_to_cod`
**What it is:** How many months between the GINR submission date and the requested Commercial Operation Date (COD). Derived from `COMMERCIAL_OPERATION_DATE - SUBMIT_DATE`.  
**Why it matters:**  
- **Too short (< 18 months):** The developer is rushing. FIS + RARF data preparation, environmental permits, and study cycles realistically take 18–36 months. Short timelines mean the RARF data is often incomplete or rushed → more SENT_BACK events.  
- **Too long (> 84 months):** The project is likely speculative (holding a queue position). ERCOT scrutinizes these more carefully.  
- **Sweet spot (24–60 months):** Realistic timeline, well-prepared developer → lower fail rate.

---

### Feature 9: `resubmission_count`
**What it is:** How many times this specific GINR request has been returned to the developer by ERCOT. From `RETURNED_TO_IE` in `ginr_request`.  
**Why it matters:**  
This is the **strongest predictor** in the model. If ERCOT has already sent a request back once, it means:
1. The first submission had problems (data gaps, network issues, wrong POIB).  
2. The developer may not have fully fixed the root cause.  
3. Second and third returns are common for developers who don't understand the technical requirements.  
- `returnedToIe = 0` → clean first submission → very likely to pass.  
- `returnedToIe = 1` → had one issue, fixed it → moderate risk.  
- `returnedToIe >= 2` → chronic issues → high fail probability.

---

## GROUP B — Fee / Process Compliance (Did they pay to play?)

---

### Feature 10: `fis_fee_paid`
**What it is:** Boolean — has the Full Interconnection Study fee been paid? From `FIS_FEE_PAID` in `ginr_request`.  
**Why it matters:**  
ERCOT **cannot begin the FIS study** until the fee is paid. It's a hard process gate. If unpaid:
- The application will be `SENT_BACK` immediately.  
- No analysis can happen regardless of data quality.  
Think of it like filing a court case without paying the filing fee — the clerk rejects it before anyone reads it.

---

### Feature 11: `ss_fee_paid`
**What it is:** Has the Scoping Study fee been paid? From `SS_FEE_PAID`.  
**Why it matters:** Same logic as FIS fee — Scoping Study requires its own fee payment to start. Projects that haven't paid either fee are obvious FAIL candidates.

---

### Feature 12: `payment_made_flag`
**What it is:** Cross-check — did a real payment transaction appear in `GINR_PAYMENT_DATA_VW.DATE_PAID`?  
**Why it matters:**  
Sometimes the fee paid flags in `ginr_request` are updated manually by staff. This flag confirms an actual **Authorize.net payment record** exists — a second verification. Discrepancies between `fis_fee_paid=true` and `payment_made_flag=false` indicate data integrity issues — also a risk signal.

---

## GROUP C — RARF Data Quality (Is the technical data complete?)

> **Important context:** POIB data and Connectivity Nodes are entered AFTER the GINR is submitted, as part of building the RARF model. The GINR submission itself doesn't include these — they are added by the developer in subsequent RARF forms. A developer who submits a GINR but then never completes the RARF → high fail risk.

---

### Feature 13: `missing_poib_flag`
**What it is:** Binary — is there ZERO POIB (Point of Interconnection Bus) data entered for this INR? Derived by counting `POIB_DATA` rows linked to this GINR via `INR_REFERENCE`.  

**What POIB data is:** When a generator connects to the grid, it connects at a specific bus on a specific substation. The POIB record identifies that exact bus, its voltage, and who owns it.  

**Why it matters:**  
Without a POIB record, ERCOT's power flow model cannot place the generator in the network topology. It's like filing a building permit but not specifying which lot the building goes on. The feasibility study literally cannot run → automatic `SENT_BACK`.

---

### Feature 14: `poi_voltage_mismatch_flag`
**What it is:** Binary — does the voltage recorded in the POIB data (`POIB_DATA.VOLTAGE`) differ from the POI voltage requested in the GINR (`ginr_request.POI_VOLTAGE`)?  

**Why it matters:**  
If the GINR says "I want to connect at 138 kV" but the POIB entry says the bus is at 69 kV, there is a topology mismatch. ERCOT cannot run a valid power flow study with conflicting voltage data. This is a common data entry error where developers copy-paste from wrong substations.

---

### Feature 15: `duplicate_substation_flag`
**What it is:** Binary — do two or more POIB entries for the same GINR point to the same `POIB_SUBSTATION_ID`?  

**Why it matters:**  
Each generator should have one primary interconnection bus. If a developer accidentally maps the same substation twice, the power flow model tries to inject power twice at the same location — invalid topology. ERCOT reviewers catch this immediately and return the application.

---

### Feature 16: `null_connectivity_node_flag`
**What it is:** Binary — are there ZERO connectivity nodes entered for this GINR's substation?  

**What connectivity nodes are:** In the CIM (Common Information Model) that ERCOT uses for its network model, a connectivity node is the electrical connection point inside a substation bay where devices (generators, transformers, breakers) connect to each other.  

**Why it matters:**  
No connectivity node = the generator has no valid place in the detailed network model. Even if POIB data is correct, the fine-grained topology study (short-circuit analysis, power flow) cannot proceed without connectivity nodes. Direct cause of `SENT_BACK`.

---

### Feature 17: `orphan_node_flag`
**What it is:** Binary — does any connectivity node exist that has **zero connectivity terminals** attached to it?  

**What terminals are:** A connectivity terminal is the actual physical connection endpoint on a device (one end of a transformer winding, one terminal of a breaker). Each connectivity node should have at least 2 terminals to form a valid circuit.  

**Why it matters:**  
An orphan node (a connectivity node with no terminals) is a dangling, unconnected point in the topology — like a door that opens to nothing. ERCOT's network model validation rejects dangling nodes, causing the entire RARF submission to fail validation.

---

## GROUP D — Network / Electrical Constraints (Does the grid have room?)

---

### Feature 18: `thermal_margin_mw`
**What it is:** The minimum normal thermal rating (in MW) of the Most Limiting Series Element (MLSE) at the POI substation. From `MOST_LIMITING_SERIES_ELEMENTS.RATING_NORMAL`.  

**What MLSE means:** Every substation has transmission lines, transformers, and cables connecting to the rest of the grid. Each has a thermal rating — the maximum power it can carry before overheating. The **most limiting** element is the weakest link.  

**Why it matters:**  
This is the **physical capacity ceiling** of the connection point. If a 500 MW project wants to connect at a substation where the weakest transmission element can only carry 350 MW — the project physically cannot operate without causing equipment overloading.

**Real example:**  
- Substation has a 138 kV transformer rated at 200 MVA (≈190 MW thermal).  
- New 300 MW solar project submits to interconnect there.  
- `thermal_margin_mw = 190`, `project_mw = 300`.  
- `project_exceeds_thermal_flag = 1` → almost certain FAIL unless upgrades are funded.

---

### Feature 19: `project_exceeds_thermal_flag`
**What it is:** Binary — is `project_mw > thermal_margin_mw`?  

**Why it matters:**  
This is a **pre-computed interaction term** that directly answers the core feasibility question. Rather than letting the logistic regression figure out the relationship between two numeric features, we give it the answer explicitly. Projects that exceed the thermal margin need costly network upgrades → ERCOT Sent Back pending upgrade agreements.

---

### Feature 20: `cmz_name`
**What it is:** The Congestion Management Zone the project falls in. From `CONGESTION_MANAGEMENT_ZONES.NAME`. One-hot encoded into `LZ_WEST`, `LZ_NORTH`, `LZ_HOUSTON`, `LZ_SOUTH`, etc.  

**What CMZ means:** ERCOT divides the Texas grid into load zones for settlement and congestion pricing. These zones also reflect where the grid is most and least stressed:  
- **LZ_WEST** (West Texas) — highest congestion, most renewable saturation.  
- **LZ_NORTH** (Dallas/Fort Worth area) — high demand, moderate congestion.  
- **LZ_HOUSTON** — high industrial load, but strong grid infrastructure.  
- **LZ_SOUTH** — mixed, some coastal wind.  

Projects in **LZ_WEST** have statistically higher feasibility failure rates because the existing generation already saturates the transmission paths to the rest of Texas.

---

## Summary Table

| # | Feature | In Plain English | Fail Signal |
|---|---|---|---|
| 1 | resource_type | What type of power plant? | Solar/Wind in CREZ = higher risk |
| 2 | project_mw | How big is the plant? | Bigger = more grid impact |
| 3 | poi_voltage_kv | What voltage level to connect? | Low voltage + high MW = mismatch |
| 4 | inr_type | What study type requested? | FIS+SS combined = most checkpoints |
| 5 | nameplate_to_maxgen_ratio | Over-building factor | Ratio > 1.25 = speculative project |
| 6 | lead_tdsp | Which utility territory? | AEP/Oncor West Texas = congested |
| 7 | crez_flag | In a CREZ zone? | CREZ = saturated grid area |
| 8 | months_to_cod | How fast do they want it done? | < 18 months = rushed = gaps |
| 9 | resubmission_count | Been sent back before? | ≥ 2 returns = chronic issues |
| 10 | fis_fee_paid | FIS study fee paid? | Unpaid = can't start study |
| 11 | ss_fee_paid | Scoping study fee paid? | Unpaid = process blocked |
| 12 | payment_made_flag | Actual payment in system? | No record = data discrepancy |
| 13 | missing_poib_flag | No bus mapping in RARF? | Can't place plant in model |
| 14 | poi_voltage_mismatch | POIB voltage ≠ POI voltage? | Topology contradiction |
| 15 | duplicate_substation | Same substation mapped twice? | Double-injection error |
| 16 | null_connectivity_node | No connectivity nodes? | No place in network model |
| 17 | orphan_node | Disconnected node in RARF? | Dangling topology |
| 18 | thermal_margin_mw | How much grid headroom? | Low margin = congestion |
| 19 | project_exceeds_thermal | Plant bigger than the wire? | Yes = almost always FAIL |
| 20 | cmz_name | Which congestion zone? | LZ_WEST = most congested |
