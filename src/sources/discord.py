"""Discord source processor for brother.skill"""

import json
from pathlib import Path


class DiscordSource:
    """Process Discord chat log exports."""

    def process_export(self, filepath: str) -> dict:
        """Process a Discord chat export (.json format)."""
        path = Path(filepath)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        messages = data if isinstance(data, list) else data.get("messages", [])

        return {
            "source": "discord",
            "filepath": filepath,
            "type": "chat",
            "message_count": len(messages),
            "signals": self.extract_signals(messages),
        }

    def extract_signals(self, messages: list) -> dict:
        """Extract bro signals from Discord messages."""
        if not messages:
            return {}

        by_author = {}
        for msg in messages:
            author = msg.get("author", {})
            name = author.get("name", author) if isinstance(author, dict) else str(author)
            by_author.setdefault(name, []).append(msg)

        profiles = {}
        for name, msgs in by_author.items():
            profiles[name] = self._analyze_author(name, msgs)

        return {
            "author_count": len(by_author),
            "total_messages": len(messages),
            "author_profiles": profiles,
        }

    def _analyze_author(self, name: str, messages: list) -> dict:
        """Analyze a single author's message patterns."""
        texts = [m.get("content", "") for m in messages]
        total = len(texts)

        caps_ratio = sum(1 for t in texts if t.isupper() and len(t) > 3) / max(total, 1)
        avg_length = sum(len(t) for t in texts) / max(total, 1)
        emoji_count = sum(sum(1 for c in t if ord(c) > 0x1F600) for t in texts)
        meme_indicators = sum(1 for t in texts if self._is_meme_message(t))

        return {
            "name": name,
            "message_count": total,
            "avg_message_length": round(avg_length, 1),
            "caps_ratio": round(caps_ratio, 2),
            "emoji_per_message": round(emoji_count / max(total, 1), 2),
            "meme_ratio": round(meme_indicators / max(total, 1), 2),
            "energy_indicator": min(10, int(caps_ratio * 10) + int(avg_length / 50)),
            "catchphrase_candidates": self._find_catchphrases(texts),
        }

    def _is_meme_message(self, text: str) -> bool:
        """Detect if a message is likely a meme/image reference."""
        indicators = ["http", ".gif", ".png", ".jpg", "attachment", "[image]"]
        return any(i in text.lower() for i in indicators)

    def _find_catchphrases(self, texts: list, min_occurrences: int = 3) -> list:
        """Find repeated phrases across messages."""
        phrase_counts = {}
        for text in texts:
            normalized = text.lower().strip()
            if len(normalized) < 50:
                phrase_counts[normalized] = phrase_counts.get(normalized, 0) + 1
        return [p for p, c in sorted(phrase_counts.items(), key=lambda x: -x[1])
                if c >= min_occurrences][:5]
