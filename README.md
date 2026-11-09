# Contoso Support Demo

A fictional service desk built on **Dynamics 365 Customer Service + Power Platform + Copilot**, documented step by step. Everything here is invented: the company, customers, cases and documents. Nothing comes from a real project.

> Status: work in progress. Built in a personal demo tenant; features are verified against Microsoft Learn and linked from each guide.

## The scenario

**Contoso Energy Home** sells smart thermostats and solar inverters to consumers, installer partners and enterprise customers. Its support team works with three service tiers:

| Tier | First response | Resolution | Hours |
|---|---|---|---|
| Standard | 8 h | 5 business days | Mon-Fri 9-18 |
| Premium | 4 h | 3 business days | Mon-Fri 8-20 |
| Partner / Enterprise | 1 h | 1 business day | 24/7 for critical |

Queues: Tier 1 General, Tier 2 Technical, Partner Desk.

## What is covered

| Topic | Guide | Status |
|---|---|---|
| Environment setup | [docs/01-environment-setup.md](docs/01-environment-setup.md) | planned |
| SLA | [docs/02-sla/](docs/02-sla/) | planned |
| Agent Scripts | [docs/03-agent-scripts/](docs/03-agent-scripts/) | planned |
| Customer Service workspace | [docs/04-workspace/](docs/04-workspace/) | planned |
| Email intake agent (AI) | [docs/08-email-intake/](docs/08-email-intake/) | planned |

## Repository layout

- `docs/` step-by-step guides (Goal, Prerequisites, Steps, Result, Gotchas, Links)
- `solutions/` unpacked Power Platform solutions (no secrets)
- `data/` synthetic data and the generator script
- `templates/` reusable checklists and templates
- `screenshots/` sanitized screenshots
- `scripts/` helper scripts

## Reproduce the demo

1. Start a Dynamics 365 Customer Service trial (see the environment guide).
2. Import the solution from `solutions/`.
3. Generate and load the synthetic data from `data/`.
4. Follow the guides in `docs/`.

## License

Code and data: [MIT](LICENSE). This is an independent community project, not affiliated with or endorsed by Microsoft. "Contoso" is a fictional company name commonly used in Microsoft examples.
