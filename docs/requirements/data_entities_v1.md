# data_entities_v1.md

# Ardtire Society Civic Digital Governance Platform
## Data Entities v1

## Document Status

- Version: v1
- Purpose: define the recommended core data entities for the platform
- Scope: logical entity inventory, field recommendations, relationships, and lifecycle relevance
- Audience: architects, engineers, API designers, database designers, QA, and product planners

---

# 1. Purpose of This Document

This document defines the recommended core data entities for the Ardtire Society Civic Digital Governance Platform.

Its purpose is to translate the platform’s domain model into a practical inventory of the data-bearing objects the system should likely persist and operate upon.

This is not yet a final relational schema or API contract. It is a structured entity design document intended to answer:

- What major entities should exist?
- What fields or field groups do they need?
- How do they relate to one another?
- Which entities are active workflow objects versus reference or record objects?
- Which entities are MVP-critical?

---

# 2. Entity Design Principles

## 2.1 Entities should correspond to real platform meaning

If a concept has meaningful lifecycle, permissions, relationships, or institutional importance, it should usually have its own entity.

## 2.2 Do not collapse distinct concepts for convenience

The model should keep separate:
- user versus membership,
- proposal versus proposal revision,
- proposal versus outcome,
- authoritative draft state versus publication item,
- moderation event versus audit event.

## 2.3 State-bearing entities should make state explicit

Workflow state should not live only in UI assumptions or scattered booleans.

## 2.4 Record preservation matters

Where institutional history matters, record entities should preserve prior states or prior versions rather than overwriting them destructively.

## 2.5 Identity, ownership, and timestamps are foundational

Nearly every important entity should carry:
- stable identifier,
- created/updated timestamps,
- actor references where meaningful,
- status/state,
- and audit/event relationships where appropriate.

---

# 3. Entity Categories

The platform’s entities can be grouped into the following categories:

1. Identity and access entities
2. Membership entities
3. Governance entities
4. Voting and outcome entities
5. Authoritative text and publication entities
6. Moderation entities
7. Audit and activity entities
8. Notification entities
9. Supporting reference entities

---

# 4. Identity and Access Entities

# 4.1 User

## Purpose
Represents the core person/account identity in the platform.

## Suggested fields

### Identity fields
- id
- username
- email
- display_name
- legal_name_or_formal_name_optional
- bio_optional

### Status fields
- access_status
- is_email_verified
- is_active
- is_deactivated

### Timestamps
- created_at
- updated_at
- last_login_at_optional

### Relationship fields
- primary_membership_record_id_optional

## Notes
The User entity is not the same as Member. Membership should remain its own domain concept.

---

# 4.2 UserRoleAssignment

## Purpose
Represents elevated or specialized role assignment for a user.

## Suggested fields
- id
- user_id
- role_type
- assigned_by_user_id
- assigned_reason_optional
- assigned_at
- revoked_at_optional
- is_active

## Notes
This should support roles such as:
- reviewer
- moderator
- editor
- administrator

---

# 4.3 UserSession

## Purpose
Represents authenticated session context.

## Suggested fields
- id
- user_id
- session_token_or_reference
- created_at
- expires_at
- last_seen_at
- revoked_at_optional
- device_or_client_metadata_optional

## Notes
Implementation may vary, but the conceptual entity is still useful.

---

# 4.4 UserProfilePreference

## Purpose
Stores user-specific preferences relevant to UX and notifications.

## Suggested fields
- id
- user_id
- notification_preferences_json
- display_preferences_json
- timezone_optional
- created_at
- updated_at

---

# 5. Membership Entities

# 5.1 MembershipApplication

## Purpose
Represents an application by a registered user to become a Society member.

## Suggested fields

### Core identity
- id
- applicant_user_id
- application_state

### Content
- application_payload_json_or_structured_fields
- applicant_statement_optional
- supporting_information_optional

### Review fields
- current_reviewer_user_id_optional
- more_info_request_note_optional
- decision_reason_optional

