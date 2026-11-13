# Creative Ad Director

[简体中文](README.zh-CN.md)

Version **2.5.1** generates scene-based video with audible character dialogue, **no background music**, and **16:9 / 720p** defaults. It retains reference pacing, four concepts, native selection, complete screenplay and automatic production between review checkpoints.

Each supported scene of **≤30 seconds** is generated directly in one request, including its internal shots. Longer scenes use a base plus sequential continuations: attach the immediately preceding actual video and include **“续写这个@视频”**, following the next approved production-table rows. A new scene starts a new base with no prior-scene video. Provider constraints are checked before dispatch; unsupported routes are resolved through native Question, never silently substituted.

## Reference pacing

The [rhythm guide](skills/creative-ad-director/references/reference-rhythm.md) records visual observations from the supplied 51.1-second reference, approximate section timecodes and evidence limits. A Rhythm Map carries trigger/action/result beats, short inserts, reaction holds, heading cues and a calmer ending through script, shot prompts and the final edit. Longer generation units do not force longer editorial shots. Duration and ratio remain project choices.

Audio presence was verified in metadata; music, speech, BPM and sound synchronization were not perceptually verified. Proposed sound design stays distinct from observed markers. No source video or extracted frames are published. Static validation does not establish that a generated Lumina film matches the reference.

## Production sequence

1. **Four distinct concepts → native selection → complete screenplay → native script review.** Keep the user's intent and product facts while varying the story. Skip concept selection only when the user explicitly asks to directly execute an existing definite script. Derive duration from natural dialogue, action and story rhythm, honoring explicit duration constraints.
2. **Character/prop generation → native visual review.** Every visible character gets a landscape **16:9 front/side/back turnaround**, independent of final-video ratio.
3. **Native voice preference per speaking role → real audition.** Offer concrete voice choices, then generate approximately **20 seconds** of clean speech for each character/narrator.
4. **Native audition review → exact final dialogue.** Lock approved voices, synthesize the actual screenplay lines, and measure durations.
5. **Shot Production Master Table → native table review.** Include source-row coverage, boards, measured speech, timing, actions, camera, dialogue, actual input mappings, dependencies, job states, QC and approvals.
6. **Automatic shot generation and repair → native shot review.** Use each shot's actual character references and approved voice-derived audio. Wait for real predecessor video in same-scene continuations; reset the video dependency at scene changes.
7. **Native finishing choice → real Video Editor work → native final review.** Assemble approved clips, preserve voices/effects, and apply chosen captions with no background music.
8. **Confirm/export → verified playable, downloadable film.** Deliver the actual output and editable project when available.

All choices and revision details use the host's real Question interface, including native custom fields where supported. Replaying existing media does not regenerate it. Each approval is bound to exact visible/playable revisions. User-answer waits remain necessary; there are no approval-by-timeout shortcuts.

## Prevent the reported r2v audio errors

Observed errors for `dreamina-seedance-2-5` in r2v require **each attached audio ≥1.8s** and **combined attached audio ≤30.2s per request**. Prepare with a practical **2.0s minimum / 30.0s total margin**, and verify actual prepared-file durations.

A 20-second audition is for user review; it is not automatically the video input. Two full auditions would total 40 seconds. Derive short clean spoken reference excerpts from approved voices, bind only the current unit's required roles, and count **all** outgoing audio entries, including final dialogue when attached. Do not deduplicate only the accounting while leaving duplicate files in the payload.

The Agent performs the checks from native media metadata using the imported Markdown rules; no Python runtime or user-run command is required. The repository keeps `scripts/validate_r2v_audio.py` for developer-side regression checks only; it is excluded from the import ZIP. See [audio preflight](skills/creative-ad-director/references/r2v-audio.md). Invalid-parameter requests must be corrected before retry, never replayed unchanged.

## Scope and runtime requirements

Use for product launches/performance ads, TikTok/Douyin narrative ads, and social marketing creative. Preserve verified product states: still images do not establish opening, dispensing, paste/cream, exact materials/colors, or efficacy. White models help with geometry only.

Defaults: every generated clip and final film **16:9, 720p (1280×720)**, Seedance **2.5** preference; **2.0** legacy mode is explicit. Duration follows the story. Verify actual model/mode support and per-unit/extension constraints. Seven comic plot modes support the four-concept exploration.

Full execution requires actual Canvas/Question tools, image/audio/video generation, duration measurement, polling/resume, inspection, Video Editor and export capabilities. A host in Manual mode may require switching to its supported automatic execution mode. The Skill cannot override the host setting, create missing tools, or supply an absent answer callback. Missing capability is a concrete blocker, not a reason to fake native cards or claim completed video.

## Install

Download [creative-ad-director-v2.5.1.zip](dist/creative-ad-director-v2.5.1.zip) and replace the previous imported Skill. Import `SKILL.md`, `agents/`, and `references/`. The ZIP contains only supported `.md` and `.yaml` files; all Python scripts and tests stay in the repository. Do not upload the repository source folder as the Skill package. The builder validates supported extensions (`.md`, `.txt`, `.json`, `.yaml`, `.yml`), lowercase extensions, and ASCII names of at most 64 characters before writing the ZIP.

## Instructions for use (under 1,000 characters)

Turn your idea into a video with Creative Ad Director.

1. Share your idea, product image/URL, references and constraints.
2. Choose from four distinct concepts through native Question options, then review the complete script. Skip concepts only when explicitly requesting execution of an existing script.
3. Approve 16:9 character sheets, choose voices and review ~20-second auditions.
4. Approve the scene-based production table. Scenes up to 30s generate directly; longer scenes continue from each preceding real video using “续写这个@视频”. New scenes start independently.
5. Review clips and the final edit through native options, then confirm export.

Videos default to 16:9, 720p, with audible scripted dialogue and no background music, including in post-production. Duration follows story rhythm. The agent advances after each approval, checks actual audio limits and preserves product evidence. Real native tools and supported continuation are required.

## Validate and build

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/creative-ad-director
python3 skills/creative-ad-director/scripts/preflight.py
python3 -m unittest discover -s tests -v
python3 skills/creative-ad-director/scripts/build_skill.py \
  --output dist/creative-ad-director-v2.5.1.zip
```

The regression tests cover both reported duration failures, inclusive limits, combined voice/dialogue inputs, duplicate attachments, missing speakers, invalid/unverified durations, and source approval. Static validation is not an end-to-end Lumina run; native cards, actual conditioning, paid video jobs, resume behavior and exports still require live verification.
