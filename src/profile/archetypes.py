"""Bro archetype detection and classification."""

BRO_ARCHETYPES = {
    "hype_man": {
        "name": "The Hype Man",
        "emoji": "\U0001f50a",
        "description": "Maximum energy, always screaming, makes everything an event",
        "famous": "IShowSpeed",
        "signals": ["high volume", "exclamation marks", "CAPS LOCK", "hype words",
                     "lets go", "insane", "crazy"],
        "energy_range": (8, 10),
        "humor_style": "volume_is_the_joke",
        "group_role": "gets_everyone_excited",
    },
    "roast_master": {
        "name": "The Roast Master",
        "emoji": "\U0001f3af",
        "description": "Surgically precise insults delivered with a straight face",
        "famous": "KSI",
        "signals": ["sarcasm", "comebacks", "wit", "deadpan delivery",
                     "burns", "savage", "ratio"],
        "energy_range": (4, 7),
        "humor_style": "surgical_precision",
        "group_role": "keeps_egos_in_check",
    },
    "cool_bro": {
        "name": "The Cool Bro",
        "emoji": "\U0001f9ca",
        "description": "Chill energy, speaks rarely, but when they do — everyone listens",
        "famous": "Keanu Reeves",
        "signals": ["short responses", "calm tone", "rare but impactful",
                     "chill", "relaxed", "understated"],
        "energy_range": (2, 4),
        "humor_style": "understatement",
        "group_role": "respected_anchor",
    },
    "chaos_agent": {
        "name": "The Chaos Agent",
        "emoji": "\U0001f921",
        "description": "Does things nobody asked for, somehow it works",
        "famous": "Jake Paul",
        "signals": ["unpredictable", "escalation", "boundary pushing",
                     "impulsive", "wild", "random"],
        "energy_range": (7, 10),
        "humor_style": "shock_value",
        "group_role": "makes_things_interesting",
    },
    "strategy_bro": {
        "name": "The Strategy Bro",
        "emoji": "\U0001f9e0",
        "description": "Turns everything into a business plan or a life lesson",
        "famous": "MrBeast",
        "signals": ["optimization", "systems thinking", "metrics",
                     "plan", "strategy", "growth"],
        "energy_range": (5, 7),
        "humor_style": "dry_wit",
        "group_role": "channels_chaos_productively",
    },
    "silent_killer": {
        "name": "The Silent Killer",
        "emoji": "\U0001f636",
        "description": "Quiet for 20 minutes then drops one line that destroys everyone",
        "famous": "That one friend. You know who.",
        "signals": ["low frequency", "high impact", "perfect timing",
                     "quiet", "lurker", "one liner"],
        "energy_range": (1, 3),
        "humor_style": "economy_of_words",
        "group_role": "drops_bombs_then_goes_quiet",
    },
    "meme_lord": {
        "name": "The Meme Lord",
        "emoji": "\U0001f4f1",
        "description": "Communicates exclusively in memes and reaction images",
        "famous": "Every group chat has one",
        "signals": ["image responses", "references", "reaction gifs",
                     "meme", "lmao", "dead"],
        "energy_range": (3, 6),
        "humor_style": "visual_contextual",
        "group_role": "communicates_in_images",
    },
    "storyteller": {
        "name": "The Storyteller",
        "emoji": "\U0001f3ad",
        "description": "Every experience becomes a 10-minute dramatic retelling",
        "famous": "Your funniest friend",
        "signals": ["long messages", "dramatic buildup", "sound effects in text",
                     "okay so basically", "you won't believe", "I swear"],
        "energy_range": (6, 9),
        "humor_style": "narrative_buildup",
        "group_role": "commands_the_floor",
    },
}


def detect_archetype(profile: dict) -> dict:
    """Detect the primary bro archetype from a profile.

    Scores each archetype based on energy range match and signal keyword
    presence in the profile data. Returns the highest-scoring archetype.
    """
    scores = {}

    energy = profile.get("energy_level", 5)

    profile_text = str(profile).lower()

    for key, archetype in BRO_ARCHETYPES.items():
        score = 0

        # Energy range match
        low, high = archetype["energy_range"]
        if low <= energy <= high:
            score += 3

        # Signal keyword matches
        for signal in archetype["signals"]:
            if signal.lower() in profile_text:
                score += 1

        scores[key] = score

    best = max(scores, key=scores.get)
    result = dict(BRO_ARCHETYPES[best])
    result["confidence"] = round(scores[best] / (3 + len(BRO_ARCHETYPES[best]["signals"])), 2)
    result["all_scores"] = {k: scores[k] for k in sorted(scores, key=scores.get, reverse=True)}
    return result


def get_archetype(name: str) -> dict:
    """Get a specific archetype by key name."""
    return BRO_ARCHETYPES.get(name, {})


def list_archetypes() -> list:
    """List all available archetypes."""
    return [{"key": k, **v} for k, v in BRO_ARCHETYPES.items()]