### Timestamps
- started_at
- submitted_at_optional
- decision_at_optional
- withdrawn_at_optional
- created_at
- updated_at

## Notes
This is a workflow entity and should be preserved historically.

---

# 5.2 MembershipApplicationRevision

## Purpose
Represents versioned application content over time where draft/resubmission history matters.

## Suggested fields
- id
- membership_application_id
- revision_number
- payload_snapshot
- created_by_user_id
- created_at
- is_current

## Notes
Optional for strict MVP if simpler draft storage suffices, but valuable if application history matters.

---

# 5.3 MembershipDecision

## Purpose
Represents a formal review decision or decision event on a membership application.

## Suggested fields
- id
- membership_application_id
- decision_type
- decided_by_user_id
- decision_reason_optional
- decision_note_optional
- decided_at
- related_rule_or_policy_reference_optional

## Notes
This helps separate the application object from discrete decision events.

---

# 5.4 MembershipRecord

## Purpose
Represents the user’s status as a Society member after approval and over time.

## Suggested fields
- id
- user_id
- membership_status
- admitted_at_optional
- suspended_at_optional
- restricted_at_optional
- terminated_at_optional
- current_status_reason_optional
- created_at
- updated_at

## Notes
This is the durable representation of membership standing, separate from the application workflow.

---

# 5.5 MembershipStatusHistory

## Purpose
Preserves changes to a user’s membership standing over time.

## Suggested fields
- id
- membership_record_id
- previous_status
- new_status
- changed_by_user_id
- change_reason_optional
- changed_at

---

# 6. Governance Entities

# 6.1 Proposal

## Purpose
Represents a formal governance or constitutional proposal moving through workflow.

## Suggested fields

### Identity and authorship
- id
- proposal_number_or_slug_optional
- title
- summary
- rationale_optional
- author_user_id
- submitting_user_id_optional

### Workflow
- proposal_state
- category
- current_revision_id_optional
- discussion_state
- current_vote_window_id_optional
- current_outcome_id_optional

### Relationship/context
- affected_domain_optional
- parent_proposal_id_optional
- superseded_by_proposal_id_optional

### Timestamps
- drafted_at_optional
- submitted_at_optional
- resolved_at_optional
- withdrawn_at_optional
- created_at
- updated_at

## Notes
Proposal is the central governance entity.

---

# 6.2 ProposalRevision

## Purpose
Represents a version of proposal text and related structured content.

## Suggested fields
- id
- proposal_id
- revision_number
- revision_state
- title_snapshot
- summary_snapshot
- rationale_snapshot_optional
- body_text_or_structured_content
- revision_note_optional
- created_by_user_id
- created_at
- accepted_as_current_at_optional
- archived_at_optional
- is_current

## Notes
This should preserve the drafting record over time.

---

# 6.3 ProposalStateTransition

## Purpose
Stores explicit lifecycle movement of a proposal.

## Suggested fields
- id
- proposal_id
- previous_state
- new_state
- transitioned_by_user_id
- transition_reason_optional
- rule_reference_optional
- transitioned_at

## Notes
This is extremely valuable for auditability and timeline reconstruction.

---

# 6.4 ProposalRelationship

## Purpose
Represents links among proposals such as supersession, merge, dependency, or related subject matter.

## Suggested fields
- id
- from_proposal_id
- to_proposal_id
- relationship_type
- note_optional
- created_by_user_id_optional
- created_at

---

# 6.5 ProposalWatcher

## Purpose
Represents a user following a proposal for notifications or dashboard relevance.

## Suggested fields
- id
- proposal_id
- user_id
- created_at

---

# 6.6 ProposalTagOrClassification

## Purpose
Represents classification labels or categories for proposals.

## Suggested fields
- id
- label
- description_optional
- classification_type
- created_at

---

# 6.7 ProposalToClassification

## Purpose
Many-to-many join between proposals and classifications.

## Suggested fields
- id
- proposal_id
- classification_id

---

# 6.8 DiscussionThread

## Purpose
Represents the discussion space associated with a proposal or other governed object.

