# domain_model_v1.md

# Ardtire Society Civic Digital Governance Platform
## Domain Model v1

## Document Status

- Version: v1
- Purpose: define the core domain model for the platform at the business/domain level
- Scope: conceptual and product-aligned domain modeling, not database schema detail
- Audience: founders, product planners, architects, engineers, QA, and governance process designers

---

# 1. Purpose of This Document

This document defines the core domain model of the Ardtire Society Civic Digital Governance Platform.

Its purpose is to describe the major business domains, their core concepts, the relationships among them, and the boundaries that should guide implementation.

This is not a low-level schema document. It is the conceptual model that sits between product vision and technical design.

It should help answer questions such as:

- What are the primary business objects of the platform?
- Which concepts belong together?
- Which concepts must remain distinct?
- What relationships and invariants shape the system?
- What domains deserve first-class treatment in architecture and implementation?

---

# 2. Modeling Premise

The platform’s core premise is that governance should be modeled as explicit institutional workflow rather than improvised social interaction.

Accordingly, the domain model centers not on generic pages or generic posts, but on civic objects and role-bearing actors such as:

- users,
- memberships,
- proposals,
- revisions,
- discussions,
- votes,
- outcomes,
- authoritative draft states,
- publications,
- moderation events,
- and audit records.

The domain model should preserve the distinction between:

- identity,
- membership,
- authority,
- governance participation,
- official publication,
- and historical record.

---

# 3. Domain Modeling Principles

## 3.1 Domains should reflect real institutional meaning

A domain exists because it represents a meaningful part of how the Society functions digitally.

## 3.2 Business objects should be modeled explicitly

If a concept matters to workflow, permissions, legitimacy, or historical record, it should usually exist as a first-class domain object.

## 3.3 Status-bearing objects must remain explicit

Objects with meaningful lifecycle state should not be collapsed into generic content or metadata blobs.

## 3.4 Authority layers must not be blurred

The model must preserve separation between:
- working governance objects,
- official/publication objects,
- and historical/archive objects.

## 3.5 Domain boundaries should reduce ambiguity

The model should help engineers and product planners determine:
- where logic belongs,
- where permissions are enforced,
- and which objects own which responsibilities.

---

# 4. Top-Level Domain Map

The recommended top-level domain map is:

1. Identity and Access Domain
2. Membership Domain
3. Governance Domain
4. Voting and Outcomes Domain
5. Authoritative Text Domain
6. Publication Domain
7. Archive and Record Domain
8. Moderation Domain
9. Administration Domain
10. Audit and Activity Domain
11. Notification and Communication Domain

These domains are related but should remain conceptually distinct.

---

# 5. Identity and Access Domain

## 5.1 Purpose

The Identity and Access Domain governs who a user is in the system, how they authenticate, and what high-level participation status they currently hold.

It answers questions such as:

- Who is this person in the platform?
- Are they authenticated?
- What current participation/access status do they have?
- What roles and permissions apply?

## 5.2 Core concepts

- User
- Account
- Credential / authentication method
- Access status
- Role assignment
- Session
- Security settings

## 5.3 Responsibilities

This domain is responsible for:
- account creation,
- account identity,
- authentication,
- account security,
- access status,
- role attachment,
- session context.

## 5.4 Key invariants

- A person must have an account to act as an authenticated participant.
- Authentication alone does not confer membership.
- Access status must remain distinguishable from role assignment.
- Permission evaluation should depend on both role and current status where relevant.

## 5.5 Key boundaries

This domain does not itself define:
- membership application review logic,
- proposal workflow logic,
- voting outcomes,
- publication authority.

It provides identity and access context to those domains.

---

# 6. Membership Domain

## 6.1 Purpose

The Membership Domain governs the transition from registered account holder to approved Society member and the management of membership status over time.

It answers questions such as:

- Has this user applied for membership?
- What is the current state of the application?
- Was the user approved, rejected, or returned for more information?
- Is the user currently an approved member?
- Has their membership standing changed?

## 6.2 Core concepts

- Membership application
- Application state
- Reviewer decision
- Membership record
- Membership standing
- Membership status history

## 6.3 Responsibilities

