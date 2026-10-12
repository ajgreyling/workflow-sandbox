---
description: "Plan and implement a backlog feature by ID (e.g. F-123), with unit, Cucumber and Chrome DevTools tests that must pass"
argument-hint: "Feature ID, e.g. F-123"
agent: "agent"
tools: [read, edit, search, execute, todo, 'chrome-devtools/*']
---
Develop the backlog feature with the ID given by the user (e.g. `F-123`).

The task is complete only when every test listed in the plan exists and passes, and the full unit, Cucumber and browser suites are green in the same final run. Until then, never report the feature as done.

## 1. Sync with main

Do this before reading or changing any files.
1. Run `git status --porcelain`. If there are uncommitted changes, stop and tell the user. Never stash, discard or commit them yourself.
2. If the current branch (`git branch --show-current`) is not `main`, switch to it with `git switch main`.
3. Run `git pull --ff-only`. If `main` has no upstream, or the pull fails (e.g. diverged history or a network error), stop and report the error.

## 2. Understand the feature

1. Find the feature's row in [docs/backlog.md](../../docs/backlog.md). If the ID is missing, or there is no row with that ID, stop and tell the user.
2. Create a branch from the updated `main` and switch to it: `git switch -c F-<number>-<slug>`. Build the slug from the feature title: 2 to 5 lowercase words joined by hyphens, using only `a-z`, `0-9` and `-` (e.g. `F-123-add-blue-red-button`). If a branch for this feature ID already exists, switch to that branch instead of creating a new one. Make all later changes on this branch.
3. Read the spec in `docs/features/F-<number>.md`, if it exists, and treat it as the source of truth. Backlog items added by hand may have no spec; in that case, work from the backlog row's title and description. Do not ask the user design questions. If something is unclear, choose the option that best fits the spec or backlog item, and record the choice under Approach in the plan.
4. Read [tests/test-pack.md](../../tests/test-pack.md), and the feature's browser tests in `tests/features/F-<number>.md` if that file exists.
5. Read [AGENTS.md](../../AGENTS.md). Its invariants apply to every feature, so the implementation must not break them. If the spec conflicts with AGENTS.md, stop and tell the user. Explore the existing code to learn the structure and test setup.
6. Set the feature's status in the backlog to `In progress`.

## 3. Create the plan

Save the plan to `docs/plans/F-<number>-plan.md` (e.g. `docs/plans/F-123-plan.md`), creating the `docs/plans/` folder if it does not exist. Use the format below, and mirror its tasks in the todo list. Keep this file up to date as you work; it is the persistent record of the plan. The plan must list the implementation tasks and all tests, so that every requirement in the spec (or, with no spec, every part of the backlog item) is covered by at least one test:
- The implementation tasks.
- The **unit tests** for the new logic.
- The **Cucumber scenarios** for the feature's behaviour, run headless in Playwright.
- The **Chrome DevTools browser tests** (`F-<number>-T<n>`) for the feature. If `tests/features/F-<number>.md` already exists, keep its tests and add any that are missing.

```markdown
# F-<number>: <Feature title> — Plan

## Goal
<One or two sentences from the backlog item.>

## Approach
<Short description of the design and the files you will touch.>

## Tasks
- [ ] ...

## Tests
### Unit
- [ ] <test name>: <what it checks>
### Cucumber (Playwright, headless)
- [ ] Scenario: <name>
### Browser (Chrome DevTools)
- [ ] F-<number>-T1: <title>

## Definition of done
- [ ] All unit tests pass
- [ ] All Cucumber scenarios pass
- [ ] All Chrome DevTools browser tests pass
```

Still in this stage, before writing any implementation code, write the browser and Cucumber tests:
1. Write the Chrome DevTools browser tests to `tests/features/F-<number>.md`, using the layout and format in [tests/test-pack.md](../../tests/test-pack.md). Include one test for each item in the plan's Browser section.
2. If Cucumber is not set up with Playwright yet, set it up:
   - Add `playwright` to the `dev` extras in `pyproject.toml`, install it, and install Chromium with `.venv/bin/python -m playwright install chromium`.
   - In `tests/cucumber/environment.py`, start the app at the base URL, launch Chromium with `headless=True`, and open a new `context.page` for each scenario. Close everything in the matching `after_*` hooks. Keep existing steps working.
   - Record the Playwright install command in the Configuration section of `tests/test-pack.md`.
3. Write `tests/cucumber/F-<number>.feature` tagged `@F-<number>`, with one scenario for each item in the plan's Cucumber section.
4. Write the step definitions in `tests/cucumber/steps/`. Use Playwright's sync API on `context.page` to act as a user would, and reuse existing steps where they fit.
5. Run `.venv/bin/python -m behave tests/cucumber --tags=@F-<number>`. The scenarios should fail only because the feature is not built yet. Fix any undefined steps or errors in the step code.

## 4. Implement

1. If the project has no unit test runner or Cucumber setup yet, add one that fits the stack. Record the commands in the Configuration section of `tests/test-pack.md`.
2. Implement the tasks. Tick each item in the plan as you finish it.
3. Add the unit tests from the plan, following the layout in `tests/test-pack.md`. Include the feature ID in the test names.
   - The browser and Cucumber tests were written in step 3. Change one only if it is wrong, and never weaken it.
4. If the app's base URL or start command is not yet set in `tests/test-pack.md`, set it.
5. If you add something every future feature must follow (a dependency, a top-level folder or a project-wide pattern), add it as one short line in the matching section of `AGENTS.md`. Never change or remove an existing invariant.

## 5. Verify (must be green)

1. Run the full unit test suite and the full Cucumber suite, not just the new tests.
2. Run all browser tests by following [test-cdp.prompt.md](./test-cdp.prompt.md).
3. Check every item in the plan's Tests section against the results. Each one must exist, must have run, and must have passed. Skipped, pending, undefined or `Blocked` counts as not green. Tick an item only once it has passed.
4. If anything fails or is not green, fix the code (or a test that is wrong because of a mistake in the test itself) and rerun all three suites. Never delete, skip or weaken a test just to make it pass, and never remove a test from the plan.
5. If a failure is still unresolved after three fix attempts, stop. Leave the status as `In progress`, leave the failing items unticked, and report the task as **not complete**, with what is failing and why.

The plan is complete only when every planned test is ticked and all three suites pass in the same run, after your last code change. Only then tick the Definition of done items and set the backlog status to `Done`.

## 6. Report

Reply with:
- The status: **Complete** (every planned test green and all suites passing) or **Not complete** (with the reason).
- The branch name.
- A link to the plan.
- The files you changed.
- A results table from the final run:

```markdown
| Suite | Passed | Failed | Skipped/Blocked |
|-------|--------|--------|-----------------|
| Unit | | | |
| Cucumber | | | |
| Browser (Chrome DevTools) | | | |
```

- If the task is not complete, list each planned test that is not green and why.
