# Test Pack

Tests for backlog features. `/dev-feature` adds and runs all three types. `/test-cdp` runs the browser tests in Chrome using the Chrome DevTools MCP server.

## Configuration

- **Base URL:** `http://127.0.0.1:8000`
- **Start command:** `.venv/bin/python -m uvicorn app.main:app --port 8000`
- **Unit test command:** `.venv/bin/python -m pytest`
- **Cucumber command:** `.venv/bin/python -m behave tests/cucumber`

## Layout

- **Unit tests:** `tests/unit/test_<name>.py` (pytest). Include the feature ID in the module docstring or test names, e.g. `test_f1_...`.
- **Cucumber:** `tests/cucumber/F-<number>.feature` (behave) tagged `@F-<number>`, with step definitions in `tests/cucumber/steps/`. UI steps drive the app through Playwright in headless Chromium (`context.page`). `/dev-feature` writes them during planning, before the implementation.
- **Browser tests (Chrome DevTools):** one file per feature, `tests/features/F-<number>.md`. The rest of this file describes them.
- Test IDs are `F-<number>-T<n>`, numbered from `T1` within each feature file.
- Steps must be things a user can do in a browser (open, click, type, select, resize). Expected results must be observable (visible text, element state, URL, console output).

## Test file format

```markdown
# F-<number>: <Feature title>

## F-<number>-T1: <Short test title>

**Steps**
1. Open the base URL.
2. ...

**Expected**
- ...
```
