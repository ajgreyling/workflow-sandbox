# Project Guidelines

Project invariants (stack, architecture and conventions) are in [AGENTS.md](../AGENTS.md).

## Workflow

- The product backlog lives in [docs/backlog.md](../docs/backlog.md).
- Each feature has a unique ID in the format `F-<number>` (e.g. `F-123`). IDs are sequential and never reused.
- Use the `/add-feature` prompt to add new features to the backlog. It asks all design questions upfront, then writes the backlog entry and a spec in `docs/features/F-<number>.md`. Backlog items can also be added by hand.
- Browser tests live in [tests/](../tests/test-pack.md), with one file per feature (`tests/features/F-<number>.md`).
- Use the `/test-cdp` prompt to run the tests in Chrome through the Chrome DevTools MCP server ([.vscode/mcp.json](../.vscode/mcp.json)).
- Use `/dev-feature F-<number>` to implement a backlog item. It pulls `main`, switches to a branch named `F-<number>-<slug>`, writes a plan to `docs/plans/F-<number>-plan.md`, writes the browser and headless Playwright Cucumber tests during planning, adds unit tests, and finishes only when all suites pass.
- Backlog statuses: `Proposed` → `In progress` → `Done`.
