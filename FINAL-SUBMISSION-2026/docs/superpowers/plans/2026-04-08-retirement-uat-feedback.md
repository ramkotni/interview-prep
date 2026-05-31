# Retirement UAT Feedback Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement three UAT-feedback-driven changes: smart calendar date restrictions for retired stations, disable Station radio for non-owners, and read-only retirement fields in standard CRs.

**Architecture:** Backend changes add `serviceStop` to the substation overview VO and a `userOwnsStation` flag to the retirable-units endpoint. Frontend changes add `maxDate`/`markDisabled` support to the shared date picker, restrict the retirement scope radio buttons based on ownership, and conditionally set retirement-related fields to read-only in non-retirement CRs.

**Tech Stack:** Java (JAX-RS, JPA), Angular (ng-bootstrap datepicker, ngx-bootstrap tooltip, reactive forms)

**Spec:** `docs/superpowers/specs/2026-04-08-retirement-uat-feedback-design.md`

---

## File Structure

### Files to Modify

| File | Responsibility |
|------|---------------|
| `rest-api/src/main/java/com/ercot/rarf/domain/vo/SubstationOverviewVO.java` | Add `serviceStop` field |
| `rest-api/src/main/java/com/ercot/rarf/domain/Substations.java:1457-1478` | Map `serviceStop` in `toOverviewVO()` |
| `rest-api/src/main/java/com/ercot/rarf/service/SubstationsService.java:4266-4381` | Add `userOwnsStation` to `getActiveUnitsForSubstation()` |
| `web-app/src/main/angular/app/shared-components/dates/date.component.ts` | Add `maxDate`, `markDisabled`, `dayTemplate`, tooltip |
| `web-app/src/main/angular/app/shared-components/dates/date.component.html` | Bind new inputs, add day template with tooltip |
| `web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.ts:80-120,354-440` | Compute date restrictions, store `userOwnsStation` |
| `web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.html:279-370` | Wire date restrictions, disable Station radio |
| `web-app/src/main/angular/app/app_update/components/cr/topics/substation/topics/substation-details.component.ts` | Set `serviceStop` readOnly conditionally |
| `web-app/src/main/angular/app/app_update/components/cr/topics/substation/topics/substation-details.component.html:148-159` | Pass `readOnly` to date component |
| `web-app/src/main/angular/app/app_update/components/cr/topics/resource/attributes/resource-attributes-dates/resource-attributes-dates.component.ts` | Set `unitEnd` readOnly conditionally |

---

## Task 1: Add `serviceStop` to SubstationOverviewVO and toOverviewVO

**Files:**
- Modify: `rest-api/src/main/java/com/ercot/rarf/domain/vo/SubstationOverviewVO.java`
- Modify: `rest-api/src/main/java/com/ercot/rarf/domain/Substations.java:1457-1478`

- [ ] **Step 1: Add `serviceStop` field to SubstationOverviewVO**

In `SubstationOverviewVO.java`, add the field after the `active` field (after line 16) and its getter/setter (after line 86):

```java
// Add field (after line 16):
private String serviceStop;

// Add getter/setter (after the setActive method, before @Override compareTo):
public String getServiceStop() {
    return serviceStop;
}

public void setServiceStop(String serviceStop) {
    this.serviceStop = serviceStop;
}
```

- [ ] **Step 2: Map `serviceStop` in `Substations.toOverviewVO()`**

In `Substations.java`, in the `toOverviewVO(Substations substation, boolean retrieveOwner)` method (line 1457), add the `serviceStop` mapping after the `substation.toVO()` call (after line 1461). The entity's `getServiceStop()` returns a `Date`; the VO stores a `String` in `MM-dd-yyyy` format:

```java
// After line 1461 (SubstationOverviewVO substationOverviewVO = substation.toVO(SubstationOverviewVO.class);):
if (substation.getServiceStop() != null) {
    java.text.SimpleDateFormat sdf = new java.text.SimpleDateFormat("MM-dd-yyyy");
    substationOverviewVO.setServiceStop(sdf.format(substation.getServiceStop()));
}
```

