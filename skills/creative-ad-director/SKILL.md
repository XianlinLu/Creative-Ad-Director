---
name: creative-ad-director
description: Produce humorous, story-driven marketing videos on Lumina Canvas from a user's idea, script, product URL, or references. Offer four distinct concepts first, obtain a native Question selection before writing the complete script, prepare character turnarounds and voices, compile an executable shot production table, and automatically generate, repair, edit, and export the approved video.
metadata:
  version: "2.4.1"
---

# Creative Ad Director

Run the production, not a conversation about running it. Start with the user's idea, deliver actual artifacts, and advance automatically after each required native Question answer. User selections are intentional checkpoints; idle stops asking the user to type “continue” are not.

## Scope and defaults

Use for product launches/performance ads, TikTok/Douyin narrative ads, and social marketing videos. Keep humor and product evidence aligned. Do not promise virality or sales. Avoid strict imitation of protected IP, real-person likenesses or established viral personas; complex ensemble/high-intensity action; or precise product movement/material reconstruction from static images alone.

Capture product/optional brand, idea, soft/hard-sell goal, audience, channel, language, format, resolution, and available product/character/scene/video/voice references. Research what is accessible and use reversible assumptions for optional gaps. Ask one critical missing fact at a time **through the native Question tool**.

- **Four concepts first:** develop exactly four materially different creative interpretations of the user's idea, save/show them, and obtain a real native **G0 创意方向选择** answer before writing the complete script. Preserve the user's product, intent, constraints, and supplied facts across all four. Skip G0 only when the user explicitly requests direct execution of an existing definite script; merely supplying an idea or draft script, asking for automation, or delegating routine work does not qualify. Record the explicit bypass instruction and script revision. See [creative-strategy.md](references/creative-strategy.md).
- **Duration follows the screenplay:** account for natural speech, actions, reactions, pauses, and CTA dwell. Give a provisional duration at script review, then refine from measured final speech before shot-table review. Do not force 15 seconds or round the whole film to 15/30/45/60. Explicit user duration is a constraint; substantial story/duration changes return to script review.
- Default final-video format is **9:16, 1080p** unless specified. Character three-view sheets are **16:9**, independently of final-video format.
- Prefer **Seedance 2.5**, with explicit **2.0** legacy mode. Discover actual capabilities before dispatch; follow [model-routing.md](references/model-routing.md). A policy preference is not proof of API support.
- All checkpoints, repair selections, voice preferences, and custom adjustments use real Lumina **Question** UI. No Markdown checkbox imitation, HTML replica, or “reply A/B in chat.” See [canvas-artifacts.md](references/canvas-artifacts.md).

## Start / resume contract

Read [autonomous-runner.md](references/autonomous-runner.md) and [canvas-artifacts.md](references/canvas-artifacts.md) on activation/resume. Discover actual Canvas, Question, image, audio, video, polling, inspection, and Video Editor tools and schemas. Resolve the current project's saved state before creating work. If the host exposes an execution mode, check whether it allows automatic continuation; a Skill cannot override host Manual mode or invent a callback.

Save a checkpoint before any wait and resume from the returned event. After an answer or completed job, execute the next eligible operation in the same resumed turn until the next real gate, pending dependency, verified delivery, or actionable blocker. Never finish an intermediate turn with only “I can do the next step.” Do not infer approval from a timeout, default option, queued task, or successful generation.

## Ordered production flow

### 1. Idea → four concepts → G0 → complete script → G1 剧本确认

Read [product-research.md](references/product-research.md) and [creative-strategy.md](references/creative-strategy.md). Create/read back **Product Evidence Sheet**, **Creative Brief**, and **Creative Board vN** with exactly four directions `C01–C04`. Differentiate their premise, character relationship/conflict, comic mechanism, product role, and ending; four slogans or hooks for the same story do not count. Recommend one, show all four, and call native **G0** with explicit concept choices. Do not pre-write a full screenplay or generate concept videos while this selection is pending. A revision choice revises the board through native controls and returns to G0.

On the actual G0 answer, lock the chosen concept and board revision and immediately write/save/read back **Scene Script vN**, without asking the user to type “continue.” If and only if the user explicitly requests direct execution of an existing definite script, record that instruction, skip concept generation/G0, and preserve that script for G1. This exception does not waive subsequent review gates; an already approved exact revision need not be reviewed twice. The complete script includes scene IDs, setting/style, cast, visible actions, exact dialogue/VO, speaker/listener relationships, pauses, ending, product role, and provisional total rhythm/duration. Do useful drafting before any optional intake.

Keep whole-scene exchanges and motivations; do not turn dialogue into disconnected slogans or comeback lines. Do not infer opening, paste/cream, dispensing, texture, exact color, or efficacy from static packshots or white models. Present the saved screenplay, then call native **G1 剧本确认**. Approval immediately starts character/prop preparation.

### 2. Script → character turnarounds → G2 角色与道具确认

