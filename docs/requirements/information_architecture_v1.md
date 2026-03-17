## `information_architecture_v1.md`

# information_architecture_v1.md

# Ardtire Society Civic Digital Governance Platform
## Information Architecture v1

## Document Status

- Version: v1
- Purpose: define the recommended information architecture for the platform
- Scope: platform-level IA, navigation, page groups, content domains, and object relationships
- Audience: founders, product planners, designers, engineers, editors, and administrators

---

# 1. Purpose of This Document

This document defines the recommended information architecture for the Ardtire Society Civic Digital Governance Platform.

Its purpose is to organize the platform into a coherent structure that supports:

- public understanding,
- identity and account progression,
- membership workflows,
- constitutional and governance participation,
- administrative operations,
- publication of authoritative materials,
- and durable institutional memory.

This is not merely a sitemap. It is a structural model for how people, pages, workflows, and governance objects should be arranged so that the platform feels intelligible, serious, and institutionally coherent.

---

# 2. Information Architecture Goals

The information architecture should achieve the following:

1. make the platform legible to first-time visitors;
2. make participation pathways obvious;
3. distinguish clearly between public, authenticated, member-only, and operator-only spaces;
4. organize governance work around structured objects rather than scattered content;
5. make current status and next actions discoverable;
6. preserve a clear distinction between active workflow spaces and authoritative publication spaces;
7. support future growth without forcing a conceptual rewrite.

---

# 3. Primary IA Principles

## 3.1 Public, participation, and operations should be distinct layers

The platform should be organized into three major layers:

### Public layer
Where non-authenticated users learn about the Society and the platform.

### Participation layer
Where registered users, applicants, and members interact with account, membership, proposal, discussion, and voting workflows.

### Operations layer
Where reviewers, moderators, editors, and administrators manage institutional and platform processes.

These layers may share branding and design language, but their information architecture should remain distinct.

## 3.2 Workflow objects matter more than generic pages

The core of the platform should not be modeled as flat pages alone.

Important governance entities should exist as first-class information objects, such as:

- users,
- accounts,
- membership applications,
- members,
- proposals,
- revisions,
- comments,
- votes,
- outcomes,
- authoritative text states,
- published records,
- moderation actions,
- audit events.

## 3.3 Authority levels must be visible in the IA

The information architecture should help users distinguish among:

- explanatory/public content,
- in-progress governance content,
- member discussion content,
- official published materials,
- historical archives.

Public pages and official records should not blur together with proposal workspaces.

## 3.4 The platform should be navigable by both role and task

Users should be able to navigate by:

- who they are,
- what they are trying to do,
- and what object they are working on.

Examples:

- a public visitor navigates by understanding and entry;
- an applicant navigates by application status;
- a member navigates by proposals, discussions, and votes;
- a reviewer navigates by pending work;
- an admin navigates by queues, states, and exceptions.

---

# 4. Top-Level IA Model

The recommended top-level platform architecture is:

1. Public Site
2. Authentication and Account
3. User Dashboard
4. Membership
5. Governance Workspace
6. Authoritative Text and Publications
7. Archive and Records
8. Operations Console
9. Platform-Level Utilities

---

# 5. Top-Level Navigation Structure

A recommended high-level navigation model is as follows.

## 5.1 Public navigation

Public users should primarily see:

- Home
- About
- Participation
- Governance
- Publications
- Archive
- Sign In
- Register

Optional public links depending on scope:

- FAQ
- Principles / Mission
- Membership
- Contact
- Public Announcements

## 5.2 Authenticated user navigation

Logged-in users should see a role-aware navigation including:

- Dashboard
- My Account
- Membership
- Governance
- Publications
- Archive

And then, depending on role:

- Review Queue
- Moderation
- Editorial
- Admin

## 5.3 Member-focused navigation

Approved members should see:

- Dashboard
- Proposals
- Discussions
- Votes
- Current Draft
- Archive
- My Activity

## 5.4 Operator navigation

Reviewers, moderators, editors, and administrators should see specialized work areas such as:

- Application Queue
- Proposal Queue
- Voting Administration
- Moderation Queue
- Publication Management
- Audit / Activity
- Admin Settings

---

# 6. IA by Domain

# 6.1 Public Site Domain

## Purpose

The Public Site domain exists to:

- explain the Society,
- explain the platform,
- explain participation pathways,
- build trust,
- and provide access to registration and public materials.

## Recommended public pages

### Home
Primary public landing page.

Should communicate:
- what the Society is,
- what the platform is for,
- why it exists,
- how participation works,
- and where to begin.

### About
Explains the Society’s mission, purpose, and general institutional framing.

### Participation
Explains:
- visitor vs registered user vs member,
- how membership works,
- how governance participation works,
- and what the pathway looks like.

### Governance
Public explanation of the governance process and constitutional drafting model.