- [ ] **Step 3: Verify the build compiles**

Run:
```bash
cd rest-api && mvn compile -q
```
Expected: BUILD SUCCESS (no compilation errors)

- [ ] **Step 4: Commit**

```bash
git add rest-api/src/main/java/com/ercot/rarf/domain/vo/SubstationOverviewVO.java rest-api/src/main/java/com/ercot/rarf/domain/Substations.java
git commit -m "feat(RIOO-2893): add serviceStop to SubstationOverviewVO for calendar restrictions"
```

---

## Task 2: Add `maxDate` and `markDisabled` support to the shared DateComponent

**Files:**
- Modify: `web-app/src/main/angular/app/shared-components/dates/date.component.ts`
- Modify: `web-app/src/main/angular/app/shared-components/dates/date.component.html`

- [ ] **Step 1: Add new `@Input()` properties to `date.component.ts`**

Add these imports and inputs after the existing `readOnly` input (line 41):

```typescript
// Add to imports at top (line 1-8), add TemplateRef:
import {
  AfterViewChecked,
  ChangeDetectorRef,
  Component,
  EventEmitter,
  Input,
  OnInit,
  Output,
  TemplateRef,
} from "@angular/core";

// Add import for NgbDateStruct (already imported on line 11, just verify NgbDate is also available):
import { NgbDateStruct, NgbInputDatepicker, NgbDate } from "@ng-bootstrap/ng-bootstrap";

// Add after line 41 (@Input() readOnly):
@Input() maxDate: NgbDateStruct;
@Input() markDisabled: (date: NgbDateStruct, current?: { year: number; month: number }) => boolean;
@Input() tooltipText: string;
@Input() dayTemplate: TemplateRef<any>;
```

- [ ] **Step 2: Update `date.component.html` to bind new properties**

Replace the `<input>` element (lines 14-30) with:

```html
<input
  class="col-6 form-control"
  name="date"
  id="{{ htmlId }}"
  (keypress)="restrictSpecialChar($event)"
  (paste)="fixSlash($event)"
  formControlName="{{ controlName }}"
  autocomplete="noAutoComplete"
  [minDate]="minDate"
  [maxDate]="maxDate"
  [markDisabled]="markDisabled"
  [dayTemplate]="dayTemplate"
  [ngClass]="readOnly ? 'pointer-events-none' : ''"
  [readOnly]="readOnly"
  maxlength="10"
  (ngModelChange)="onDateChange()"
  placeholder="{{ placeholder }}"
  ngbDatepicker
  #d="ngbDatepicker"
/>
```

The key additions are: `[maxDate]="maxDate"`, `[markDisabled]="markDisabled"`, and `[dayTemplate]="dayTemplate"`. When these inputs are not provided (undefined), ng-bootstrap ignores them.

- [ ] **Step 3: Verify Angular compiles**

Run:
```bash
cd web-app && npx ng build --configuration=development 2>&1 | tail -5
```
Expected: Build succeeds. No compilation errors.

- [ ] **Step 4: Commit**

```bash
git add web-app/src/main/angular/app/shared-components/dates/date.component.ts web-app/src/main/angular/app/shared-components/dates/date.component.html
git commit -m "feat(RIOO-2893): add maxDate, markDisabled, and dayTemplate support to DateComponent"
```

---

## Task 3: Implement smart calendar restrictions on CR start page

**Files:**
- Modify: `web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.ts`
- Modify: `web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.html`

- [ ] **Step 1: Add properties and imports to `change-request-start.component.ts`**

Add these imports at the top of the file (with the existing NgbDateStruct import if present, or add new):

```typescript
import { NgbDateStruct } from "@ng-bootstrap/ng-bootstrap";
import { DateSupport } from "../../../../services/dates/date-support";
```

Add these properties after the existing `displayInprogressCrMsg` property (around line 120):