This domain is responsible for:
- membership application creation,
- application submission,
- review workflow,
- decision recording,
- membership status activation,
- standing changes such as suspension or restriction.

## 6.4 Key invariants

- A user cannot become a member without a valid approval path.
- Membership approval should have a durable recorded basis.
- Membership standing changes should be preserved historically.
- Membership state should be reflected in effective permissions.

## 6.5 Key boundaries

This domain does not itself manage:
- proposal lifecycle logic,
- voting logic,
- publication logic.

However, it directly affects whether a user may participate in those other domains.

---

# 7. Governance Domain

## 7.1 Purpose

The Governance Domain is the heart of the platform.

It governs the creation, revision, discussion, and procedural movement of proposals through formal civic workflow.

It answers questions such as:

- What proposals exist?
- Who authored them?
- What text is currently under consideration?
- What stage is a proposal in?
- What revisions and discussion history exist?

## 7.2 Core concepts

- Proposal
- Proposal state
- Proposal revision
- Proposal author / submitter
- Discussion thread
- Comment / reply
- Proposal relationship
- Workflow transition
- Proposal history

## 7.3 Responsibilities

This domain is responsible for:
- proposal drafting,
- proposal submission,
- revision management,
- discussion management,
- governance object visibility,
- lifecycle state transitions prior to and around voting.

## 7.4 Key invariants

- A proposal should have one current operative revision at a time.
- A proposal’s lifecycle state must be explicit.
- Revision history should be preserved.
- Discussion context should remain linked to the proposal.
- Proposal state transitions should be recorded and constrained.

## 7.5 Key boundaries

This domain does not own final vote tally logic or authoritative draft publication, though it is upstream from both.

---

# 8. Voting and Outcomes Domain

## 8.1 Purpose

This domain governs formal decision-making on proposals.

It answers questions such as:

- Is a proposal currently being voted on?
- Who is eligible to vote?
- Has a vote opened or closed?
- What ballots were cast?
- What was the outcome?
- Was the outcome certified or voided?

## 8.2 Core concepts

- Vote window
- Vote eligibility context
- Ballot
- Vote choice
- Tally
- Outcome
- Certification / voiding record
- Outcome basis / rule reference

## 8.3 Responsibilities

This domain is responsible for:
- opening vote windows,
- capturing ballots,
- preventing invalid voting,
- closing votes,
- deriving and storing results,
- recording certified outcomes.

## 8.4 Key invariants

- A ballot may be cast only by eligible actors in an open vote window.
- Duplicate or invalid ballots must be prevented or invalidated.
- Outcome logic must be traceable to an explicit basis.
- Vote windows and proposals should remain synchronized in meaning.

## 8.5 Key boundaries

This domain does not define who is a member; it depends on the Membership Domain for voter eligibility context.

This domain does not publish the current authoritative text; it may trigger downstream updates in the Authoritative Text Domain.

---

# 9. Authoritative Text Domain

## 9.1 Purpose

This domain governs the officially recognized current drafting state of constitutional or governance text.

It answers questions such as:

- What text is currently authoritative?
- When did it become authoritative?
- What proposal outcomes caused the change?
- What prior authoritative states exist?

## 9.2 Core concepts

- Authoritative draft state
- Draft snapshot
- Current authoritative pointer
- Superseded authoritative state
- Change basis / source outcome

## 9.3 Responsibilities

This domain is responsible for:
- representing current authoritative drafting state,
- preserving prior authoritative states,
- linking authoritative changes to their basis,
- keeping the canonical drafting record coherent.

## 9.4 Key invariants

- There should be only one current authoritative state at a time.
- Every authoritative update should have a traceable basis.
- Superseded authoritative states must remain preserved.

## 9.5 Key boundaries

This domain does not manage free-form proposal discussion or voting windows. It receives validated, resolved inputs from those domains.

---

# 10. Publication Domain

## 10.1 Purpose

This domain governs official public or semi-public publication of institutional content.

It answers questions such as:

- What items have been officially published?
- Is this item a draft or an official publication?
- What public explanation or official record is available?

## 10.2 Core concepts

- Publication item
- Publication state
- Public page content
- Published official record
- Editorial workflow state

