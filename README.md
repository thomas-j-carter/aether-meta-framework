# aether-meta-framework

## Name: AETHER (Architectural Evolution & Technical Handover Engine for Recursion)

## Description

AETHER is a self-evolving AI meta-framework designed for high-rigor software development. It mandates a recursive SDLC through strict "Halt & Verify" gates, ensuring every line of code is preceded by architectural consensus and domain modeling. By utilizing a "Triad Review" system (Architect, Security, Implementer) and a self-healing diagnostic protocol, AETHER ensures project idempotency.

This repository now includes an **AI-first delivery system** so an LLM can both build the project and teach along the way.

## AI-Driven Development Goals

When used with an LLM (ChatGPT, Claude, Gemini, etc.), the workflow should:

1. Answer questions and provide implementation help.
2. Explain reasoning in explicit, step-by-step detail.
3. Recommend commit boundaries and commit messages at natural checkpoints.
4. Produce repeatable, idempotent outputs for other developers.
5. Generate living documentation for engineers and end users.

## Project Structure (AI + Documentation)

```text
├── .ai/
│   └── README.md                         # Instructions an LLM should follow while assisting.
├── docs/
│   ├── architecture/
│   │   ├── adr/
│   │   │   └── 0001-ai-first-development-workflow.md
│   │   └── domain_model_v1.md
│   ├── requirements/
│   │   ├── user_stories_v1.md
│   │   └── vision_v1.md
│   └── tutorial/
│       ├── IDEMPOTENT_TUTORIAL.md        # End-to-end reproducible implementation guide.
│       └── MASTER_LOG.md                 # Chronological progress log.
```

## Recommended AI Session Contract

Before coding, tell your AI assistant to follow these rules:

- Operate in small, verifiable steps.
- For each step: plan → execute → explain → verify.
- After each successful checkpoint, suggest a commit with a clear Conventional Commit message.
- Keep docs updated as part of every implementation step.
- Capture architecture decisions as ADRs.

The concrete version of this contract lives in `AI/README.md`.

## Starting Workflow

1. Define or refine product intent in `docs/requirements/vision_v1.md`.
2. Break intent into user stories in `docs/requirements/user_stories_v1.md`.
3. Record major architectural decisions in `docs/architecture/adr/`.
4. Ask the AI to implement one story at a time and update `docs/tutorial/IDEMPOTENT_TUTORIAL.md`.
5. Keep `docs/tutorial/MASTER_LOG.md` current after every major milestone.

## Why This Works

This structure turns the repository into both:

- a production codebase, and
- a self-contained tutorial that others can replay to reach the same result.

That combination enables reliable handoff, auditability, and educational onboarding.
