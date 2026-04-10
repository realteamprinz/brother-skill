#!/usr/bin/env python3
"""Example: Distill a bro from your own manual description."""

from src.distiller import BroDistiller
from src.sources.manual import ManualSource
from src.profile.builder import ProfileBuilder
from src.profile.archetypes import detect_archetype
from src.interaction.voice import BroVoice

# Describe your bro
description = """
Mike is the quiet one in our group chat. He barely messages — maybe once every
20 messages from everyone else. But when he does type something, the whole chat
goes silent and then everyone sends the skull emoji. His humor is extremely dry
and deadpan. He never uses exclamation marks. His go-to move is responding to
a 10-message argument with a single sentence that somehow addresses everything
and makes everyone feel stupid. He's been like this since high school. His
catchphrase is literally just "interesting" — but the way he uses it somehow
conveys judgment, amusement, and dismissal all at once.
"""

# Process manually
source = ManualSource()
data = source.process_text(description)

print("Extracted signals:")
for key, value in data["signals"].items():
    print(f"  {key}: {value}")
print()

# Build profile
builder = ProfileBuilder()
profile = builder.build(
    name="Mike",
    raw_data=data,
    source_type="manual"
)

# Detect archetype
archetype = detect_archetype(profile)
profile["archetype"] = archetype

print(f"Name: {profile['name']}")
print(f"Archetype: {archetype['name']} {archetype['emoji']}")
print(f"Description: {archetype['description']}")
print(f"Confidence: {archetype['confidence']}")
print()

# Generate voice
voice = BroVoice(profile)
print(f"Greeting: {voice.get_greeting()}")
print()
print("System prompt for interaction mode:")
print(voice.generate_response(""))
