# RIOO-2893 Retirement CR - Gap Implementation Design

**Date**: 2026-03-13
**Branch**: feature/RIOO-2893-retirement-logic
**Status**: Draft

## Context

The retirement CR feature (RIOO-2893) has been partially implemented. The tech lead identified five gaps that need to be addressed before the feature is complete.

## Gap 1: Single-Page RSCR (Create + Submit in One Action)

### Current State
- The start page (`change-request-start.component`) creates a retirement CR in "Saved" status and navigates to "review/main" via `navTo()` → `createCr("welcome/main")`.
- Button label is "Let's Get Started" for new CRs or "Save and Continue" for existing ones.
- No single-action submit flow exists for retirement CRs.

### Design

**Frontend (`change-request-start.component.ts`):**

1. Add a new method `submitRetirementCr()` that:
   - Calls `populateCreateData()` to build the CR payload
   - Uses RxJS `switchMap` to chain: `dataService.saveCR(data)` → `dataService.updateCRstatus(crId, ChangeRequestStatus.PendingReview)`
   - On success, navigates to summary using `this.redirect("summary/main")` (which builds `/cr/{crId}/summary/main`)
   - On error at any stage, re-enables `canCreate`, hides spinner, and if save succeeded but status update failed, navigates to summary page so the user can submit from there
   - Shows spinner during the entire operation

2. Modify `navTo()` to route retirement CRs through `submitRetirementCr()` instead of `createCr()`:
   ```
   if (this.retirementCr && !this.crId) {
     this.submitRetirementCr();
   } else if (this.crId) {
     // existing update flow
   } else {
     // existing create flow
   }
   ```

3. Update `btnLabel` to show "Submit to ERCOT" when `retirementCr` is true and it's a new CR (no `crId`).

**Frontend (`change-request-start.component.html`):**
- No template changes needed - the existing button wiring with `(click)="navTo()"` and `{{ btnLabel | async }}` will work with the logic changes above.

**Backend:** No changes needed - reuses existing `saveCR` and `updateCRstatus` endpoints.

### Edge Cases
- If the save succeeds but status update fails: re-enable `canCreate`, navigate to summary page so the user can retry submission from there. The CR remains in "Saved" status.
- For **existing** retirement CRs (user returns to start page to edit), the flow stays as-is: save + navigate to review/summary via the existing `updateCr("review/main")` path. The single-action submit only applies to new retirement CRs.
- Re-submitting an already-saved retirement CR that failed the initial status update is handled by the summary page's existing submit button.

## Gap 2: RSCR Summary Page - Retirement Details

### Current State
- `CrSummaryChangeInfoComponent` displays standard CR info (substation, PLD, contact, description) in a table.
- No retirement-specific fields (scope, units, effective retirement date) are shown.
- The `ChangeRequests` entity has `retirementScope` and `retirementUnitIds` fields, and `ChangeRequestsVO` exposes them.

### Design

**Frontend (`cr-summary-change-info.component.ts`):**

Extend the `changeInfoAttributes` array to conditionally include retirement fields when the CR is a retirement type. Use `ChangeTypeValue.RET` enum instead of magic number `6`:

```typescript
if (this.cr.changeTypeId === ChangeTypeValue.RET) {
  // Calculate retirement date (PLD - 1 day)
  const pld = new Date(this.cr.targetDate);
  pld.setDate(pld.getDate() - 1);
  const retirementDate = this.tss.formatDate(pld, "MM-dd-yyyy");

  this.changeInfoAttributes.push(
    { label: "Retirement Scope", value: this.cr.retirementScope === "STATION" ? "Station" : "Unit(s)" },
    { label: "Effective Retirement Date", value: retirementDate }
  );

  if (this.cr.retirementScope === "UNITS" && this.cr.retirementUnitIds) {
    this.changeInfoAttributes.push(
      { label: "Units to Retire", value: this.cr.retirementUnitIds }
    );
  }
}
```

**Unit Names Resolution:** The `retirementUnitIds` field stores IDs in `TABLE_NAME:ID` format (e.g., `WIND_GENERATORS:42`). For a better display, we need to resolve these to human-readable names. Two options:

- **Option A (Recommended):** Add a new field `retirementUnitNames` to `ChangeRequestsVO` that the backend populates when loading a retirement CR. Since `toVO()` is a static method without EntityManager access, the resolution must happen in the service layer (e.g., in `ChangeRequestService` methods that load CRs) after the `toVO()` call.
- **Option B:** Make a frontend API call to `/substations/units/{substationId}` and match IDs. Less efficient, adds another API call.

