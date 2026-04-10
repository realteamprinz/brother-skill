#!/usr/bin/env python3
"""Example: Distill your group chat bros from a chat export."""

from src.distiller import BroDistiller
from src.sources.groupchat import GroupChatSource
from src.profile.builder import ProfileBuilder
from src.profile.archetypes import detect_archetype
from src.interaction.groupchat_sim import GroupChatSimulator

# Process a group chat export
source = GroupChatSource()
data = source.process_export("examples/sample_groupchat.txt")

print(f"Found {data['author_count']} participants")
print(f"Total messages: {data['message_count']}")
print()

# Build profiles for each participant
builder = ProfileBuilder()
profiles = []

for name, signals in data["signals"].get("author_profiles", {}).items():
    profile = builder.build(
        name=name,
        raw_data={"signals": signals, "messages": []},
        source_type="groupchat"
    )
    archetype = detect_archetype(profile)
    profile["archetype"] = archetype
    profiles.append(profile)
    print(f"{name}: {archetype['name']} {archetype['emoji']} (energy: {profile.get('energy_level', '?')}/10)")

print()

# Simulate group dynamics
if len(profiles) >= 2:
    sim = GroupChatSimulator(profiles)
    dynamics = sim.predict_dynamics()
    print("Group Dynamics:")
    print(f"  Most active: {dynamics['most_active']}")
    print(f"  Least active: {dynamics['least_active']}")
    print(f"  Drama starter: {dynamics['drama_starter']}")
    print(f"  Peacemaker: {dynamics['peacemaker']}")
    print(f"  Chaos potential: {dynamics['chaos_potential']}")
