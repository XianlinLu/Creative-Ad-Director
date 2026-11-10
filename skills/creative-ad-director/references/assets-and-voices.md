# Appearance, voice audition, and production audio

Read after script approval and before any asset generation/binding. Follow the separate G2 visual, G3 voice-preference, and G4 audition gates in `canvas-artifacts.md`.

## Visual preparation

Extract visible characters, including identified non-speaking roles, from the approved screenplay. Generate one **16:9 landscape three-view sheet per character**, with front, side, and back views, full-body framing where appropriate, consistent face/hair/body/wardrobe/accessories/scale, neutral background, and coherent lighting. The sheet ratio is independent of the final film's ratio. Inspect all three views; three unrelated people do not satisfy a turnaround. Preserve originals and version edits under the same character ID.

Prepare `PM` product references with evidenced states, optional `WM` white-model geometry, `PR` important props and `SC` scene layouts only as needed. An off-screen narrator has no visual sheet unless the story actually depicts them. Do not add an extra character just to attach a voice.

Await and show actual ready visuals before G2. Only after visual approval move to G3. Do not combine appearance and voice approval into one early gate.

## Voice preference → audition → production

1. **G3 choice per speaking role:** associate the approved character sheet where available. Offer 2–3 specific voice directions with timbre, perceived age, accent/language, pace, performance, pronunciation needs, and a brief reason. A native custom path may refine them. The image informs creative fit but does not mechanically encode a voice.
2. **Audition `VO`:** after selection, generate about 20 seconds of actual clean speech, no music or effects. Use meaningful sample text with enough connected speech to hear identity, pronunciation, and emotional range; do not fill 20 seconds with silence. Inspect/play it and record actual duration. The narrator is a separate role.
3. **G4 approval:** present playable role-labeled auditions. Replay reuses the existing asset. Revise only the selected role, then present its new audition. Never equate a chosen voice description with approval of unheard audio.
4. **Final lines `DL`:** synthesize the screenplay's exact dialogue/VO using the approved voice, through a real voice ID or supported reference-audio mechanism. Record speaker, listener, script line IDs, delivery, actual audio handle, measured duration, pauses, and revision. Do not insert audition test text into the film.
5. **Reference excerpts `VR`:** derive short clean identity-preserving spoken excerpts from approved auditions for shot-level conditioning. Select natural phrase boundaries and keep a source time range and checksum/revision. These are not final lines and must not be pasted onto the film's soundtrack. Validate actual prepared-file durations using `r2v-audio.md` before binding.

If a tool supports voice-reference audio only, bind a valid VR excerpt and the shot's exact dialogue text. If it supports dialogue-driven/lip-sync audio, bind the actual DL asset to that documented input. If both are needed, count every attached audio entry in the request total. Do not confuse a generic audio-reference slot with a lip-sync or speaker-routing capability. If the required mechanism is unavailable, use a native Question for a supported alternative. Separate narration in the editor is allowed when specified in the approved table; it is not native r2v conditioning.

For multi-speaker units, map every line to its own character/narrator and approved voice. Bind only speakers audible in that unit; a visible silent character needs its image but no audio reference. Preserve line timing and listener reactions. Never use one role's voice for another merely to fit the audio budget.

## Asset Register and readiness

| Semantic ID / role | Kind (CH/PM/PR/SC/VO/VR/DL) | Source / range / revision | Lifecycle | Actual native handle | Inspected / audible | Measured duration if audio | Approval provenance | Allowed usage |
|---|---|---|---|---|---|---|---|---|

`missing → preparing → ready`, plus `failed` and `stale`. Readiness requires actual accessible output and relevant inspection. Approval, readiness, and binding are separate facts. Only verified ready current handles may be submitted. An expired handle must be resolved/reuploaded through a supported tool and revalidated, not replaced with its semantic ID.

Product packshots authorize only visible states: no guessed opening mechanics, inner cream/paste, liquid flow, exact finish, or efficacy. White-model renders do not establish their own invented surfaces as evidence.

## Actual reference binding

After the selected table is stable, list first appearance/first audible entrance in global time. Within each modality, preserve that order; resolve simultaneous appearances by the table's entity order. A same-scene continuation has one exception: its required predecessor video is bound first in the actual source-video input, followed by current references. New scenes clear that predecessor relationship.

| Shot / request revision | Role / purpose | Source asset revision | Prepared handle | Measured audio seconds | Real port / slot | First use | Accepted job / submitted-payload evidence |
|---|---|---|---|---|---|---|---|

For each shot, explicitly map `speaker → approved CH (if visible) → approved VO → selected VR and/or DL → real input slot or editor track`. Record the incoming payload mapping before submission and returned confirmation when exposed. Typed @mentions or prompt prose alone do not attach assets. If the tool does not expose accepted bindings, report the known submitted bindings rather than fabricate confirmation. Recompute bindings when a role, asset revision, shot order, or audio crop changes.
