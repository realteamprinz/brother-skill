"""Core distillation engine for brother.skill"""

from pathlib import Path
import json


class BroDistiller:
    """Processes source materials into structured bro data."""

    SUPPORTED_SOURCES = [
        "youtube", "tiktok", "twitch", "twitter",
        "discord", "wechat", "groupchat", "manual"
    ]

    def __init__(self, source_type: str):
        if source_type not in self.SUPPORTED_SOURCES:
            raise ValueError(f"Unknown source: {source_type}")
        self.source_type = source_type
        self._loader = self._get_loader()

    def _get_loader(self):
        """Get the appropriate source loader."""
        loaders = {
            "youtube": self._load_youtube,
            "tiktok": self._load_tiktok,
            "twitch": self._load_twitch,
            "twitter": self._load_twitter,
            "discord": self._load_discord,
            "wechat": self._load_wechat,
            "groupchat": self._load_groupchat,
            "manual": self._load_manual,
        }
        return loaders[self.source_type]

    def load_from_url(self, url: str) -> dict:
        """Load source data from a URL."""
        return self._loader(url=url)

    def load_from_file(self, filepath: str) -> dict:
        """Load source data from a local file."""
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        return self._loader(filepath=str(path))

    def load_from_interactive(self) -> dict:
        """Load source data from interactive user input."""
        print("\nDescribe your bro. Include:")
        print("- How they talk (catchphrases, slang, volume)")
        print("- What makes them funny")
        print("- Their energy level and vibe")
        print("- Memorable moments or stories")
        print("- Their role in the group")
        print("\nType your description (press Enter twice to finish):\n")

        lines = []
        empty_count = 0
        while empty_count < 1:
            line = input()
            if line == "":
                empty_count += 1
            else:
                empty_count = 0
                lines.append(line)

        return {
            "source": "manual",
            "content": "\n".join(lines),
            "type": "description"
        }

    def _load_youtube(self, url=None, filepath=None):
        """Process YouTube content — transcripts, comments, clip analysis."""
        return {"source": "youtube", "url": url, "filepath": filepath, "type": "video"}

    def _load_tiktok(self, url=None, filepath=None):
        """Process TikTok/Douyin short-form video content."""
        return {"source": "tiktok", "url": url, "filepath": filepath, "type": "short_video"}

    def _load_twitch(self, url=None, filepath=None):
        """Process Twitch clips and VOD timestamps."""
        return {"source": "twitch", "url": url, "filepath": filepath, "type": "stream"}

    def _load_twitter(self, url=None, filepath=None):
        """Process X/Twitter posts and profile data."""
        return {"source": "twitter", "url": url, "filepath": filepath, "type": "posts"}

    def _load_discord(self, url=None, filepath=None):
        """Process Discord chat exports (.json format)."""
        if filepath:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return {"source": "discord", "messages": data, "type": "chat"}
        return {"source": "discord", "url": url, "type": "chat"}

    def _load_wechat(self, url=None, filepath=None):
        """Process WeChat message exports and screenshots."""
        return {"source": "wechat", "filepath": filepath, "type": "chat"}

    def _load_groupchat(self, url=None, filepath=None):
        """Process generic group chat text exports."""
        if filepath:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            return {"source": "groupchat", "content": content, "type": "chat"}
        return {"source": "groupchat", "type": "chat"}

    def _load_manual(self, url=None, filepath=None):
        """Process manual text descriptions."""
        if filepath:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            return {"source": "manual", "content": content, "type": "description"}
        return {"source": "manual", "type": "description"}
