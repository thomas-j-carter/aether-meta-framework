## `permissions_matrix_v1.md`

# permissions_matrix_v1.md

# Ardtire Society Civic Digital Governance Platform
## Permissions Matrix v1

## Document Status

- Version: v1
- Purpose: define the recommended role and permission model for the platform
- Scope: product-level access and action permissions, not low-level implementation ACL detail
- Audience: founders, product planners, architects, engineers, QA, and operators

---

# 1. Purpose of This Document

This document defines the recommended permissions model for the Ardtire Society Civic Digital Governance Platform.

The platform’s product logic depends heavily on maintaining clear distinctions between:

- public access,
- authenticated access,
- membership,
- governance participation,
- moderation authority,
- editorial authority,
- and administrative authority.

The permissions model exists to ensure that these distinctions are operationally enforceable.

This document is intentionally product-level and human-readable. It is meant to serve as a source of truth for:

- workflow design,
- UI visibility,
- backend authorization,
- QA scenarios,
- and future policy refinement.

---

# 2. Permission Model Principles

## 2.1 Authentication is not membership

A user may have an account and still lack member governance rights.

## 2.2 Membership is not staff authority

An approved member may participate in governance without having moderation, review, editorial, or administrative powers.

## 2.3 Elevated roles should be explicit

Reviewer, moderator, editor, and administrator roles should never be implied.

## 2.4 Permissions should reflect institutional meaning

The permission model should map to real platform and civic roles, not arbitrary technical categories.

## 2.5 Visibility and action are separate concerns

A user may be able to view something without being able to create, edit, approve, moderate, or publish it.

## 2.6 The UI should reflect permission reality

Users should not routinely be shown actions they cannot take.

## 2.7 Sensitive actions require auditability

Important permission-gated actions should generate durable audit records.

---

# 3. Recommended Role Set

The following roles are recommended as the primary product roles.

## 3.1 Anonymous Public Visitor
Non-authenticated platform visitor.

## 3.2 Registered User
Authenticated account holder who is not yet an approved member.

## 3.3 Membership Applicant
A registered user with an application in progress or under review.

This may be treated as a status rather than a completely separate role, but it has meaningful product consequences.

## 3.4 Approved Member
Authenticated user with member governance participation rights.

## 3.5 Membership Reviewer
Trusted operator who may review membership applications.

## 3.6 Moderator
Trusted operator who may manage discussion and moderation actions.

## 3.7 Editor / Publisher
Trusted operator who may manage publication workflows and authoritative/public content.

## 3.8 Administrator
Trusted operator with broad operational authority over users, roles, workflows, and settings.

---

# 4. Role Relationship Model

A user may hold multiple roles or statuses at once.

Examples:
- a person may be both Member and Moderator;
- a person may be both Member and Editor;
- a person may be both Reviewer and Administrator.

The effective permission set should generally be the union of granted role permissions, subject to any explicit deny or policy constraints.

However, UI and governance design should still preserve conceptual separation among these authorities.

---

# 5. Permission Categories

Permissions are grouped by domain:

1. Public content
2. Account and profile
3. Membership application
4. Membership review and member management
5. Proposal lifecycle
6. Discussion
7. Voting
8. Authoritative text and publication
9. Archive and records
10. Moderation
11. Administration
12. Audit visibility

---

# 6. Action Vocabulary

For clarity, actions are described using these common verbs:

- View
- Create
- Edit
- Submit
- Withdraw
- Comment
- Vote
- Review
- Approve
- Reject
- Return
- Transition
- Publish
- Archive
- Moderate
- Manage
- Configure

---

# 7. High-Level Permissions Summary

# 7.1 Anonymous Public Visitor

May generally:
- view public pages,
- view public publications,
- view public archive materials,
- access registration and sign-in pages.

May not generally:
- access authenticated dashboards,
- apply for membership,
- create proposals,
- comment in member governance spaces,
- vote,
- access operator tools.

# 7.2 Registered User

May generally:
- manage own account,
- begin membership application,
- submit membership application,
- track own application,
- view public and own authenticated spaces.

May not generally:
- submit governance proposals,
- vote,
- access member-only governance participation,
- review applications,
- moderate,
- publish official content,
- administer system.

# 7.3 Membership Applicant

May generally:
- do everything a registered user can,
- view and respond to membership application workflow,
- provide additional information if requested.

May not generally:
- receive member governance rights until approval.

# 7.4 Approved Member

May generally:
- view member governance spaces,
- create and submit proposals,
- participate in discussion,
- view current draft and archives,
- vote where eligible,
- track own governance activity.

May not generally:
- review membership applications unless also reviewer,
- moderate unless also moderator,
- publish official materials unless also editor,
- administer system unless also admin.

