"""Manual description source processor for brother.skill"""

from pathlib import Path


class ManualSource:
    """Process manual text descriptions of a bro."""

    def process_text(self, text: str) -> dict:
        """Process a text description into bro signals."""
        return {
            "source": "manual",
            "type": "description",
            "content": text,
            "signals": self.extract_signals(text),
        }

    def process_file(self, filepath: str) -> dict:
        """Process a text file containing a bro description."""
        path = Path(filepath)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return self.process_text(content)

    def extract_signals(self, text: str) -> dict:
        """Extract bro signals from a freeform description."""
        text_lower = text.lower()
        words = text.split()

        return {
            "description_length": len(words),
            "energy_keywords": self._count_energy_keywords(text_lower),
            "humor_keywords": self._count_humor_keywords(text_lower),
            "relationship_keywords": self._count_relationship_keywords(text_lower),
            "mentioned_platforms": self._detect_platforms(text_lower),
        }

    def _count_energy_keywords(self, text: str) -> dict:
        """Count energy-related keywords to estimate default energy."""
        high_energy = ["loud", "screaming", "yelling", "hype", "crazy", "insane",
                       "wild", "chaotic", "maximum", "intense", "explodes"]
        low_energy = ["quiet", "calm", "chill", "relaxed", "laid back", "mellow",
                      "subtle", "understated", "zen", "peaceful"]
        return {
            "high": sum(1 for w in high_energy if w in text),
            "low": sum(1 for w in low_energy if w in text),
        }

    def _count_humor_keywords(self, text: str) -> dict:
        """Count humor-related keywords to classify comedy style."""
        categories = {
            "roast": ["roast", "insult", "burns", "savage", "destroy", "comeback"],
            "sarcasm": ["sarcastic", "sarcasm", "deadpan", "dry humor", "ironic"],
            "physical": ["slapstick", "physical comedy", "falls", "gestures", "faces"],
            "storytelling": ["story", "stories", "tells", "dramatic", "retelling"],
            "absurdist": ["absurd", "random", "nonsense", "weird", "bizarre"],
        }
        return {cat: sum(1 for w in words if w in text)
                for cat, words in categories.items()}

    def _count_relationship_keywords(self, text: str) -> dict:
        """Detect relationship type from description."""
        types = {
            "real_brother": ["brother", "sibling", "grew up", "family"],
            "friend": ["friend", "buddy", "homie", "bro", "squad", "group chat"],
            "online": ["youtube", "streamer", "tiktoker", "creator", "influencer",
                       "channel", "content"],
        }
        return {t: sum(1 for w in words if w in text) for t, words in types.items()}

    def _detect_platforms(self, text: str) -> list:
        """Detect mentioned platforms."""
        platforms = ["youtube", "tiktok", "douyin", "twitch", "twitter", "discord",
                     "wechat", "instagram", "bilibili", "reddit", "tik tok"]
        return [p for p in platforms if p in text]
