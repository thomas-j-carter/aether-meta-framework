## `state_machines_v1.md`

# state_machines_v1.md

# Ardtire Society Civic Digital Governance Platform
## State Machines v1

## Document Status

- Version: v1
- Purpose: define the recommended core state machines for the platform
- Scope: platform workflow state models for key civic and operational objects
- Audience: founders, product planners, engineers, architects, QA, and governance process designers

---

# 1. Purpose of This Document

This document defines the recommended state machines for the Ardtire Society Civic Digital Governance Platform.

The platform’s core product thesis is that governance should be treated as explicit workflow, not as informal collaboration.

Accordingly, important platform objects should move through clear, modeled states with:

- allowed transitions,
- transition actors,
- guards,
- side effects,
- and terminal states where applicable.

This document does not attempt to encode every future edge case. Its purpose is to define the foundational workflow logic required for a serious MVP and a scalable future governance platform.

---

# 2. State Machine Design Principles

## 2.1 Important civic objects should have explicit states

If an object matters institutionally, it should usually have a state.

## 2.2 States should represent meaningful business reality

State names should reflect real process meaning, not UI convenience.

## 2.3 Transitions should be controlled

A state machine is useful only if transitions are constrained.

## 2.4 Guard conditions matter

Not every actor can perform every transition, and not every transition should be possible at all times.

## 2.5 Side effects should be explicit

State changes often trigger:
- notifications,
- permission changes,
- visibility changes,
- audit records,
- or creation of related records.

## 2.6 Terminal states should be clear

Where a workflow concludes, the platform should represent that conclusively.

## 2.7 History should be preserved

Transition history is part of the record, not merely an implementation detail.

---

# 3. Notation Used

Each state machine below is expressed using the following structure:

- Object
- Purpose
- States
- Allowed transitions
- Guards
- Side effects
- Terminal states
- Notes

Transition style:

`FROM_STATE -> TO_STATE`

---

# 4. Account / Access Status State Machine

# 4.1 Purpose

This state machine tracks the user’s access-related platform participation state at a high level.

It is not the same as membership application state. It is the broader participation/access state visible to the platform.

# 4.2 Object

`UserAccessStatus`

# 4.3 Recommended states

- Unregistered
- Registered
- Applicant
- Member
- Suspended
- Restricted
- Deactivated

# 4.4 State meanings

## Unregistered
No platform account exists for this person.

## Registered
Account exists, but no approved membership yet.

## Applicant
User has an active membership application in process.

## Member
User is an approved member with member-level platform rights.

## Suspended
User’s participation is temporarily suspended.

## Restricted
User may retain some access but with reduced rights.

## Deactivated
Account is deactivated or otherwise no longer active for normal participation.

# 4.5 Allowed transitions

- Unregistered -> Registered
- Registered -> Applicant
- Applicant -> Registered
- Applicant -> Member
- Member -> Suspended
- Member -> Restricted
- Suspended -> Member
- Restricted -> Member
- Registered -> Deactivated
- Applicant -> Deactivated
- Member -> Deactivated
- Suspended -> Deactivated
- Restricted -> Deactivated

# 4.6 Guards

## Unregistered -> Registered
- valid account registration completed

## Registered -> Applicant
- user submits membership application

## Applicant -> Registered
- application withdrawn, rejected, or closed without approval

## Applicant -> Member
- application approved by authorized reviewer

## Member -> Suspended
- authorized administrative action
- policy basis exists

## Member -> Restricted
- authorized administrative action
- policy basis exists

## Suspended -> Member
- reinstatement approved

## Restricted -> Member
- restriction lifted

## * -> Deactivated
- authorized admin action or account deactivation condition

# 4.7 Side effects

- status audit entry
- permission recalculation
- dashboard/status badge update
- notification to user when appropriate
- logging of actor and reason for status change

# 4.8 Terminal states

- Deactivated

# 4.9 Notes

This state should remain distinct from the membership application state machine. A user can have an application state and an access state that inform each other but are not identical objects.

---

# 5. Membership Application State Machine

# 5.1 Purpose

