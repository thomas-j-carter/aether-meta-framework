# AI Assistant Operating Guide

Use this file as the baseline operating contract for any AI assistant contributing to this repository.

## Core Behavior

The assistant must do more than produce code. It must also:

1. Teach while building.
2. Expose reasoning and trade-offs.
3. Mitigate risk proactively.
4. Keep work reproducible and auditable.

## Required Response Pattern (Every Task)

For each requested change, the assistant should produce output in this order:

1. **Intent**
   - Restate the objective in plain language.
2. **Plan**
   - Break into minimal, testable steps.
3. **Execution**
   - Implement one step at a time.
4. **Reasoning**
   - Explain why the chosen approach is preferred.
5. **Validation**
   - Run checks/tests and interpret results.
6. **Commit Recommendation**
   - If a coherent checkpoint is reached, recommend a commit.
7. **Documentation Delta**
   - Update user/dev docs and tutorial notes.

## Commit Guidance

Commit whenever one of the following is complete:

- A single user story slice is implemented and verified.
- A structural refactor is complete and tests pass.
- A documentation milestone is fully updated.
- An ADR is accepted and applied.

Commit message format (Conventional Commits):

- `feat(scope): short summary`
- `fix(scope): short summary`
- `docs(scope): short summary`
- `refactor(scope): short summary`
- `test(scope): short summary`
- `chore(scope): short summary`

Example:

- `docs(ai): add idempotent tutorial and workflow ADR`

## Documentation Obligations

When changing behavior or architecture, update as needed:

- `docs/requirements/*` for intent and stories.
- `docs/architecture/adr/*` for decision records.
- `docs/tutorial/IDEMPOTENT_TUTORIAL.md` for step-by-step reproducibility.
- `docs/tutorial/MASTER_LOG.md` for chronological milestones.

## Idempotency Rules

The assistant should ensure another developer can reproduce outcomes by following the docs exactly:

- Include exact commands.
- State assumptions and prerequisites.
- Avoid hidden/manual-only steps.
- Record expected output where useful.
- Keep steps deterministic.

## Risk Controls

The assistant should explicitly watch for:

- breaking changes,
- dependency/security concerns,
- ambiguous requirements,
- missing tests or validation,
- documentation drift.

When a risk is found, the assistant should surface it immediately with a mitigation proposal.
