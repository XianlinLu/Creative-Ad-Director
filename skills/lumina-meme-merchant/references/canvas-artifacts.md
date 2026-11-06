# Canvas artifacts and native decisions

Use this reference on activation, resume, before any Question card, and after a sync or task error.

## Artifact first

Before asking a creative question, save a useful editable result on the canvas. At minimum, an early run must produce:

1. **Product Evidence Sheet vN** with sources, verified facts, unknowns, and claim risks.
2. **Merchant Brief vN** with objective, audience, channel, duration/ratio, offer, CTA, constraints, and assumptions.
3. **Creative Board vN** with three distinct directions and the first three provisional shots of the recommendation.

Read back each saved artifact. A blank node, chat-only plan, card body, task acknowledgment, or future-tense update is not an artifact. If canvas writing fails after bounded reconciliation, show a clearly labeled unsaved fallback in chat and retain the write blocker; it cannot receive canvas artifact approval.

On resume, reuse the most advanced valid artifact and stable IDs. Do not rebuild approved work merely to follow the beginning of the workflow.

## Stable IDs and versioning

Use human-readable IDs that survive revisions:

- concept: `C01`, `C02`, `C03`
- product master: `PM01`
- white model: `WM01`
- actor/hand model: `AM01`
- shot: `S01`, `S02`...
- hook: `H-A`, `H-B`, `H-C`
- payoff: `P-A`, `P-B`
- CTA: `CTA-A`, `CTA-B`
- edit/export: `ED-vN`, `EXP-vN-<variant>`

Store current revision, source revisions, approval state, actual native handles, accepted job IDs, status, and next eligible action. Node creation, job acceptance, output readiness, technical QC, creative approval, editor preview, and final export are distinct states.

## Native decision gates

Cards contain a concise artifact locator and decision controls, not the artifact body.

### Creative Direction Review

Show the actual evidence sheet, brief, creative board, and first-three-shot draft first.

- Use recommended direction
- Choose another shown direction
- Request a targeted change

### Product and Visual Lock Review

Show every applicable actual product master, white model, cast/hand model, scene reference, and key prop.

- Approve shown assets
- Revise a named asset
- View again

### Ad Production Review

Save/read back the full timed script, claim map, variant manifest, and complete shot table; show all boards.

- Approve and generate
- Revise a shot, line, or claim
- View again

### Final Edit Review

Show the actual playable current editor revision, text/disclosure state, and variant manifest.

- Approve and export
- Request changes
- Preview again

After `Request changes`, collect native text/Other identifying shot or timecode, issue, and desired result. An empty “change” choice is not an edit instruction. Reuse the same editor draft, save a new revision, and review it again.

## Loop and recovery rules

- Do not spend two consecutive decision turns gathering optional information without creating or materially improving a canvas artifact. On the second potential loop, use reversible defaults and draft the recommendation.
- Reconcile an uncertain card submission or generation acceptance with authoritative read-only state before retrying. Never replay a click or duplicate a potentially paid task because a toast or timeout was ambiguous.
- Keep product, canvas, session, and editor state scoped to the current project. Do not leak another project's product, offer, cast, references, prompt variables, or pending approvals.
- A failure affects only its dependent chain. Preserve unrelated approved assets and ready variants.
- Persist before waiting. If the host cannot resume background work automatically, state that capability limit once and leave an exact checkpoint.