```typescript
public retirementMaxDate: NgbDateStruct;
public retirementMarkDisabled: (date: NgbDateStruct) => boolean;
public retirementDayTemplate: any; // TemplateRef set from template
public retirementTooltipText: string = "This station will be retired after this date. Changes cannot be made.";
```

- [ ] **Step 2: Compute date restrictions when substation is selected**

In the `substationChange` method (line 354), after the line that sets `this.substationId` (line 359), add logic to look up the selected substation's `serviceStop` and compute the restrictions. Add this right after `this.substationId = Number.parseInt(event.target.value);` (line 359):

```typescript
// Compute retirement date restrictions for calendar
const selectedSubstation = this.substations
  .getValue()
  .find((s) => s.id === this.substationId);
if (selectedSubstation && selectedSubstation.serviceStop) {
  const serviceStopStruct = DateSupport.dateStringToStruct(
    selectedSubstation.serviceStop
  );
  // maxDate = serviceStop - 1 day (i.e., PLD - 2)
  const serviceStopDate = DateSupport.structToDate(serviceStopStruct);
  serviceStopDate.setDate(serviceStopDate.getDate() - 1);
  this.retirementMaxDate = DateSupport.dateToStruct(serviceStopDate);
  // markDisabled for dates >= serviceStop
  this.retirementMarkDisabled = (date: NgbDateStruct) => {
    const d = new Date(date.year, date.month - 1, date.day);
    const ss = DateSupport.structToDate(serviceStopStruct);
    return d >= ss;
  };
} else {
  this.retirementMaxDate = undefined;
  this.retirementMarkDisabled = undefined;
}
```

Also reset these values in `enableSubstation` (around line 279) after the line `this.retirableUnits.next([]);` (line 291):

```typescript
this.retirementMaxDate = undefined;
this.retirementMarkDisabled = undefined;
```

- [ ] **Step 3: Add day template with tooltip and wire date picker in template**

In `change-request-start.component.html`, add a day template near the top of the file (e.g., right after the opening form tag or before the date picker section). Also add `TooltipModule` import to the component.

First, add the `TooltipModule` import to `change-request-start.component.ts` imports array:

```typescript
import { TooltipModule } from "ngx-bootstrap/tooltip";

// In @Component imports array, add:
TooltipModule,
```

Then in `change-request-start.component.html`, add a custom day template before the `rs-date` usage (before line 279). Place it at the top of the template file:

```html
<!-- Retirement date restriction day template -->
<ng-template #retirementDay let-date let-disabled="disabled">
  <span
    [class.text-muted]="disabled"
    [class.retirement-disabled]="disabled"
    [tooltip]="disabled ? retirementTooltipText : ''"
    containerClass="retirement-tooltip"
    container="body"
  >
    {{ date.day }}
  </span>
</ng-template>
```

Then update the `rs-date` component usage (lines 288-296) to pass the new properties:

```html
<rs-date
  [formGroup]="form"
  [controlName]="'targetDate'"
  [caption]="dateCaption"
  [maxDate]="retirementMaxDate"
  [markDisabled]="retirementMarkDisabled"
  [dayTemplate]="retirementMaxDate ? retirementDay : null"
  (dateChangeEvent)="
    validateTargetDate(form, showModal, showEmailModal)
  "
></rs-date>
```

The `#retirementDay` template ref is referenced directly in the HTML template via `retirementDay` in the binding `[dayTemplate]="retirementMaxDate ? retirementDay : null"`, so no `@ViewChild` is needed in the TS.

- [ ] **Step 4: Verify Angular compiles**

Run:
```bash
cd web-app && npx ng build --configuration=development 2>&1 | tail -5
```
Expected: Build succeeds.

- [ ] **Step 5: Commit**

```bash
git add web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.ts web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.html
git commit -m "feat(RIOO-2893): add smart calendar date restrictions for retired stations"
```

---

## Task 4: Add `userOwnsStation` to getActiveUnitsForSubstation backend

