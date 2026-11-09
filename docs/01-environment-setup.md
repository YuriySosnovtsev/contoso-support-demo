# Environment setup

## Goal
A clean demo environment with Dynamics 365 Customer Service where the demo can be reproduced.

## Prerequisites
- A Microsoft account / tenant that is NOT tied to any employer
- Work or school Entra identity as admin (needed for the admin center, trial extension, extra users)

## Steps
1. Start the Dynamics 365 Customer Service trial.
2. Confirm the Copilot Service admin center opens.
3. Enable calendar export and import for SLAs (Service terms > Other SLA settings).
4. Create the custom solution `ContosoSupport` with its own publisher.
5. Import the demo solution and load the synthetic data.

## Result
_TBD_

## Gotchas
- Trial: 30 days, one extension; expires after 14 days of inactivity; cannot be reset, backed up or copied.
- Check availability of Agent Scripts, Copilot and AI Builder in your region.

## Links
- https://learn.microsoft.com/dynamics365/customer-service/implement/try-customer-service
- https://learn.microsoft.com/dynamics365/customer-service/implement/trial-faq

_Verified on: 2026-11-09 (docs only; not yet tested end to end)_