**Backend (`ChangeRequestsVO.java` + `ChangeRequestService.java`):**
- Add `retirementUnitNames` field to `ChangeRequestsVO` (getter/setter)
- In the service methods that load retirement CRs (e.g., `loadChangeRequest`, `findActiveRetirementCrs`), after calling `toVO()`, resolve unit IDs to names using the EntityManager and populate the field

**No new components needed** - extending the existing `CrSummaryChangeInfoComponent` keeps it simple since we're showing standard info alongside retirement details.

## Gap 3: Ownership Checks

### Current State
- `SubstationsService.getActiveUnitsForSubstation()` returns ALL active units for a substation without ownership filtering.
- `createRetirementData()` in `ChangeRequestService` processes `retirementUnitIds` without validating the user owns those units.
- The `/changeRequests/retirement/active/{substationId}` endpoint has no ownership filtering.

### Design

**3a. Filter units by ownership in `SubstationsService.getActiveUnitsForSubstation()`:**

The method currently iterates over all generator types (conventional, wind, solar, combined-cycle, ESR) and adds non-retired units. Add ownership filtering:

1. Check `FILTER_BY_OWNERSHIP` flag first (consistent with all other ownership checks in `BaseService`)
2. ERCOT users (roles: `ERCOT_EDIT`, `ERCOT_VIEW`) bypass this filter and see all units
3. Get the current user's DUNS list via `getRarfDuns()`
4. For each generator (ConventionalGenerators, WindGenerators, etc.), access the parent `Assets` entity via the generator's asset relationship, then get ownership DUNS via `getOwnersDuns(asset)`
5. Only include units where at least one ownership DUNS matches the user's DUNS

This follows the same pattern as `checkOwnership()` in `BaseService.java` (lines 850-929) which checks asset ownership DUNS against user DUNS via the `Assets` entity.

**3b. Validate unit ownership in `createRetirementData()`:**

Before creating `ChangeRequestData` records for each unit:

1. Wrap `Long.valueOf(parts[1].trim())` in try-catch for `NumberFormatException` to handle malformed input
2. Verify each unit ID exists in the database
3. Verify each unit belongs to the substation on the CR
4. Verify the user owns the unit (DUNS check)
5. If any validation fails, add an error message to the response and skip that unit
6. **Fix pre-existing bug:** When loading each unit for validation, also read the current `unitEnd` value and set it as `dataOld` on the `ChangeRequestData` record (currently only the STATION scope sets `dataOld`; UNITS scope does not)

**3c. Ownership filtering on `/changeRequests/retirement/active/{substationId}`:**

This endpoint is used to display warnings on the summary page. The warning message is informational for all users (ERCOT/RE), so ownership filtering is **not needed** here - all users should see warnings about conflicting retirement CRs regardless of ownership. The endpoint already has `@RolesAllowed` for authorization.

## Gap 4: Checkbox List for Unit Selection

### Current State
- Plain HTML `<select multiple>` with `size="6"` and help text "Hold Ctrl/Cmd to select multiple units".
- Not consistent with the app's Bootstrap-based form styling.

### Design

Replace the `<select multiple>` with a checkbox list using Bootstrap `form-check` classes:

**Frontend (`change-request-start.component.html`):**

Replace lines 330-352 with:
```html
<div *ngIf="retirementScope === 'UNITS'" class="col-12 col-lg-4 pt-3">
  <label>Select unit(s) to retire</label>
  <div class="border rounded p-2" style="max-height: 250px; overflow-y: auto;">
    <div *ngFor="let unit of retirableUnits | async"
         class="form-check">
      <input type="checkbox"
             class="form-check-input"
             [id]="'unit-' + unit.id"
             [value]="unit.tableName + ':' + unit.id"
             (change)="onUnitCheckboxChange($event)"
             [checked]="selectedUnitIds.includes(unit.tableName + ':' + unit.id)">
      <label class="form-check-label" [for]="'unit-' + unit.id">
        {{ unit.name }} ({{ unit.type }})
      </label>
    </div>
  </div>
</div>
```

**Frontend (`change-request-start.component.ts`):**

Replace `onUnitSelectionChange()` with `onUnitCheckboxChange()`:
```typescript
public onUnitCheckboxChange(event: any) {
  const value = event.target.value;
  if (event.target.checked) {
    // Use spread to create new array reference (OnPush change detection)
    this.selectedUnitIds = [...this.selectedUnitIds, value];
  } else {
    this.selectedUnitIds = this.selectedUnitIds.filter(id => id !== value);
  }
}
```

Remove the old `onUnitSelectionChange()` method.

## Gap 5: Conflicting RSCR Messages on ALL Summary Pages

### Current State
- `checkRetirementWarning()` in `cr-summary.component.ts` (lines 327-358) already shows warnings for:
  - Non-retirement CRs when a retirement CR exists for the same substation
  - Retirement CRs when other retirement CRs exist for the same substation