## 10.3 Responsibilities

This domain is responsible for:
- editorial preparation,
- publication workflow,
- public-facing official content,
- controlled visibility of public materials,
- maintenance of official explanatory materials.

## 10.4 Key invariants

- Draft publication items should not be confused with published official items.
- Publication state must be explicit.
- Authoritative text and publication item should be related but not conflated.

## 10.5 Key boundaries

This domain is not identical to the Authoritative Text Domain. Some authoritative drafting states may be published through this domain, but the concepts are not the same.

---

# 11. Archive and Record Domain

## 11.1 Purpose

This domain preserves historic institutional memory.

It answers questions such as:

- What happened before?
- What past proposals and outcomes exist?
- What was once current but is no longer current?
- How did the constitutional text evolve?

## 11.2 Core concepts

- Archived proposal
- Historic revision
- Historic authoritative state
- Historic publication
- Record view
- Timeline / chronology

## 11.3 Responsibilities

This domain is responsible for:
- preservation,
- retrieval,
- historical browsing,
- distinguishing current objects from historical objects,
- institutional continuity over time.

## 11.4 Key invariants

- Historical records should remain durable.
- Historic states should not overwrite current states.
- Archived material should preserve enough context to remain intelligible.

## 11.5 Key boundaries

This domain may expose records originating in many other domains, but it does not own their active workflow logic.

---

# 12. Moderation Domain

## 12.1 Purpose

The Moderation Domain preserves quality, order, and civic seriousness in user-contributed discourse and participation spaces.

It answers questions such as:

- Has content been reported?
- Has a moderation action been taken?
- Is a discussion locked?
- Has a user’s participation been restricted?

## 12.2 Core concepts

- Moderation report
- Moderation action
- Restricted content state
- Discussion lock state
- Participation restriction

## 12.3 Responsibilities

This domain is responsible for:
- report intake,
- moderation review,
- moderation action recording,
- discussion restriction,
- limited user participation restriction where policy permits.

## 12.4 Key invariants

- Moderation action should be explicit and auditable.
- Moderation should not silently rewrite history.
- Moderation authority should remain distinct from authorship and membership.

## 12.5 Key boundaries

This domain does not own the proposal lifecycle, but it can affect discussion access and participation conditions.

---

# 13. Administration Domain

## 13.1 Purpose

The Administration Domain provides platform operators with the tools necessary to keep workflows, statuses, roles, and exceptional cases manageable.

It answers questions such as:

- What needs operational attention?
- Which users or objects require intervention?
- Which roles are assigned?
- How are exceptions handled?

## 13.2 Core concepts

- Admin action
- Role assignment management
- Status override or exceptional-case intervention
- System configuration
- Operational queue

## 13.3 Responsibilities

This domain is responsible for:
- role management,
- user management,
- exceptional-case workflow handling,
- platform settings,
- operational oversight.

## 13.4 Key invariants

- Administrative actions should be auditable.
- Admin authority should not be invisible.
- Exceptional intervention should not destroy the normal workflow model.

## 13.5 Key boundaries

This domain may reach across many other domains operationally, but should not erase domain boundaries conceptually.

---

# 14. Audit and Activity Domain

## 14.1 Purpose

This domain preserves a durable record of important actions and state changes across the platform.

It answers questions such as:

- Who changed what?
- When did it happen?
- What was the prior state and the new state?
- Why did the action occur?

## 14.2 Core concepts

- Audit event
- Activity event
- Actor
- Target object
- Before/after state
- Reason or note
- Related object references

## 14.3 Responsibilities

This domain is responsible for:
- immutable or controlled-write logging of meaningful events,
- exposing reviewable activity history,
- supporting institutional traceability.

## 14.4 Key invariants

- Important actions should generate audit records.
- Audit records should not be casually editable.
- Events should preserve enough context to reconstruct institutional history.

## 14.5 Key boundaries

The Audit Domain is cross-cutting. It does not own business workflows but records them.

---

# 15. Notification and Communication Domain

## 15.1 Purpose

This domain ensures that users and operators are informed when important workflow events occur.

It answers questions such as:

