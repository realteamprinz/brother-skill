"""Voice simulation for brother.skill — respond in a bro's voice."""

from pathlib import Path
import json


class BroVoice:
    """Respond in a distilled bro's voice, slang, and energy."""

    def __init__(self, profile: dict):
        self.profile = profile
        self.name = profile.get("name", "Bro")
        self.energy = profile.get("energy_level", 5)
        self.archetype = profile.get("archetype", {})

    def generate_response(self, prompt: str) -> str:
        """Generate a response in this bro's voice.

        Uses the profile dimensions to shape tone, vocabulary, and energy.
        The actual LLM call happens upstream — this builds the system prompt.
        """
        return self._build_system_prompt()

    def _build_system_prompt(self) -> str:
        """Build a system prompt that captures this bro's voice."""
        voice = self.profile.get("voice", {})
        comedy = self.profile.get("comedy", {})
        archetype_name = self.archetype.get("name", "Unknown")
        archetype_desc = self.archetype.get("description", "")

        catchphrases = voice.get("catchphrases", [])
        slang = voice.get("slang_vocabulary", [])
        volume = voice.get("volume_level", self.energy)
        humor = comedy.get("humor_type", "")

        prompt_parts = [
            f"You are {self.name}.",
            f"Archetype: {archetype_name} — {archetype_desc}",
            f"Energy level: {self.energy}/10.",
            f"Volume level: {volume}/10.",
        ]

        if catchphrases:
            prompt_parts.append(f"Catchphrases you use: {', '.join(catchphrases)}")
        if slang:
            prompt_parts.append(f"Slang you use: {', '.join(slang)}")
        if humor:
            prompt_parts.append(f"Humor style: {humor}")

        prompt_parts.extend([
            "",
            "Rules:",
            "- Stay in character at all times",
            "- Match the energy level consistently",
            "- Use catchphrases naturally, not forced",
            "- Roasts come from love, never be actually mean",
            "- If you would say something offensive, soften it but keep the energy",
        ])

        if self.energy >= 8:
            prompt_parts.append("- Use CAPS for emphasis. Exclamation marks are your friend!")
        elif self.energy <= 3:
            prompt_parts.append("- Keep responses short. Less is more. Let silence do the work.")

        return "\n".join(prompt_parts)

    def get_greeting(self) -> str:
        """Get this bro's characteristic greeting."""
        greetings_by_energy = {
            (1, 3): ["hey.", "sup.", "yo."],
            (4, 6): ["what's good", "hey what's up", "yo what's going on"],
            (7, 8): ["YO! What's up!", "Ayyyy let's go!", "What's GOOD bro!"],
            (9, 10): ["YOOOOO!! WHAT'S GOOD!!", "LET'S GOOOOO!!", "BRO!! WHAT'S UP!!"],
        }
        for (low, high), greetings in greetings_by_energy.items():
            if low <= self.energy <= high:
                return greetings[0]
        return "hey"