Read [assets-and-voices.md](references/assets-and-voices.md). Extract all visible identified characters (including silent roles), important props/product assets, and required scenes from the approved script. Generate **one landscape 16:9 front/side/back three-view sheet per visible character**, preserving identity, wardrobe, scale, and neutral background. Prepare needed product/prop references without inventing unseen details.

Await real ready outputs, inspect/show them, and record actual asset IDs/revisions. Call native **G2**. Keep voice generation separate: approval here locks appearance, not sound. If the script has no visible characters, explicitly record that and review only applicable visuals; never invent a face for an off-screen narrator.

### 3. Characters → voice preferences → G3 角色音色方案

For each speaking character and independent narrator, show 2–3 tailored voice options with timbre, perceived age, pace, accent/language, delivery, and fit. Use a native Question per role, or supported role-specific fields with unambiguous role IDs. Include an in-card custom path. Respect existing specific preferences while still presenting the requested voice-choice checkpoint; do not send the user to the chat composer.

After a role's choice, automatically create a real **approximately 20-second clean audition** using meaningful representative speech and varied delivery. Await playable audio; text describing a voice is not an audition. Continue through all required speaking roles. Silent roles need no audition.

### 4. Real auditions → G4 角色试音确认

Show every current playable audition with its role label and actual duration; call native **G4**. Let users approve, replay, or change a named voice through native options. Replaying reuses the same audio; changing one voice preserves approved others.

On approval, create exact final dialogue/VO with the approved voice and measure the real speech duration. **Audition audio, short voice-reference excerpts, and final dialogue audio are distinct assets.** Read [r2v-audio.md](references/r2v-audio.md): do not attach every full audition to each shot. For observed Seedance 2.5 r2v limits, each attached audio must be at least **1.8s** and the request's combined attached audio at most **30.2s**; target **2.0s minimum / 30.0s total** for preparation margin, using measured files.

### 5. Measured speech → 镜头生产总表 → G5 总表确认

Read [production-workflow.md](references/production-workflow.md) and [shot-prompt-compiler.md](references/shot-prompt-compiler.md). Compile the approved script and locked visuals/voices into the complete **Shot Production Master Table (镜头生产总表)**, grouped by scene. Prepare needed boards/starting frames; include an explicit reason where a board is unnecessary.

Record source script rows, stable shot IDs, continuous global timing and local integer intervals, actual speech duration and action/reaction allowance, exact text/actions/camera, appearance/voice/audio handles, predecessor dependencies, generation route, complete prompts, actual lifecycle state, QC and approval state. Resolve ready references; future predecessor outputs may be declared dependencies but cannot be submitted as placeholders. Save/read back the table and call native **G5**. Table approval authorizes production, not unseen output approval.

### 6. Table → shot generation / QC → G6 分镜成片确认

Automatically submit ready rows, track accepted jobs, prepare sound, inspect outputs, and repair failures. Use only each shot's visible characters and audible speaker/narrator mappings. Bind actual current character images and approved voice-derived audio to supported ports; keep speaker assignment explicit. Check every outgoing audio against [r2v-audio.md](references/r2v-audio.md) before dispatch. Purely editorial narration is added on its mapped track, not falsely claimed as native conditioning.

For same-scene continuation, await the real predecessor video, inspect its ending, bind it first as the source video, then current required references. New scenes start from their own references and clear the previous-scene video dependency. Never submit “pending video” or a typed @mention as an actual asset.

Read [compliance-and-qc.md](references/compliance-and-qc.md). Check **people, product, space, sound, text** per shot. Remove unwanted generated music while preserving speech/effects/ambience. Show real playable prepared clips via **G6**, individually or an explicit batch whose exact revisions are all available for review. Record approval per shot; repair only rejected/failed units and actual dependents. Continue producing independent approved-scope work while a gate waits if the host supports it.

### 7. Approved shots → G7 后期方式 → automatic edit → G8 成片确认

Call native **G7** for editing mode unless already specifically chosen: assemble + captions (recommended), assemble only, captions only on an existing assembled timeline, or in-card customization. Use the real native Video Editor, ready approved clips, exact source ranges, separate speech/effects/music/caption tracks, and unchanged approved voice identities. Do not ask “shall I open the editor?”

Show the complete playable current edit with sound, then call native **G8**: confirm/export, targeted revision, or replay. A revision returns only affected work to review. Confirm/export immediately starts real export and observes it to completion.

### 8. Verify delivery

Verify exported media actually plays and downloads, covers all required shots, and has the approved timing, format, resolution, captions, dialogue, music, and sound effects. Return actual video(s), editable draft, and production/evidence manifests when available. A prompt package, queued render, or editor acknowledgment is not a delivered film. Publishing/campaign spending remains separately authorized.

## Hard boundaries

Use real available tools, not invented API names or fabricated success. If a native Question, binding port, generation feature, or resume mechanism is absent, record a concrete capability blocker; preserve useful work and do not silently replace the requested native interaction with chat. User selection waits are mandatory; “automatic” never means approving on the user's behalf. Stop only for a genuine pending answer/job dependency, explicit pause, unrecoverable bounded blocker, or verified delivery.
