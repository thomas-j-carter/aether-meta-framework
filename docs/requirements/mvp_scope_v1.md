# mvp_scope_v1.md

# Ardtire Society Civic Digital Governance Platform
## MVP Scope v1

## Document Status

- Version: v1
- Purpose: define the recommended minimum viable product scope for the first coherent release
- Scope: product scope and release boundary, not implementation architecture
- Audience: founders, product planners, designers, engineers, and operators

---

# 1. Purpose of This Document

This document defines the recommended MVP scope for the Ardtire Society Civic Digital Governance Platform.

The purpose of the MVP is not to build every eventual feature of the platform.

The purpose of the MVP is to prove that the Ardtire Society can run its foundational civic-digital process in one coherent system.

That means the MVP should deliver the smallest complete institutional loop that allows the platform to function as a real governance environment rather than a concept site.

---

# 2. Core MVP Thesis

The MVP succeeds if it enables the following end-to-end progression:

1. a person discovers the Society publicly;
2. the person registers an account;
3. the registered user applies for membership;
4. the application is reviewed and decided;
5. the approved applicant becomes a member;
6. the member can access governance participation features;
7. the member can submit a proposal;
8. members can discuss and revise the proposal;
9. the proposal can enter a voting window;
10. eligible members can vote;
11. the outcome is recorded;
12. the authoritative drafting state can be understood and published.

If that loop works, the platform is already demonstrating its reason for existing.

---

# 3. MVP Product Goal

The goal of the MVP is to establish a credible, usable, serious, and operationally manageable platform for constitutional and governance formation.

It must be good enough that the Society could actually use it for real early-stage civic work.

---

# 4. What “Minimum Viable” Means Here

“Minimum viable” does not mean trivial.

For this platform, minimum viable means:

- the smallest coherent product that expresses the platform’s real institutional purpose;
- not a prototype with fake flows;
- not just public pages and login;
- not just a discussion forum;
- not a document repository without workflow;
- not a vague alpha with missing process boundaries.

The MVP should be minimal in breadth, but complete in civic logic.

---

# 5. MVP In-Scope Domains

The MVP should include the following domains.

## 5.1 Public presence

The platform must have a public-facing layer that explains:
- what the Ardtire Society is,
- what the platform is for,
- how participation works,
- and how a visitor may register and move toward membership.

## 5.2 Account registration and authentication

The platform must allow:
- account creation,
- secure login,
- account identity persistence,
- password reset or equivalent account recovery basics.

## 5.3 Membership application workflow

The platform must allow:
- a registered user to begin a membership application,
- save progress where appropriate,
- submit the application,
- track the application’s status.

## 5.4 Membership review workflow

The platform must allow authorized reviewers to:
- view submitted applications,
- review details,
- request additional information where needed,
- approve, reject, or return applications,
- and have the outcome reflected in platform permissions.

## 5.5 Member access layer

The platform must distinguish clearly between:
- public visitors,
- registered users,
- applicants,
- and approved members.

Approved members must gain access to member-only governance features.

## 5.6 Proposal submission workflow

The platform must allow approved members to:
- create proposal drafts,
- enter core proposal information,
- submit proposals into the workflow,
- and see their current state.

## 5.7 Proposal discussion and revision

The platform must allow:
- member discussion on proposals,
- preserved comment history,
- preserved proposal revisions,
- visibility into what version is current within the workflow.

## 5.8 Proposal workflow state model

The platform must provide explicit workflow states for proposals.

The exact state names may evolve, but the MVP should include a meaningful sequence such as:

- draft,
- submitted,
- under review,
- open for discussion,
- ready for vote,
- voting open,
- resolved,
- adopted / rejected / returned / withdrawn / superseded.

The important point is not the exact wording, but that the lifecycle is explicit.

## 5.9 Voting

The platform must allow:
- eligible members to vote on proposals in an active voting window,
- votes to be recorded correctly,
- duplicate or invalid voting to be prevented,
- voting windows to open and close under controlled conditions.

## 5.10 Outcome recording

The platform must allow:
- vote results to be preserved,
- proposal outcomes to be visible,
- post-vote status updates,
- and linkage between proposal outcome and authoritative drafting state where applicable.

## 5.11 Publication of authoritative drafting state

