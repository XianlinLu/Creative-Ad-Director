# Model routing and screenplay-derived timing

Use actual tool schemas before dispatch. These routes are requested workflow policies, not independently verified provider specifications. The observed r2v audio errors and their guard are documented separately in `r2v-audio.md`.

## Film length is not request length

Derive the film's proposed duration from the approved script and measured final dialogue/action/reaction rhythm. Honor explicit user duration. 15/30/45/60 seconds are convenient user presets, not mandatory totals; do not round a 38-second story into a 45-second film merely to fit a preset.

Partition the approved table by scene identity first, then by supported production units within each scene. A camera angle, insert or reaction cut within the same continuous location/time is an editorial shot, not a new scene. A location/time reset is a new scene even if the cast is unchanged. Preserve approved scene IDs; do not invent scene breaks to avoid continuation. A unit may contain multiple editorial shots with a continuous local timeline. Use integer unit duration if required by the actual provider; preserve exact speech and feasible action. Use the whole-scene dialogue as continuity context while binding only the current unit's required assets.

| Version / situation | Route |
|---|---|
| Seedance 2.5 default, a complete scene of ≤30s fitting supported output duration | One direct base generation for the scene, including internal shot changes with continuous local timestamps |
| Seedance 2.5, a continuous scene >30s | Generate the base (up to 30s), then sequentially extend each real immediately preceding video; include “续写这个@视频” and only the next approved table span; obey the extension operation's own duration/input contract |
| Seedance 2.5, new scene | New base unit using this scene's references; no previous-scene continuation video; assemble scene outputs later |
| Seedance 2.0 explicit legacy mode | Units at most 15 seconds with planned handoffs and actual supported continuation/conditioning |

The 30-second threshold applies to each scene, not to total film duration: two independent 20-second scenes use two base requests, never a 30s+10s extension chain. Exactly 30 seconds stays on the direct route. Do not split a supported ≤30s scene into independent videos merely because its table has multiple editorial shots.

For a continuous 45-second scene, a 30s base plus supported 15s extension may work; for a continuous 60-second scene, use supported extension lengths. These are planning examples, not a mandate to put a boundary mid-sentence. Choose handoffs at complete exchanges/actions before the limit; a 28s base may be preferable to cutting a sentence at 30s. Keep subsequent continuations chained to the immediately preceding successful output, not always the original base. Each continuation must follow the next rows of the approved table without repeating or skipping speech. If a short scene falls below a tool minimum, an audio budget is infeasible, or a route/format cannot be supported, resolve a concrete alternative through native Question before changing the approved production plan. Do not silently create independent same-scene clips. Explicit legacy 2.0 retains its supported ≤15s units; disclose that exception at G5. Unsupported model/extension/voice ports require one concrete native Question choice; never switch silently or call stitched standalone clips a native extension.

## Capability and input checks

Discover model identifier, mode, duration/resolution/ratio support, image/video/audio ports, audio reference semantics, reference count limits, native extension, status inspection and output playback. Default every base request, extension request, board and final export to **16:9, 720p (1280×720)**; character sheets remain 16:9. Persist ratio/resolution per unit and check actual returned metadata. Do not silently fall back to 9:16 or 1080p, or claim native 720p for a resized result. Enable the actual supported audio-generation control for scripted dialogue; do not guess an API field name. Disable music independently where supported and include the no-music instruction in all video prompts. A global audio-off switch is not a substitute for music suppression. Do not infer extension constraints from base-output constraints.

For `dreamina-seedance-2-5` r2v, run the per-entry and combined audio preflight after assembling the actual payload. Long whole-film dialogue or all full auditions must not be attached to each request. Video duration and audio-reference duration are independent constraints.

## Timelines and extension

Keep a gap-free global timeline and a separate local `0…N` timeline per request. Source row/line coverage must be complete. Measure actual speech, preserve response causality and pauses, and avoid zero-length rounded intervals.

Before a same-scene extension, inspect the real predecessor ending: character poses/positions/gaze/wardrobe, product state/contact, props/light/camera, last complete line, unfinished actions, and sound/voice identity. Bind the actual immediately preceding ready source-video handle first. Start the continuation instruction with **“续写这个@视频”**, resolving `@视频` to that attached native video asset (or its actual host label, while retaining the required phrase). Record the label-to-handle mapping; text alone is not a video input. State the approved scene/unit IDs, source table rows, added-span timing and preserved ending state. Do not use the reference ad, a placeholder, or a prior scene as the predecessor. Record global offset, requested added duration, and whether the returned result is cumulative or extension-only. Never concatenate the base a second time when the result already contains it.

A new scene resets the video dependency and uses fresh scene references. Failed continuation preserves the valid base; a changed base ending invalidates its dependent chain only. Completed jobs still need actual picture/sound QC and native G6 review.
