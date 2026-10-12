---
description: "Run all browser tests in the test pack using Chrome DevTools (CDP)"
argument-hint: "Optional: feature or test IDs to run (default: all)"
agent: "agent"
tools: [read, search, execute, 'chrome-devtools/*']
---
Run the browser tests in the test pack using the Chrome DevTools MCP tools.

Do not change application code or test files. Only run the tests and report the results.

Steps:
1. Read [tests/test-pack.md](../../tests/test-pack.md) for the base URL and start command. If either one is not set, stop and tell the user which value is missing.
2. Find the test files in `tests/features/`. Run every test unless the user listed specific feature or test IDs.
3. If the base URL can't be reached, start the app with the start command (as a background process) and wait until it responds.
4. Launch Chrome through the Chrome DevTools tools and open a new page.
5. For each test, in file order:
   - Run the steps on a freshly loaded base URL.
   - Take a page snapshot to find elements, then click, type, or select as the steps describe.
   - Check every expected result against the page snapshot and the console messages.
   - Mark the test `Pass`, `Fail`, or `Blocked` (if it could not be run). For a `Fail`, record what you saw. Take a screenshot when it helps explain the failure.
6. Close the browser pages you opened and stop any process you started.

Reply with a results table, followed by the details of any failures:

```markdown
| Test ID | Title | Result | Notes |
|---------|-------|--------|-------|
| F-1-T1 | Page loads without errors | Pass | |
```

End with a summary line: `<passed> passed, <failed> failed, <blocked> blocked`.
