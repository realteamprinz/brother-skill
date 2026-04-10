"""Build bro profiles from processed source data."""

from pathlib import Path
from datetime import datetime


class ProfileBuilder:
    """Builds structured bro profiles from raw distillation data."""

    def build(self, name: str, raw_data: dict, source_type: str) -> dict:
        """Build a bro profile from raw source data."""
        profile = {
            "name": name,
            "created": datetime.utcnow().isoformat(),
            "source_type": source_type,
            "data_points": 1,
            "voice": {},
            "comedy": {},
            "energy": {},
            "content": {},
            "relationship": {},
        }

        if source_type == "manual":
            profile = self._build_from_description(profile, raw_data)
        elif source_type in ("discord", "wechat", "groupchat"):
            profile = self._build_from_chat(profile, raw_data)
        elif source_type in ("youtube", "tiktok", "twitch"):
            profile = self._build_from_video(profile, raw_data)
        elif source_type == "twitter":
            profile = self._build_from_posts(profile, raw_data)

        return profile

    def _build_from_description(self, profile, raw_data):
        """Build profile from manual text description."""
        content = raw_data.get("content", "")
        profile["raw_description"] = content

        signals = raw_data.get("signals", {})
        energy_kw = signals.get("energy_keywords", {})
        high = energy_kw.get("high", 0)
        low = energy_kw.get("low", 0)
        if high > low:
            profile["energy_level"] = min(10, 5 + high)
        elif low > high:
            profile["energy_level"] = max(1, 5 - low)
        else:
            profile["energy_level"] = 5

        return profile

    def _build_from_chat(self, profile, raw_data):
        """Build profile from chat messages."""
        messages = raw_data.get("messages", [])
        profile["message_count"] = len(messages) if isinstance(messages, list) else 0
        signals = raw_data.get("signals", {})
        profile["data_points"] = profile["message_count"]

        author_profiles = signals.get("author_profiles", {})
        if author_profiles:
            first_author = next(iter(author_profiles.values()), {})
            profile["energy_level"] = first_author.get("energy_indicator", 5)

        return profile

    def _build_from_video(self, profile, raw_data):
        """Build profile from video content."""
        profile["video_url"] = raw_data.get("url", "")
        profile["energy_level"] = 7
        return profile

    def _build_from_posts(self, profile, raw_data):
        """Build profile from social media posts."""
        profile["post_url"] = raw_data.get("url", "")
        profile["energy_level"] = 6
        return profile

    def save_profile(self, profile: dict, filepath: Path):
        """Save profile as markdown."""
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        name = profile["name"]
        archetype = profile.get("archetype", {})
        archetype_name = archetype.get("name", "Unknown")
        archetype_emoji = archetype.get("emoji", "")
        archetype_desc = archetype.get("description", "")
        confidence = archetype.get("confidence", 0)
        data_points = profile.get("data_points", 1)

        confidence_label = "Low"
        if data_points > 50:
            confidence_label = "Very High"
        elif data_points > 20:
            confidence_label = "High"
        elif data_points > 5:
            confidence_label = "Medium"

        md = f"""# Bro Profile: {name}

> {archetype_emoji} Archetype: {archetype_name}
> {archetype_desc}
> Distilled: {profile['created']}
> Source: {profile['source_type']}
> Data points: {data_points} | Confidence: {confidence_label}

---

## Voice & Language
- Catchphrases: [extracted from source]
- Slang: [extracted from source]
- Volume level: {profile.get('energy_level', '?')}/10

## Comedy Style
- Humor type: [extracted from source]
- Timing: [extracted from source]

## Energy & Vibe
- Default energy: {profile.get('energy_level', '?')}/10
- Group role: [extracted from source]

## Memorable Moments
1. [from source data]

---

*This profile deepens with every new input. Keep feeding it content.*
*{data_points} data point(s) processed. Confidence: {confidence_label}.*
"""
        filepath.write_text(md, encoding="utf-8")

    def merge_profiles(self, existing: dict, new_data: dict) -> dict:
        """Merge new data into an existing profile. Never overwrite, always append."""
        existing["data_points"] = existing.get("data_points", 1) + 1
        existing["last_updated"] = datetime.utcnow().isoformat()

        for key in ["voice", "comedy", "energy", "content", "relationship"]:
            if key in new_data and isinstance(new_data[key], dict):
                existing.setdefault(key, {}).update(new_data[key])

        return existing
