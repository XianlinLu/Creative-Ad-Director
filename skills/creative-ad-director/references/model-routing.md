# Model routing and continuous time

Read before timing a storyboard, submitting video generation, or extending a clip. These are the user-requested production presets. Verify exposed provider capabilities at runtime; this file is not provider API documentation.

## Routes

| Version | Final duration | Required route |
|---|---|---|
| Seedance 2.5 (default) | 15 / 30 seconds | One native output with continuous shot timestamps; native base-output policy is 4–30 seconds |
| Seedance 2.5 | 45 seconds | Generate the first 30 seconds, then append 15 seconds with actual native extension |
| Seedance 2.5 | 60 seconds | Generate the first 30 seconds, then append 30 seconds if supported, otherwise two supported 15-second native extensions |
| Seedance 2.0 (explicit legacy mode) | 15 / 30 / 45 / 60 seconds | 1 / 2 / 3 / 4 segments of at most 15 seconds each, with explicit continuity handoffs |

The four advertised duration presets are 15/30/45/60 seconds. A specifically requested 4–30 second shorter output may use the 2.5 base route if the tool supports that exact duration; do not silently round it. Do not infer extension limits from base-output limits. Every extension must satisfy its own tool schema and actual duration semantics.

Check model identifier, base duration, extension operation, source-video input, aspect ratio, resolution, image/voice reference support, audio settings, job polling, and output inspection. Record the selected version and actual native identifier. Keep 9:16 and 1080p as defaults, not fabricated output properties. If unsupported, ask one question about a concrete supported alternative; do not automatically switch version, stitch 2.5 long clips, or claim an upscale is native 1080p.

## Timeline and dialogue

Keep one global timeline `[0, target_duration]`. Each shot interval starts where the previous ends; all required actions, replies, reaction holds, and text dwell fit inside it. Shot intervals are editorial units, not necessarily separate generation tasks. Camera cuts within a native 30-second timeline are allowed while character, product, space, and conversation state remain coherent.

Maintain a full scene script before the shot table. Give each line its speaker, listener, intent, cue, and reaction. Preserve setup → answer → consequence across cuts. If speech does not fit, simplify the action or revise the exchange without reducing it to slogans, unexplained rebuttals, or unmotivated punchlines. Audition lines at natural speed and leave room for breaths, interruptions, reactions, and the joke's pause.

For extension jobs, record both global intervals and tool-local intervals. Example: final 45-second ad has a ready base covering global `0–30`; its extension covers global `30–45`, local `0–15` when required by the API. Determine whether returned media is the extension alone or the cumulative 45-second clip. Never append a cumulative result to the base again.

## Extension handoff

Before extending, inspect the actual base ending and record:

- source output handle/revision and inspected ending timecode;
- character poses, screen positions, gaze, wardrobe, and speaker/listener state;
- product identity, visible use state, hand contact, and important props;
- scene geography, light, camera direction/motion, and ambient sound;
- last complete line, any unfinished action, and the intended next beat;
- bound product, character, scene, and independent voice references.

Prefer a stable moment or completed phrase near the boundary. Do not cut a sentence simply to fill 30 seconds. A planned transition can occur inside the continuing video but must not reset character knowledge or product state. Use the real native source-video input. Prompt text saying “continue the previous clip” without that binding is not extension.

If an extension fails, preserve the valid base and repair that extension. If a changed base ending invalidates later continuation, mark only the dependent chain stale and repair it. A completed task still needs actual playback and shot QC.