- The warning is displayed via an `<alert>` component in `cr-summary.component.html` (lines 30-32)

### Design

The current implementation already handles both cases (retirement and non-retirement CRs). However, it needs enhancement:

1. **Show warnings on ALL active CRs for the substation**, not just when retirement CRs exist. The message should also appear on non-retirement CRs to warn that a retirement CR will affect the substation.

2. **Improve the warning message** to be more specific:
   - For non-retirement CRs: "There are multiple active RSCRs for this substation. RSCR-{id} was created for retiring a Substation/Unit with PLD {date}."
   - For retirement CRs when other CRs exist: "There are multiple active RSCRs for this substation. RSCR-{id} is also an active change request for this substation."

3. **Show ALL conflicting CRs**, not just the first one. If there are 3 active CRs for a substation, show a warning for each.

**Backend enhancement:**
- Create a new endpoint `/changeRequests/active/{substationId}` that returns ALL active CRs for a substation (not just retirement CRs). Do not modify the existing `/changeRequests/retirement/active/{substationId}` endpoint to avoid breaking its contract.
- The new endpoint should filter out rejected/withdrawn/processed CRs, similar to the existing retirement query but without the `changeType` filter.

**Frontend (`cr-summary.component.ts`):**
- Rename `retirementWarning: string` to `retirementWarnings: string[]` (update both the component class and the template)
- Modify `checkRetirementWarning()` to:
  1. Fetch active retirement CRs (existing call)
  2. Build warning messages for ALL relevant conflicting CRs
  3. Populate the `retirementWarnings` array with one entry per conflicting CR

**Frontend (`cr-summary.component.html`):**
Replace the existing single `<alert>` with:
```html
<ng-container *ngIf="retirementWarnings?.length > 0">
  <alert *ngFor="let warning of retirementWarnings" type="warning" dismissible="true">
    <h5>{{ warning }}</h5>
  </alert>
</ng-container>
```

## Note: Stale Retirement Data on Re-save

The `createRetirementData()` method is only called when `createChangeRequestTransition` is true (new CR creation, line 485). If a user goes back to the start page and changes the selected units on an existing retirement CR, the old `ChangeRequestData` records are NOT cleaned up. However, this scenario is mitigated by the single-page submit flow: once a retirement CR is created and submitted in one action, the user cannot change selected units from the start page. If they need changes, they would withdraw and create a new CR. No additional handling is needed for this release.

## Unit Testing Requirements

### Backend Tests Needed

1. **Ownership filtering in `getActiveUnitsForSubstation()`**:
   - Test: Only returns units owned by the requesting user
   - Test: ERCOT users see all units
   - Test: Empty result when user owns no units on the substation

2. **Unit ownership validation in `createRetirementData()`**:
   - Test: Rejects unit IDs that don't exist
   - Test: Rejects unit IDs not belonging to the substation
   - Test: Rejects unit IDs the user doesn't own
   - Test: Succeeds for valid owned units

3. **Existing retirement tests** (`RetirementDataCreationTest.java`, `AssetsRetirementTest.java`):
   - Verify existing tests still pass after ownership changes

### Frontend Tests
- Test `submitRetirementCr()` flow: save + status update + navigation
- Test checkbox selection/deselection updates `selectedUnitIds`
- Test retirement info displays on summary page
- Test multiple warning messages display

## Files to Modify

### Backend
| File | Change |
|------|--------|
| `SubstationsService.java` | Add ownership filtering in `getActiveUnitsForSubstation()` |
| `ChangeRequestService.java` | Add unit ownership validation in `createRetirementData()` |
| `ChangeRequestsVO.java` | Add `retirementUnitNames` field |
| `ChangeRequestService.java` | Populate `retirementUnitNames` when loading retirement CRs |
| `ChangeRequestsResource.java` | Add `/changeRequests/active/{substationId}` endpoint |
| `ChangeRequestsRepository.java` | Add `findActiveCrs(substationId)` query |

### Frontend
| File | Change |
|------|--------|
| `change-request-start.component.ts` | Add `submitRetirementCr()`, update `navTo()`, update btn label, replace unit selection handler |
| `change-request-start.component.html` | Replace `<select multiple>` with checkbox list |
| `cr-summary-change-info.component.ts` | Add retirement fields to `changeInfoAttributes` |
| `cr-summary.component.ts` | Enhance `checkRetirementWarning()` for all CRs |
| `cr-summary.component.html` | Support multiple warning messages |

### Tests
| File | Change |
|------|--------|
| New: `RetirementOwnershipTest.java` | Test ownership filtering for units |
| Existing: `RetirementDataCreationTest.java` | Add ownership validation test cases |
