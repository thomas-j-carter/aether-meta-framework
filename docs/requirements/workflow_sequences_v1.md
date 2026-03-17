# workflow_sequences_v1.md

# Ardtire Society Civic Digital Governance Platform
## Workflow Sequences v1

## Document Status

- Version: v1
- Purpose: define the recommended end-to-end workflow sequences for the platform
- Scope: human-readable sequence flows for key user and operator journeys
- Audience: founders, product planners, architects, engineers, QA, designers, and operators

---

# 1. Purpose of This Document

This document defines the major workflow sequences for the Ardtire Society Civic Digital Governance Platform.

Its purpose is to translate the platform’s product intent, state models, and permissions into concrete process flows showing:

- who acts,
- in what order,
- on which objects,
- under which conditions,
- and with what resulting state changes.

These are not low-level UML sequence diagrams. They are practical workflow narratives that can guide implementation, QA, and UX design.

---

# 2. Workflow Design Principles

## 2.1 The platform should optimize for coherent end-to-end flow

A workflow is not complete unless the user can move from entry to meaningful resolution without ambiguity.

## 2.2 Every major workflow should have an identifiable entry point

Users should know how to begin.

## 2.3 Every major workflow should have visible current state and next actions

Users should not have to guess what happens next.

## 2.4 Operator steps must be treated as first-class workflow steps

Reviewer, moderator, editor, and admin actions are part of the product, not back-office afterthoughts.

## 2.5 Workflows should emit records

Important workflow steps should create durable records, status transitions, and audit history.

---

# 3. Core Workflow Inventory

The most important workflows are:

1. Public discovery and registration
2. Authentication and account access
3. Membership application
4. Membership review and decision
5. Member activation
6. Proposal drafting and submission
7. Proposal review and discussion
8. Proposal revision loop
9. Vote preparation and vote opening
10. Member voting
11. Outcome resolution and certification
12. Authoritative draft update
13. Publication workflow
14. Moderation workflow
15. Administrative intervention workflow
16. Archive and history retrieval workflow

---

# 4. Workflow 1: Public Discovery and Registration

## Purpose

Allow a public visitor to understand the Society and create an account.

## Primary actors

- Public Visitor
- Platform

## Primary objects

- Public page
- User account

## Sequence

### Step 1
Public visitor lands on a public page such as Home, Participation, or Governance.

### Step 2
Platform presents:
- mission/context,
- participation pathway,
- distinction between registration and membership,
- and registration call to action.

### Step 3
Visitor chooses to register.

### Step 4
Platform presents registration form.

### Step 5
Visitor enters required account information.

### Step 6
Platform validates:
- required fields,
- uniqueness constraints,
- password/security rules.

### Step 7
If validation passes, platform creates User account in Registered state.

### Step 8
Platform optionally triggers verification flow.

### Step 9
Platform confirms successful registration and directs user toward sign-in or dashboard.

## Result

- User account exists.
- User access status is Registered.
- Visitor can now authenticate.

---

# 5. Workflow 2: Authentication and Account Access

## Purpose

Allow a registered user to sign in and understand current status.

## Primary actors

- Registered User
- Platform

## Primary objects

- User
- Session
- Dashboard

## Sequence

### Step 1
User navigates to Sign In.

### Step 2
User provides credentials.

### Step 3
Platform authenticates credentials.

### Step 4
If successful, platform creates session context.

### Step 5
Platform resolves:
- user access status,
- role assignments,
- active restrictions if any.

### Step 6
Platform routes user to role-aware dashboard.

### Step 7
Dashboard presents:
- current status,
- available actions,
- next recommended step.

## Result

- Authenticated session exists.
- User sees an intelligible home state.

---

# 6. Workflow 3: Membership Application

## Purpose

Allow a registered user to apply for Society membership.

## Primary actors

- Registered User / Applicant
- Platform

## Primary objects

- MembershipApplication

## Preconditions

- User is authenticated.
- User is not already an approved member.

## Sequence

### Step 1
User navigates to Membership area.

