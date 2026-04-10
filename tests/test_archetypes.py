"""Tests for bro archetype detection."""

import pytest
from src.profile.archetypes import (
    BRO_ARCHETYPES,
    detect_archetype,
    get_archetype,
    list_archetypes,
)


class TestArchetypes:
    """Test suite for archetype detection and classification."""

    def test_all_archetypes_defined(self):
        """All 8 archetypes should be defined."""
        assert len(BRO_ARCHETYPES) == 8
        expected_keys = [
            "hype_man", "roast_master", "cool_bro", "chaos_agent",
            "strategy_bro", "silent_killer", "meme_lord", "storyteller"
        ]
        for key in expected_keys:
            assert key in BRO_ARCHETYPES

    def test_archetype_structure(self):
        """Each archetype should have required fields."""
        required_fields = ["name", "emoji", "description", "famous",
                           "signals", "energy_range"]
        for key, archetype in BRO_ARCHETYPES.items():
            for field in required_fields:
                assert field in archetype, f"{key} missing {field}"

    def test_energy_ranges_valid(self):
        """Energy ranges should be valid (low <= high, within 1-10)."""
        for key, archetype in BRO_ARCHETYPES.items():
            low, high = archetype["energy_range"]
            assert 1 <= low <= 10, f"{key} low energy out of range"
            assert 1 <= high <= 10, f"{key} high energy out of range"
            assert low <= high, f"{key} low > high energy"

    def test_detect_hype_man(self):
        """High energy profile with hype signals should detect as Hype Man."""
        profile = {
            "energy_level": 9,
            "volume_level": 10,
            "humor_type": "hype",
            "description": "CAPS LOCK exclamation marks high volume lets go",
        }
        result = detect_archetype(profile)
        assert "Hype Man" in result["name"]

    def test_detect_silent_killer(self):
        """Low energy profile with precision signals should detect as Silent Killer."""
        profile = {
            "energy_level": 2,
            "volume_level": 1,
            "humor_type": "deadpan",
            "description": "low frequency high impact perfect timing quiet lurker one liner",
        }
        result = detect_archetype(profile)
        assert "Silent Killer" in result["name"]

    def test_detect_returns_confidence(self):
        """Detection result should include confidence score."""
        profile = {"energy_level": 5}
        result = detect_archetype(profile)
        assert "confidence" in result
        assert 0 <= result["confidence"] <= 1

    def test_detect_returns_all_scores(self):
        """Detection result should include scores for all archetypes."""
        profile = {"energy_level": 5}
        result = detect_archetype(profile)
        assert "all_scores" in result
        assert len(result["all_scores"]) == 8

    def test_get_archetype_valid(self):
        """get_archetype should return archetype dict for valid key."""
        result = get_archetype("hype_man")
        assert result["name"] == "The Hype Man"

    def test_get_archetype_invalid(self):
        """get_archetype should return empty dict for invalid key."""
        result = get_archetype("nonexistent")
        assert result == {}

    def test_list_archetypes(self):
        """list_archetypes should return all 8 archetypes."""
        result = list_archetypes()
        assert len(result) == 8
        assert all("key" in a for a in result)
        assert all("name" in a for a in result)
