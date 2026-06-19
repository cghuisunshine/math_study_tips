# Index Chinese Mode Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an inline Chinese read-aloud mode to `index.html` using the existing Chinese audio and timing assets.

**Architecture:** Keep the existing single-page reader and introduce a small mode layer around its rendering, audio source, progress, labels, and highlighting. English continues to use the embedded manifest; Chinese fetches the existing timing JSON and renders timed word spans into the same reader.

**Tech Stack:** Standalone HTML/CSS/JavaScript, Python `unittest`, browser HTML5 Audio and Fetch APIs.

---

### Task 1: Add the regression contract

**Files:**
- Create: `tests/test_index_zh_mode.py`
- Test: `index.html`

- [ ] **Step 1: Write the failing test**

Create a `unittest` case that reads `index.html` and asserts it contains:

- `id="enModeButton"` and `id="zhModeButton"`
- the Chinese timing JSON and MP3 paths
- separate English and Chinese progress keys
- a Chinese timed-word renderer
- a mode switching function

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_index_zh_mode.py -v`

Expected: FAIL because the mode controls and Chinese integration are absent.

### Task 2: Implement inline language modes

**Files:**
- Modify: `index.html`
- Test: `tests/test_index_zh_mode.py`

- [ ] **Step 1: Add the mode switch markup and styles**

Add an accessible `En / Zh` switch beside the existing title/time region, using the project palette and existing button geometry.

- [ ] **Step 2: Add Chinese asset and state constants**

Define the Chinese JSON and MP3 paths, a selected-mode storage key, and separate progress keys.

- [ ] **Step 3: Add Chinese loading and validation**

Fetch the timing JSON once, validate text, words, timing bounds, and character offsets, then cache it.

- [ ] **Step 4: Add Chinese timed-text rendering**

Split canonical text by blank lines. Use text nodes and `.tts-word` spans for timed ranges. Attach paragraph click handlers that seek to the first timed word in each paragraph.

- [ ] **Step 5: Make playback UI mode-aware**

Route source loading, titles, navigation state, time labels, seek behavior, and highlighting through the active mode.

- [ ] **Step 6: Preserve mode-specific progress**

Save English chapter/paragraph progress and Chinese current time separately. Restore progress after the relevant audio metadata loads.

- [ ] **Step 7: Run test to verify it passes**

Run: `python3 -m unittest tests/test_index_zh_mode.py -v`

Expected: PASS.

### Task 3: Browser verification

**Files:**
- Verify: `index.html`

- [ ] **Step 1: Start a local server**

Run: `python3 -m http.server 8000`

- [ ] **Step 2: Exercise both modes**

Open `http://127.0.0.1:8000/index.html`, confirm English initially renders, switch to Chinese, confirm Chinese text and timed spans render, then switch back to English.

- [ ] **Step 3: Verify controls and console**

Confirm previous/next disable in Chinese mode, seek works, playback uses the Chinese MP3, and no console errors occur.

- [ ] **Step 4: Run final automated verification**

Run: `python3 -m unittest discover -s tests -v`

Expected: all tests pass.