### Step 2
Platform displays:
- what membership means,
- current status,
- application start action.

### Step 3
User starts application.

### Step 4
Platform creates MembershipApplication in Draft state.

### Step 5
User fills required fields and optionally saves progress.

### Step 6
Platform validates completion when user attempts submission.

### Step 7
If valid, user submits application.

### Step 8
Platform transitions MembershipApplication:
- Draft -> Submitted

### Step 9
Platform updates user-facing application status.
Platform may also update access status context to Applicant.

### Step 10
Platform adds application to reviewer queue and notifies applicant.

## Result

- Membership application is formally submitted.
- Applicant can track status.

---

# 7. Workflow 4: Membership Review and Decision

## Purpose

Allow an authorized reviewer to process a submitted application.

## Primary actors

- Membership Reviewer
- Applicant
- Platform

## Primary objects

- MembershipApplication
- MembershipDecision
- MembershipRecord

## Preconditions

- Application is Submitted or MoreInfoRequested and ready for resumed review.
- Reviewer has authority.

## Sequence

### Step 1
Reviewer opens membership review queue.

### Step 2
Platform shows pending applications with status and filtering tools.

### Step 3
Reviewer opens a specific application.

### Step 4
Platform presents full application details and current state.

### Step 5
Reviewer chooses one of the permitted actions:
- take into review,
- request more information,
- approve,
- reject.

### Step 6A: Request more information path
- Platform transitions application to MoreInfoRequested.
- Platform records reviewer note/request.
- Platform notifies applicant.
- Applicant later responds and reviewer resumes review.

### Step 6B: Approval path
- Reviewer approves application.
- Platform records MembershipDecision.
- Platform transitions application to Approved.
- Platform creates or activates MembershipRecord.
- Platform updates user access state to Member.
- Platform notifies user.

### Step 6C: Rejection path
- Reviewer rejects application with reason.
- Platform records MembershipDecision.
- Platform transitions application to Rejected.
- Platform updates access context accordingly.
- Platform notifies user.

## Result

- Application reaches terminal decision or loops for more information.
- Approved applicant becomes member.

---

# 8. Workflow 5: Member Activation and First Governance Access

## Purpose

Allow a newly approved member to recognize their new status and enter governance participation.

## Primary actors

- Approved Member
- Platform

## Primary objects

- MembershipRecord
- Dashboard
- Proposal index
- Current draft

## Sequence

### Step 1
User signs in after approval or refreshes existing session context.

### Step 2
Platform recalculates permissions based on MembershipRecord and roles.

### Step 3
Dashboard now displays member-specific modules such as:
- proposals,
- votes,
- current draft,
- member discussions.

### Step 4
Platform may display a membership-approved notice or onboarding prompt.

### Step 5
User enters governance workspace.

## Result

- User now experiences member-only participation flows.

---

# 9. Workflow 6: Proposal Drafting and Submission

## Purpose

Allow a member to create and submit a governance proposal.

## Primary actors

- Member
- Platform

## Primary objects

- Proposal
- ProposalRevision

## Preconditions

- User is authenticated.
- User is approved member.
- User is not blocked from proposal submission.

## Sequence

### Step 1
Member enters Governance > Create Proposal.

### Step 2
Platform presents proposal creation form with structured fields such as:
- title,
- summary,
- rationale,
- proposed text,
- category.

### Step 3
Platform creates Proposal in Draft state and initial ProposalRevision in DraftRevision state or equivalent.

### Step 4
Member saves progress, edits, and refines content.

### Step 5
Member submits proposal.

### Step 6
Platform validates required content and submission eligibility.

### Step 7
If valid:
- Proposal transitions Draft -> Submitted.
- Submitted revision becomes current operative revision.
- Proposal enters proposal intake queue.
- Proposal author receives confirmation.
- Audit event recorded.

## Result

- Proposal is in formal workflow.

---

# 10. Workflow 7: Proposal Review and Discussion Opening

## Purpose

