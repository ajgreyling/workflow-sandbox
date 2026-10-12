---
description: "Add a new feature with a unique F-<number> ID to docs/backlog.md, plus its spec"
argument-hint: "Describe the feature to add"
agent: "agent"
tools: [read, edit, search, vscode/askQuestions]
---
Add the feature described by the user to the backlog in [docs/backlog.md](../../docs/backlog.md).

Only add the backlog entry and its spec, and update [AGENTS.md](../../AGENTS.md) when an answer sets a project invariant. Do not write tests (`/dev-feature` writes them when it plans the feature), do not implement the feature, and do not change any other files.

## 1. Ask questions first

This is the only chance to ask questions. `/dev-feature` implements the feature later without asking anything, so every design or high-impact decision must be settled now.

1. Read `docs/backlog.md`, [AGENTS.md](../../AGENTS.md), [tests/test-pack.md](../../tests/test-pack.md) and enough of the app to know what already exists. Don't ask about anything AGENTS.md already settles. If the feature would break an invariant in AGENTS.md, ask whether to change the invariant or the feature.
2. Before writing any files, ask the user every question whose answer would change the design, the behaviour or the tests. Check each area below and skip only what the user's input already answers clearly:
   - **Goal and scope:** who it is for, what problem it solves, what is explicitly out of scope.
   - **Stack and architecture:** only if the feature needs something AGENTS.md doesn't cover yet, such as a new library, data store, folder layout or pattern.
   - **UI:** where it appears, labels and text, exact colours, sizes and layout, and how it fits with existing controls.
   - **Behaviour:** the initial state, every state and transition, and what each user action does.
   - **Data and persistence:** what is stored, where, and for how long (reload, new tab, other users).
   - **Backend and API:** new endpoints, request and response shapes, validation.
   - **Errors and edge cases:** invalid input, rapid or repeated actions, empty states, failures.
   - **Accessibility:** keyboard use, focus, accessible names, colour contrast.
   - **Devices and browsers:** screen sizes and responsiveness.
   - **Interaction with existing features:** what it must not break or change.
   - **Acceptance criteria:** what must be true for the feature to count as done.
3. Ask every question as a multiple-choice question:
   - Give 2–4 concrete options, and mark one as **(recommended)**.
   - Always add a final **Other** option where the user can type their own answer.
   - Allow more than one selection when the options don't exclude each other (e.g. which screen sizes to support).
4. Ask all questions in one round, grouped by area, using #tool:vscode/askQuestions. If that tool is not available, write them as one numbered list in a single message, in this format, then end your turn and wait for the answers:

   ```markdown
   **UI**
   3. Where should the button appear?
      - a) On the home screen, next to the existing controls **(recommended)**
      - b) In a header bar
      - c) Other: ___
   ```

   The user can reply "use recommended", or answer with the question number and letter (e.g. `3b`). For Other, they type their own answer (e.g. `3c: in the footer`).
5. If the answers raise new questions or contradict each other, ask a follow-up round in the same way. Continue only when nothing that affects the design is left open.

## 2. Write the backlog entry and spec

Steps:
1. If `docs/backlog.md` does not exist, create it with the table header shown below.
2. Find the highest existing feature ID (`F-<number>`) and use the next number. If there are none, start at `F-1`. Never reuse an ID.
3. Write a short title and a one-sentence description from the user's input.
4. Append a new row to the end of the table with status `Proposed`.
5. Write the spec to `docs/features/F-<number>.md` using the spec format below. Record every answer, including the agreed error and edge cases. The spec is the source of truth for `/dev-feature`, which derives the plan and all tests from it.
6. Update [AGENTS.md](../../AGENTS.md) with any answer that sets a project invariant, meaning a rule every current and future feature must follow:
   - **Invariants (AGENTS.md):** stack and library choices, architecture and folder layout, data storage approach, API conventions, coding and testing conventions, and UI-wide rules such as the accessibility baseline or supported screen sizes.
   - **Not invariants (spec only):** anything that applies to this feature alone or is likely to change, such as its behaviour, labels, colours, flows, endpoints and data fields.
   - Add each invariant to the matching section (Stack, Architecture or Conventions). Update an existing line rather than adding a duplicate. Keep each item to one short line, and record it in the spec's Decisions as well.

Table format:

```markdown
| ID | Title | Description | Status |
|----|-------|-------------|--------|
| F-1 | Example title | One-sentence description. | Proposed |
```

Spec format:

```markdown
# F-<number>: <Feature title> — Spec

## Summary
<Two or three sentences on the goal and who it is for.>

## Requirements
1. <One testable statement per requirement.>

## Decisions
- **<Question>:** <Answer> (<"user" or "recommended">)

## Out of scope
- ...
```

When you're done, reply with the new feature ID and title, a link to the spec, and any changes to AGENTS.md.
