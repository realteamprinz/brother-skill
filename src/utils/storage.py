"""Local file storage management for brother.skill"""

import json
from pathlib import Path
from datetime import datetime


class BroStorage:
    """Manages local storage of bro profiles and interaction logs."""

    DEFAULT_BASE = Path.home() / ".brother-skill" / "bros"

    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or self.DEFAULT_BASE
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def get_bro_dir(self, name: str) -> Path:
        """Get the directory for a specific bro."""
        safe_name = name.lower().replace(" ", "_")
        bro_dir = self.base_dir / safe_name
        bro_dir.mkdir(parents=True, exist_ok=True)
        return bro_dir

    def save_profile(self, name: str, profile_content: str):
        """Save a bro profile markdown file."""
        bro_dir = self.get_bro_dir(name)
        profile_path = bro_dir / "PROFILE.md"
        profile_path.write_text(profile_content, encoding="utf-8")

    def load_profile(self, name: str) -> str:
        """Load a bro profile markdown file."""
        bro_dir = self.get_bro_dir(name)
        profile_path = bro_dir / "PROFILE.md"
        if profile_path.exists():
            return profile_path.read_text(encoding="utf-8")
        return ""

    def log_interaction(self, name: str, entry: dict):
        """Append an interaction log entry (JSONL format). Never overwrites."""
        bro_dir = self.get_bro_dir(name)
        log_path = bro_dir / "interaction-log.jsonl"
        entry["timestamp"] = datetime.utcnow().isoformat()
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def get_interaction_log(self, name: str) -> list:
        """Read all interaction log entries for a bro."""
        bro_dir = self.get_bro_dir(name)
        log_path = bro_dir / "interaction-log.jsonl"
        if not log_path.exists():
            return []
        entries = []
        with open(log_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    entries.append(json.loads(line))
        return entries

    def list_bros(self) -> list:
        """List all distilled bros."""
        if not self.base_dir.exists():
            return []
        return [d.name for d in self.base_dir.iterdir()
                if d.is_dir() and (d / "PROFILE.md").exists()]

    def delete_bro(self, name: str) -> bool:
        """Delete a bro profile and all associated data."""
        import shutil
        bro_dir = self.get_bro_dir(name)
        if bro_dir.exists():
            shutil.rmtree(bro_dir)
            return True
        return False

    def get_data_point_count(self, name: str) -> int:
        """Count the number of data points (interaction log entries) for a bro."""
        return len(self.get_interaction_log(name))
