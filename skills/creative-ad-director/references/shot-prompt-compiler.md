# Compile the approved table into scene-specific prompts

Use bundled examples for workflow structure only. A user-selected reference may also authorize its pacing and visual treatment; [reference-rhythm.md](reference-rhythm.md) defines the owner's current pacing preference and evidence limits. Never automatically import illustrative plots, characters, locations or dialogue. The approved current screenplay and production table are the content authority.

## Reconcile source rows before writing

Read the scene and adjacent rows; retain source row/line IDs, exact speech, shot size, camera motion, character action, setting, props, and duration. If a source item is intentionally absent, mark none; if essential content is missing, resolve it from the approved script or a native Question. Do not invent a new plot while compiling prompts.

Group all editorial shots by approved scene ID first. A supported scene of ≤30s is one generation unit; >30s scenes use a base and chained continuations as defined in `model-routing.md`. Consider merging a sub-4-second editorial shot with adjacent compatible action only when scene/time/place, characters, wardrobe, lighting, and camera intent remain coherent and all source content survives. Never merge across a new scene or erase an independent reveal, reaction hold, or punchline just to meet a tool's minimum duration. Record source-row coverage for every merged unit. An editorial shot can remain short inside a longer supported generation unit.

## Timing

Read the approved Rhythm Map with source rows. Carry each beat's trigger, reveal, result hold and cut cue into the local action plan. Preserve sub-second editorial targets on a separate edit map even when the provider requires integer requests. Longer generation units supply usable ranges; they do not authorize lengthening every short insert. If internal cuts cannot be controlled reliably, use native Question to approve a specific alternative before departing from scene-based generation; preserve the approved source rows and rhythm. Preserve the opening reveal, repeated demonstrations and calmer finish when that profile is selected.

Measure exact final speech first. Allocate action, transitions, breath, and reaction time. Merge compatible rows before rounding. For a provider expecting integer seconds, use half-up rounding for provisional timings, then reconcile to a feasible sequence: each local request starts at 0, each interval starts at the previous end, no interval has zero/negative duration, and the final end equals the unit duration. Never round into less room than actual dialogue/action requires; increase the containing interval or split naturally while retaining the approved story and hard user duration constraint.

Maintain both a continuous global film timeline and local `0…N` request intervals. Multiple generation units are distinct from editorial shot counts. Do not independently round every global timestamp and create gaps. If measured delivery materially changes the screenplay rhythm/length, return the updated artifact to the affected gate before production.

## Prompt order

For each production unit, write one unambiguous instruction:

1. **Continuation only:** begin with the exact instruction **“续写这个@视频”** and identify the actual immediately preceding output bound to the video port. Resolve the mention to that real asset, then request only the next approved table span. The same-scene predecessor must be ready and inspected. No continuation phrase or preceding-scene video for a new scene.
2. State approved style, location, time/light, character/wardrobe identity, and relevant product state. Resolve every reference mention to the actual attached input.
3. Give integer unit duration when required and **16:9, 720p (1280×720)** unless the user explicitly chose another format. Set these on actual base/extension request controls as well as in the prompt.
4. For every local interval, specify shot size/camera, visible character action/expression/eyeline, props, composition, exact speaker-labeled words/VO, listening reactions, and the ending pose/state.
5. State continuity, voice-to-role mapping, lip-sync requirement when applicable, audible dialogue, required effects/ambience, and the explicit no-background-music restriction below. Keep price/label/CTA microtext editable rather than relying on generated lettering.

No alternative camera plans joined by “or,” no vague “as appropriate,” no additional dialogue or weather that is absent from the approved table. Preserve the whole exchange across cuts; attaching a voice does not license arbitrary spoken text.

## Required sound instruction for every video prompt

Include this block in both base and continuation prompts, adapting only the approved role/line mapping:

> Audio on. Render the exact scripted character dialogue and approved narration audibly using the bound approved voices; synchronize visible speech with lip movements. Preserve listening pauses and required scene sound effects/ambience. No background music, no BGM, no instrumental score, no musical stings, no soundtrack bed, and no singing unless explicitly scripted. Do not replace speech with silence or add unscripted words. Output 16:9, 720p (1280×720).

For a unit without scripted speech, say “No dialogue or narration in this unit; only the approved effects/ambience, no music.” Never invent speech simply because audio is enabled. Explicit user format changes override the format sentence. Actual supported audio/format controls must match the prompt. Inspect playback: a written restriction is not proof of audible dialogue or absence of music.

For a continuation, precede the regular scene prompt with:

> 续写这个@视频。接续已绑定的上一段视频结尾，仅生成已确认镜头生产总表中本段对应的后续内容。保持人物、商品、空间、动作和声线连续，不重复上一段内容。按本段局部时间戳执行。

Append resolved scene/unit IDs, table rows, added duration, local intervals and exact dialogue; this template is not a replacement for those details. Bind the previous actual video to the native input slot before dispatch. Never use this continuation instruction for a new scene.

## Scene dependencies and canvas layout

Each scene gets its own heading/table with input references, full prompt, generated-video slot/status, and notes. Notes preserve source-row coverage, merge decisions, unresolved dependencies, and model route. Save/read back each written scene and check the full chain afterward.

- First unit: use this scene's character/product/prop/scene image references and required voice inputs; no preceding-scene video.
- Same-scene continuation: bind the actual previous ready video first through the source-video port, then relevant current image/audio references. Use local timing for the added span and record global offsets.
- New scene: clear previous video continuation; use its own references and timing.

Before generation, a future video may be shown as an unresolved dependency in the table. The agent must replace it with the actual returned handle when ready; do not instruct the user to paste that handle manually. All textual reference labels must have matching real attachments before dispatch. Check `r2v-audio.md` after assembling the final audio list.
