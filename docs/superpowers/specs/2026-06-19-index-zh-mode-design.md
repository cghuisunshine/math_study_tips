# Index Chinese Mode Design

## Goal

Add an inline `En / Zh` mode switch to `index.html`. English remains the current aligned paragraph reader. Chinese uses the text, `zh-CN-XiaoxiaoNeural` audio, and word timing data already produced by `math-study-read-aloud`.

## User Interface

- Add a compact two-button language switch to the existing top bar.
- `En` is selected initially.
- The selected button uses the existing dark button color and exposes `aria-pressed="true"`.
- Switching language pauses playback before replacing the content and audio source.
- Keep the existing sidebar, reader surface, player, and responsive layout.

## English Mode

- Preserve the existing chapter manifest and paragraph-level highlighting.
- Preserve chapter navigation, previous/next controls, seeking, and English progress.
- Keep the current title and English labels.

## Chinese Mode

- Load `math-study-read-aloud/generated-audio/math-study.words.json`.
- Load `math-study-read-aloud/generated-audio/math-study.mp3`.
- Split the canonical Chinese text on blank lines and render one reader paragraph per block.
- Render timed words as safe DOM text spans using the timing character offsets.
- Highlight the active word and its containing paragraph from `audio.currentTime`.
- Use one Chinese chapter named `把苦学转化为稳定发挥`.
- Disable previous/next controls because Chinese mode has one chapter.
- Keep click-to-seek behavior on Chinese paragraphs.
- Show Chinese player labels while Chinese mode is active.

## State and Progress

- Store the selected mode in local storage.
- Store English and Chinese playback positions under separate keys.
- Restore each mode's last position when switching back to it.
- If Chinese timing data cannot be loaded or validated, show a clear inline error and keep playback disabled.

## Testing

- Add a static regression test that checks the language switch, Chinese asset paths, separate progress keys, timed-word rendering, and mode-switch handler.
- Verify the test fails before implementation and passes after implementation.
- Run the page through a local HTTP server and exercise `En → Zh → En` in a browser.

