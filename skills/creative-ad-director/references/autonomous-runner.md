# Automatic progression, checkpoints, and recovery

The instruction layer coordinates available native tools. It cannot install missing host capabilities, force Auto mode, bypass a required user answer, or turn a text-only session into a background service.

## Runner loop

At activation, reconcile the current canvas, artifacts, existing questions, accepted generation jobs, and editor revision. Record available tools for canvas read/write, native Question, image generation, voice/audio preparation and duration measurement, video generation and status, playback/QC, editor, and export. Read any visible Manual/Auto execution setting; explain once if host Manual mode prevents the requested automatic execution. Do not confuse permission to run with permission to answer creative gates.

Persist this logical state (map it to actual host storage, not an invented API):

`project, stage, artifact revisions, gate/question state, per-role voice choices, per-shot readiness/approval, accepted job IDs, actual output handles, audio validation, dependency graph, retry counts, next_action, blocker`

Then repeatedly:

1. Reconcile answers and accepted job results against authoritative state. Deduplicate events by question/job ID plus revision.
2. If a valid answer arrived, record it and unlock the next stage. Execute that stage now; do not end with a proposed next step.
3. If a creative gate is due, save/read back/show its artifacts and issue exactly one native Question. Persist before yielding for its answer.
4. Otherwise prepare eligible assets, validate payloads, submit ready jobs within actual concurrency limits, and poll accepted jobs with the supported wait/status mechanism. Continue independent eligible work; serialize same-scene predecessor dependencies.
5. Inspect actual outputs, update the table, and repair only the smallest failed unit. Advance to the next gate automatically when prerequisites are satisfied.
6. After final approval, run and verify export; only then mark delivered.

Never declare a pending video ready, a prepared file uploaded, or an uploaded file bound without actual evidence. Never ask “continue?” between routine operations already authorized by the latest gate.

## State distinctions

Assets: missing → preparing → ready / failed / stale.
Jobs: not-submitted → submission-uncertain / accepted → running → succeeded / failed.
QC: not-inspected / pass / fail.
Approval: not-requested / pending / approved / rejected / stale.

These are separate axes. A successful job can fail QC, and QC pass is not user approval. Future predecessor outputs may remain declared dependencies in an approved production table; they cannot be dispatched until resolved to ready handles.

## Recover instead of stopping silently

| Failure | Automatic response |
|---|---|
| Invalid parameter / HTTP 400 | Record the actual validation message; inspect offending field and current schema. Correct the payload or asset, then validate before any resubmission. Never replay an unchanged invalid request. For r2v audio use `r2v-audio.md`. |
| Submission timeout / unknown acceptance | Query authoritative task state using saved correlation/job IDs. Do not blindly repeat a potentially charged submission. |
| Asset pending / stale / expired handle | Wait for known preparation or resolve/reimport the same authorized source; verify readiness and update affected bindings. Do not submit placeholder strings. |
| Temporary status/network failure | Retry read-only reconciliation with bounded backoff; retain accepted IDs. A timeout is not generation failure. |
| Failed output / wrong voice / dialogue truncated | Inspect the actual unit, repair the mapped input/timing or smallest affected range, and recheck dependent transitions. Keep passed work. |
| Question creation timeout / missing answer | Reconcile the existing card and exact revision; wait for real input. Do not auto-approve or create duplicates. |
| Artifact write failure | Reconcile by ID, patch/retry the affected write, then read back. Do not seek approval on an unsaved artifact as if it existed. |
| Editor/export failure | Reconcile saved timeline/export job first; fix affected media/track/output only. Keep the approved source cut. |

Limit automatic corrective generation to two additional attempts per failure signature within the authorized scope. After that, save the exact blocker and use a native Question with concrete alternatives if the user can resolve it. Missing native Question capability is a host blocker, not permission to emulate it in chat. A waiting answer/job, explicit pause, actual capability blocker, or verified delivery are the only legitimate boundaries; ordinary internal step completion is not.

## Revision invalidation

Script changes invalidate affected lines, shot rows, prompts, clips, and edits; unchanged character identity can be reused. Appearance changes invalidate dependent visual shots, not unrelated voices. Voice changes invalidate that role's derived reference excerpts, final lines, dependent audio/video, and affected edit spans, not other roles. A changed predecessor ending invalidates only dependent continuation units. Return to the earliest affected review gate and then resume forward without restarting the project.
