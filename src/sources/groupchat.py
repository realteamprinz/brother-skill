"""Generic group chat source processor for brother.skill"""

from pathlib import Path


class GroupChatSource:
    """Process generic group chat text exports from any platform."""

    def process_export(self, filepath: str) -> dict:
        """Process a group chat text export."""
        path = Path(filepath)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        messages = self._parse_messages(content)
        authors = set(m["author"] for m in messages)

        return {
            "source": "groupchat",
            "filepath": filepath,
            "type": "chat",
            "message_count": len(messages),
            "author_count": len(authors),
            "signals": self.extract_signals(messages),
        }

    def extract_signals(self, messages: list) -> dict:
        """Extract group dynamics and individual bro signals."""
        if not messages:
            return {}

        by_author = {}
        for msg in messages:
            name = msg["author"]
            by_author.setdefault(name, []).append(msg["content"])

        profiles = {}
        for name, texts in by_author.items():
            profiles[name] = {
                "message_count": len(texts),
                "avg_length": round(sum(len(t) for t in texts) / len(texts), 1),
                "caps_ratio": round(sum(1 for t in texts if t.isupper()) / len(texts), 2),
                "initiates_conversations": self._is_initiator(name, messages),
                "responds_to_others": self._response_rate(name, messages),
                "group_role_signals": self._detect_role(name, texts),
            }

        return {
            "author_profiles": profiles,
            "group_dynamics": self._analyze_dynamics(messages, by_author),
        }

    def _parse_messages(self, content: str) -> list:
        """Parse raw chat export into structured messages."""
        messages = []
        for line in content.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            if ":" in line:
                author, text = line.split(":", 1)
                messages.append({"author": author.strip(), "content": text.strip()})
        return messages

    def _is_initiator(self, name: str, messages: list) -> bool:
        """Check if this person tends to start conversations."""
        if not messages:
            return False
        first_messages = []
        prev_author = None
        gap_count = 0
        for msg in messages:
            if prev_author is None or msg["author"] != prev_author:
                gap_count += 1
                if gap_count <= 10:
                    first_messages.append(msg["author"])
            prev_author = msg["author"]
        return first_messages.count(name) > len(first_messages) / len(set(m["author"] for m in messages))

    def _response_rate(self, name: str, messages: list) -> float:
        """Calculate how often this person responds to others."""
        responses = 0
        opportunities = 0
        prev_author = None
        for msg in messages:
            if prev_author and prev_author != name:
                opportunities += 1
                if msg["author"] == name:
                    responses += 1
            prev_author = msg["author"]
        return round(responses / max(opportunities, 1), 2)

    def _detect_role(self, name: str, texts: list) -> list:
        """Detect group role signals from message patterns."""
        roles = []
        avg_len = sum(len(t) for t in texts) / max(len(texts), 1)
        caps_count = sum(1 for t in texts if t.isupper())

        if caps_count / max(len(texts), 1) > 0.3:
            roles.append("hype_man")
        if avg_len < 20 and len(texts) < len(texts) * 0.5:
            roles.append("silent_killer")
        if avg_len > 100:
            roles.append("storyteller")
        if any("http" in t or "[image]" in t.lower() for t in texts):
            roles.append("meme_lord")
        return roles

    def _analyze_dynamics(self, messages: list, by_author: dict) -> dict:
        """Analyze group-level dynamics."""
        authors = list(by_author.keys())
        total = len(messages)
        return {
            "most_active": max(authors, key=lambda a: len(by_author[a])),
            "least_active": min(authors, key=lambda a: len(by_author[a])),
            "message_distribution": {a: round(len(msgs) / total, 2) for a, msgs in by_author.items()},
        }