### Publications
Public-facing official materials and public records.

### Archive
Publicly accessible historical materials, where appropriate.

### Register
Account creation entry point.

### Sign In
Authentication entry point.

## Public IA notes

The public layer should not overwhelm visitors with internal workflow detail, but it should establish seriousness and clarity.

The public site should answer:

- What is this?
- Why does it exist?
- How does participation work?
- How do I begin?
- What official or public materials can I read?

---

# 6.2 Authentication and Account Domain

## Purpose

This domain manages user identity and the transition from anonymous visitor to authenticated participant.

## Recommended pages and objects

### Register
- account creation form
- credential creation
- agreement and policy acknowledgment as needed

### Verify Account
- email verification or equivalent flow

### Sign In
- login form
- session start

### Forgot Password / Reset Password
- account recovery basics

### Account Overview
- personal account status
- current permissions/status
- identity basics

### Security Settings
- password change
- session management
- authentication hardening as supported

## IA notes

This area should clearly distinguish:
- being authenticated,
- being registered,
- being an applicant,
- being a member,
- being an operator.

The account area is not the same as the governance area.

---

# 6.3 Dashboard Domain

## Purpose

The dashboard is the user’s role-aware home base after login.

It should orient the user around:
- who they are in the system,
- what status they hold,
- what actions are available,
- and what requires attention.

## Recommended dashboard variants

### Registered User Dashboard
Should emphasize:
- current status,
- membership application start or progress,
- account completeness,
- public/member pathway.

### Applicant Dashboard
Should emphasize:
- application status,
- requests for additional information,
- next steps,
- notices.

### Member Dashboard
Should emphasize:
- active proposals,
- open votes,
- discussion activity,
- current draft state,
- relevant alerts.

### Operator Dashboard
Should emphasize:
- queues,
- pending actions,
- moderation/review items,
- recent high-signal events.

## Core dashboard modules

Potential dashboard modules include:
- status card
- next actions
- membership/application summary
- active proposals
- open votes
- recent discussions
- proposal watchlist
- review queue
- moderation queue
- recent institutional activity

---

# 6.4 Membership Domain

## Purpose

This domain manages progression from registered user to applicant to approved member.

## Primary objects

- membership application
- application draft
- application status
- reviewer decision
- membership status record

## Recommended pages

### Membership Overview
Explains the meaning of membership and current user status.

### Start Application
Entry point into membership application workflow.

### Application Form
Structured membership application.

### Application Draft / Resume
Saved in-progress work.

### Application Status
Tracks current application state.

### Reviewer Queue
Operator list view of pending applications.

### Application Detail
Detailed review view for authorized reviewers.

### Membership Roster or Member Status Management
Operator-only management view.

## IA notes

The membership domain is one of the platform’s most important progression areas.

It should never be ambiguous whether the user is:
- only registered,
- currently applying,
- approved,
- rejected,
- suspended,
- or otherwise restricted.

---

# 6.5 Governance Workspace Domain

## Purpose

This is the heart of the product.

It exists to support:
- proposal submission,
- deliberation,
- revision,
- workflow progression,
- voting,
- outcomes,
- and linkage to authoritative drafting state.

## Core governance objects

- proposal
- proposal revision
- discussion thread / comments
- vote window
- ballot / vote record
- outcome
- related proposal relationship
- workflow state transition
- rule reference
- status history

## Recommended governance pages

### Proposal Index
List of proposals.

Should support:
- status filters,
- search,
- category filters,
- sorting,
- role-aware visibility.

### Proposal Detail
Primary working surface for a governance item.

Should show:
- title,
- summary,
- rationale,
- author,
- state,
- revision history,
- current text,
- discussion,
- voting state,
- related records,
- outcome when available.

### Create Proposal
Proposal drafting and submission flow.

### Proposal Drafts
User’s saved proposal drafts.

### Discussions
Optional cross-proposal discussion aggregation view.

### Votes
List of active and recent voting items.

### Vote Detail
Proposal-specific voting context and outcome detail.

### My Governance Activity
Personal participation area.

## IA notes

The governance workspace should be object-centered, not generic-page-centered.

Proposal detail pages should function as the central hub for a governance item.

---

# 6.6 Authoritative Text and Publications Domain

## Purpose

This domain exists to distinguish official or currently authoritative material from active workflow objects.

This is a critical architectural separation.

## Core objects

- authoritative draft state
- adopted text
- published governance record
- public notice
- official publication item

## Recommended pages

### Current Draft / Authoritative Text
Displays the current authoritative constitutional or governance drafting state.

Must be clearly labeled as authoritative or current.

### Publications Index
Official publications and public institutional outputs.

### Publication Detail
Single public or semi-public official item.

### Outcome Publications
Optional publication layer for adopted or resolved proposal outputs.