This state machine governs the lifecycle of a membership application.

# 5.2 Object

`MembershipApplication`

# 5.3 Recommended states

- Draft
- Submitted
- UnderReview
- MoreInfoRequested
- Approved
- Rejected
- Withdrawn

# 5.4 State meanings

## Draft
Application has been started but not formally submitted.

## Submitted
Application has been formally submitted and awaits review handling.

## UnderReview
Reviewer has taken the application into active review.

## MoreInfoRequested
Reviewer requires additional information from the applicant.

## Approved
Application has been accepted.

## Rejected
Application has been denied.

## Withdrawn
Applicant has withdrawn the application or it has otherwise been voluntarily closed before decision.

# 5.5 Allowed transitions

- Draft -> Submitted
- Draft -> Withdrawn
- Submitted -> UnderReview
- Submitted -> Withdrawn
- UnderReview -> MoreInfoRequested
- UnderReview -> Approved
- UnderReview -> Rejected
- UnderReview -> Withdrawn
- MoreInfoRequested -> UnderReview
- MoreInfoRequested -> Withdrawn

# 5.6 Guards

## Draft -> Submitted
- required fields complete
- validation passes
- applicant is eligible to submit

## Submitted -> UnderReview
- authorized reviewer takes review action

## UnderReview -> MoreInfoRequested
- reviewer identifies missing or unclear required information

## UnderReview -> Approved
- reviewer has authority
- application satisfies policy/requirements

## UnderReview -> Rejected
- reviewer has authority
- rejection basis recorded

## MoreInfoRequested -> UnderReview
- applicant provides requested information
- reviewer resumes review

## * -> Withdrawn
- user permitted to withdraw at current stage
- or authorized operator closes by policy

# 5.7 Side effects

## Draft -> Submitted
- application submission timestamp set
- user access status may become Applicant
- notification sent
- application enters reviewer queue
- audit event created

## Submitted -> UnderReview
- reviewer assignment or review timestamp created
- audit event created

## UnderReview -> MoreInfoRequested
- applicant notified
- request details recorded
- dashboard/action item created for applicant

## UnderReview -> Approved
- decision recorded
- applicant access status updated to Member
- member permissions activated
- notification sent
- audit event created

## UnderReview -> Rejected
- decision recorded
- applicant access status updated appropriately
- notification sent
- audit event created

## * -> Withdrawn
- application closed
- user status recalculated
- audit event created

# 5.8 Terminal states

- Approved
- Rejected
- Withdrawn

# 5.9 Notes

This is one of the highest-priority MVP state machines because it governs the transition from ordinary authenticated user to governance participant.

---

# 6. Proposal Lifecycle State Machine

# 6.1 Purpose

This is the platform’s central civic workflow.

It governs how a proposal moves from creation to review, deliberation, voting, and final resolution.

# 6.2 Object

`Proposal`

# 6.3 Recommended states

- Draft
- Submitted
- UnderReview
- OpenForDiscussion
- ReadyForVote
- VotingOpen
- ResolvedAdopted
- ResolvedRejected
- ReturnedForRevision
- Withdrawn
- Superseded

# 6.4 State meanings

## Draft
Proposal exists as a private or author-editable draft and is not yet in formal workflow.

## Submitted
Proposal has entered formal workflow but has not yet been reviewed for discussion readiness.

## UnderReview
Authorized reviewer/moderator/operator is evaluating procedural readiness.

## OpenForDiscussion
Proposal is available for structured member discussion and deliberation.

## ReadyForVote
Proposal has completed required discussion/review conditions and may be opened for voting.

## VotingOpen
An active voting window exists and eligible members may vote.

## ResolvedAdopted
Proposal has completed process and been adopted.

## ResolvedRejected
Proposal has completed process and not been adopted.

## ReturnedForRevision
Proposal needs changes before it can continue.

## Withdrawn
Proposal has been withdrawn by authorized actor.

## Superseded
Proposal has been replaced, merged, or made obsolete by another proposal/process outcome.

# 6.5 Allowed transitions

- Draft -> Submitted
- Draft -> Withdrawn

