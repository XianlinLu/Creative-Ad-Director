# Production master table, generation, and editable delivery

Read after G4 audition approval and before G5. Use `assets-and-voices.md` for separate visual/voice assets, `shot-prompt-compiler.md` for prompt construction, `model-routing.md` for supported units, and `r2v-audio.md` for every outgoing audio payload.

## Measure before allocating shots

Synthesize exact approved lines using each approved voice and measure real audio. Auditions establish identity; they are not the final film's dialogue. Preserve speaker/listener motivation, reaction time, breaths, and joke pauses. Derive film duration from this rhythm unless the user gave a fixed duration; do not arbitrarily compress the script into 15 seconds.

Prepare required starting frames/storyboard boards using approved character turnarounds and actual product/prop/scene references. Keep the final-video ratio distinct from 16:9 character-sheet ratio. If a production unit does not need a board, state why and identify its actual conditioning sources instead of leaving an unexplained blank.

## 镜头生产总表 / Shot Production Master Table

Save one scene heading and table per scene plus an overall ordered index. This is the execution ledger, not just a synopsis. It includes:

| Column | Required content |
|---|---|
| Scene / shot / generation unit | Stable IDs and source script rows/line IDs; exact merge coverage |
| Board / starting frame | Real current handle/revision or explicit not-needed reason |
| Timing | Measured final speech, action/reaction allowance, unit/shot duration, continuous global start/end, local integer intervals where required |
| Rhythm / editorial map | Rhythm Map revision and beat ID; narrative job; editorial duration distinct from generation duration; trigger/reveal/result time; minimum reaction hold; cut cue; heading in/out; sound marker evidence status |
| Picture and blocking | Who/what is where; expression, action, eyeline, props, product use state, opening/ending state |
| Camera and format | Shot size, angle/motion, final ratio, resolution, safe areas |
| Exact speech | Speaker → listener; exact dialogue/VO, performance and reaction; silent if none |
| Sound | Voice identity, final line audio and duration, effects, ambience, music handling, editor-only narration where applicable |
| Text | Exact editable captions, offer, CTA, qualifiers/disclosures and readable dwell |
| Product evidence | Source IDs and permitted demonstrated states/claims |
| Locked inputs | Character/product/prop/scene image revisions, approved audition VO, selected VR and/or DL handles, actual ports/slots and measured audio sum |
| Dependencies and mode | New-scene base / same-scene continuation / supported standalone unit; predecessor ID and resolved handle when ready; model/version; audio route |
| Full generation prompt | Complete source-faithful local-timeline prompt, not a short label |
| Preparation and job state | Missing/preparing/ready; not-submitted/submission-uncertain/accepted/running/succeeded/failed; actual task/output IDs |
| Review | QC per people/product/space/sound/text; user approval per shown output revision; repair notes |

No table row may claim ready while essential handles or measured audio durations are missing. Future predecessor outputs may be explicitly unresolved dependencies while the overall plan is approved; only resolved rows can dispatch. Read back every scene table and the overall coverage before G5. G5 authorizes production scope; it does not approve future video quality.

## Dispatch and monitor automatically

After G5 approval, submit eligible rows without another “continue?” question. Preflight real supported parameters, required references, audio limits, line coverage, duration, aspect ratio and resolution. Record actual payload/bindings and accepted task IDs. Same-scene continuation waits for a real inspected predecessor and binds its video first. Independent scenes may proceed within tool concurrency/cost constraints.

Observe tasks with actual status/wait operations. A queue acknowledgment is not a playable clip. Reconcile unknown acceptance before retry; fix parameter errors before any new submission. Follow bounded recovery in `autonomous-runner.md`. On completion inspect playback, prepared sound, and all five QC dimensions. Preserve passed assets and repair only affected shots/dependencies. Do not multiply unrequested variants.

## G6 prepared-shot review

Before showing a shot for native G6, remove unintended model music while preserving intended speech/effects/ambience through actual supported audio tools. Muting the whole mixed track is not a valid music-removal technique when it removes required dialogue. If separation is unavailable, regenerate with supported sound controls or reconstruct approved dialogue/effects on separate tracks and verify; escalate only the genuinely blocked choice through a native Question.

Show actual playable current clips, not just contact sheets. Record the exact shot/revision approved. A batch card may list several reviewable shots explicitly, but never unseen future results. Rejected clips return to targeted repair and G6. Pending independent work may continue within authorized scope without making the user type more instructions.

## G7 / native Video Editor

When required shots are approved, collect the finishing choice through G7 unless already specified. Reuse/create the actual editor project, read its latest state, preserve user changes and unrelated locked tracks, then:

1. Import ready approved assets and confirm actual media availability.
2. Assemble in approved global order with explicit source ranges. Determine extension-only versus cumulative video to avoid duplicating earlier footage. New scenes are assembled as approved; do not claim those cuts are native extension.
3. Keep dialogue, effects/ambience, final music, captions and exact product/offer/CTA text on separate supported tracks. Do not replace native speech with another voice accidentally or double it with a second dialogue track.
4. Apply requested music treatment; duck it under speech and retain comic pauses. Use observed playback/waveform timing, not invented BPM.
5. Generate captions from final actual dialogue timing and recalculate after trims/module swaps. Check readable dwell, safe areas, typography and spelling at phone size.
6. Save and play the full revision with sound, inspect every transition and final frame, then present native G8.

Apply [reference-rhythm.md](reference-rhythm.md) to the actual edit: trim independently framed inserts from longer generated clips, retain readable demonstration results, and slow the emotional ending. Save actual source-in/out and timeline cuts against the approved Rhythm Map. Use actual supported editor precision; native integer generation durations must not quantize final cuts. Check heading timing separately from dialogue captions and distinguish verified audio accents from proposed sound design. Show rhythm deviations with the existing G8 preview and repair only affected spans.

For captions-only finishing, operate on an existing assembled timeline. If none exists, ask the native finishing choice to resolve the mismatch rather than delivering disconnected captioned shots as a completed film.

## G8 → verified export

A returned confirm/export answer immediately starts native export of the shown revision. Local revision requests use native options and preserve unrelated tracks. Revision changes invalidate only affected final approval; show the updated full preview before exporting it.

Verify actual playable/downloadable media, duration, ratio, resolution, complete approved shot coverage, correct speaker voices, captions, required text, sound effects and music. Return the file and actual editable draft, evidence sheet, production table, binding manifest and QC log where available. A queued export, expired link, invented filename, or screenshot of a timeline is not delivery. No publishing or ad-spend changes without explicit authorization.
