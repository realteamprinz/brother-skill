#!/usr/bin/env python3
"""Example: Distill Jake Paul from YouTube content."""

from src.distiller import BroDistiller
from src.profile.builder import ProfileBuilder
from src.profile.archetypes import detect_archetype

# Distill from a YouTube URL
distiller = BroDistiller(source_type="youtube")
raw_data = distiller.load_from_url("https://youtube.com/watch?v=example")

# Build profile
builder = ProfileBuilder()
profile = builder.build(
    name="Jake Paul",
    raw_data=raw_data,
    source_type="youtube"
)

# Detect archetype
archetype = detect_archetype(profile)
profile["archetype"] = archetype

print(f"Name: {profile['name']}")
print(f"Archetype: {archetype['name']} {archetype['emoji']}")
print(f"Description: {archetype['description']}")
print(f"Famous example: {archetype['famous']}")
print()
print("Expected profile traits:")
print("- Catchphrase: IT'S EVERYDAY BRO")
print("- Energy: 11/10 at all times")
print("- Humor: shock value + flexing + in-your-face")
print("- Handles criticism: doubles down, louder")
print("- Signature move: over-the-top reaction to everything")
