# RIOO-2893: Retirement UAT Feedback — Design Spec

**Date:** 2026-04-08
**Branch:** feature/RIOO-2893-retirement-logic
**Status:** Approved

Three changes driven by Business/UAT testing feedback on the retirement CR feature.

---

## Requirement 1: Smart Calendar Date Restrictions

When creating any change request for a station that has an approved retirement (i.e., `serviceStop` is set on the substation record), the date picker must restrict selectable dates.

### Rules

- `serviceStop` on the substation record = PLD - 1
- Dates from today through `serviceStop - 1 day` (PLD - 2) are **enabled**
- Dates on or after `serviceStop` (PLD - 1) are **disabled**
- Example: PLD = 5/15/2026, `serviceStop` = 5/14/2026. Enabled: today through 5/13/2026. Disabled: 5/14/2026+.
- Hovering over or clicking a disabled date shows a tooltip: *"This station will be retired after this date. Changes cannot be made."*
- This applies to **all** CR types, not just retirement CRs.

### Backend Changes

**`SubstationOverviewVO.java`** — Add `serviceStop` field (String).

**`Substations.toOverviewVO()`** — Map the substation entity's `serviceStop` to the VO. This piggybacks on the existing `listUserSubstations` → `getSubstationsForUser` call so no new endpoint is needed.

### Frontend Changes

**`date.component.ts`** — Add two `@Input()` properties:
- `maxDate: NgbDateStruct` — bound to `[maxDate]` on NgbInputDatepicker
- `markDisabled: (date: NgbDate) => boolean` — bound to `[markDisabled]` on the picker

**`date.component.html`** — Add `[maxDate]="maxDate"` and `[markDisabled]="markDisabled"` bindings on the datepicker directive. Add a `[dayTemplate]` with a custom `ng-template` that wraps each day in an element with `ngbTooltip` when the date is disabled due to retirement.

**`change-request-start.component.ts`** — When a substation is selected (in the `substationId` change handler):
1. Look up the selected substation from the already-loaded `substations` BehaviorSubject
2. If `serviceStop` is present, compute `retirementMaxDate = serviceStop - 1 day` as an `NgbDateStruct`
3. Create a `markDisabled` function that returns `true` for dates >= `serviceStop`
4. Pass both to the target date picker component

### Files Changed

| File | Change |
|------|--------|
| `SubstationOverviewVO.java` | Add `serviceStop` field + getter/setter |
| `Substations.toOverviewVO()` (`Substations.java`) | Map `serviceStop` from entity |
| `date.component.ts` | Add `maxDate` and `markDisabled` inputs |
| `date.component.html` | Bind `maxDate`, `markDisabled`, and `dayTemplate` with tooltip |
| `change-request-start.component.ts` | Compute and pass date restrictions when substation selected |
| `change-request-start.component.html` | Wire `maxDate`/`markDisabled` to target date picker |

---

## Requirement 2: Station Radio Button Disabled for Non-Station Owners

When creating a retirement CR, if the user only owns units within the station (not the station itself), the "Station" radio button must be disabled with a tooltip.

### Ownership Determination

- The `SUBSTATIONS` table has an `ASSET_ID` column
- The `OWNERSHIP` table links `ASSET_ID` to a company DUNS
- If the user's DUNS is linked to the substation's `ASSET_ID` in `OWNERSHIP` → user owns the station
- Station ownership is independent of unit ownership

### Backend Changes

**`SubstationsService.getActiveUnitsForSubstation()`** — Extend the response to include a `userOwnsStation` boolean. After fetching retirable units, also check the OWNERSHIP table for the substation's own ASSET_ID against the user's DUNS list. Bundle this into the existing response map to avoid a separate API call.

### Frontend Changes

**`change-request-start.component.ts`** — When the `getActiveUnitsForSubstation` response arrives:
- Store `userOwnsStation` from the response
- Use it to control the disabled state of the "Station" radio button

**`change-request-start.component.html`** — On the "Station" radio button:
- Add `[disabled]="!userOwnsStation"` binding
- Wrap in a container with `ngbTooltip="You do not own the station."` that shows only when disabled

### Edge Cases

- User owns station but no units: "Station" enabled, "Units" enabled but unit list is empty (existing behavior)
- User owns both station and units: Both options enabled (existing behavior)
- ERCOT users: `getActiveUnitsForSubstation` already bypasses the ownership filter for ERCOT roles (checks `isUserInRole` for ERCOT_EDIT, ERCOT_VIEW, etc.). For station ownership, set `userOwnsStation = true` when the user has an ERCOT role, so the radio button is always enabled for ERCOT users.

### Files Changed

| File | Change |
|------|--------|
| `SubstationsService.java` (`getActiveUnitsForSubstation`) | Add `userOwnsStation` boolean to response |
| `change-request-start.component.ts` | Store and use `userOwnsStation` from API response |
| `change-request-start.component.html` | Disable "Station" radio + tooltip when `!userOwnsStation` |

---

## Requirement 3: Read-Only Retirement Fields in Standard CRs

RE users can currently edit `Stop Service` (substation Details tab) and `Retirement Date` (unit Dates tab) in standard CRs. These fields must be made read-only for all non-ERCOT users in non-retirement CRs.

### Fields Affected

| Panel | Field Label | Data Key | Column |
|-------|------------|----------|--------|
| Substation Details | Stop Service | `serviceStop` | `SERVICE_STOP` |
| Unit Dates (all types) | Retirement Date | `unitEnd` | `UNIT_END` |

### Conditional Logic

```
if (!isErcotUser && crType !== Retirement) {
  serviceStop → readOnly
  unitEnd → readOnly
}
```

- **ERCOT users**: Fields remain editable in all CR types
- **Non-ERCOT users in retirement CRs**: Fields remain editable (that's the purpose of the CR)
- **Non-ERCOT users in all other CR types**: Fields are read-only

### Frontend Changes

**`substation-details.component.ts`** — After the form is built, check `!this.sess.rarfUserHasErcotRole()` and `crType !== Retirement`. If both true, set `readOnly` on the `serviceStop` form control. This leverages the existing pattern where the template checks `ctrl.controls[section.dataKey]['readOnly']` to disable fields (substation-details.component.html line 241-245).

**`resource-attributes-dates.component.ts`** (`ResourceAttributesDatesComponent`) — Same pattern: after form build, if user is not ERCOT and CR is not retirement type, set `readOnly` on the `unitEnd` form control. This single component handles dates for all generator types (Conventional, Wind, Solar, CC, ESR) since they share the same dates panel definition.

### Behavior

- Fields remain **visible** (not hidden) but rendered as read-only / greyed out
- Consistent with how other `readOnly` fields already appear in the app (pointer-events-none, disabled attribute)
- No tooltip needed — the field is simply not interactive

### Files Changed

| File | Change |
|------|--------|
| `substation-details.component.ts` | Set `serviceStop` readOnly for non-ERCOT in non-retirement CRs |
| `resource-attributes-dates.component.ts` | Set `unitEnd` readOnly for non-ERCOT in non-retirement CRs |

---

## Out of Scope

- Backend validation to reject retirement date changes in standard CRs (could be a future hardening step)
- Changes to the retirement CR flow itself (already implemented)
- ERCOT dashboard changes (separate work item)
