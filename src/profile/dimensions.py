"""All profile dimensions for brother.skill bro profiles."""

DIMENSIONS = {
    "voice": {
        "name": "Voice & Language",
        "fields": {
            "catchphrases": {"type": "list", "description": "Signature lines they repeat constantly"},
            "slang_vocabulary": {"type": "list", "description": "Words they overuse"},
            "speech_pattern": {"type": "str", "description": "Fast talker, slow drawl, screamer, mumbler"},
            "greeting": {"type": "str", "description": "How they greet people"},
            "goodbye": {"type": "str", "description": "How they say goodbye"},
            "go_to_insult": {"type": "str", "description": "Their default insult"},
            "go_to_compliment": {"type": "str", "description": "Their default compliment (if they give one)"},
            "volume_level": {"type": "int", "range": (1, 10), "description": "Whisper to MAXIMUM VOLUME"},
        }
    },
    "comedy": {
        "name": "Comedy Style",
        "fields": {
            "humor_type": {"type": "str", "description": "roast, sarcasm, slapstick, deadpan, absurdist, shock, storytelling, self-deprecating"},
            "timing": {"type": "str", "description": "Instant comeback, slow burn, delayed punchline"},
            "signature_move": {"type": "str", "description": "Funny face, gesture, sound effect, physical comedy"},
            "always_jokes_about": {"type": "list", "description": "Topics they always joke about"},
            "never_jokes_about": {"type": "list", "description": "The line they don't cross"},
            "handles_roasts_by": {"type": "str", "description": "Laughs it off, escalates, fake mad, actually mad"},
        }
    },
    "energy": {
        "name": "Energy & Vibe",
        "fields": {
            "default_level": {"type": "int", "range": (1, 10), "description": "Default energy level"},
            "peak_trigger": {"type": "str", "description": "What triggers peak energy"},
            "quiet_trigger": {"type": "str", "description": "What makes them go quiet"},
            "group_role": {"type": "str", "description": "Leader, hype man, quiet bomber, instigator, peacemaker"},
            "entrance_energy": {"type": "str", "description": "How you know they arrived"},
        }
    },
    "content": {
        "name": "Content Personality",
        "fields": {
            "platform": {"type": "str", "description": "YouTube, TikTok, Douyin, Twitch, Bilibili, X, Instagram"},
            "content_style": {"type": "str", "description": "Vlogs, reactions, pranks, gaming, commentary, comedy skits"},
            "upload_pattern": {"type": "str", "description": "Daily, weekly, sporadic, binge uploads"},
            "audience_interaction": {"type": "str", "description": "Reads comments, ignores, fights with comments"},
            "collab_chemistry": {"type": "list", "description": "Who they work best with"},
            "evolution": {"type": "str", "description": "How their content/personality has changed"},
        }
    },
    "relationship": {
        "name": "Relationship With You",
        "fields": {
            "how_found": {"type": "str", "description": "Real life, algorithm, friend, went viral"},
            "inside_jokes": {"type": "list", "description": "Shared jokes or running gags"},
            "learned_from": {"type": "str", "description": "What you've learned from them"},
            "favorite_moment": {"type": "str", "description": "The moment you always go back to"},
            "zombie_survival_rating": {"type": "int", "range": (1, 10), "description": "Would they survive?"},
        }
    },
}


def get_dimension(name: str) -> dict:
    """Get a specific dimension definition."""
    return DIMENSIONS.get(name, {})


def get_all_fields() -> list:
    """Get a flat list of all profile fields."""
    fields = []
    for dim_key, dim in DIMENSIONS.items():
        for field_key, field in dim["fields"].items():
            fields.append({
                "dimension": dim_key,
                "field": field_key,
                "type": field["type"],
                "description": field["description"],
            })
    return fields