## IA notes

This domain must remain distinct from the proposal workspace.

A proposal page is not the same thing as authoritative text.

A discussion thread is not the same thing as official publication.

---

# 6.7 Archive and Records Domain

## Purpose

This domain preserves institutional memory.

It should help users understand:
- what happened,
- when,
- why,
- under what status,
- and in what sequence.

## Core objects

- archived proposals
- historic revisions
- past outcomes
- historic authoritative states
- audit-relevant public records
- record bundles or timelines as later phases permit

## Recommended pages

### Archive Index
General historic entry point.

### Historic Proposal Index
Past proposals with outcomes and dates.

### Historic Proposal Detail
Preserved proposal detail and resolution history.

### Historic Draft States
Past authoritative drafting snapshots.

### Record Timeline
Optional timeline-based historic view.

## IA notes

The archive should not be treated as dead storage. It is part of the product’s civic credibility.

---

# 6.8 Operations Console Domain

## Purpose

This domain is for trusted platform operators.

It exists to keep institutional workflows manageable.

## Core operational areas

### Membership Review
- application queue
- application detail
- reviewer actions

### Governance Administration
- proposal queue
- state transition tools
- voting administration

### Moderation
- flagged content
- moderation actions
- user restrictions as permitted

### Editorial
- publication workflow
- authoritative text updates
- public content maintenance

### Administration
- user management
- role management
- exceptional case handling
- audit visibility
- platform configuration

## IA notes

Operations tools should be task-oriented and queue-oriented.

Operators need fast access to:
- pending items,
- filtered views,
- action affordances,
- history/context,
- and recorded outcomes.

---

# 6.9 Platform-Level Utilities Domain

## Purpose

These are cross-cutting utilities needed throughout the system.

## Recommended utilities

- global search
- notifications
- help / guidance
- policy references
- status labeling system
- breadcrumbs / contextual navigation
- audit or activity feed surfaces
- system notices / banners

---

# 7. IA Tree

A recommended structural tree is below.

```text
/
├── home
├── about
├── participation
├── governance
├── publications
├── archive
├── sign-in
├── register
│
├── app
│   ├── dashboard
│   ├── account
│   │   ├── overview
│   │   ├── profile
│   │   └── security
│   │
│   ├── membership
│   │   ├── overview
│   │   ├── apply
│   │   ├── draft
│   │   ├── status
│   │   └── history
│   │
│   ├── governance
│   │   ├── proposals
│   │   │   ├── index
│   │   │   ├── create
│   │   │   ├── drafts
│   │   │   └── {proposalId}
│   │   │       ├── overview
│   │   │       ├── revisions
│   │   │       ├── discussion
│   │   │       ├── voting
│   │   │       └── history
│   │   │
│   │   ├── votes
│   │   │   ├── index
│   │   │   └── {voteId}
│   │   │
│   │   ├── current-draft
│   │   └── my-activity
│   │
│   ├── publications
│   │   ├── index
│   │   └── {publicationId}
│   │
│   ├── archive
│   │   ├── index
│   │   ├── proposals
│   │   ├── draft-states
│   │   └── records
│   │
│   ├── notifications
│   └── help
│
└── ops
    ├── dashboard
    ├── membership
    │   ├── queue
    │   ├── applications
    │   └── members
    │
    ├── governance
    │   ├── queue
    │   ├── proposals
    │   ├── voting
    │   └── outcomes
    │
    ├── moderation
    │   ├── queue
    │   ├── reports
    │   └── actions
    │
    ├── editorial
    │   ├── publications
    │   ├── current-draft
    │   └── public-content
    │
    ├── admin
    │   ├── users
    │   ├── roles
    │   ├── audit
    │   └── settings
    │
    └── search
```

---

# 8. Navigation Model by Persona

# 8.1 Public Visitor

Primary navigation needs:

* understand the Society,
* understand participation,
* find registration,
* read official/public materials.

Suggested priority:

1. Home
2. Participation
3. Governance
4. Publications
5. Register

# 8.2 Registered User

Primary navigation needs:

* understand current status,
* manage account,
* begin or track membership.

Suggested priority:

1. Dashboard
2. Membership
3. Account
4. Publications
5. Archive

# 8.3 Applicant

Primary navigation needs:

* see status,
* respond to requests,
* complete application.

Suggested priority:

1. Dashboard
2. Membership Status
3. Application
4. Account
5. Help

# 8.4 Member

Primary navigation needs:

* view active governance work,
* participate in proposals,
* vote,
* read current draft.

Suggested priority:

1. Dashboard
2. Proposals
3. Votes
4. Current Draft
5. My Activity
6. Archive

# 8.5 Reviewer / Moderator / Admin

Primary navigation needs:

* work queues,
* pending actions,
* operational detail,
* exception handling.

