# AGENTS.md

Project invariants: rules about the stack, architecture and conventions that hold for every feature and don't change from one feature to the next. Changing one is a deliberate project decision, never a side effect of a feature. Feature-specific behaviour belongs in `docs/features/F-<number>.md`, not here.

## Stack

- Python 3.11+, [FastAPI](https://fastapi.tiangolo.com/) app served by uvicorn.
- HTML pages: Jinja2 templates rendered by FastAPI, with small vanilla JS where needed. No frontend framework.
- Database: SQLite through Python's built-in `sqlite3` module. No ORM.
- Dependencies are in [pyproject.toml](pyproject.toml). Set up with `python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"`.
- Unit tests: pytest (`tests/unit/`).
- Cucumber tests: behave (`tests/cucumber/`), driving the UI with Playwright in headless Chromium.
- Browser tests: Chrome DevTools MCP server (`tests/features/`), run with `/test-cdp`.
- All test and run commands are in [tests/test-pack.md](tests/test-pack.md).

## Architecture

- Single FastAPI app in `app/`, with its entry point at `app.main:app`.
- `GET /health` returns `{"status": "ok"}` and is used by smoke tests.
- The home screen is the page at `/`.
- The SQLite database is `data/app.db` (git-ignored). Override the path with the `APP_DB_PATH` environment variable; tests use a temporary database.
- Tables are created on app startup with `CREATE TABLE IF NOT EXISTS`. No migrations.
- JSON APIs live under `/api/` and are REST-style: `201` on create, `200` on read and update, `204` on delete, `404` if not found, `422` for invalid input.
- Timestamps are stored in UTC.

## Conventions

- Run all Python tools through the venv (`.venv/bin/python -m ...`).
- Tests are tagged or named with their feature ID (`F-<number>`), following [tests/test-pack.md](tests/test-pack.md).
- Validate user input in both the browser and the server.
- The UI must be usable without horizontal scrolling on mobile (375px and up), tablet and desktop.
- Accessibility baseline: every input has a visible, associated label; error messages are linked to their inputs (`aria-describedby`); Enter submits forms.
- Modals and dialogs: Cancel and Escape close them, focus is trapped while open and returns to the opener on close.
