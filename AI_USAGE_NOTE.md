# AI Usage Note

I used AI tools as a support tool during this project, mainly for brainstorming the application structure, checking implementation approaches, generating an initial set of dummy records, and reviewing the code for obvious issues.

I did not treat the AI output as the final decision-maker. I kept the solution intentionally simple because the scenario describes a small business whose warehouse team is experienced but not very comfortable with technology.

## Examples of my own judgment over an AI suggestion

**1. Scope of the application**

An initial AI-style approach could easily turn this into a much larger warehouse-management system with many screens and workflows. I chose not to do that. I focused on the problems explicitly described in the case: order visibility, priority handling, inventory risk, missed pickups and exceptions. This keeps the prototype realistic for a small team.

**2. Exception handling**

I chose to make exceptions a dedicated view instead of relying only on charts. A chart can show that delayed orders exist, but the operations team needs to know which orders need action. The Exceptions page therefore surfaces delayed orders, priority orders at risk, low-stock items and missed pickups as concrete work items.

AI was useful for acceleration and review, but the final scope, workflow and operational priorities were based on the case requirements and my own judgment.