- Submitted -> UnderReview
- Submitted -> ReturnedForRevision
- Submitted -> Withdrawn

- UnderReview -> OpenForDiscussion
- UnderReview -> ReturnedForRevision
- UnderReview -> Withdrawn
- UnderReview -> Superseded

- OpenForDiscussion -> ReadyForVote
- OpenForDiscussion -> ReturnedForRevision
- OpenForDiscussion -> Withdrawn
- OpenForDiscussion -> Superseded

- ReturnedForRevision -> Draft
- ReturnedForRevision -> Submitted
- ReturnedForRevision -> Withdrawn

- ReadyForVote -> VotingOpen
- ReadyForVote -> ReturnedForRevision
- ReadyForVote -> Withdrawn
- ReadyForVote -> Superseded

- VotingOpen -> ResolvedAdopted
- VotingOpen -> ResolvedRejected
- VotingOpen -> ReturnedForRevision
- VotingOpen -> Superseded

# 6.6 Guards

## Draft -> Submitted
- author is eligible member
- required proposal fields complete
- required proposal text present
- validation passes

## Submitted -> UnderReview
- authorized reviewer/operator takes intake action

## UnderReview -> OpenForDiscussion
- proposal meets procedural completeness standards
- any initial moderation checks passed

## UnderReview -> ReturnedForRevision
- procedural or quality issues require revision

## OpenForDiscussion -> ReadyForVote
- minimum discussion/review conditions satisfied
- proposal version to be voted is fixed or explicitly selected
- authorized actor advances it

## ReadyForVote -> VotingOpen
- eligible voting population defined
- vote window configured
- proposal is in a votable state
- authorized actor opens vote

## VotingOpen -> ResolvedAdopted
- vote window closed
- outcome satisfies adoption rules

## VotingOpen -> ResolvedRejected
- vote window closed
- outcome does not satisfy adoption rules

## VotingOpen -> ReturnedForRevision
- rules permit return instead of final reject/adopt
- or vote invalidated / procedural issue requires revision workflow

## * -> Withdrawn
- actor has authority to withdraw at that stage
- withdrawal policy allows it

## * -> Superseded
- superseding proposal or merge action recorded
- authorized actor confirms supersession basis

# 6.7 Side effects

## Draft -> Submitted
- submission timestamp set
- proposal enters formal queue
- notifications sent as configured
- audit event created

## Submitted -> UnderReview
- reviewer/operator action recorded

## UnderReview -> OpenForDiscussion
- proposal becomes visible to intended discussion audience
- discussion opens
- notification sent

## UnderReview -> ReturnedForRevision
- revision request recorded
- author notified
- required changes or reasons logged

## OpenForDiscussion -> ReadyForVote
- votable revision locked or reference version attached
- ready-for-vote timestamp recorded

## ReadyForVote -> VotingOpen
- vote window object created or activated
- vote open timestamp set
- eligible voters notified

## VotingOpen -> ResolvedAdopted
- outcome record created
- authoritative drafting update may be triggered
- result published
- proposal locked from ordinary editing
- audit event created

## VotingOpen -> ResolvedRejected
- outcome record created
- result published
- audit event created

## VotingOpen -> ReturnedForRevision
- outcome/return reason recorded
- author/relevant parties notified

## * -> Withdrawn
- status visible in record
- related active actions disabled as appropriate
- audit event created

## * -> Superseded
- superseding relationship recorded
- prior proposal record preserved
- audit event created

# 6.8 Terminal states

- ResolvedAdopted
- ResolvedRejected
- Withdrawn
- Superseded

# 6.9 Notes

This is the single most important platform state machine and should be treated as a first-class domain model rather than an incidental UI field.

---

# 7. Proposal Revision State Machine

# 7.1 Purpose

This state machine governs the lifecycle of individual proposal revisions or text versions.

# 7.2 Object

`ProposalRevision`

# 7.3 Recommended states

- DraftRevision
- SubmittedRevision
- AcceptedAsCurrent
- ArchivedRevision

# 7.4 State meanings

