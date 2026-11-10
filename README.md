# Creative Ad Director

[简体中文](README.zh-CN.md)

A Lumina Canvas skill for humorous, story-driven marketing videos grounded in product evidence. Version **2.3.0** aligns this repository with the supplied design brief: four distinct concepts, continuous-time storyboards, independent character/voice preparation, real reference bindings, and shot-level repair.

## Use cases

1. Product launches and performance ads.
2. TikTok / Douyin short-drama ads.
3. 15–60 second social marketing creative.

Not suited to strict replication of protected IP, real-person likenesses or established viral personas; precise opening, dispensing, texture or color reconstruction from still-life images alone; complex ensembles or intense continuous action.

## Inputs and workflow

Provide a product or URL, optional brand, soft-sell/hard-sell objective, channel, audience, duration, ratio, resolution, and optional product/character/scene/video/voice references. Missing critical information is requested **one question at a time**. Accessible page text is not proof that webpage images have been inspected. White-model renders support geometry, not unobserved materials, mechanics, or efficacy.

1. Build a sourced product evidence sheet and brief.
2. Present **four materially different concepts**, then develop the selected one.
3. Prepare product/character/scene assets and **independent voice auditions**; track actual readiness.
4. Write the whole scene and compile continuous shot timestamps, preserving conversational relationships and reactions.
5. Bind actual references in first-appearance order and use the selected native generation route.
6. Review **people, product, space, sound, and text for every shot**; repair only failed spans and actual dependents.
7. Verify the editable final cut and actual export. Extra variants require scoped authorization.

## Parameters and model policy

- Model: **Seedance 2.5** default; **2.0** legacy compatibility.
- Duration: **15 / 30 / 45 / 60 seconds**; default 15.
- Format: **9:16, 1080p** by default.
- Creative controls: soft-sell/hard-sell, visual style, seven plot modes, optional trending-structure reference.
- Seven modes: escalating misunderstanding, expectation versus reality, deadpan absurdity, personified problem, failed workarounds, callback, and status reversal. The supplied brief specifies seven modes but does not name them; these operationalize the repository's existing comic engines.
- 2.5 route: native **4–30 second** base output; continuous timestamps within 30 seconds; **45/60 seconds through native extension** from the ready preceding clip.
- 2.0 route: each segment **at most 15 seconds**, with planned continuity handoffs.

These are requested workflow presets, not independently verified provider specifications. Before generation, the skill checks actual tools, model availability, input ports, duration/extension semantics, and resolution. Unsupported capabilities are surfaced; no silent model switch or simulated binding is allowed.

## Install

Download [creative-ad-director-v2.3.0.zip](dist/creative-ad-director-v2.3.0.zip), extract it, and import `SKILL.md`, `agents/`, and `references/` into Lumina. The ZIP excludes repository-only scripts and tests. This replaces the previous `lumina-meme-merchant` skill identity; remove/disable the old imported copy when replacing it to avoid duplicate discovery.

Example:

> Use Creative Ad Director to turn this product URL into a 30-second, 9:16, 1080p humorous soft-sell ad for TikTok. Show four distinct story concepts first. Preserve natural dialogue and use only product states supported by the references.

## Instructions for use (under 1,000 characters)

Create humorous, story-driven marketing videos with Creative Ad Director.

1. Share a product URL, photos, white-model renders, or a brief. Upload images if webpage visuals are inaccessible.
2. Specify your audience, channel, soft-sell or hard-sell goal, duration, ratio, resolution, style, and optional character, scene, video, or voice references. Missing essentials are asked one at a time.
3. Choose from four distinct concepts across seven plot modes.
4. Review character visuals, independent voice auditions, and a continuous-time storyboard with natural dialogue.
5. Generate, review each shot, and refine only failed parts.

Defaults: Seedance 2.5, 15 seconds, 9:16, 1080p. Choose 15/30/45/60 seconds; 45/60 use native extension. Seedance 2.0 uses segments up to 15 seconds. Actual tool support is checked first.

Use verified product details. Still images do not prove opening, dispensing, texture, or efficacy. Best for product launches, TikTok/Douyin story ads, and social campaigns.

## Validate and build

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/creative-ad-director
python3 skills/creative-ad-director/scripts/preflight.py
python3 -m unittest discover -s tests -v
python3 skills/creative-ad-director/scripts/build_skill.py \
  --output dist/creative-ad-director-v2.3.0.zip
```

Static checks validate structure and packaging. Live model capabilities, paid generation, voice binding, native extension, playback QC, and exports require the actual Lumina environment; they are not established by these checks.