# 7.5 Membership Reviewer

May generally:
- view application queues,
- review applications,
- request more information,
- approve or reject applications,
- view member records relevant to review workflow.

May not automatically:
- moderate discussions,
- publish official text,
- manage all system settings,
unless also holding those roles.

# 7.6 Moderator

May generally:
- review reports,
- moderate discussion content,
- restrict participation as policy allows,
- record moderation reasons.

May not automatically:
- approve membership,
- publish official content,
- change broad platform settings,
unless also holding those roles.

# 7.7 Editor / Publisher

May generally:
- manage publication items,
- publish official materials,
- manage authoritative-text publication workflow,
- update public explanatory content.

May not automatically:
- approve membership,
- moderate users,
- change system-wide permissions,
unless also holding those roles.

# 7.8 Administrator

May generally:
- manage users,
- manage role assignments,
- manage platform workflows,
- resolve operational edge cases,
- view audit information,
- configure settings within policy bounds.

Administrators should still be subject to audit and should not bypass institutional logic silently.

---

# 8. Detailed Permissions Matrix

Legend:
- Y = allowed
- N = not allowed
- C = conditional / allowed only in limited circumstances or based on state/policy
- O = operator-only specialized permission

## 8.1 Public Content and Discovery

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View public site pages | Y | Y | Y | Y | Y | Y | Y | Y |
| View public participation info | Y | Y | Y | Y | Y | Y | Y | Y |
| View public governance explanation | Y | Y | Y | Y | Y | Y | Y | Y |
| View public publications | Y | Y | Y | Y | Y | Y | Y | Y |
| View public archive items | Y | Y | Y | Y | Y | Y | Y | Y |
| Register account | Y | N | N | N | N | N | N | N |
| Sign in | N | Y | Y | Y | Y | Y | Y | Y |

## 8.2 Account and Profile

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View own account dashboard | N | Y | Y | Y | Y | Y | Y | Y |
| Edit own basic profile | N | Y | Y | Y | Y | Y | Y | Y |
| Change own password/security settings | N | Y | Y | Y | Y | Y | Y | Y |
| View own status badges | N | Y | Y | Y | Y | Y | Y | Y |
| View another user’s private account data | N | N | N | N | C | C | N | O |

## 8.3 Membership Application

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View membership overview | Y | Y | Y | Y | Y | Y | Y | Y |
| Start own application | N | Y | C | N | N | N | N | O |
| Save draft application | N | Y | Y | N | N | N | N | O |
| Resume own draft application | N | Y | Y | N | N | N | N | O |
| Submit own application | N | Y | Y | N | N | N | N | O |
| View own application status | N | C | Y | C | O | N | N | O |
| Provide additional requested info | N | C | Y | N | N | N | N | O |
| Withdraw own application | N | C | Y | N | N | N | N | O |

## 8.4 Membership Review and Member Management

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View application review queue | N | N | N | N | O | N | N | O |
| View full submitted applications | N | N | N | N | O | N | N | O |
| Request more information | N | N | N | N | O | N | N | O |
| Approve application | N | N | N | N | O | N | N | O |
| Reject application | N | N | N | N | O | N | N | O |
| Return application for clarification | N | N | N | N | O | N | N | O |
| View member roster | N | N | N | C | O | N | N | O |
| Change member status | N | N | N | N | C | N | N | O |
| Suspend or restrict member | N | N | N | N | N | C | N | O |
| Assign review ownership | N | N | N | N | O | N | N | O |

## 8.5 Proposal Creation and Proposal Lifecycle

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View proposal index (member-only proposals) | N | N | N | Y | Y | Y | Y | Y |
| View proposal detail | N | N | N | Y | Y | Y | Y | Y |
| Create proposal draft | N | N | N | Y | Y | Y | Y | Y |
| Edit own proposal draft | N | N | N | Y | Y | Y | Y | Y |
| Submit proposal | N | N | N | Y | Y | Y | Y | Y |
| Withdraw own early-stage proposal | N | N | N | C | C | C | C | O |
| View proposal state history | N | N | N | Y | Y | Y | Y | Y |
| Transition proposal from Submitted to UnderReview | N | N | N | N | O | C | N | O |
| Transition proposal to OpenForDiscussion | N | N | N | N | O | C | N | O |
| Return proposal for revision | N | N | N | N | O | C | N | O |
| Mark proposal ReadyForVote | N | N | N | N | O | C | N | O |
| Open proposal voting | N | N | N | N | N | N | N | O |
| Supersede proposal | N | N | N | N | C | C | N | O |
| Resolve proposal manually in exceptional case | N | N | N | N | N | N | N | O |

