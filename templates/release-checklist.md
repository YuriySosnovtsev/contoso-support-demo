# Pre-publish checklist (run before every push)

- [ ] `scripts/prepublish-scan.ps1` passes with no findings
- [ ] No environment URLs (*.crm*.dynamics.com, *.powerapps.com, make.*.com/environments/<GUID>)
- [ ] No tenant / environment / user GUIDs, no real email domains
- [ ] Unpacked solution: connection references and environment variables have no values/secrets
- [ ] Screenshots: no address bar, tenant/org names, user names, avatars, notifications
- [ ] File metadata cleaned (images, Office files)
- [ ] Git author is the GitHub noreply address
- [ ] Nothing resembles a real employer or client project (names, process, SLA numbers invented)
- [ ] No Microsoft logos used as our own; disclaimer present in README
- [ ] Links to Microsoft Learn checked; "Verified on" dates filled
- [ ] Manual read of `git diff --staged`