## Suggested fields
- id
- related_object_type
- related_object_id
- discussion_state
- opened_at_optional
- locked_at_optional
- archived_at_optional
- created_at
- updated_at

## Notes
For MVP, discussion may effectively be one thread per proposal.

---

# 6.9 Comment

## Purpose
Represents a discussion contribution inside a thread.

## Suggested fields
- id
- thread_id
- author_user_id
- parent_comment_id_optional
- body
- comment_state
- is_edited
- created_at
- updated_at
- deleted_or_hidden_at_optional

## Notes
Comment state may distinguish active, hidden, removed, archived, etc.

---

# 6.10 CommentEditHistory

## Purpose
Preserves prior versions of comment text when edit history is desired.

## Suggested fields
- id
- comment_id
- prior_body
- edited_by_user_id
- edited_at

---

# 7. Voting and Outcome Entities

# 7.1 VoteWindow

## Purpose
Represents a formal voting event associated with a proposal.

## Suggested fields
- id
- proposal_id
- vote_window_state
- opens_at
- closes_at
- opened_by_user_id_optional
- closed_by_user_id_optional
- certified_by_user_id_optional
- voided_by_user_id_optional
- void_reason_optional
- rule_reference_optional
- created_at
- updated_at

## Notes
This is distinct from the ballots cast within it.

---

# 7.2 VoteEligibilitySnapshot

## Purpose
Represents the eligible voting population or eligibility basis for a vote window.

## Suggested fields
- id
- vote_window_id
- eligibility_basis_type
- eligibility_snapshot_json
- created_at

## Notes
This is useful if eligibility must be historically reconstructable.

---

# 7.3 Ballot

## Purpose
Represents a user’s vote/ballot in a vote window.

## Suggested fields
- id
- vote_window_id
- voter_user_id
- ballot_state
- choice_value
- choice_payload_optional
- cast_at_optional
- updated_at_optional
- locked_at_optional
- invalidated_at_optional
- invalidation_reason_optional
- current_effective_version_number_optional

## Notes
Uniqueness rules should prevent duplicate effective ballots per user per vote window.

---

# 7.4 BallotHistory

## Purpose
Preserves changes to a ballot if vote updates are allowed before close.

## Suggested fields
- id
- ballot_id
- prior_choice_value
- new_choice_value
- changed_at
- changed_by_user_id_or_system

---

# 7.5 VoteTally

## Purpose
Represents computed result totals for a closed vote window.

## Suggested fields
- id
- vote_window_id
- total_eligible_count_optional
- total_cast_count
- total_valid_count
- total_invalid_count
- result_breakdown_json
- computed_at
- computed_by_system_version_optional

---

# 7.6 ProposalOutcome

## Purpose
Represents the formal outcome of a proposal.

## Suggested fields
- id
- proposal_id
- outcome_type
- vote_window_id_optional
- outcome_summary_optional
- outcome_reason_optional
- rule_reference_optional
- decided_or_certified_by_user_id_optional
- outcome_at
- created_at

## Notes
This is intentionally separate from proposal state.

---

# 7.7 OutcomeCertification

## Purpose
Represents formal certification or confirmation of an outcome.

## Suggested fields
- id
- proposal_outcome_id
- certified_by_user_id
- certification_note_optional
- certified_at

---

# 8. Authoritative Text and Publication Entities

# 8.1 AuthoritativeDraftState

## Purpose
Represents a snapshot/version of the current authoritative constitutional or governance drafting state.

## Suggested fields
- id
- version_number_or_label
- title_optional
- body_text_or_structured_document
- state
- based_on_outcome_id_optional
- supersedes_draft_state_id_optional
- published_as_current_at_optional
- superseded_at_optional
- created_by_user_id_optional
- created_at
- updated_at

## Notes
Only one should typically be current.

---

# 8.2 AuthoritativeDraftSectionOptional

## Purpose
Represents section-level storage if the drafting model is structured by articles/sections rather than monolithic text.