**Files:**
- Modify: `rest-api/src/main/java/com/ercot/rarf/service/SubstationsService.java:4266-4381`

- [ ] **Step 1: Add station ownership check to `getActiveUnitsForSubstation`**

In `SubstationsService.java`, in the `getActiveUnitsForSubstation` method, after the line `response.setData(units);` (around line 4375) and before the catch block, add the station ownership check. The method already has `substation`, `filterByOwnership`, and `userDuns` in scope:

```java
// After response.setData(units); — add userOwnsStation flag
// Wrap the response in a map that includes both units and the ownership flag
boolean userOwnsStation;
if (!filterByOwnership) {
    // ERCOT users always "own" the station
    userOwnsStation = true;
} else {
    // Check if user's DUNS is in the substation's asset ownership
    userOwnsStation = false;
    Assets substationAsset = substation.getAsset();
    if (substationAsset != null) {
        List<String> stationOwnerDuns = getOwnersDuns(substationAsset);
        userOwnsStation = isOwner(stationOwnerDuns, userDuns);
    }
}
```

Now we need to restructure the response slightly. Currently `response.setData(units)` returns a list. We need to return a map with both `units` and `userOwnsStation`. Replace `response.setData(units);` with:

```java
Map<String, Object> responseData = new HashMap<>();
responseData.put("units", units);
responseData.put("userOwnsStation", userOwnsStation);
response.setData(responseData);
```

- [ ] **Step 2: Verify the build compiles**

Run:
```bash
cd rest-api && mvn compile -q
```
Expected: BUILD SUCCESS

- [ ] **Step 3: Commit**

```bash
git add rest-api/src/main/java/com/ercot/rarf/service/SubstationsService.java
git commit -m "feat(RIOO-2893): add userOwnsStation flag to getActiveUnitsForSubstation response"
```

---

## Task 5: Update frontend to handle new response structure and disable Station radio

**Files:**
- Modify: `web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.ts`
- Modify: `web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.html`

- [ ] **Step 1: Add `userOwnsStation` property to the component**

In `change-request-start.component.ts`, add this property with the other retirement-related properties (around line 115):

```typescript
public userOwnsStation: boolean = true; // default true until API response overrides
```

- [ ] **Step 2: Update the `getActiveUnitsForSubstation` response handler**

The existing handler (lines 424-437) currently expects `unitRes.data` to be an array of units. Now it's a map with `units` and `userOwnsStation`. Update the subscribe block:

Replace this code (lines 424-437):
```typescript
if (this.retirementCr && this.substationId) {
  this.dataService
    .getActiveUnitsForSubstation(this.substationId)
    .pipe(first())
    .subscribe((unitRes: ResponseStatus) => {
      this.retirableUnits.next(unitRes.data || []);
      this.retirableUnitListData.next(
        (unitRes.data || []).map((u: any) => ({
          id: u.tableName + ":" + u.id,
          value: u.name + " (" + u.type + ")",
        }))
      );
    });
}
```

With:
```typescript
if (this.retirementCr && this.substationId) {
  this.dataService
    .getActiveUnitsForSubstation(this.substationId)
    .pipe(first())
    .subscribe((unitRes: ResponseStatus) => {
      const units = unitRes.data?.units || [];
      this.userOwnsStation = unitRes.data?.userOwnsStation ?? true;
      this.retirableUnits.next(units);
      this.retirableUnitListData.next(
        units.map((u: any) => ({
          id: u.tableName + ":" + u.id,
          value: u.name + " (" + u.type + ")",
        }))
      );
    });
}
```

Also reset `userOwnsStation` in `enableSubstation` (around line 279) alongside the other resets:

```typescript
this.userOwnsStation = true;
```

- [ ] **Step 3: Disable Station radio button and add tooltip in template**

In `change-request-start.component.html`, update the Station radio button (lines 341-349). Replace:

```html
<div
  class="input--group custom-control custom-radio custom-control-inline"
>
  <input
    type="radio"
    name="retirementScope"
    value="STATION"
    class="col pl-0"
    (change)="onRetirementScopeChange($event)"
    [checked]="retirementScope === 'STATION'"
  />&nbsp;Station
</div>
```

With:

```html
<div
  class="input--group custom-control custom-radio custom-control-inline"
  [tooltip]="!userOwnsStation ? 'You do not own the station.' : ''"
  container="body"
>
  <input
    type="radio"
    name="retirementScope"
    value="STATION"
    class="col pl-0"
    (change)="onRetirementScopeChange($event)"
    [checked]="retirementScope === 'STATION'"
    [disabled]="!userOwnsStation"
  />&nbsp;Station
</div>
```

Ensure `TooltipModule` from `ngx-bootstrap/tooltip` is imported in the component (already added in Task 3).

- [ ] **Step 4: Verify Angular compiles**

Run:
```bash
cd web-app && npx ng build --configuration=development 2>&1 | tail -5
```
Expected: Build succeeds.

- [ ] **Step 5: Commit**

```bash
git add web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.ts web-app/src/main/angular/app/app_update/components/cr/start/change-request-start.component.html
git commit -m "feat(RIOO-2893): disable Station radio for non-station owners with tooltip"
```

---

## Task 6: Make `Stop Service` read-only in substation-details for non-ERCOT in non-retirement CRs

**Files:**
- Modify: `web-app/src/main/angular/app/app_update/components/cr/topics/substation/topics/substation-details.component.ts`
- Modify: `web-app/src/main/angular/app/app_update/components/cr/topics/substation/topics/substation-details.component.html`

- [ ] **Step 1: Set `serviceStop` section readOnly conditionally in the component**

In `substation-details.component.ts`, add the import for `ChangeTypeValue` and override `ngOnInit` to mark the section read-only after the base class builds the form. The `ercotUser` property is already set by `BaseFormComponent.ngOnInit()` (line 137 of base). The current CR's `changeTypeId` is available via `this.sess.getCurrentCr()`.

Add the import at the top:

```typescript
import { ChangeTypeValue } from "../../../../../../enum/changetypevalue.enum";
```

Update the `ngOnInit()` method to add the readOnly logic after the existing code:

```typescript
ngOnInit() {
  super.ngOnInit();
  const rarf = this.sess.getSubstationData();
  this.substationCode = rarf ? rarf["code"] : "";

  const states = InAppData.states;
  const counties = InAppData.counties;
  this.selectOptions = {
    county: counties,
    state: states,
  };

  // Make serviceStop read-only for non-ERCOT users in non-retirement CRs
  if (!this.ercotUser) {
    const currentCr = this.sess.getCurrentCr();
    if (currentCr && currentCr.changeTypeId !== ChangeTypeValue.RET) {
      this.subscription.add(
        this.crSections.subscribe((sections) => {
          const serviceStopSection = sections.find(
            (s) => s.dataKey === "serviceStop"
          );
          if (serviceStopSection) {
            serviceStopSection.readOnly = true;
          }
        })
      );
    }
  }

  this.spinnerService.display(false);
}
```

- [ ] **Step 2: Pass `readOnly` to the rs-date component in the template**

In `substation-details.component.html`, the `rs-date` for date fields (lines 148-159) doesn't currently pass `[readOnly]`. Add it:

Replace:
```html
<rs-date
  [formGroup]="ctrl"
  [controlName]="section.dataKey"
  [htmlId]="section.dataKey + i"
  [caption]="section.label"
  [minDate]="minDate"
  [placeholder]="
    section.placeholder[
      ctrl.controls['id'].value
    ]
  "
></rs-date>
```

With:
```html
<rs-date
  [formGroup]="ctrl"
  [controlName]="section.dataKey"
  [htmlId]="section.dataKey + i"
  [caption]="section.label"
  [minDate]="minDate"
  [readOnly]="section.readOnly"
  [placeholder]="
    section.placeholder[
      ctrl.controls['id'].value
    ]
  "
></rs-date>
```