- Has the user been notified that something changed?
- What events should generate alerts?
- Which messages are informational versus action-requiring?

## 15.2 Core concepts

- Notification
- Notification preference
- Delivery channel
- Trigger event
- Read/unread state

## 15.3 Responsibilities

This domain is responsible for:
- generating notifications from business events,
- storing notification state,
- delivering action prompts and status changes,
- supporting user preferences where appropriate.

## 15.4 Key invariants

- Important workflow events should be notifiable.
- Notifications should correspond to real domain events.
- Notification state should not be confused with workflow state itself.

## 15.5 Key boundaries

Notification is derived from other domains. It should not be treated as the source of truth for business state.

---

# 16. Cross-Domain Relationships

## 16.1 Identity and Access -> Membership

A user account may initiate one or more membership-related interactions, but the effective current membership standing determines governance eligibility.

## 16.2 Membership -> Governance

Only users whose access/membership context allows it should create proposals, comment in member spaces, or vote.

## 16.3 Governance -> Voting and Outcomes

A proposal becomes votable only through valid governance workflow progression.

## 16.4 Voting and Outcomes -> Authoritative Text

Adopted outcomes may trigger creation of a new authoritative draft state.

## 16.5 Authoritative Text -> Publication

Authoritative text may be surfaced publicly or semi-publicly through publication workflows.

## 16.6 Governance / Voting / Publication -> Archive

Historic versions, outcomes, and published items feed the archive.

## 16.7 Governance / Membership / Administration / Moderation -> Audit

All important actions in these domains should emit audit events.

## 16.8 All eventful domains -> Notification

Meaningful state changes may emit user-facing or operator-facing notifications.

---

# 17. Aggregate Candidates

The following are strong candidates for aggregate roots or equivalent domain ownership centers in implementation:

- User
- MembershipApplication
- MembershipRecord
- Proposal
- VoteWindow
- ProposalOutcome
- AuthoritativeDraftState
- PublicationItem
- ModerationReport
- AuditEvent

The exact implementation pattern may vary, but these objects represent major ownership and consistency boundaries.

---

# 18. Core Domain Invariants

Across the entire model, the following invariants should generally hold.

## 18.1 Registration is not membership
A registered account does not imply member participation rights.

## 18.2 Membership is required for core governance participation
Proposal authoring, formal governance discussion, and voting should generally require approved membership, unless policy explicitly provides otherwise.

## 18.3 Proposals require explicit state
A proposal should always have a meaningful workflow state.

## 18.4 Revisions must be preserved
Proposal text history should not be destructively overwritten.

## 18.5 Outcomes must be traceable
Proposal outcomes should be linked to vote/result basis and recorded explicitly.

## 18.6 Only one authoritative draft state may be current
The current authoritative drafting state must be singular and explicit.

## 18.7 Official publication is distinct from working process
A published official item is not the same as a draft proposal or working discussion.

## 18.8 Important actions must be auditable
Where legitimacy, authority, or institutional history is affected, durable recording is required.

---

# 19. Bounded Context Recommendations

A practical bounded-context decomposition for implementation would likely look like this:

1. Identity / Access Context
2. Membership Context
3. Governance Context
4. Voting Context
5. Authoritative Draft Context
6. Publication Context
7. Moderation Context
8. Administration Context
9. Audit / Activity Context
10. Notification Context

These may map to modules, packages, services, or internal boundaries depending on architecture, but the conceptual separation is useful even in a monolith.

---

# 20. MVP-Critical Domains

For the earliest credible version, the most important domains are:

1. Identity and Access
2. Membership
3. Governance
4. Voting and Outcomes
5. Authoritative Text
6. Administration
7. Audit

Publication, Archive, Moderation, and Notification are also important, but the MVP’s institutional proof comes first from making the core civic loop work.

---

# 21. Summary

The Ardtire Society Civic Digital Governance Platform should be modeled as a multi-domain civic system centered on:

- identity,
- membership,
- governance participation,
- voting and outcomes,
- authoritative drafting state,
- official publication,
- historical preservation,
- moderation,
- administration,
- audit,
- and notifications.

This model is necessary because the platform is not just content management. It is institutional process management with durable civic memory.