The platform must allow users to distinguish between:
- proposals under consideration,
- working draft materials,
- and the currently authoritative drafting state.

Even if the earliest authoritative publication model is simple, it must be explicit.

## 5.12 Basic administration and moderation

The platform must include enough operator tooling to manage:
- users,
- membership applications,
- proposal states,
- discussion moderation,
- and exceptional operational cases.

## 5.13 Basic auditability

The platform must preserve enough record to reconstruct:
- membership decisions,
- proposal submissions,
- proposal state changes,
- revisions,
- votes,
- and important administrative actions.

---

# 6. Detailed MVP Capability List

# 6.1 Public Site

In scope:

- homepage or equivalent public landing page;
- public explanation of the Society and platform;
- clear participation pathway explanation;
- registration entry point;
- public access to selected official/public materials.

Not required for MVP:

- expansive editorial/news ecosystem;
- deep media library;
- complex public campaign features.

---

# 6.2 User Accounts

In scope:

- sign up;
- sign in;
- sign out;
- password recovery basics;
- basic account/profile view;
- visible current user status.

Not required for MVP:

- extensive social profiles;
- advanced personalization;
- broad profile customization.

---

# 6.3 Membership

In scope:

- application start;
- draft/save or equivalent workable completion flow;
- application submission;
- applicant status tracking;
- reviewer queue;
- approval / rejection / return-for-more-info;
- status-based permission upgrade on approval.

Not required for MVP:

- complex multi-stage committee review structures;
- advanced interview scheduling;
- elaborate recommendation/reference systems unless later required.

---

# 6.4 Proposals

In scope:

- proposal creation;
- title, summary, rationale, and proposed text fields;
- proposal drafts;
- proposal submission;
- proposal detail view;
- current workflow state display;
- author visibility per platform rules;
- proposal list/search/filter basics.

Not required for MVP:

- highly advanced document-assembly tooling;
- nested amendment engines;
- multi-document dependency engines beyond basic relationships.

---

# 6.5 Discussion

In scope:

- proposal comments;
- threaded or at least intelligibly structured discussion;
- comment timestamps;
- moderation actions;
- preserved discussion history.

Not required for MVP:

- chat-like real-time debate systems;
- rich reaction mechanics;
- broad social engagement features.

---

# 6.6 Revisions and Versioning

In scope:

- preserved proposal revisions;
- visible revision history;
- ability to identify what changed at a meaningful level;
- clear indication of which proposal version is current in process.

Not required for MVP:

- extremely advanced redlining/diff tooling, if simple but clear history suffices initially;
- full legal-document comparison suite.

---

# 6.7 Voting

In scope:

- vote eligibility enforcement;
- active voting window;
- vote recording;
- duplicate vote prevention;
- close of vote;
- visible result state.

Not required for MVP:

- advanced quorum-rule engines if a simpler explicit rule implementation suffices;
- complex delegation or proxy voting;
- public referenda;
- multi-chamber bicameral procedures.

---

# 6.8 Authoritative Draft Publication

In scope:

- clearly marked authoritative drafting state;
- distinction between authoritative text and active proposals;
- timestamp or revision marker for authoritative state.

Not required for MVP:

- full gazette publishing system;
- elaborate publication pipelines;
- advanced comparative constitutional publication features.

---

# 6.9 Admin and Operator Tools

In scope:

- membership application queue;
- user status management;
- proposal state management;
- moderation of comments;
- essential operational dashboards or worklists.

Not required for MVP:

- extremely deep analytics suite;
- complex staff org charts and delegation layers;
- highly granular internal workflow automation beyond what is needed for operational viability.

---

# 6.10 Audit and Records

In scope:

- records of application decisions;
- records of proposal submissions;
- records of proposal state transitions;
- records of revisions;
- records of votes and outcomes;
- records of important moderation/admin actions.

Not required for MVP:

- enterprise-grade reporting warehouse;
- highly complex archival research tooling;
- long-form record export suites beyond practical basics.

---

# 7. Recommended MVP User Roles

The MVP should support the following distinct user/role states at minimum:

- public visitor,
- registered user,
- membership applicant,
- approved member,
- reviewer,
- moderator,
- administrator.

Additional roles can come later if necessary.

---

# 8. Recommended MVP Proposal Lifecycle