## Suggested fields
- id
- authoritative_draft_state_id
- section_key
- section_title
- section_body
- ordering_index
- created_at
- updated_at

## Notes
Optional but likely useful if the constitution is modeled structurally.

---

# 8.3 PublicationItem

## Purpose
Represents public or official published content.

## Suggested fields
- id
- publication_type
- title
- slug
- summary_optional
- body
- publication_state
- visibility_scope
- author_or_editor_user_id_optional
- published_at_optional
- archived_at_optional
- created_at
- updated_at

---

# 8.4 PublicationRevision

## Purpose
Represents revisions to a publication item.

## Suggested fields
- id
- publication_item_id
- revision_number
- body_snapshot
- title_snapshot
- changed_by_user_id
- created_at
- is_current

---

# 8.5 PublicPageOptional

## Purpose
Represents structured public site pages such as About, Participation, Governance, etc.

## Suggested fields
- id
- page_key
- title
- slug
- body
- page_state
- visibility_scope
- created_at
- updated_at

---

# 9. Archive and Record Entities

# 9.1 RecordTimelineEvent

## Purpose
Represents a normalized historical event usable in archive/timeline views.

## Suggested fields
- id
- related_object_type
- related_object_id
- event_type
- title_or_summary
- occurred_at
- actor_user_id_optional
- metadata_json

## Notes
Useful for cross-object institutional history views.

---

# 9.2 ArchiveEntryOptional

## Purpose
Represents a curated or indexed archive object.

## Suggested fields
- id
- related_object_type
- related_object_id
- archive_category
- archive_summary_optional
- visibility_scope
- archived_at
- created_at

---

# 10. Moderation Entities

# 10.1 ModerationReport

## Purpose
Represents a user-submitted or system-generated moderation issue.

## Suggested fields
- id
- report_state
- reported_by_user_id_optional
- target_object_type
- target_object_id
- report_reason_type
- report_note_optional
- assigned_moderator_user_id_optional
- created_at
- updated_at
- resolved_at_optional

---

# 10.2 ModerationAction

## Purpose
Represents a concrete moderation action taken in response to a report or issue.

## Suggested fields
- id
- moderation_report_id_optional
- target_object_type
- target_object_id
- action_type
- reason_note_optional
- taken_by_user_id
- taken_at

---

# 10.3 ParticipationRestriction

## Purpose
Represents a restricted participation condition applied to a user.

## Suggested fields
- id
- user_id
- restriction_type
- applies_to_scope
- reason_optional
- starts_at
- ends_at_optional
- imposed_by_user_id
- created_at

---

# 11. Audit and Activity Entities

# 11.1 AuditEvent

## Purpose
Represents a durable record of a meaningful system or operator action.

## Suggested fields
- id
- event_type
- actor_user_id_optional
- target_object_type
- target_object_id
- previous_state_optional
- new_state_optional
- reason_optional
- metadata_json_optional
- occurred_at

## Notes
This is a cross-cutting entity and should be heavily used.

---

# 11.2 ActivityFeedEvent

## Purpose
Represents a user-facing activity item, distinct from deep audit logging.

## Suggested fields
- id
- audience_scope
- related_object_type
- related_object_id
- summary
- created_at

## Notes
This may be derived from domain events rather than primary stored data in some architectures.

---

# 12. Notification Entities

# 12.1 Notification

## Purpose
Represents a user-facing notification generated from workflow events.

## Suggested fields
- id
- recipient_user_id
- notification_type
- title
- body_or_summary
- related_object_type_optional
- related_object_id_optional
- delivery_state
- read_at_optional
- created_at

---

# 12.2 NotificationPreference

## Purpose
Represents a user’s preferences for notification categories or channels.

## Suggested fields
- id
- user_id
- preference_key
- enabled
- channel_type_optional
- created_at
- updated_at

---

# 13. Supporting Reference Entities

# 13.1 RuleReferenceOptional

## Purpose
Represents a versioned procedural rule or policy reference used by outcomes or transitions.