Allow an authorized operator to move a proposal into active discussion.

## Primary actors

- Reviewer / Governance Operator / Moderator depending policy
- Proposal Author
- Members
- Platform

## Primary objects

- Proposal
- ProposalStateTransition
- DiscussionThread

## Preconditions

- Proposal is Submitted or UnderReview.
- Operator has authority.

## Sequence

### Step 1
Operator opens proposal queue.

### Step 2
Platform lists proposals awaiting intake/review.

### Step 3
Operator opens proposal detail and evaluates:
- completeness,
- fit for discussion,
- procedural readiness.

### Step 4
Operator chooses one of the allowed actions:
- move to UnderReview,
- return for revision,
- move to OpenForDiscussion,
- withdraw/supersede if policy allows.

### Step 5A: Return for revision
- Platform records state transition to ReturnedForRevision.
- Platform records reason.
- Author notified.

### Step 5B: Open for discussion
- Platform transitions proposal to OpenForDiscussion.
- Platform opens associated DiscussionThread.
- Platform notifies relevant members or watchers.
- Proposal becomes discoverable in active discussion lists.

## Result

- Proposal is either sent back for revision or opened for structured deliberation.

---

# 11. Workflow 8: Proposal Revision Loop

## Purpose

Allow proposal text to improve through feedback and iterative drafting.

## Primary actors

- Proposal Author
- Members
- Reviewer / Moderator / Operator
- Platform

## Primary objects

- Proposal
- ProposalRevision
- Comment
- ProposalStateTransition

## Sequence

### Step 1
Members discuss proposal in thread.

### Step 2
Author reviews feedback.

### Step 3
Author creates a new ProposalRevision.

### Step 4
Platform stores revision history and marks new revision as pending/current according to workflow rules.

### Step 5
Operator or system updates current operative revision when accepted.

### Step 6
If proposal was previously ReturnedForRevision:
- author revises,
- resubmits,
- proposal returns to Submitted or review-ready state.

### Step 7
Discussion continues until proposal is ready to move toward vote.

## Result

- Proposal evolves without losing prior history.

---

# 12. Workflow 9: Vote Preparation and Vote Opening

## Purpose

Allow a proposal that has completed discussion/review to enter formal voting.

## Primary actors

- Authorized Operator / Admin / Clerk-like role
- Platform
- Eligible Members

## Primary objects

- Proposal
- VoteWindow
- VoteEligibilitySnapshot

## Preconditions

- Proposal is OpenForDiscussion or ReadyForVote.
- Required pre-vote conditions are satisfied.

## Sequence

### Step 1
Operator reviews proposal readiness.

### Step 2
Operator marks proposal ReadyForVote.

### Step 3
Platform records proposal state transition.

### Step 4
Operator configures vote window:
- open time,
- close time,
- eligibility basis,
- rule reference if applicable.

### Step 5
Platform creates VoteWindow in Scheduled state and stores eligibility snapshot where needed.

### Step 6
At open time or via authorized action:
- VoteWindow transitions Scheduled -> Open.
- Proposal transitions ReadyForVote -> VotingOpen.
- Eligible voters are notified.

## Result

- Proposal is in active formal voting.

---

# 13. Workflow 10: Member Voting

## Purpose

Allow eligible members to cast votes on an open proposal.

## Primary actors

- Eligible Member
- Platform

## Primary objects

- VoteWindow
- Ballot

## Preconditions

- User is authenticated.
- User is eligible.
- Vote window is Open.

## Sequence

### Step 1
Member views active votes list or proposal voting page.

### Step 2
Platform checks eligibility and displays ballot options.

### Step 3
Member casts vote.

### Step 4
Platform validates:
- membership status,
- eligibility,
- vote window open,
- ballot format.

### Step 5
Platform creates or updates Ballot.

### Step 6
Platform confirms vote capture.

### Step 7
If allowed by rules, member may update vote before close.
Platform records ballot history where relevant.

### Step 8
When vote window closes:
- ballots become locked,
- further changes prevented.

