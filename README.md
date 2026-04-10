<div align="center">

# brother.skill

**Distill your bros.**

The ones who make you laugh until you can't breathe.
The ones who say stupid things that somehow make sense.
Online or offline — if they're your brother, this skill remembers everything.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-compatible-blue)](https://clawhub.ai)
[![Hermes](https://img.shields.io/badge/Hermes-compatible-purple)](https://github.com/NousResearch/hermes-agent)

</div>

---

## What is brother.skill?

An AI agent skill that distills the bros in your life — how they talk, what makes them funny, their catchphrases, their chaos energy. Feed it clips, screenshots, group chat logs, and stories. It learns to respond like them.

Works for:
- **Your actual brother** — the one who's been roasting you since you were born
- **Your group chat bros** — the boys, the squad, the homies
- **Online bros** — YouTubers, streamers, TikTokers you watch every day
- **Internet legends** — Jake Paul, Logan Paul, MrBeast, IShowSpeed, KSI, PewDiePie, and that one guy in your Discord

## How It Works

1. **Feed it content** — clips, screenshots, stories, group chat logs, descriptions
2. **It builds a bro profile** — voice, humor style, energy level, catchphrases, roast patterns
3. **Talk to your bro** — it responds in their voice, their slang, their energy
4. **It learns** — every new input makes the bro profile more accurate

## Examples

### Jake Paul

> "What would Jake Paul say about my bad day?"
>
> "BRO. BAD DAY? We don't DO bad days. You know what we do? We buy a Lamborghini and DRIVE THROUGH the bad day. IT'S EVERYDAY BRO."

### Logan Paul

> "Should I start a podcast?"
>
> "Bro. Everyone has a podcast. But not everyone has IMPAULSIVE. What's your hook? ... Actually just start it. Figure it out later. That's literally what I did."

### MrBeast

> "How do I get more views?"
>
> "Change your thumbnail. No seriously. Have you tried giving away $10,000? That usually works. Also your title needs to make people NEED to click."

### Your Group Chat

> "Write our group chat planning a road trip"
>
> **Mike:** yo road trip this weekend who's in
> **Dave:** depends where
> **Mike:** idk somewhere cool
> **Dave:** that's not a plan
> **Jason:** [sends meme]
> **Mike:** jason you in or not
> **Jason:** [sends another meme]
> **Dave:** I'll drive but someone's paying for gas
> **Mike:** bro you drive a Tesla
> **Dave:** exactly. Someone's paying for the charging

## Bro Archetypes

brother.skill recognizes different bro types:

| Archetype | Description | Famous Example |
|---|---|---|
| **The Hype Man** | Maximum energy, always screaming, makes everything an event | IShowSpeed |
| **The Roast Master** | Surgically precise insults delivered with a straight face | KSI |
| **The Cool Bro** | Chill energy, speaks rarely, but when they do — everyone listens | Keanu Reeves |
| **The Chaos Agent** | Does things nobody asked for, somehow it works | Jake Paul |
| **The Strategy Bro** | Turns everything into a business plan or a life lesson | MrBeast |
| **The Silent Killer** | Quiet for 20 minutes then drops one line that destroys everyone | That one friend. You know who. |
| **The Meme Lord** | Communicates exclusively in memes and reaction images | Every group chat has one |
| **The Storyteller** | Every experience becomes a 10-minute dramatic retelling | Your funniest friend |

## Bro Profile Dimensions

Each bro is profiled across five dimensions:

### Voice & Language
Catchphrases, slang, speech patterns, volume level, go-to insults, go-to compliments (rare).

### Comedy Style
Humor type, timing, signature moves, what they always joke about, what they never touch.

### Energy & Vibe
Default energy level, peak triggers, group role, entrance energy.

### Content Personality (online bros)
Platform, content style, audience interaction, collab chemistry, how they've evolved.

### Relationship With You
How you found them, inside jokes, favorite moments, zombie apocalypse survival rating.

## Features

### Bro Interaction Mode
Talk to any distilled bro. The skill responds in their voice, their slang, their energy. Roasts you if they would. Hypes you if they would. Stays in character.

### Content Analysis
Share a clip or screenshot. The skill analyzes why it's funny, compares it to the bro's known patterns, and predicts what they'd do next.

### Group Chat Simulation
Profile multiple bros and simulate their group dynamics. Generate realistic conversations. Find out who starts drama, who escalates, and who sends the meme that ends the argument.

### Self-Learning
Every input makes the profile more accurate. Tracks confidence levels from rough sketch (1-5 data points) to near-perfect recreation (50+). Never overwrites — always appends.

## Memory Architecture

```
bros/
  [name]/
    PROFILE.md              — Living bro profile (updated with each input)
    interaction-log.jsonl   — Every input logged with timestamp
```

- Profiles persist across sessions
- Confidence scores track accuracy
- Contradictions flagged for user clarification
- Evolution tracked over time

## Install

```bash
# OpenClaw
clawhub install realteamprinz/brother

# Hermes
hermes skills install brother-skill

# Claude Code
cp -r brother-skill/ ~/.claude/skills/
```

## Emotional Guidelines

1. **Roasts come from love.** Bro humor means you can say terrible things BECAUSE you love them. Never actually hurtful.
2. **Respect the real person.** Capture energy, not caricature. Stay respectful when distilling real creators.
3. **Cultural sensitivity.** Chinese internet humor, American YouTube humor, UK banter — all different. Respect the context.
4. **The quiet bro matters.** Not every bro is loud. Some speak once and destroy everyone. That restraint is their power.

## Part of the Family

**Daily tier:**
- [mom.skill](https://clawhub.ai/realteamprinz/mom) — Parenting co-pilot for mothers
- [dad.skill](https://clawhub.ai/realteamprinz/dad) — Parenting co-pilot for fathers
- **brother.skill** — Distill your bros *(you are here)*

**Legacy tier:**
- [mother.skill](https://clawhub.ai/realteamprinz/mother) — Preserve your mother's wisdom
- [father.skill](https://clawhub.ai/realteamprinz/father) — Preserve your father's legacy
- [grandma.skill](https://clawhub.ai/realteamprinz/grandma) — Her stories and recipes
- [grandpa.skill](https://clawhub.ai/realteamprinz/grandpa) — His stories and strength

**Pet tier:**
- [paw.skill](https://clawhub.ai/realteamprinz/paw) — Distill your pet's soul
- [dog.skill](https://clawhub.ai/realteamprinz/dog) — Canine intelligence
- [cat.skill](https://clawhub.ai/realteamprinz/cat) — Feline intelligence

**Wealth tier:**
- [midas.skill](https://clawhub.ai/realteamprinz/midas) — Extract wealth systems

---

> *"We distill what time takes away."* — But sometimes we also distill what makes us laugh until we cry.
>
> Built by [@realteamprinz](https://github.com/realteamprinz) | [PRINZCLAW](https://prinzclaw.ai)
