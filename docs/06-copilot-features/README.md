# Copilot features for agents: what works in the trial (Contoso Support)

> Tested on 2026-11-20 in a 30-day Dynamics 365 Customer Service trial with no purchased Copilot Credits. Results can differ by tenant, region and release; verify against Microsoft Learn.

## Goal
Find out which Copilot-based agent features run on the demo environment without paid capacity, so the posts and videos only promise what a reader can reproduce in a trial.

## Summary
| Feature | Where | Result in the trial |
|---|---|---|
| Case summary | Card on the case form | Works |
| Copilot help pane (Ask a question) | Copilot pane next to the case | Opens, but every question returned "There's no answer related to your question" |
| Smart assist | Productivity pane | Nothing shown on a case; by design (see below) |
| Similar cases | Case > Related > Similar Cases | Not tested yet |

## Case summary
Steps:
1. Copilot Service admin center > Support experience > Productivity > Summaries > Manage: turn on "Make case summaries available to representatives" (opt in to the terms if asked).
2. Fill the case so the source fields hold enough text. Learn: at least 38 English words across the fields Copilot uses (title, description, notes, emails), otherwise no summary is generated.
3. Open the case in Copilot Service workspace and expand the Case summary card.

Result: the summary reproduced the case facts (device, symptoms, what the customer tried, the agent note and the next step). The card offers Copy, Refresh and feedback, and shows the "AI-generated content may be incorrect" notice.

![Case summary](../../screenshots/06-copilot-features/01-case-summary.png)

## Copilot help pane (Ask a question)
Steps: Copilot for questions and emails > Ask a question On; in the experience profile the Copilot help pane toggle On; refresh the browser.

Result: the pane opened, but three questions ("Summarize this case", "How do I fix Wi-Fi pairing on the thermostat?", "What should I check before approving a warranty replacement?") all returned "There's no answer related to your question. Provide more details or try another topic." The details for tech support only list a request ID, and there was no message about missing credits. The cause is not established.

![Copilot help pane](../../screenshots/06-copilot-features/02-copilot-help-pane-no-answer.png)

## Smart assist
The experience profile has Smart assist On, but no Smart assist content appears in the Productivity pane on a case. This is not a trial limit. Microsoft Learn (Manage smart assist) says:
- the case and knowledge suggestions in smart assist are not supported starting 2 June 2025 (see deprecations in Customer Service);
- smart assist now shows recommendations from your own agent built with Azure Bot Service, in conversation channels such as chat, SMS and Facebook, excluding the Entity Records channel (case forms);
- Copilot Studio agents are not supported as smart assist agents, and recommendations appear only after the representative sends a message.

So the toggle in the experience profile does not give AI suggestions for cases any more. Use the Knowledge search pane (see [05-knowledge-base](../05-knowledge-base/README.md)) and Similar cases instead.

Separately, the Insights settings page in Copilot Service admin center shows "Insights settings are unavailable. The free trial and air gapped organizations do not have access to the insights settings." Insights-based features cannot be configured in a trial.

## Gotchas
- Case summary needs enough text in the case fields (about 38 English words); cases with an empty description get no summary.
- A working Case summary does not mean the Copilot help pane works: the two are separate settings and the pane returned no answers here.
- Smart assist no longer suggests knowledge articles or similar cases (deprecated 2 June 2025); it only shows recommendations from a custom bot in conversation channels. Do not build a post around it for case forms.
- Insights settings are not available in a free trial.
- Do not promise these features to readers without checking licences and capacity in their own tenant.

## Links
- https://learn.microsoft.com/dynamics365/customer-service/use/copilot-use-summary
- https://learn.microsoft.com/dynamics365/contact-center/administer/copilot-enable-summary
- https://learn.microsoft.com/dynamics365/customer-service/administer/configure-copilot-features
- https://learn.microsoft.com/dynamics365/customer-service/use/oc-view-ai-suggested-cases-articles
- https://learn.microsoft.com/dynamics365/customer-service/administer/productivity-tools
- https://learn.microsoft.com/dynamics365/customer-service/administer/smart-assist

_Verified on: 2026-11-20 (live trial; Learn pages above)_
