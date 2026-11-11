# SLA setup checklist

Order matters. Work top to bottom. Each step links to Microsoft Learn; items marked "(trial)" come from testing in the Contoso Support demo environment.

## 1. Pause: decide first
- [ ] Decide which case statuses pause the clock (for example On Hold, Waiting for Details) and at which level: entity (Service Configuration Settings), SLA KPI, or SLA item (Override Criteria).
- [ ] Decide it before building: **Allow Pause and Resume cannot be changed after the SLA item is first saved** (trial).
- [ ] Remember: resuming cancels the current SLA KPI instance and creates a new one.
- Learn: [Configure pause conditions](https://learn.microsoft.com/dynamics365/customer-service/administer/set-pause-conditions-sla)

## 2. Calendars, holidays, owners
- [ ] Business hours calendars created (standard, extended, 24/7) and holiday schedules added.
- [ ] A named owner for holiday schedules (they need yearly updates; add next year's dates).
- [ ] Calendar time zone set. When reading timers, the user's time zone should match the calendar time zone, or Failure and Warning times look shifted.
- Learn: [Warning and failure times incorrect](https://learn.microsoft.com/troubleshoot/dynamics-365/customer-service/service-level-agreements/warning-failure-times-incorrect-sla)

## 3. KPIs and one SLA per tier
- [ ] SLA KPIs defined (First Response By, Resolve By); Applicable From is a date/time field that is always filled in (not Modified On).
- [ ] One SLA per tier. Applicable When uses a field that does not change after creation (for example Created On).
- [ ] No two SLA items with the same KPI and the same Applicable When in one SLA.
- Learn: [Define SLAs](https://learn.microsoft.com/dynamics365/customer-service/administer/define-service-level-agreements), [SLA limitations](https://learn.microsoft.com/dynamics365/customer-service/administer/sla-limitations)

## 4. Warning and failure actions
- [ ] Warning and failure durations set in the calendar's business hours.
- [ ] Actions configured (notification, flow, escalation). They are asynchronous, so short durations (under an hour) can fire late.
- Learn: [Define SLAs](https://learn.microsoft.com/dynamics365/customer-service/administer/define-service-level-agreements)

## 5. How the SLA reaches the case
- [ ] Choose: automatic (flow or plug-in), entitlement, or default SLA. Lookup order: automatic, then entitlement, then default.
- [ ] If using entitlements: Customer is the account, SLA is set, dates cover today, entitlement is Active. Check that the Entitlement field on the case is filled (it was not filled automatically in the trial).
- [ ] Only one SLA can apply to a case.
- Learn: [Apply SLAs](https://learn.microsoft.com/dynamics365/customer-service/administer/apply-slas)

## 6. Activate and test
- [ ] SLAs activated (edits to active SLA items create active-layer changes; plan changes through solution upgrades).
- [ ] One test case per tier: timer starts, warns, breaches, pauses and resumes.

## 7. Deployment
- [ ] "Enable calendar export and import" turned on before exporting the solution.
- [ ] SLAs added to the solution; deactivate them in the target before re-import.
- [ ] After import, check the SLA status in the target environment and activate manually if needed (trial experience).

## 8. Reporting
- [ ] After pauses and resumes a case has several KPI instances for the same KPI. Merge or filter them per case and KPI in reports (keep the active or latest one).

Verified against Microsoft Learn on: 2026-11-11
