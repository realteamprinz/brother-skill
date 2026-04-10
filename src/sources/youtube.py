"""YouTube source processor for brother.skill"""

import re


class YouTubeSource:
    """Process YouTube clips and transcripts into bro signals."""

    def process_url(self, url: str) -> dict:
        """Process a YouTube video URL — extract transcript and metadata."""
        video_id = self._extract_video_id(url)
        return {
            "source": "youtube",
            "video_id": video_id,
            "url": url,
            "type": "video",
            "signals": {
                "transcript": None,
                "comments": [],
                "metadata": {},
            }
        }

    def process_transcript(self, text: str) -> dict:
        """Process raw transcript text into bro signals."""
        words = text.split()
        caps_ratio = sum(1 for w in words if w.isupper() and len(w) > 1) / max(len(words), 1)
        exclamation_count = text.count("!")
        avg_sentence_len = len(text) / max(text.count(".") + text.count("!") + text.count("?"), 1)

        return {
            "volume_indicator": min(10, int(caps_ratio * 20) + int(exclamation_count / 10)),
            "energy_indicator": min(10, int(caps_ratio * 15) + int(exclamation_count / 5)),
            "word_count": len(words),
            "avg_sentence_length": round(avg_sentence_len, 1),
            "catchphrase_candidates": self._find_repeated_phrases(text),
        }

    def _extract_video_id(self, url: str) -> str:
        """Extract video ID from YouTube URL."""
        patterns = [
            r'(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})',
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return ""

    def _find_repeated_phrases(self, text: str, min_occurrences: int = 3) -> list:
        """Find phrases that appear multiple times — potential catchphrases."""
        words = text.lower().split()
        phrases = {}
        for n in range(2, 5):
            for i in range(len(words) - n + 1):
                phrase = " ".join(words[i:i + n])
                phrases[phrase] = phrases.get(phrase, 0) + 1
        return [p for p, c in sorted(phrases.items(), key=lambda x: -x[1]) if c >= min_occurrences][:10]
