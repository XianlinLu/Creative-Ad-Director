# Character, voice, and reference preparation

Read before making assets, reviewing asset readiness, or binding references for generation.

## Prepare only what the selected story needs

- `PM01`: canonical product/SKU and only evidenced use states.
- `WM01`: optional neutral white-model sheet for geometry and staging; unknown finish or mechanics remain unknown.
- `CH01…`: original character appearance sheets with face/hair, age range, body proportions, wardrobe, accessories, scale, and useful views. For a recurring role, keep one revision across shots.
- `VO01…`: independent voice asset for each speaking character or narrator. Record language/accent, vocal range, timbre, pace, emotional range, pronunciation, and associated character ID. Create a short playable audition with representative dialogue before final voice binding. Use actual authorized voice inputs; descriptive voice prompts alone are not an audition or a bound voice.
- `SC01…` and `PR01…`: necessary scene geography and props. Maintain entrances, character positions, eyelines, product placement, and light direction.

Do not create characters or voices for a product-only silent concept. If a required voice tool or reference port is absent, mark that dependency blocked and continue independent visuals/script work. Offer a supported separate voice track or another explicit production choice; do not claim a character image locks voice identity. Separately produced speech is not automatically lip-synced.

## Asset Register

| Asset ID | Type / role | Source and evidence | Revision | Lifecycle status | Actual native handle | Inspection / audition | Approval scope | Allowed use / unknowns |
|---|---|---|---|---|---|---|---|---|

Use lifecycle states `missing → preparing → ready`, with `failed` for unsuccessful preparation and `stale` when dependencies change. A real accessible output plus visual inspection or audible audition is required for `ready`. Track approval and binding separately: approval does not make an upload ready, and readiness does not mean the generation task used it. Revalidate a handle whose asset was deleted, replaced, or became inaccessible.

For a still product photograph, register only the visible state. A sealed package does not prove the lid's mechanism, inner cream/paste, dispensing behavior, or efficacy. User confirmation can resolve specifications, but exact movement/texture reconstruction still needs inspectable evidence. A generated white model cannot become independent evidence for its own invented surfaces.

## First-appearance binding

After the selected timeline is stable:

1. List the first visual appearance or first audible entrance of every reference-dependent entity using global time and shot ID.
2. Assign a stable first-use order; for simultaneous entrances, use the written shot-table entity order as the tie-breaker. Keep semantic IDs separate from numbered reference slots.
3. Map this order to actual exposed image/video/audio ports. Where the tool has separate modality lists, preserve first-use order within each list and retain the global ordering in the manifest. Voice enters at first speech, not automatically at the character's first visual appearance.
4. Confirm every required asset is ready, current, and authorized for its role. Bind actual handles through real tool parameters or observed UI attachments. Mentioning `PM01` or “reference image 1” in prompt text is not a binding.
5. Inspect the assembled request before submission and record accepted payload/attachments when exposed. If execution details are unavailable, record the submitted bindings as such; do not invent provider confirmation.

| Order | First global time / shot | Entity / purpose | Asset ID + revision | Native handle | Actual port / slot | Job ID | Binding evidence / status |
|---|---|---|---|---|---|---|---|

An extension may need a source-video port plus reattached references; follow its actual schema. Do not reset or omit voice/product identity merely because the base clip exists. If shot order changes, recompute affected slot mappings before submitting the changed request. Keep each submitted manifest revision immutable for traceability.