- [ ] **Step 3: Verify Angular compiles**

Run:
```bash
cd web-app && npx ng build --configuration=development 2>&1 | tail -5
```
Expected: Build succeeds.

- [ ] **Step 4: Commit**

```bash
git add web-app/src/main/angular/app/app_update/components/cr/topics/substation/topics/substation-details.component.ts web-app/src/main/angular/app/app_update/components/cr/topics/substation/topics/substation-details.component.html
git commit -m "feat(RIOO-2893): make Stop Service read-only for non-ERCOT in non-retirement CRs"
```

---

## Task 7: Make `Retirement Date` read-only in resource-attributes-dates for non-ERCOT in non-retirement CRs

**Files:**
- Modify: `web-app/src/main/angular/app/app_update/components/cr/topics/resource/attributes/resource-attributes-dates/resource-attributes-dates.component.ts`

- [ ] **Step 1: Set `unitEnd` section readOnly conditionally**

In `resource-attributes-dates.component.ts`, add the import and update `ngOnInit()`. The `rs-update-form` template already passes `[readOnly]="section.readOnly"` to `rs-date` (line 175 of update-form.component.html), so we only need to set `readOnly` on the section object.

Add import:
```typescript
import { ChangeTypeValue } from "../../../../../../enum/changetypevalue.enum";
```

Update `ngOnInit()`:

```typescript
ngOnInit() {
  super.ngOnInit();
  this.disableFormFields(this.formUnits$.getValue());

  // Make unitEnd (Retirement Date) read-only for non-ERCOT users in non-retirement CRs
  if (!this.ercotUser) {
    const currentCr = this.sess.getCurrentCr();
    if (currentCr && currentCr.changeTypeId !== ChangeTypeValue.RET) {
      this.subscription.add(
        this.crSections.subscribe((sections) => {
          const unitEndSection = sections.find(
            (s) => s.dataKey === "unitEnd"
          );
          if (unitEndSection) {
            unitEndSection.readOnly = true;
          }
        })
      );
    }
  }
}
```

- [ ] **Step 2: Verify Angular compiles**

Run:
```bash
cd web-app && npx ng build --configuration=development 2>&1 | tail -5
```
Expected: Build succeeds.

- [ ] **Step 3: Commit**

```bash
git add web-app/src/main/angular/app/app_update/components/cr/topics/resource/attributes/resource-attributes-dates/resource-attributes-dates.component.ts
git commit -m "feat(RIOO-2893): make Retirement Date read-only for non-ERCOT in non-retirement CRs"
```

---

## Task 8: Final build verification and integration commit

- [ ] **Step 1: Full backend build**

Run:
```bash
cd rest-api && mvn compile -q
```
Expected: BUILD SUCCESS

- [ ] **Step 2: Full frontend build**

Run:
```bash
cd web-app && npx ng build --configuration=development 2>&1 | tail -10
```
Expected: Build succeeds with no errors.

- [ ] **Step 3: Manual verification checklist**

Verify these scenarios work correctly:
1. **Smart Calendar:** Select a substation with `serviceStop` set → target date picker should disable dates >= `serviceStop` and show tooltip on hover
2. **Smart Calendar (no retirement):** Select a substation without `serviceStop` → date picker should have no max date restriction
3. **Station Radio:** Create a retirement CR as a user who only owns units → "Station" radio should be disabled with tooltip
4. **Station Radio (owner):** Create a retirement CR as a user who owns the station → both radios enabled
5. **Stop Service read-only:** Open a standard CR, navigate to substation Details → "Stop Service" field should be read-only for non-ERCOT
6. **Retirement Date read-only:** Open a standard CR, navigate to unit Dates → "Retirement Date" field should be read-only for non-ERCOT
7. **Retirement CR editable:** Open a retirement CR → both fields should remain editable
8. **ERCOT user:** All fields should remain editable regardless of CR type
