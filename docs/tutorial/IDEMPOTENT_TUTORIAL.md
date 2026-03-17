# Idempotent Tutorial: AI-Driven Project Delivery

This tutorial defines a reproducible workflow for building the project with AI support.

## 0) Prerequisites

- Git installed.
- Python tooling as needed for project runtime.
- One AI assistant (ChatGPT, Claude, Gemini, etc.).

## 1) Clone and Baseline

```bash
git clone <your-repo-url>
cd aether-meta-framework
git status
```

Expected state: clean working tree.

## 2) Establish AI Session Contract

At the beginning of every AI session, provide this instruction:

> Work in small, verifiable steps. For each step: explain intent, plan, implementation, reasoning, validation, and whether this is a good commit point (with a recommended commit message). Update project docs and tutorial artifacts when behavior or architecture changes.

Then ask the AI to confirm the contract before coding.

## 3) Delivery Loop (Repeat Per Story)

For each user story:

1. Clarify acceptance criteria.
2. Ask AI for a minimal implementation plan.
3. Implement one step.
4. Run tests/checks.
5. Update docs.
6. Commit at a stable checkpoint.

### Commit Prompt Template

Use this if the AI forgets commit guidance:

> Is this a coherent commit point? If yes, propose a Conventional Commit message and a short commit body.

## 4) Recommended Milestone Commits

Use these examples as a baseline:

1. `docs(requirements): refine product vision and user stories`
2. `docs(adr): add workflow decision records`
3. `feat(core): implement first executable story slice`
4. `test(core): add coverage for acceptance criteria`
5. `docs(tutorial): update reproducible build and run steps`

## 5) Required Artifact Updates

When a significant change is made, update:

- `docs/requirements/vision_v1.md`
- `docs/requirements/user_stories_v1.md`
- `docs/architecture/adr/*`
- `docs/tutorial/MASTER_LOG.md`
- end-user docs (README or dedicated guides)

## 6) Verification Gate

Before merging, run project checks and ensure docs are current.

```bash
git status
git log --oneline -n 5
```

If docs or ADRs are missing for major changes, do not merge.

## 7) Handoff Checklist

- [ ] Features validated.
- [ ] Risks documented.
- [ ] ADRs updated.
- [ ] Tutorial updated.
- [ ] Commit history readable and scoped.
