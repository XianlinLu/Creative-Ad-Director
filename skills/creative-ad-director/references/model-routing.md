# Model routing and screenplay-derived timing

Use actual tool schemas before dispatch. These routes are requested workflow policies, not independently verified provider specifications. The observed r2v audio errors and their guard are documented separately in `r2v-audio.md`.

## Film length is not request length

Derive the film's proposed duration from the approved script and measured final dialogue/action/reaction rhythm. Honor explicit user duration. 15/30/45/60 seconds are convenient user presets, not mandatory totals; do not round a 38-second story into a 45-second film merely to fit a preset.

Partition the approved table by scenes and production units. A unit may contain multiple editorial shots with a continuous local timeline. Use integer unit duration if required by the actual provider; preserve exact speech and feasible action. Use the whole-scene dialogue as continuity context while binding only the current unit's required assets.

| Version / situation | Route |
|---|---|
| Seedance 2.5 default, scene/base unit fitting supported 4–30s output | Native base generation with continuous local shot timestamps |
| Seedance 2.5, same scene requiring more than the native base | Append through actual native extension from the ready predecessor where supported; obey that operation's own duration/input contract |
| Seedance 2.5, new scene | New base unit using this scene's references; no previous-scene continuation video; assemble scene outputs later |
| Seedance 2.0 explicit legacy mode | Units at most 15 seconds with planned handoffs and actual supported continuation/conditioning |

For a continuous 45-second scene, a 30s base plus supported 15s extension may work; for a continuous 60-second scene, use supported extension lengths. These are planning examples, not a mandate to put a boundary mid-sentence. If a supported duration cannot cover a proposed unit, split/merge compatible rows in the table before G5. Unsupported model/extension/voice ports require one concrete native Question choice; never switch silently or call stitched standalone clips a native extension.

## Capability and input checks

Discover model identifier, mode, duration/resolution/ratio support, image/video/audio ports, audio reference semantics, reference count limits, native extension, status inspection and output playback. Default final video is 9:16, 1080p; character sheets remain 16:9. Do not claim native 1080p for an upscale. Do not infer extension constraints from base-output constraints.

For `dreamina-seedance-2-5` r2v, run the per-entry and combined audio preflight after assembling the actual payload. Long whole-film dialogue or all full auditions must not be attached to each request. Video duration and audio-reference duration are independent constraints.

## Timelines and extension

Keep a gap-free global timeline and a separate local `0…N` timeline per request. Source row/line coverage must be complete. Measure actual speech, preserve response causality and pauses, and avoid zero-length rounded intervals.

Before a same-scene extension, inspect the real predecessor ending: character poses/positions/gaze/wardrobe, product state/contact, props/light/camera, last complete line, unfinished actions, and sound/voice identity. Bind the actual ready source-video handle first; text saying “continue” is not sufficient. Record global offset, requested added duration, and whether the returned result is cumulative or extension-only. Never concatenate the base a second time when the result already contains it.

A new scene resets the video dependency and uses fresh scene references. Failed continuation preserves the valid base; a changed base ending invalidates its dependent chain only. Completed jobs still need actual picture/sound QC and native G6 review.