## Result

- Eligible ballots are captured and preserved.

---

# 14. Workflow 11: Outcome Resolution and Certification

## Purpose

Resolve a proposal after voting and record its formal outcome.

## Primary actors

- Platform
- Authorized Operator / Certifier / Admin
- Members

## Primary objects

- VoteWindow
- VoteTally
- ProposalOutcome
- Proposal

## Preconditions

- VoteWindow is Closed.

## Sequence

### Step 1
Platform computes or finalizes VoteTally.

### Step 2
Platform evaluates outcome basis according to rule reference.

### Step 3
Platform creates ProposalOutcome with one of the allowed result types, such as:
- Adopted,
- Rejected,
- Returned,
- Voided.

### Step 4
Platform updates Proposal state consistently with result.

### Step 5
If certification is required:
- authorized actor reviews result,
- certifies outcome,
- certification record stored.

### Step 6
Platform publishes visible outcome summary to relevant users.

### Step 7
Audit events are written for close, tally, result, and certification.

## Result

- Proposal reaches formal outcome state.

---

# 15. Workflow 12: Authoritative Draft Update

## Purpose

Update the current authoritative drafting state when adopted outcomes require it.

## Primary actors

- Editor / Authorized Operator / Admin
- Platform

## Primary objects

- ProposalOutcome
- AuthoritativeDraftState

## Preconditions

- ProposalOutcome is Adopted.
- Outcome affects current authoritative text.

## Sequence

### Step 1
Authorized actor reviews adopted outcome and affected drafting content.

### Step 2
Platform or editor prepares new draft snapshot based on prior current authoritative state plus adopted change.

### Step 3
Platform creates new AuthoritativeDraftState in Drafting or pending state.

### Step 4
Authorized actor confirms publication of this new authoritative state.

### Step 5
Platform transitions new draft state to PublishedCurrent.

### Step 6
Platform transitions prior current authoritative state to SupersededHistorical.

### Step 7
Platform updates current authoritative pointer.

### Step 8
Platform exposes updated current draft to the appropriate audience and records change history.

## Result

- Canonical current drafting state is updated without losing prior versions.

---

# 16. Workflow 13: Publication Workflow

## Purpose

Prepare and publish official explanatory or institutional content.

## Primary actors

- Editor / Publisher
- Platform

## Primary objects

- PublicationItem
- PublicationRevision

## Sequence

### Step 1
Editor creates or opens a PublicationItem draft.

### Step 2
Editor writes or revises content.

### Step 3
Platform stores PublicationRevision history as needed.

### Step 4
Editor submits item for review or directly publishes if policy allows.

### Step 5
Platform transitions PublicationItem to Published.

### Step 6
Public site or relevant audience surfaces update automatically.

### Step 7
If item is later retired or replaced:
- item may be unpublished or archived.

## Result

- Official/public content is controlled and traceable.

---

# 17. Workflow 14: Moderation Workflow

## Purpose

Handle problematic or disruptive content in discussion spaces.

## Primary actors

- Member or reporting user
- Moderator
- Platform

## Primary objects

- ModerationReport
- ModerationAction
- Comment / DiscussionThread
- ParticipationRestriction optional

## Sequence

### Step 1
Member reports a comment or discussion item.

### Step 2
Platform creates ModerationReport in Open state.

### Step 3
Moderator reviews report queue.

### Step 4
Moderator opens report detail and relevant content context.

### Step 5
Moderator chooses one of the permitted outcomes:
- dismiss,
- hide/remove content,
- lock discussion,
- apply user restriction if policy allows.

### Step 6
Platform records ModerationAction.

### Step 7
Platform updates content state or participation state accordingly.

### Step 8
Platform closes report and writes audit events.

## Result

- Moderation issue is resolved with durable record.

---

# 18. Workflow 15: Administrative Intervention Workflow

## Purpose

Handle exceptional cases or platform-level operational needs.

## Primary actors

- Administrator
- Platform

## Primary objects

