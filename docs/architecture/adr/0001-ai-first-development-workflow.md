# ADR 0001: Adopt an AI-First Development Workflow

- **Status:** Accepted
- **Date:** 2026-03-17
- **Deciders:** Project maintainers

## Context

The project is intended to be developed with active support from AI assistants.

Without a defined workflow, outcomes become inconsistent:

- prompts are ad hoc,
- reasoning is opaque,
- commit history is noisy,
- documentation quality drifts,
- onboarding and reproducibility suffer.

## Decision

We will standardize an AI-first workflow with explicit artifacts and process gates.

### Chosen Rules

1. Keep an assistant operating contract in `AI/README.md`.
2. Require step-wise, explainable execution for implementation tasks.
3. Require commit recommendations at meaningful checkpoints.
4. Treat documentation updates as a first-class deliverable.
5. Maintain an idempotent tutorial so others can reproduce outcomes.

## Consequences

### Positive

- Higher transparency and maintainability.
- Better onboarding for developers and users.
- Stronger audit trail for architecture and behavior changes.
- Easier project handoff across teams.

### Negative

- Increased documentation overhead.
- Slower short-term iteration due to process discipline.

## Alternatives Considered

1. **Ad hoc prompting only**
   - Rejected due to poor reproducibility and high variance.
2. **Code-first with minimal docs**
   - Rejected because the project goals include teaching and tutorial quality.

## Follow-Up Actions

1. Keep tutorial logs aligned with implementation milestones.
2. Add future ADRs for changes to the AI collaboration protocol.
