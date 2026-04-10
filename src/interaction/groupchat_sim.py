"""Group chat simulation for brother.skill."""


class GroupChatSimulator:
    """Simulate group chat conversations between multiple distilled bros."""

    def __init__(self, profiles: list):
        self.profiles = {p["name"]: p for p in profiles}
        self.names = list(self.profiles.keys())

    def simulate_conversation(self, topic: str, num_messages: int = 20) -> list:
        """Generate a simulated group chat conversation about a topic.

        Returns a list of message dicts with author and content.
        The actual generation uses LLM calls upstream — this builds the prompt.
        """
        return self._build_simulation_prompt(topic, num_messages)

    def _build_simulation_prompt(self, topic: str, num_messages: int) -> str:
        """Build the prompt for group chat simulation."""
        parts = [
            f"Simulate a group chat conversation about: {topic}",
            f"Generate exactly {num_messages} messages.",
            "",
            "Participants:",
        ]

        for name, profile in self.profiles.items():
            archetype = profile.get("archetype", {})
            energy = profile.get("energy_level", 5)
            parts.append(
                f"- {name}: {archetype.get('name', 'Unknown')} "
                f"(energy: {energy}/10) — {archetype.get('description', '')}"
            )

        parts.extend([
            "",
            "Rules:",
            "- Each person speaks in their own voice and style",
            "- Not everyone talks the same amount",
            "- The instigator starts drama, the peacemaker tries to calm it",
            "- Meme lords respond with [meme description] not words",
            "- Silent killers speak rarely but devastatingly",
            "- Match each person's actual energy level",
            "- Include realistic group dynamics (interruptions, tangents, callbacks)",
        ])

        return "\n".join(parts)

    def predict_dynamics(self) -> dict:
        """Predict how these bros would interact."""
        roles = {}
        for name, profile in self.profiles.items():
            archetype_key = profile.get("archetype", {}).get("name", "Unknown")
            energy = profile.get("energy_level", 5)
            roles[name] = {
                "archetype": archetype_key,
                "energy": energy,
                "predicted_message_share": self._predict_share(energy),
                "likely_role": self._predict_group_role(archetype_key, energy),
            }

        return {
            "participants": roles,
            "drama_starter": self._find_role("instigator", roles),
            "peacemaker": self._find_role("mediator", roles),
            "most_active": max(roles, key=lambda n: roles[n]["energy"]),
            "least_active": min(roles, key=lambda n: roles[n]["energy"]),
            "chaos_potential": self._calculate_chaos(roles),
        }

    def _predict_share(self, energy: int) -> float:
        """Predict message share based on energy level."""
        total_energy = sum(p.get("energy_level", 5) for p in self.profiles.values())
        return round(energy / max(total_energy, 1), 2)

    def _predict_group_role(self, archetype: str, energy: int) -> str:
        """Predict what role this person will play in the group."""
        role_map = {
            "The Hype Man": "energizer",
            "The Roast Master": "commentator",
            "The Cool Bro": "anchor",
            "The Chaos Agent": "instigator",
            "The Strategy Bro": "organizer",
            "The Silent Killer": "sniper",
            "The Meme Lord": "reactor",
            "The Storyteller": "narrator",
        }
        return role_map.get(archetype, "participant")

    def _find_role(self, role: str, roles: dict) -> str:
        """Find who fills a specific group role."""
        role_mapping = {
            "instigator": ["The Chaos Agent", "The Hype Man"],
            "mediator": ["The Cool Bro", "The Strategy Bro"],
        }
        target_archetypes = role_mapping.get(role, [])
        for name, info in roles.items():
            if info["archetype"] in target_archetypes:
                return name
        return self.names[0] if self.names else "unknown"

    def _calculate_chaos(self, roles: dict) -> str:
        """Calculate the chaos potential of this group combination."""
        avg_energy = sum(r["energy"] for r in roles.values()) / max(len(roles), 1)
        chaos_agents = sum(1 for r in roles.values() if "Chaos" in r["archetype"])
        anchors = sum(1 for r in roles.values() if r["archetype"] in ["The Cool Bro", "The Strategy Bro"])

        if chaos_agents >= 2 and anchors == 0:
            return "nuclear"
        elif avg_energy > 7:
            return "high"
        elif avg_energy > 5:
            return "medium"
        return "controlled"
