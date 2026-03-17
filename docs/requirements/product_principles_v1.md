# product_principles_v1.md

# Ardtire Society Civic Digital Governance Platform
## Product Principles v1

## Document Status

- Version: v1
- Purpose: define the product principles that should govern planning, design, implementation, and prioritization
- Scope: product and UX principles, not constitutional law or internal legal instruments
- Audience: founders, product planners, designers, engineers, content editors, operators, and future governance stewards

---

# 1. Purpose of This Document

This document defines the core product principles of the Ardtire Society Civic Digital Governance Platform.

These principles exist to ensure that the platform is designed and built in a way that reflects its purpose: a serious digital civic environment for structured constitutional and governance formation.

These principles should guide decisions about:

- scope,
- workflow design,
- UX,
- content architecture,
- permissions,
- governance object modeling,
- moderation,
- publication,
- auditability,
- and future iteration.

When two design options compete, the one that better satisfies these principles should generally be preferred.

---

# 2. Foundational Product Orientation

This platform is not being built as a generic community website or casual social system.

It is being built as a structured civic process platform.

Accordingly, the product should always favor:

- legitimacy over improvisation,
- clarity over cleverness,
- explicitness over ambiguity,
- durable record over transient interaction,
- institutional seriousness over superficial engagement,
- and coherent progression over feature sprawl.

---

# 3. Core Product Principles

# 3.1 Legitimacy Over Improvisation

The platform should privilege explicit, traceable, rule-aware process over informal or ambiguous collaboration.

Important civic actions should not depend on unwritten assumptions, hidden operator knowledge, or off-platform coordination wherever avoidable.

## Implications

- workflow states should be explicit;
- important transitions should be controlled;
- outcome rules should be visible or at least traceable;
- significant decisions should be recorded;
- authority should not be implied.

## Anti-patterns to avoid

- ad hoc decision states,
- manual off-platform resolution as the default,
- hidden process logic,
- unclear proposal lifecycle.

---

# 3.2 Governance Is a Workflow

Governance should be treated as a structured lifecycle, not a pile of documents and comments.

The product should model important civic actions as first-class workflow objects with status, transitions, actors, and history.

## Implications

- proposals need lifecycle states;
- applications need lifecycle states;
- votes need opening, closing, and outcome states;
- publication needs explicit status;
- state changes need timestamps and actor history.

## Anti-patterns to avoid

- flat content systems pretending to be governance tools,
- “everything is just a post” modeling,
- overwriting state instead of preserving history.

---

# 3.3 Identity, Membership, and Authority Must Be Distinct

The platform must clearly distinguish between:
- having an account,
- being a member,
- having operational authority,
- and holding governance authority.

These are not the same thing and should never be collapsed in product design.

## Implications

- registration must not equal membership;
- member-only functions must be controlled separately from authentication;
- moderation powers must be distinct from ordinary participation rights;
- dashboards and UI labels should reflect user state clearly.

## Anti-patterns to avoid

- ambiguous “user” permissions,
- hidden role assumptions,
- blurred boundaries between platform access and civic standing.

---

# 3.4 Status Clarity Is a First-Class Requirement

Users should always be able to understand the current status of themselves and the civic objects they interact with.

A serious governance platform cannot depend on users guessing where they stand.

## The platform should make clear

- a user’s current participation state,
- a membership application’s state,
- a proposal’s workflow state,
- a vote’s state,
- a publication’s authority state,
- and whether an item is current, historical, adopted, draft, or superseded.

## Anti-patterns to avoid

- unlabeled process stages,
- hidden eligibility logic,
- unclear authoritative text.

---

# 3.5 Transparency Where Appropriate

The platform should make procedural status, proposal history, drafting evolution, and formal outcomes visible and intelligible wherever appropriate.

Transparency is a major source of trust and legitimacy.

## Implications

- proposal histories should be reviewable;
- revision chains should be visible;
- outcome records should be intelligible;
- public-facing official materials should be clearly labeled.

## Transparency does not mean

- indiscriminate exposure of sensitive internal data,
- destruction of privacy boundaries,
- or elimination of operator-only functions.

The principle is not total visibility. It is intelligible legitimacy.

---

# 3.6 Historical Durability Matters

The platform should preserve the institutional memory of how constitutional and governance work unfolded.

History is not a secondary archive feature. It is part of the core product value.

## Implications

- revisions should be preserved;
- important actions should be logged;
- outcomes should remain reconstructable;
- authoritative text changes should be traceable.

## Anti-patterns to avoid

- destructive overwrites,
- “latest only” design,
- missing reason/history context.

---

# 3.7 Authority Must Be Explicit

The platform must clearly distinguish among:

- proposed text,
- draft text,
- under-review text,
- voting text,
- adopted text,
- superseded text,
- and archived text.

Users should never need to infer authority from context clues.

## Implications

- authoritative labels must be visible;
- the publication layer must not blur with working-draft space;
- official outputs must be clearly marked;
- historical items must be clearly marked as historical.

