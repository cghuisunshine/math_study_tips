import unittest
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = ROOT / "index.html"


class IndexChineseModeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX_HTML.read_text(encoding="utf-8")

    def test_has_accessible_language_switch(self):
        self.assertIn('id="enModeButton"', self.html)
        self.assertIn('id="zhModeButton"', self.html)
        self.assertIn('aria-pressed="true"', self.html)

    def test_reuses_existing_chinese_read_aloud_assets(self):
        self.assertIn(
            "math-study-read-aloud/generated-audio/math-study.words.json",
            self.html,
        )
        self.assertIn(
            "math-study-read-aloud/generated-audio/math-study.mp3",
            self.html,
        )

    def test_keeps_language_progress_separate(self):
        self.assertIn("aligned-reader-progress:en:", self.html)
        self.assertIn("aligned-reader-progress:zh:", self.html)

    def test_contains_chinese_timed_word_rendering(self):
        self.assertIn("function renderChineseReader", self.html)
        self.assertIn("tts-word", self.html)
        self.assertIn("start_char", self.html)
        self.assertIn("end_char", self.html)

    def test_contains_mode_switching_handler(self):
        self.assertIn("async function switchMode", self.html)
        self.assertIn("zhModeButton.addEventListener", self.html)
        self.assertIn("enModeButton.addEventListener", self.html)

    def test_direct_file_mode_falls_back_to_existing_chinese_page(self):
        self.assertIn("function renderChineseFileFallback", self.html)
        self.assertIn(
            "math-study-read-aloud/math-study-read-aloud.html",
            self.html,
        )
        self.assertIn("chinese-file-fallback", self.html)

    def test_direct_file_audio_avoids_fetch_cors_error(self):
        source_function = re.search(
            r"async function setAudioSource\(source\) \{(?P<body>.*?)\n    \}",
            self.html,
            re.DOTALL,
        )
        self.assertIsNotNone(source_function)
        self.assertIn(
            "if (location.protocol === 'file:')",
            source_function.group("body"),
        )


if __name__ == "__main__":
    unittest.main()