## DraftRevision
Working revision not yet submitted into the proposal flow.

## SubmittedRevision
Revision has been submitted for consideration as the current proposal version.

## AcceptedAsCurrent
This revision is the current operative version of the proposal in workflow.

## ArchivedRevision
Older non-current revision preserved for historical record.

# 7.5 Allowed transitions

- DraftRevision -> SubmittedRevision
- SubmittedRevision -> AcceptedAsCurrent
- AcceptedAsCurrent -> ArchivedRevision
- SubmittedRevision -> ArchivedRevision
- DraftRevision -> ArchivedRevision

# 7.6 Guards

## DraftRevision -> SubmittedRevision
- author allowed to submit revision
- revision data complete enough for evaluation

## SubmittedRevision -> AcceptedAsCurrent
- authorized actor accepts it as current working version
- or system does so on valid proposal submission/update event

## AcceptedAsCurrent -> ArchivedRevision
- a newer revision is accepted as current

# 7.7 Side effects

- revision timestamp set
- current revision pointer updated
- diff history preserved
- notification may be sent
- audit event created

# 7.8 Terminal states

- ArchivedRevision

# 7.9 Notes

A proposal may have many revisions, but only one should normally be the current operative revision at a time.

---

# 8. Proposal Discussion Thread State Machine

# 8.1 Purpose

This state machine manages high-level discussion availability on a proposal.

# 8.2 Object

`ProposalDiscussionState`

# 8.3 Recommended states

- Closed
- Open
- Locked
- Archived

# 8.4 State meanings

## Closed
Discussion is not currently open for new comments.

## Open
Comments and replies are allowed per permissions.

## Locked
Existing discussion remains visible, but no new participation is allowed.

## Archived
Discussion is preserved as historical record only.

# 8.5 Allowed transitions

- Closed -> Open
- Open -> Locked
- Locked -> Open
- Locked -> Archived
- Closed -> Archived

# 8.6 Guards

## Closed -> Open
- proposal enters discussion-ready state
- authorized actor opens discussion
- or system opens by workflow automation

## Open -> Locked
- moderation or workflow reason exists
- proposal enters stage where discussion closes
- authorized actor acts

## Locked -> Open
- reopening is permitted
- authorized actor acts

## * -> Archived
- proposal resolved/closed and archival policy applies

# 8.7 Side effects

- visibility/participation rules updated
- participants notified as configured
- audit event created

# 8.8 Terminal states

- Archived

---

# 9. Voting Window State Machine

# 9.1 Purpose

This state machine governs a specific vote window for a proposal.

# 9.2 Object

`VoteWindow`

# 9.3 Recommended states

- Scheduled
- Open
- Closed
- Certified
- Voided

# 9.4 State meanings

## Scheduled
Vote has been configured but not yet opened.

## Open
Voting is active.

## Closed
Voting has ended and no further ballots may be cast.

## Certified
Outcome has been formally confirmed/finalized.

## Voided
Vote has been invalidated.

# 9.5 Allowed transitions

- Scheduled -> Open
- Open -> Closed
- Closed -> Certified
- Scheduled -> Voided
- Open -> Voided
- Closed -> Voided

# 9.6 Guards

## Scheduled -> Open
- current time reaches open time or authorized actor manually opens
- eligible voters defined
- proposal in votable state

## Open -> Closed
- current time reaches close time or authorized actor closes under permitted conditions

## Closed -> Certified
- tally complete
- certification actor has authority
- no blocking irregularity remains unresolved

## * -> Voided
- authorized actor
- procedural failure, invalidation, or policy-defined reason recorded

# 9.7 Side effects

## Scheduled -> Open
- vote open timestamp set
- eligible voters notified
- proposal status may update to VotingOpen

## Open -> Closed
- vote close timestamp set
- tally calculation triggered
- proposal outcome evaluation triggered

## Closed -> Certified
- certification record stored
- final result published
- linked proposal resolution finalized if not already

## * -> Voided
- invalidation reason recorded
- linked proposal may revert or move to ReturnedForRevision depending on rules
- participants notified