## Anti-patterns to avoid

- mixing official and in-progress text without clear markers,
- ambiguous publication states,
- unclear canonical sources.

---

# 3.8 Participation With Structure

The platform should be open enough to allow meaningful contribution, but structured enough to preserve order, seriousness, and institutional coherence.

This product is not intended to optimize for maximum frictionless posting. It is intended to optimize for meaningful civic work.

## Implications

- members should be able to contribute;
- workflows should allow revision and discussion;
- contribution should occur inside governed pathways;
- submission and voting should not be reduced to social-media mechanics.

## Anti-patterns to avoid

- unbounded contribution without process,
- gamified participation that weakens seriousness,
- “engagement-first” design that obscures governance substance.

---

# 3.9 Institution Before Interface

The interface exists to serve the institution’s process, not the reverse.

A polished UI is valuable, but the platform’s credibility depends more on whether the underlying civic logic is coherent than on whether the interface is flashy.

## Implications

- model the process well first;
- design UI around process clarity;
- prioritize legibility over novelty;
- reduce ambiguity in actions and outcomes.

## Anti-patterns to avoid

- visual polish masking weak workflow design,
- trendy interaction patterns that reduce seriousness,
- design choices that privilege novelty over institutional clarity.

---

# 3.10 Public Trust Through Operational Clarity

Trust comes not only from ideals, but from whether the platform behaves in ways users can understand.

Users should be able to answer:
- What is this place?
- Who am I in it?
- What can I do?
- What happens next?
- What just happened?
- What record exists?

## Implications

- statuses should be obvious;
- next steps should be visible;
- outcomes should be interpretable;
- operator actions should be bounded and auditable where appropriate.

---

# 3.11 Seriousness of Tone

The platform should communicate civic dignity, procedural seriousness, and institutional intent.

This does not mean stiffness for its own sake. It means the product should feel like a real civic environment rather than a casual online community toy.

## Implications

- language should be clear and respectful;
- important actions should feel consequential;
- public pages should convey coherence and trustworthiness;
- drafting and governance spaces should feel purposeful.

## Anti-patterns to avoid

- overly playful governance UX,
- vague or unserious copy,
- casual framing of formal actions.

---

# 3.12 Design for Evolution, Not Overbuilding

The platform should be designed so that more formal governance, parliamentary, archival, and publication features can be added later without forcing a complete conceptual rewrite.

At the same time, the early platform should not overbuild speculative future institutions before the foundational civic loop works.

## Implications

- choose models that can grow;
- keep MVP scope disciplined;
- avoid locking the product into dead-end abstractions;
- do not build ceremonial complexity before the core loop functions.

---

# 4. Practical Product Rules Derived From the Principles

The following practical rules should usually hold true.

## Rule 1
If a civic object matters procedurally, it should probably have an explicit state.

## Rule 2
If a decision matters institutionally, it should probably be recorded.

## Rule 3
If text changes over time, the old version should probably be preserved.

## Rule 4
If authority differs between two kinds of content, the UI should make that difference obvious.

## Rule 5
If a user’s rights differ from another user’s rights, the platform should make those boundaries understandable.

## Rule 6
If a workflow affects legitimacy, it should not depend mainly on human memory or private side-channel coordination.

## Rule 7
If a design idea increases excitement but weakens seriousness or clarity, it should usually be rejected.

---

# 5. Product Decision Tests

When evaluating a feature, workflow, or design choice, ask:

## Clarity test
Does this make the system easier to understand?

## Legitimacy test
Does this strengthen explicit and traceable process?

## Role test
Does this preserve the distinction between identity, membership, and authority?

## History test
Does this preserve institutional memory rather than erase it?

## Authority test
Does this make official versus non-official state clearer?

## Seriousness test
Does this feel appropriate for a civic-governance platform?

## MVP discipline test
Does this help the foundational loop work, or is it premature?

---

# 6. Things the Product Should Generally Avoid

The platform should generally avoid:

- treating governance as generic social posting;
- hiding workflow logic from participants;
- conflating draft, proposal, and official text;
- making users guess their status or permissions;
- depending on operator improvisation for routine lifecycle management;
- shipping high-polish public pages with weak governance internals;
- adding broad community features that distract from the constitutional process;
- overbuilding ceremonial or advanced parliamentary features before the core loop is stable.

---

# 7. Principle Priorities for MVP

For the earliest version, the most important principles are:

1. legitimacy over improvisation;
2. governance is a workflow;
3. identity, membership, and authority must be distinct;
4. status clarity is a first-class requirement;
5. authority must be explicit;
6. participation with structure;
7. design for evolution, not overbuilding.

If those principles are honored, the MVP can be credible even before the full long-term platform exists.

---

# 8. Summary

The product principles of this platform can be summarized simply:

Build a serious, intelligible, workflow-driven civic system in which people can move from public understanding to structured participation to durable governance record, under explicit roles, clear statuses, and visible institutional logic.

That is the standard against which the product should be judged.
