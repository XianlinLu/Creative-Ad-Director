# Seedance 2.5 r2v audio preflight and repair

Read before every r2v video submission, including extensions and retries. The user's observed `InvalidParameter` responses for `dreamina-seedance-2-5` in r2v specify:

- An attached audio entry must have actual duration **at least 1.8 seconds**.
- Combined attached audio duration in one request must be **at most 30.2 seconds**.

Treat these as observed model/mode constraints, not universal rules for all providers. Check current tool constraints and honor stricter exposed limits; a new validation response may update the known envelope. Do not confuse audio-input limits with final video length. A 45-second film does not authorize 45 seconds of audio in a single r2v request.

## Three different assets

- **Audition VO:** about 20 seconds for the user's G4 review. Keep the approved source intact.
- **Voice reference VR:** a clean spoken excerpt from the approved VO, commonly 4–8 seconds for each needed speaker. Preserve identity, pronunciation and source provenance. Its purpose is conditioning, not playback as the final line.
- **Dialogue DL:** exact approved words at natural delivery, measured after rendering. Its timing constrains the shot. Attach only if the actual tool has the corresponding audio-driven input, or place it on the approved editor track.

Two full 20-second auditions would total 40 seconds and fail the observed 30.2-second cap. Do not attach all project voices to every shot, nor attach the same audition again under another slot. Voice samples and final dialogue both count when both are actually present in the outgoing audio list.

## Mandatory pre-dispatch checks

1. Enumerate the **actual outgoing** audio entries, including repeated entries and all reference/driving types. Map them to the shot's audible roles. Do not sum the project library or just the longest file.
2. Resolve ready actual handles. Measure each prepared file from authoritative decoded-media duration or supported native media metadata after crop/re-encode. Prompted duration, filename, source crop arithmetic, and rounded display labels are not measurement. Missing measurement blocks that request while independent work continues.
3. Confirm speaker/voice/source revision, source approval, correct usage port, exact script lines for DL, and audible clean content. A 2-second silent file is not a useful identity reference even if it meets the numeric limit.
4. Require **each duration ≥1.8s** and **sum ≤30.2s**. Prefer preparing files of at least **2.0s** and combined duration at most **30.0s**, avoiding boundary uncertainty. The sum must include every submitted audio entry; deduplicate unnecessary repeated bindings before creating the payload, not just while counting.
5. Confirm fit to the shot for audio-driven DL and verify no omitted speaker. Save the validation result and exact request/asset revisions. Any audio change invalidates this check and requires remeasurement.
6. If Python is available, run `scripts/validate_r2v_audio.py <manifest.json>` on the measured metadata. The packaged helper checks metadata bounds and role coverage; it neither measures media nor proves audio quality or native binding. In a host without Python, perform the same checks with native metadata and arithmetic; do not require a nonexistent shell.

The manifest has `model`, `mode`, `required_roles` (roles whose audio is actually required in this native request), and `audio` entries with `role_id`, `asset_id`, `duration_seconds`, `duration_verified`, `source_approved`, and `purpose` (`voice_reference` or `dialogue`). Roles handled only on editor tracks are documented in the table and excluded from this request's required roles. The validator's `ready_to_submit` concerns this audio guard only, not all generation prerequisites.

## Deterministic repair policy

**An entry is too short:** for voice conditioning, select a longer natural spoken phrase from the same approved audition, normally 4–8 seconds; upload and remeasure. Do not submit a clipped phoneme, empty/silent sample, or a final micro-line as an identity reference. For a genuinely short final line, keep exact wording: use a valid VR plus text if the tool supports it, use a supported dialogue preparation with natural lead/trail room and suitable shot timing, or an approved editor/VO route. Do not add unapproved words or pad an identity sample with silence just to pass validation.

**Combined audio is too long:** remove irrelevant roles and duplicate attachments, then shorten VR samples at natural boundaries while keeping each valid. Use one good reference per required voice when supported. For many speakers, allocate the ≤30.0-second planning budget explicitly before cropping. If exact dialogue itself exceeds the available budget, split at meaningful dialogue/action boundaries into supported production units without losing words or changing voices. Material changes to the approved table go back through G5; a technically equivalent crop from the same approved voice needs only revalidation, not a new creative gate.

**HTTP 400 InvalidParameter:** inspect the named entry if present, the actual outgoing list, measured durations, and total. Correct the implicated asset/payload first. Never retry an unchanged 400 request, switch model silently, drop a required voice, or shorten the user's film merely to fix input references. Record the error category without storing private request IDs in shared documents. After the runner's bounded repair limit, offer concrete native Question choices instead of looping or asking for a chat reply.