## 8.6 Proposal Revisions

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View proposal revisions | N | N | N | Y | Y | Y | Y | Y |
| Create new revision of own proposal | N | N | N | Y | Y | Y | Y | Y |
| Submit revision for consideration | N | N | N | Y | Y | Y | Y | Y |
| Compare revisions | N | N | N | Y | Y | Y | Y | Y |
| Accept revision as current | N | N | N | C | O | C | N | O |
| Archive obsolete revision | N | N | N | N | O | C | N | O |

## 8.7 Discussion and Comments

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View member discussion | N | N | N | Y | Y | Y | Y | Y |
| Comment on proposal | N | N | N | Y | Y | Y | Y | Y |
| Reply to comment | N | N | N | Y | Y | Y | Y | Y |
| Edit own comment within allowed window | N | N | N | C | C | C | C | O |
| Delete/withdraw own comment when permitted | N | N | N | C | C | C | C | O |
| Report comment or discussion item | N | N | N | Y | Y | Y | Y | Y |
| Lock discussion thread | N | N | N | N | C | O | N | O |
| Hide/remove comment | N | N | N | N | N | O | N | O |

## 8.8 Voting

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View active votes list | N | N | N | Y | Y | Y | Y | Y |
| View vote detail | N | N | N | Y | Y | Y | Y | Y |
| Cast vote on eligible proposal | N | N | N | C | C | C | C | C |
| Update vote before close if rules allow | N | N | N | C | C | C | C | C |
| View own vote confirmation | N | N | N | Y | Y | Y | Y | Y |
| Open voting window | N | N | N | N | N | N | N | O |
| Close voting window | N | N | N | N | N | N | N | O |
| Certify voting result | N | N | N | N | N | N | N | O |
| Void vote window | N | N | N | N | N | N | N | O |

Note: “Cast vote” is conditional because voting depends on eligibility, proposal state, membership status, and timing.

## 8.9 Outcomes and Authoritative Draft

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View proposal outcome | N | N | N | Y | Y | Y | Y | Y |
| View current authoritative draft | Y/C | Y/C | Y/C | Y | Y | Y | Y | Y |
| Publish/update authoritative draft state | N | N | N | N | N | N | O | O |
| View historic authoritative states | Y/C | Y/C | Y/C | Y | Y | Y | Y | Y |
| Link adopted proposal to authoritative draft update | N | N | N | N | N | N | O | O |

Note: public visibility of the current draft may be public or member-visible depending on policy. That is why some cells are conditional.

## 8.10 Publications

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View public publications | Y | Y | Y | Y | Y | Y | Y | Y |
| Create publication draft | N | N | N | N | N | N | O | O |
| Edit publication draft | N | N | N | N | N | N | O | O |
| Submit publication for review | N | N | N | N | N | N | O | O |
| Publish official item | N | N | N | N | N | N | O | O |
| Unpublish official item | N | N | N | N | N | N | O | O |
| Archive publication item | N | N | N | N | N | N | O | O |

## 8.11 Archive and Records

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View public archive | Y | Y | Y | Y | Y | Y | Y | Y |
| View member-only historic governance records | N | N | N | Y | Y | Y | Y | Y |
| View full internal record details | N | N | N | C | O | O | O | O |
| Search archive | Y/C | Y/C | Y/C | Y | Y | Y | Y | Y |

## 8.12 Moderation

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View moderation queue | N | N | N | N | N | O | N | O |
| Review report | N | N | N | N | N | O | N | O |
| Hide/remove content | N | N | N | N | N | O | N | O |
| Lock discussion | N | N | N | N | C | O | N | O |
| Restrict user participation | N | N | N | N | N | C | N | O |
| Record moderation reason | N | N | N | N | N | O | N | O |

## 8.13 Administration

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View admin dashboard | N | N | N | N | N | N | N | O |
| View all users | N | N | N | N | C | C | N | O |
| Assign/revoke roles | N | N | N | N | N | N | N | O |
| Override exceptional workflow state | N | N | N | N | N | N | N | O |
| Configure system settings | N | N | N | N | N | N | N | O |
| Access full operational search | N | N | N | N | O | O | O | O |

## 8.14 Audit and Activity Visibility

| Action | Public Visitor | Registered User | Applicant | Member | Reviewer | Moderator | Editor | Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| View own visible activity | N | Y | Y | Y | Y | Y | Y | Y |
| View proposal state history | N | N | N | Y | Y | Y | Y | Y |
| View membership decision audit details | N | N | N | N | O | N | N | O |
| View moderation audit details | N | N | N | N | N | O | N | O |
| View full audit log | N | N | N | N | N | N | N | O |

---