# 9.8 Terminal states

- Certified
- Voided

---

# 10. Individual Ballot State Machine

# 10.1 Purpose

This state machine governs an individual member’s ballot/vote record.

# 10.2 Object

`Ballot`

# 10.3 Recommended states

- NotCast
- Cast
- Updated
- Locked
- Invalidated

# 10.4 State meanings

## NotCast
Eligible ballot opportunity exists, but no vote yet recorded.

## Cast
A ballot has been submitted.

## Updated
A previously cast ballot has been changed, if the rules permit changes before close.

## Locked
Ballot is fixed and can no longer be changed.

## Invalidated
Ballot is no longer valid.

# 10.5 Allowed transitions

- NotCast -> Cast
- Cast -> Updated
- Cast -> Locked
- Updated -> Updated
- Updated -> Locked
- Cast -> Invalidated
- Updated -> Invalidated

# 10.6 Guards

## NotCast -> Cast
- voter eligible
- vote window open
- ballot data valid

## Cast -> Updated
- vote changes allowed
- vote window still open

## * -> Locked
- vote window closes
- or rules specify immediate lock on first cast

## * -> Invalidated
- eligibility issue discovered
- duplicate/invalid ballot condition
- vote invalidation reason recorded

# 10.7 Side effects

- vote timestamp updated
- latest effective choice stored
- audit event created
- tally recalculation on change if necessary

# 10.8 Terminal states

- Locked
- Invalidated

---

# 11. Proposal Outcome State Machine

# 11.1 Purpose

This machine tracks the formal outcome record associated with a proposal after voting or other resolution.

# 11.2 Object

`ProposalOutcome`

# 11.3 Recommended states

- Pending
- Adopted
- Rejected
- Returned
- Withdrawn
- Superseded
- Voided

# 11.4 Allowed transitions

- Pending -> Adopted
- Pending -> Rejected
- Pending -> Returned
- Pending -> Withdrawn
- Pending -> Superseded
- Pending -> Voided

# 11.5 Guards

- must correspond to valid proposal resolution path
- authorized actor or certified system action
- rule basis recorded

# 11.6 Side effects

- result publication
- audit entry
- linkage to authoritative text update where applicable
- notification

# 11.7 Terminal states

- Adopted
- Rejected
- Returned
- Withdrawn
- Superseded
- Voided

# 11.8 Notes

This outcome record can be separate from the proposal state itself, enabling cleaner reporting and auditing.

---

# 12. Authoritative Draft State Machine

# 12.1 Purpose

This state machine governs snapshots or versions of the currently authoritative constitutional drafting text.

# 12.2 Object

`AuthoritativeDraftState`

# 12.3 Recommended states

- Drafting
- PublishedCurrent
- SupersededHistorical
- Archived

# 12.4 State meanings

## Drafting
A not-yet-published next authoritative snapshot is being prepared.

## PublishedCurrent
This is the current authoritative drafting state.

## SupersededHistorical
This was once current but has been replaced by a newer authoritative state.

## Archived
Historic retained record, potentially deeper archival layer.

# 12.5 Allowed transitions

- Drafting -> PublishedCurrent
- PublishedCurrent -> SupersededHistorical
- SupersededHistorical -> Archived

# 12.6 Guards

## Drafting -> PublishedCurrent
- authorized publication action
- source basis for update recorded
- prior current state handled correctly

## PublishedCurrent -> SupersededHistorical
- new authoritative state published

# 12.7 Side effects

- current authoritative pointer updated
- publication timestamp set
- public/member visibility updated
- change log recorded
- prior current version preserved
- notification or publication event emitted

# 12.8 Terminal states

- Archived

# 12.9 Notes

Only one authoritative draft state should normally be current at a time.

---

# 13. Publication Item State Machine

# 13.1 Purpose

This governs publication workflow for public/official content items.

# 13.2 Object

`PublicationItem`

# 13.3 Recommended states

- Draft
- InReview
- Published
- Unpublished
- Archived

# 13.4 Allowed transitions

