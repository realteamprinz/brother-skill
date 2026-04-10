"""Tests for the BroDistiller core engine."""

import pytest
from src.distiller import BroDistiller


class TestBroDistiller:
    """Test suite for BroDistiller."""

    def test_supported_sources(self):
        """All expected source types should be supported."""
        expected = ["youtube", "tiktok", "twitch", "twitter",
                    "discord", "wechat", "groupchat", "manual"]
        for source in expected:
            distiller = BroDistiller(source_type=source)
            assert distiller.source_type == source

    def test_invalid_source_raises(self):
        """Invalid source type should raise ValueError."""
        with pytest.raises(ValueError, match="Unknown source"):
            BroDistiller(source_type="invalid_source")

    def test_load_from_file_not_found(self):
        """Loading from nonexistent file should raise FileNotFoundError."""
        distiller = BroDistiller(source_type="manual")
        with pytest.raises(FileNotFoundError):
            distiller.load_from_file("/nonexistent/path/file.txt")

    def test_youtube_loader_returns_dict(self):
        """YouTube loader should return a dict with expected keys."""
        distiller = BroDistiller(source_type="youtube")
        result = distiller.load_from_url("https://youtube.com/watch?v=test123")
        assert isinstance(result, dict)
        assert result["source"] == "youtube"
        assert result["type"] == "video"
        assert result["url"] == "https://youtube.com/watch?v=test123"

    def test_tiktok_loader_returns_dict(self):
        """TikTok loader should return short_video type."""
        distiller = BroDistiller(source_type="tiktok")
        result = distiller.load_from_url("https://tiktok.com/@user/video/123")
        assert result["source"] == "tiktok"
        assert result["type"] == "short_video"

    def test_twitter_loader_returns_dict(self):
        """Twitter loader should return posts type."""
        distiller = BroDistiller(source_type="twitter")
        result = distiller.load_from_url("https://x.com/user")
        assert result["source"] == "twitter"
        assert result["type"] == "posts"

    def test_manual_loader_returns_dict(self):
        """Manual loader without file should return description type."""
        distiller = BroDistiller(source_type="manual")
        result = distiller._load_manual()
        assert result["source"] == "manual"
        assert result["type"] == "description"

    def test_groupchat_loader_from_file(self, tmp_path):
        """Group chat loader should parse a text file."""
        chat_file = tmp_path / "chat.txt"
        chat_file.write_text("Mike: hey what's up\nDave: not much\nMike: cool\n")

        distiller = BroDistiller(source_type="groupchat")
        result = distiller.load_from_file(str(chat_file))
        assert result["source"] == "groupchat"
        assert result["type"] == "chat"
        assert "Mike" in result["content"]

    def test_discord_loader_from_file(self, tmp_path):
        """Discord loader should parse a JSON export."""
        import json
        chat_file = tmp_path / "discord.json"
        messages = [
            {"author": {"name": "Dave"}, "content": "yo what's up"},
            {"author": {"name": "Mike"}, "content": "not much"},
        ]
        chat_file.write_text(json.dumps(messages))

        distiller = BroDistiller(source_type="discord")
        result = distiller.load_from_file(str(chat_file))
        assert result["source"] == "discord"
        assert result["type"] == "chat"
        assert len(result["messages"]) == 2