Suggested priority:

1. Ops Dashboard
2. Relevant Queue
3. Detailed Work Area
4. Audit / Activity
5. Admin Utilities

---

# 9. Page Types and Object Types

The architecture should distinguish between page types and object types.

## 9.1 Page types

* public content page
* dashboard page
* list/index page
* detail page
* create/edit form page
* queue page
* status page
* record/archive page

## 9.2 Object types

* user
* account
* membership application
* membership status
* proposal
* proposal revision
* comment
* vote window
* ballot / vote
* outcome
* publication
* authoritative draft snapshot
* moderation action
* audit event

This distinction is important because the product is fundamentally built around governed objects that are displayed through page surfaces.

---

# 10. List Views Required

The platform should support strong list/index views for the following:

* proposals
* active votes
* publications
* archive items
* application queue
* member records
* flagged comments/content
* users
* audit events

List views should generally support:

* search,
* filtering,
* sorting,
* status labels,
* and direct navigation to detail pages.

---

# 11. Detail Views Required

The platform should support strong detail pages for:

* membership applications
* proposals
* proposal revisions
* vote windows / outcome views
* publication items
* archived records
* user/admin records as role allows

A detail page should generally answer:

* what this object is,
* what state it is in,
* what happened to it,
* who is involved,
* what can happen next,
* and what related records exist.

---

# 12. Cross-Linking Rules

The IA should support strong cross-linking between related objects.

Examples:

* a proposal links to its revisions;
* a proposal links to its discussion;
* a proposal links to its vote window;
* a proposal links to its outcome;
* an adopted proposal links to the authoritative text state it affected;
* an archive item links back to original workflow history;
* an application decision links to reviewer record and status change history.

This cross-linking is essential for institutional legibility.

---

# 13. Search Architecture

Search should be designed by domain and by visibility scope.

## Recommended searchable domains

### Public search

* public pages
* publications
* public archive items

### Member search

* proposals
* discussions
* votes
* current draft references
* archive

### Operator search

* users
* applications
* proposals
* moderation items
* publications
* audit events

Search results should visibly indicate:

* object type,
* status,
* visibility level,
* and whether the result is current or historical.

---

# 14. Status Labeling System

A consistent status-labeling system is a major IA need.

Status labels should appear prominently in list views and detail views for objects such as:

* membership applications,
* member status,
* proposals,
* vote windows,
* publication states,
* archive states.

Status labels should be:

* explicit,
* plain-language,
* visually consistent,
* and semantically meaningful.

---

# 15. Authority Layering in the IA

The architecture should visibly separate four authority layers.

## Layer 1: Explanatory public content

“Here is what the Society and the platform are.”

## Layer 2: Active governance workflow content

“Here is what is currently being proposed, discussed, revised, or voted.”

## Layer 3: Authoritative current text

“Here is the current authoritative drafting state.”

## Layer 4: Historic record

“Here is what happened previously.”

Users should not need to infer which layer they are viewing.

---

# 16. Recommended URL / Route Semantics

Route semantics should reinforce clarity.

Examples:

* `/governance/proposals` for active governance objects
* `/current-draft` for authoritative current text
* `/archive/proposals` for historic proposal records
* `/ops/membership/queue` for operational review space

Avoid route structures that blur:

* workflow content with official content,
* archive content with current content,
* public content with operator tools.

---

# 17. IA Risks to Avoid

The following information architecture mistakes should be avoided.

## 17.1 Public-site-first architecture with governance bolted on

This would reduce the platform to a brochure with weak civic internals.

## 17.2 Treating proposals as generic blog posts

Governance objects require lifecycle and history.

## 17.3 Blurring current draft with active proposals

This would damage legitimacy and user trust.

## 17.4 Hiding operator workflows

Reviewers and admins need first-class areas, not improvised backdoors.

## 17.5 Poor status discoverability

Users must not hunt for key state information.

## 17.6 Archive as afterthought

Institutional memory is not optional.

---

# 18. MVP IA Priorities

For the earliest version, the most important IA components are:

1. public site explaining mission and participation;
2. registration and account entry points;
3. user dashboard;
4. membership application flow and status area;
5. proposal index and proposal detail;
6. discussion and revision surfaces;
7. voting surface;
8. current authoritative draft surface;
9. operator queues for applications and proposal management;
10. basic archive/history surfaces.

---

# 19. Summary

The recommended information architecture for the Ardtire Society Civic Digital Governance Platform is a layered civic structure composed of:

* a public understanding layer,
* an identity and progression layer,
* a governance workspace layer,
* an authoritative publication layer,
* a historical archive layer,
* and an operational control layer.

This architecture is designed to ensure that the platform is not merely navigable, but institutionally legible: users should be able to tell where they are, what type of thing they are looking at, what authority it carries, what state it is in, and what happens next.