# 9. Conditional Permission Rules

Many permissions above are conditional. The most important conditional rules are listed below.

## 9.1 Proposal submission
A user may submit a proposal only if:
- authenticated,
- approved member,
- not suspended/restricted in a way that blocks submission,
- proposal passes validation.

## 9.2 Commenting
A user may comment only if:
- authenticated,
- approved member or otherwise permitted role,
- discussion is open,
- account not restricted from participation.

## 9.3 Voting
A user may vote only if:
- authenticated,
- approved member,
- eligible for that vote under policy,
- proposal is in active vote window,
- vote window open,
- user has not been disqualified or restricted.

## 9.4 Application review
A user may approve/reject membership applications only if:
- they hold reviewer or admin authority,
- the application is in a reviewable state,
- they satisfy any required policy or workflow conditions.

## 9.5 Publication of authoritative text
A user may publish/update authoritative text only if:
- they hold editor or admin authority,
- the source basis for the update is valid,
- publication requirements are satisfied.

## 9.6 Moderation actions
A user may moderate only if:
- they hold moderator or admin authority,
- the relevant content exists and is within scope,
- a reason or basis is recorded where required.

---

# 10. Ownership Rules

Ownership matters for some permissions.

## 10.1 Users may manage their own basic account
Users may edit their own profile/security details, but not platform-assigned roles or statuses.

## 10.2 Proposal authorship grants limited authority, not total authority
Proposal authors may:
- edit their own drafts,
- submit proposals,
- create revisions,
- sometimes withdraw in early stages.

Proposal authors should not automatically be able to:
- force status transitions,
- open voting,
- certify outcomes,
- publish authoritative text.

## 10.3 Comment authors may have limited self-management
Comment authors may edit or withdraw their own comments only within policy-defined limits.

---

# 11. Visibility Model

Permissions should distinguish among four major visibility scopes.

## 11.1 Public
Visible to anyone.

## 11.2 Authenticated
Visible only to signed-in users.

## 11.3 Member-only
Visible only to approved members and authorized operators.

## 11.4 Operator-only
Visible only to reviewers, moderators, editors, administrators, or some subset thereof.

This visibility model should apply consistently across pages, lists, objects, and search results.

---

# 12. UI Guidance Derived From Permissions

The UI should reflect the permission model in the following ways.

## 12.1 Hide inaccessible actions where possible
Users should not constantly see buttons they cannot use.

## 12.2 Explain locked capabilities where helpful
In some cases, it is useful to show a gated action with explanatory copy, such as:
- “Membership required”
- “Voting not yet open”
- “Reviewer access required”

## 12.3 Display current role/status clearly
Users should be able to tell:
- whether they are registered,
- applicant,
- member,
- reviewer,
- moderator,
- editor,
- or admin.

## 12.4 Show reasoned state gating
A user should understand whether they cannot act because of:
- role,
- state,
- timing,
- or policy.

---

# 13. Audit Requirements for Permissioned Actions

The following actions should always generate strong audit records:

- application approval/rejection/return
- member suspension/restriction
- proposal state transitions
- vote open/close/certify/void actions
- publication of authoritative text
- moderation actions
- role assignment/revocation
- admin overrides or exceptional-case interventions

Each audit record should include:
- actor
- action
- target object
- previous state if applicable
- new state if applicable
- timestamp
- reason/note where applicable

---

# 14. MVP Priority Permissions

For the earliest release, the most important permission boundaries to enforce cleanly are:

1. public vs authenticated
2. registered user vs approved member
3. member vs reviewer
4. member vs moderator
5. member vs editor
6. operator roles vs administrator
7. public content vs member governance content
8. proposal participation vs authoritative publication

If these boundaries are weak, the platform’s legitimacy will be weak.

---

# 15. Risks to Avoid

## 15.1 Treating all logged-in users as equivalent
This would destroy the distinction between registration and membership.

## 15.2 Giving authors too much procedural control
Proposal authors should not be able to bypass formal workflow.

## 15.3 Silent operator powers
Elevated actions should be explicit, bounded, and auditable.

## 15.4 Blurred publication authority
Not every member contribution should become public or authoritative content automatically.

## 15.5 Excessively hidden permissions logic
Users should understand why they can or cannot act.

---

# 16. Summary

The permissions model for the Ardtire Society Civic Digital Governance Platform should enforce a clear institutional hierarchy of access and action:

- public access for understanding,
- authenticated access for identity,
- membership-gated access for governance participation,
- specialized operator access for review, moderation, and publication,
- and administrative access for platform control and exceptional-case handling.

This model is essential because the platform’s core legitimacy depends on maintaining clean distinctions among identity, membership, participation, authority, and official publication.
