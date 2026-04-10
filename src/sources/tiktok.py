"""TikTok/Douyin source processor for brother.skill"""


class TikTokSource:
    """Process TikTok and Douyin short-form video content."""

    def process_url(self, url: str) -> dict:
        """Process a TikTok/Douyin video URL."""
        return {
            "source": "tiktok",
            "url": url,
            "type": "short_video",
            "signals": {
                "captions": None,
                "sounds": [],
                "hashtags": [],
                "comments": [],
            }
        }

    def process_saved_clip(self, filepath: str) -> dict:
        """Process a locally saved TikTok clip."""
        return {
            "source": "tiktok",
            "filepath": filepath,
            "type": "short_video",
            "signals": {}
        }

    def extract_signals(self, data: dict) -> dict:
        """Extract bro signals from TikTok content."""
        return {
            "energy_indicator": self._estimate_energy(data),
            "humor_type": "short_form",
            "viral_potential": self._assess_viral_markers(data),
        }

    def _estimate_energy(self, data: dict) -> int:
        """Estimate energy level from short-form content signals."""
        score = 5
        captions = data.get("signals", {}).get("captions", "") or ""
        if captions.count("!") > 3:
            score += 2
        if any(w.isupper() for w in captions.split() if len(w) > 2):
            score += 1
        return min(10, score)

    def _assess_viral_markers(self, data: dict) -> list:
        """Identify viral content markers — trends, sounds, formats."""
        return data.get("signals", {}).get("hashtags", [])