## Suggested fields
- id
- rule_type
- rule_key
- version_label
- summary_optional
- definition_json_or_text
- effective_from_optional
- effective_to_optional
- created_at

## Notes
This is strongly recommended, especially if the platform later versions quorum, thresholds, or eligibility rules.

---

# 13.2 CategoryReference

## Purpose
Represents structured categories for proposals, publications, or other objects.

## Suggested fields
- id
- domain_type
- key
- label
- description_optional
- created_at

---

# 13.3 VisibilityScopeReferenceOptional

## Purpose
Represents allowed visibility scopes such as public, authenticated, member-only, operator-only.

## Suggested fields
- id
- key
- label
- description_optional

---

# 14. Relationship Highlights

Below are the most important relationships.

## Identity and membership
- User 1 -> many MembershipApplications
- User 1 -> 0..1 current MembershipRecord
- MembershipRecord 1 -> many MembershipStatusHistory
- User 1 -> many UserRoleAssignments

## Governance
- User 1 -> many Proposals as author
- Proposal 1 -> many ProposalRevisions
- Proposal 1 -> many ProposalStateTransitions
- Proposal 1 -> 1 DiscussionThread
- DiscussionThread 1 -> many Comments

## Voting
- Proposal 1 -> 0..many VoteWindows
- VoteWindow 1 -> many Ballots
- VoteWindow 1 -> 0..1 VoteTally
- Proposal 1 -> 0..many ProposalOutcomes

## Authoritative text
- ProposalOutcome 0..1 -> may lead to 1 AuthoritativeDraftState
- AuthoritativeDraftState 1 -> 0..many AuthoritativeDraftSections optional

## Publication
- PublicationItem 1 -> many PublicationRevisions

## Moderation and audit
- ModerationReport 1 -> 0..many ModerationActions
- Almost any entity -> many AuditEvents

---

# 15. MVP-Critical Entities

For the earliest credible version, the most important entities are:

- User
- UserRoleAssignment
- MembershipApplication
- MembershipDecision
- MembershipRecord
- Proposal
- ProposalRevision
- ProposalStateTransition
- DiscussionThread
- Comment
- VoteWindow
- Ballot
- VoteTally
- ProposalOutcome
- AuthoritativeDraftState
- PublicationItem
- ModerationReport
- ModerationAction
- AuditEvent
- Notification

These should be treated as foundational.

---

# 16. Optional but Strongly Recommended Early Entities

Even if not all are implemented fully on day one, these are very valuable:

- MembershipStatusHistory
- VoteEligibilitySnapshot
- OutcomeCertification
- PublicationRevision
- RecordTimelineEvent
- NotificationPreference
- RuleReference

---

# 17. Suggested Common Field Conventions

Across major entities, it is recommended to standardize:

## Common identity fields
- id

## Common lifecycle fields
- state or status
- created_at
- updated_at

## Common authorship/actor fields
- created_by_user_id_optional
- updated_by_user_id_optional where useful

## Common archival fields
- archived_at_optional
- deleted_at_optional only if soft-delete policy exists

## Common visibility fields
- visibility_scope_optional

This consistency will help later API and admin tooling.

---

# 18. Entity Risks to Avoid

## 18.1 Overloading User with membership data
Keep user identity separate from membership record.

## 18.2 Storing proposal text only on Proposal without revisions
This would weaken drafting history.

## 18.3 Treating outcomes as only a proposal status field
A separate outcome entity is much stronger for auditing and reporting.

## 18.4 Collapsing authoritative text into publication items
Current authoritative drafting state deserves a distinct model.

## 18.5 Using comments as a catch-all event model
Discussion entities and audit entities should remain separate.

---

# 19. Summary

The platform should be built around a deliberate set of structured entities that reflect its real civic and institutional logic.

At minimum, those entities must support:

- user identity,
- membership progression,
- proposal drafting and workflow,
- discussion,
- voting,
- outcomes,
- authoritative draft state,
- publication,
- moderation,
- audit,
- and notifications.

This entity model provides the foundation for later schema design, API contracts, admin tooling, and stateful workflow implementation.