The exact names may change, but the MVP should implement a coherent lifecycle similar to:

1. Draft
2. Submitted
3. Under Review
4. Open for Discussion
5. Ready for Vote
6. Voting Open
7. Resolved

Possible terminal or result states:

- Adopted
- Rejected
- Returned for Revision
- Withdrawn
- Superseded

The exact terminology matters less than clarity and consistency.

---

# 9. Recommended MVP Membership Lifecycle

The MVP should support a coherent lifecycle such as:

1. Registered
2. Application In Progress
3. Application Submitted
4. Under Review
5. More Information Requested
6. Approved
7. Rejected
8. Withdrawn
9. Suspended or Restricted if required by policy

Again, clarity is more important than perfect wording at this stage.

---

# 10. Explicit Out-of-Scope Items for the Earliest MVP

The following should generally be treated as out of scope for the earliest credible release unless later required immediately:

- advanced parliamentary procedure engines;
- committee and subcommittee systems;
- bicameral or multi-body legislative logic;
- live floor management;
- real-time debate chamber mechanics;
- delegate representation systems;
- proxy voting systems;
- public referendum mechanics;
- deeply configurable procedural law engines;
- full constitutional clause dependency engine;
- advanced legal markup and drafting IDE features;
- broad social community features unrelated to the constitutional process;
- extensive media, fundraising, commerce, or event-management modules;
- ceremonial features that do not strengthen the foundational loop.

---

# 11. MVP UX Priorities

The MVP should optimize for:

## 11.1 Clarity
Users should understand who they are, where they are, what they can do, and what happens next.

## 11.2 Seriousness
The product should feel institutionally credible.

## 11.3 Process legibility
Proposal, application, and vote states should be obvious.

## 11.4 Role-aware navigation
Public, registered, member, and operator experiences should feel intentionally differentiated.

## 11.5 Low ambiguity
The product should minimize situations where users must infer process from scattered context.

---

# 12. MVP Success Criteria

The MVP should be considered successful if the following are true:

1. A public visitor can understand the Society and the participation pathway.
2. A visitor can register and authenticate successfully.
3. A registered user can apply for membership.
4. A reviewer can process applications inside the platform.
5. An approved applicant becomes a member with changed permissions.
6. A member can submit a proposal.
7. Members can discuss and revise proposals.
8. Proposals move through visible workflow states.
9. Eligible members can vote during a controlled window.
10. Outcomes are recorded and visible.
11. The current authoritative drafting state is distinguishable from proposals.
12. Operators can manage the platform without depending primarily on off-platform workaround systems.

If those are true, the MVP is real.

---

# 13. MVP Risks to Watch

## Risk 1: Building a public site without the civic loop
A beautiful public site is not enough if the governance workflow is weak.

## Risk 2: Shipping login without meaningful post-login progression
Authenticated emptiness will weaken confidence.

## Risk 3: Treating proposal discussion as enough
Discussion alone is not governance; workflow and outcomes matter.

## Risk 4: Weak role/status distinction
If users cannot tell whether they are registered, applicant, or member, trust will drop.

## Risk 5: Weak authoritative text distinction
If draft and official text blur together, institutional legitimacy will suffer.

## Risk 6: Operator pain
If reviewers and admins must use external tools for core flows, the product is not yet viable.

---

# 14. Recommended Release Slices Within the MVP

A practical MVP build path could be:

## Slice 1: Public and identity foundation
- public pages
- registration
- login
- account status basics

## Slice 2: Membership workflow
- application creation
- application submission
- reviewer handling
- approval status transition

## Slice 3: Member governance participation
- proposal submission
- proposal list/detail
- comments/discussion
- revisions

## Slice 4: Formal process
- proposal states
- voting windows
- vote capture
- outcomes

## Slice 5: Institutional clarity
- authoritative draft publication
- admin tooling
- audit trails
- moderation basics

These slices should build toward one coherent product, not five separate mini-products.

---

# 15. MVP Summary Statement

The MVP of the Ardtire Society Civic Digital Governance Platform should be the smallest serious platform that allows a person to move from public discovery to account creation to membership approval to structured constitutional participation through proposal, discussion, revision, voting, and recorded outcome, with a clearly distinguishable authoritative drafting state and enough operational tooling to run the process coherently.

That is the scope boundary the MVP should defend.
