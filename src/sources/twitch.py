"""Twitch source processor for brother.skill"""


class TwitchSource:
    """Process Twitch clips, VODs, and chat logs."""

    def process_clip(self, url: str) -> dict:
        """Process a Twitch clip URL."""
        return {
            "source": "twitch",
            "url": url,
            "type": "clip",
            "signals": {
                "chat_messages": [],
                "emotes_used": [],
                "rage_moments": [],
                "hype_moments": [],
            }
        }

    def process_chat_log(self, messages: list) -> dict:
        """Process Twitch chat messages to extract bro signals."""
        total = len(messages)
        if total == 0:
            return {"message_count": 0}

        caps_messages = sum(1 for m in messages if m.get("content", "").isupper())
        emote_messages = sum(1 for m in messages if self._has_emotes(m.get("content", "")))

        return {
            "message_count": total,
            "caps_ratio": round(caps_messages / total, 2),
            "emote_ratio": round(emote_messages / total, 2),
            "energy_indicator": min(10, int((caps_messages / total) * 15)),
            "frequent_emotes": self._top_emotes(messages),
        }

    def _has_emotes(self, text: str) -> bool:
        """Check if message contains common Twitch emotes."""
        common_emotes = ["PogChamp", "KEKW", "LUL", "Kreygasm", "monkaS",
                         "OMEGALUL", "PepeHands", "Sadge", "COPIUM", "EZ"]
        return any(e in text for e in common_emotes)

    def _top_emotes(self, messages: list, top_n: int = 5) -> list:
        """Find most frequently used emotes."""
        emote_counts = {}
        for msg in messages:
            for word in msg.get("content", "").split():
                if word[0].isupper() and len(word) > 3 and word.isalpha():
                    emote_counts[word] = emote_counts.get(word, 0) + 1
        return sorted(emote_counts, key=emote_counts.get, reverse=True)[:top_n]
