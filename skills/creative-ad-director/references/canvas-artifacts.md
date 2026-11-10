# Canvas artifacts and native Question checkpoints

This is the authoritative gate contract. Read before the first question and after resume. Use Lumina's actual native Question tool and returned schema, not a generic chat question helper, Markdown choices, HTML buttons, or a fabricated tool call. Discover its real tool identifier, option fields, question ID, result format, and callback/status behavior in the active host. This Skill does not hardcode undocumented API keys.

## Artifact before review

Create/save/read back the full artifact on the actual canvas. A review card contains a concise question, asset locator(s)/revision(s), and actionable options; it is not a substitute for the script, table, image, playable audition, or playable video. Failed/blank/pending media must not be presented as ready for approval. User edits on canvas require re-reading the artifact before approving/using the revision.

Default labels below are localized to the user's language. Every adjustment is offered inside the native card. Use actionable presets first; custom details belong in native Other/free-text fields when supported. Never require the ordinary chat composer to continue or revise. If the native card lacks custom text, follow with supported native selectable edit dimensions rather than pretending a free-text field exists.

## Gates and automatic successors

| Gate | Required visible artifact | Native options | On actual approval/selection |
|---|---|---|---|
| G1 剧本确认 | Complete saved script, visual style, estimated rhythm/duration | 通过并生成角色 / 调整剧本 / 更换风格 | Lock script revision; generate character/prop references |
| G2 角色与道具确认 | Ready 16:9 character front/side/back sheets plus applicable product/prop/scene references | 全部通过 / 调整指定角色或道具 / 重新查看 | Lock visual revisions; open role-specific voice preference gate |
| G3 角色音色方案 | Named role, character image if visible, 2–3 described voice choices | 推荐方案 / 另一具体方案 / 自定义音色 | Save that role's choice; generate ~20s clean audition; continue outstanding roles |
| G4 角色试音确认 | Playable, role-labeled real auditions and durations | 全部通过 / 调整指定声音 / 再听一次 | Lock voices; generate/measure final lines; compile full shot table |
| G5 镜头生产总表确认 | Complete saved table, source mapping, boards, timing, input bindings/dependencies | 按此表生成分镜 / 调整指定镜头 / 重新查看 | Dispatch ready shot jobs and monitor automatically |
| G6 分镜成片确认 | Actual current playable prepared shot(s), with correct dialogue and no unwanted model music | 通过当前镜头或明确列出的批次 / 调整指定镜头 / 重播 | Approve listed revisions only; continue remaining shots or post-production |
| G7 后期制作方式 | Ordered approved shot inventory and proposed finishing scope | 剪辑拼接＋字幕 / 仅剪辑拼接 / 仅添加字幕 / 自定义 | Execute selected native editor operations; captions-only requires an existing assembled timeline |
| G8 成片确认 | Full playable current edit with sound | 确认并导出下载 / 局部修改 / 再看一次 | Export exactly approved revision, verify output, deliver |

Do not ask empty gates: a silent film skips voice gates with a recorded reason; an off-screen narrator has voice gates but no fabricated visual identity. A user who already chose the exact post-production mode does not need G7 again. An existing approval may satisfy the same gate for the exact current revision, never a newly changed artifact. G3 preferences are not G4 audio approval; G5 production approval is not G6 finished-shot approval.

## Native revision flow

If the user chooses revision without details, do not wait for a chat message. Issue one native question for the affected artifact/role/shot (unless already selected), then a native question offering concrete edits suited to it. Examples of dimensions: pacing, ending, visual style, wardrobe, voice warmth/pace/accent, pronunciation, shot action, camera, text, or mix. Preserve all other approved work. Apply an in-card custom answer directly when specific enough; do not ask it again. Save the changed artifact and present its new revision at the corresponding gate.

Replay/view-again reopens existing ready artifacts, never regenerates or incurs a new generation charge. A gate may represent several shots only when each is visibly accessible and the approved scope lists every ID/revision; do not approve hidden future clips by implication.

## Question lifecycle

Persist project ID, gate ID, entity IDs, artifact revision/hash, question ID, status (`creating`, `pending`, `answered`, `stale`), returned choice, and next eligible action. Only one unanswered decision should be active for the user at a time. When creation times out, query whether that exact question exists before retrying. Never create several duplicate cards for the same revision.

On answer, verify project, question, role/shot, and artifact revision. Reject stale responses for superseded artifacts; show the current artifact and a fresh native question. Process each returned answer once. A default selection, displayed card, elapsed time, canceled card, or tool status “completed” without a submitted answer is not approval. Do not choose on the user's behalf to keep the workflow moving.

If the host's native Question waits synchronously, continue immediately after it returns. If it yields, persist the checkpoint and use the actual answer event/resume facility; no “type continue” instruction. If no resume facility exists, report that host limitation once rather than claiming this Markdown Skill can provide a background worker.

## Stable artifact IDs

Use `SCRIPT-vN`, `CH01-vN`, `PM01-vN`, `PR01-vN`, `SC01-vN`, `VO01-audition-vN`, `VR01-reference-vN`, `DL01-line-vN`, `TABLE-vN`, `S01-vN`, `ED-vN`, and `EXP-vN`. Keep actual native handles separate from these semantic labels. Scope all IDs and approvals to the current canvas project.
