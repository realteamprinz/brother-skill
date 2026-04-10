"""X/Twitter source processor for brother.skill"""


class TwitterSource:
    """Process X/Twitter posts, replies, and profile data."""

    def process_profile(self, url: str) -> dict:
        """Process an X/Twitter profile URL."""
        return {
            "source": "twitter",
            "url": url,
            "type": "profile",
            "signals": {
                "tweets": [],
                "replies": [],
                "quote_tweets": [],
                "bio": "",
            }
        }

    def process_export(self, filepath: str) -> dict:
        """Process exported tweet data (JSON or CSV)."""
        return {
            "source": "twitter",
            "filepath": filepath,
            "type": "export",
            "signals": {}
        }

    def extract_signals(self, tweets: list) -> dict:
        """Extract bro signals from tweet collection."""
        if not tweets:
            return {}

        total = len(tweets)
        avg_length = sum(len(t.get("text", "")) for t in tweets) / total
        ratio_replies = sum(1 for t in tweets if t.get("text", "").startswith("@")) / total
        hot_take_ratio = sum(1 for t in tweets if self._is_hot_take(t.get("text", ""))) / total

        return {
            "avg_tweet_length": round(avg_length, 1),
            "reply_ratio": round(ratio_replies, 2),
            "hot_take_ratio": round(hot_take_ratio, 2),
            "humor_indicators": self._detect_humor(tweets),
            "common_topics": self._extract_topics(tweets),
        }

    def _is_hot_take(self, text: str) -> bool:
        """Detect hot take patterns."""
        indicators = ["unpopular opinion", "hot take", "i don't care what anyone says",
                      "nobody's ready for this", "ratio", "L take", "W take"]
        return any(i in text.lower() for i in indicators)

    def _detect_humor(self, tweets: list) -> dict:
        """Detect humor patterns in tweets."""
        sarcasm_markers = sum(1 for t in tweets if "/s" in t.get("text", "") or
                              t.get("text", "").endswith("..."))
        return {
            "sarcasm_indicator": min(10, sarcasm_markers),
            "emoji_heavy": sum(1 for t in tweets if
                               sum(1 for c in t.get("text", "") if ord(c) > 0x1F600) > 2),
        }

    def _extract_topics(self, tweets: list, top_n: int = 5) -> list:
        """Extract common hashtags and topics."""
        tags = {}
        for t in tweets:
            for word in t.get("text", "").split():
                if word.startswith("#"):
                    tags[word.lower()] = tags.get(word.lower(), 0) + 1
        return sorted(tags, key=tags.get, reverse=True)[:top_n]