- User
- Role assignment
- MembershipRecord
- Proposal
- VoteWindow
- Settings
- AuditEvent

## Sequence

### Step 1
Administrator identifies issue through dashboard, report, or support case.

### Step 2
Administrator navigates to relevant object detail.

### Step 3
Administrator performs authorized intervention such as:
- changing role assignment,
- resolving stuck workflow state,
- correcting visibility,
- deactivating account,
- applying exceptional state handling.

### Step 4
Platform validates admin authority and consistency rules.

### Step 5
Platform performs change and records strong audit entry including reason.

### Step 6
Affected users are notified where appropriate.

## Result

- Exceptional operational issue is resolved without hidden or silent changes.

---

# 19. Workflow 16: Archive and History Retrieval Workflow

## Purpose

Allow users to retrieve institutional history and understand how decisions evolved.

## Primary actors

- Member
- Public Reader where visibility permits
- Operator
- Platform

## Primary objects

- Archived Proposal
- ProposalRevision
- ProposalOutcome
- AuthoritativeDraftState
- RecordTimelineEvent

## Sequence

### Step 1
User navigates to Archive or history-related view.

### Step 2
Platform provides search/filter tools.

### Step 3
User selects historic proposal, historic draft state, or record timeline.

### Step 4
Platform displays:
- prior states,
- revision history,
- outcome,
- related proposals,
- authoritative effects where applicable.

### Step 5
User follows linked history across objects.

## Result

- Institutional memory is explorable and legible.

---

# 20. Cross-Workflow Dependencies

## 20.1 Registration precedes membership application
A public visitor must become a registered user before applying.

## 20.2 Membership approval precedes core governance participation
Proposal creation and voting depend on approved membership.

## 20.3 Proposal workflow precedes voting
A proposal should not enter voting without valid prior progression.

## 20.4 Voting outcome may trigger authoritative draft update
An adopted proposal may require canonical text update.

## 20.5 Publication and archive workflows depend on stable records
Strong historical and official outputs depend on preserved workflow data.

---

# 21. Failure and Exception Patterns

The platform should handle the following exceptions clearly.

## 21.1 Invalid registration or authentication attempts
User receives clear validation or authentication error.

## 21.2 Incomplete application submission
Application remains in draft until corrected.

## 21.3 Proposal returned for revision
Proposal loops back into drafting/review rather than disappearing.

## 21.4 Vote voiding
If procedural failure occurs, VoteWindow may be voided and Proposal may return to prior workflow state as policy allows.

## 21.5 Membership restriction during active participation
Permissions should recalculate immediately and block disallowed future actions while preserving historical records of prior valid actions.

## 21.6 Admin override
Exceptional action should remain explicit and auditable.

---

# 22. MVP-Critical Workflow Sequences

For the earliest credible release, the most important sequences to implement cleanly are:

1. Public discovery -> registration
2. Registration -> login -> dashboard
3. Membership application -> review -> approval
4. Member activation -> proposal creation
5. Proposal submission -> review -> discussion
6. Revision loop
7. Ready for vote -> vote window open
8. Member voting
9. Vote close -> outcome
10. Adopted outcome -> authoritative draft update
11. Admin queue handling
12. Audit generation across each of the above

These are the workflows that prove the platform is real.

---

# 23. QA Scenarios Implied by These Workflows

Each workflow should later yield QA scenarios such as:

- happy path,
- invalid input path,
- permissions denial path,
- concurrent update path,
- stale state path,
- notification trigger path,
- audit record verification path,
- archive/history verification path.

This document should therefore be treated as a direct precursor to test-case design.

---

# 24. Summary

The Ardtire Society Civic Digital Governance Platform should be implemented as a sequence-driven civic system in which users and operators move through clear, recorded workflows for:

- registration,
- membership,
- proposal authoring,
- discussion,
- revision,
- voting,
- outcomes,
- authoritative drafting,
- publication,
- moderation,
- administration,
- and historical review.

The product succeeds when those workflows are not merely possible, but intelligible, bounded, and durable.