- Draft -> InReview
- InReview -> Published
- InReview -> Draft
- Published -> Unpublished
- Published -> Archived
- Unpublished -> Published
- Unpublished -> Archived

# 13.5 Guards

- appropriate editor/publisher permissions
- publication integrity requirements met

# 13.6 Side effects

- public visibility change
- publication timestamps
- audit event
- optional notifications

# 13.7 Terminal states

- Archived

---

# 14. Moderation Report State Machine

# 14.1 Purpose

This machine tracks the handling of a reported discussion item or moderation issue.

# 14.2 Object

`ModerationReport`

# 14.3 Recommended states

- Open
- UnderReview
- ActionTaken
- Dismissed
- Closed

# 14.4 Allowed transitions

- Open -> UnderReview
- UnderReview -> ActionTaken
- UnderReview -> Dismissed
- ActionTaken -> Closed
- Dismissed -> Closed

# 14.5 Guards

- moderator authority
- report exists with enough context

# 14.6 Side effects

- moderation audit entry
- content/user restrictions if action taken
- reporter notification as policy permits

# 14.7 Terminal states

- Closed

---

# 15. Audit Event State Model

Audit events are generally append-only records rather than workflow objects with many transitions.

For most purposes, they should be treated as immutable once written.

Possible simple status values:
- Recorded
- RedactedIfRequiredByPolicy

In general, audit events should not be routinely edited.

---

# 16. Cross-State Dependencies

The platform must enforce relationships among state machines.

## 16.1 Membership affects proposal and voting permissions
A person generally must be in Member access state to:
- submit proposals,
- comment in member-only governance spaces,
- vote where eligible.

## 16.2 Membership application approval affects access state
When a membership application becomes Approved:
- user access state should become Member.

## 16.3 Proposal state affects discussion state
When a proposal enters OpenForDiscussion:
- discussion state should generally become Open.

When a proposal resolves:
- discussion may become Locked or Archived.

## 16.4 Proposal state affects vote window state
A vote window should not open unless the proposal is in ReadyForVote.

When a vote window is Open:
- proposal should generally be in VotingOpen.

## 16.5 Vote window closure affects proposal outcome
When a vote window closes:
- tally and rule evaluation should determine outcome path.
- proposal should transition to adopted/rejected/returned or other permitted result state.

## 16.6 Adopted outcome affects authoritative draft state
Where the proposal changes current authoritative drafting text:
- a new authoritative draft state may need to be generated and published.

---

# 17. Global Guard Categories

For implementation and product planning, guards should generally be categorized as follows.

## 17.1 Role guards
Does the actor have the necessary role or authority?

## 17.2 Status guards
Is the object in the correct current state?

## 17.3 Completeness guards
Are required fields or required related objects present?

## 17.4 Temporal guards
Is this action occurring within the permitted time window?

## 17.5 Policy/rule guards
Do configured rules permit this transition?

## 17.6 Integrity guards
Would this transition violate invariants, such as:
- multiple current authoritative versions,
- duplicate ballots,
- impossible lifecycle sequence?

---

# 18. Required Audit Data for Every Transition

Every meaningful state transition should record at minimum:

- object type
- object identifier
- previous state
- new state
- actor
- timestamp
- reason or note where applicable
- rule/policy reference where applicable
- related object references where applicable

This is necessary for institutional legibility.

---

# 19. MVP Priority State Machines

For the first credible release, the highest-priority state machines are:

1. UserAccessStatus
2. MembershipApplication
3. Proposal
4. ProposalRevision
5. VoteWindow
6. Ballot
7. ProposalOutcome
8. AuthoritativeDraftState

These should be treated as foundational domain models rather than deferred implementation details.

---

# 20. Summary

The Ardtire Society Civic Digital Governance Platform should be built around explicit state machines for the objects that matter most institutionally.

At minimum, that includes:
- access status,
- membership applications,
- proposals,
- revisions,
- discussion availability,
- voting windows,
- ballots,
- outcomes,
- and authoritative draft states.

This state-machine approach is essential because the platform’s legitimacy depends on making civic process explicit, traceable, enforceable, and historically durable.
