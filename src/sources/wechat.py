"""WeChat source processor for brother.skill"""

from pathlib import Path


class WeChatSource:
    """Process WeChat message exports and screenshots."""

    def process_export(self, filepath: str) -> dict:
        """Process a WeChat chat export."""
        path = Path(filepath)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        messages = self._parse_messages(content)

        return {
            "source": "wechat",
            "filepath": filepath,
            "type": "chat",
            "message_count": len(messages),
            "signals": self.extract_signals(messages),
        }

    def extract_signals(self, messages: list) -> dict:
        """Extract bro signals from WeChat messages."""
        if not messages:
            return {}

        by_author = {}
        for msg in messages:
            name = msg.get("author", "unknown")
            by_author.setdefault(name, []).append(msg)

        return {
            "author_count": len(by_author),
            "total_messages": len(messages),
            "has_voice_messages": any(m.get("type") == "voice" for m in messages),
            "has_stickers": any(m.get("type") == "sticker" for m in messages),
            "chinese_internet_signals": self._detect_chinese_internet_culture(messages),
        }

    def _parse_messages(self, content: str) -> list:
        """Parse raw WeChat export text into structured messages."""
        messages = []
        for line in content.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            if ":" in line:
                author, text = line.split(":", 1)
                messages.append({
                    "author": author.strip(),
                    "content": text.strip(),
                    "type": "text",
                })
        return messages

    def _detect_chinese_internet_culture(self, messages: list) -> dict:
        """Detect Chinese internet culture markers."""
        texts = " ".join(m.get("content", "") for m in messages)
        return {
            "uses_internet_slang": any(term in texts for term in
                                       ["yyds", "666", "awsl", "xswl", "emo",
                                        "绝绝子", "内卷", "躺平", "社死"]),
            "uses_emoji_expressions": "哈哈" in texts or "笑死" in texts,
            "storytelling_style": texts.count("然后") > 5 or texts.count("就是说") > 3,
        }
