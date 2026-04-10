<div align="center">

# brother.skill

> "Your bro quit the group chat, and now nobody remembers why we call Dave 'The Incident.'
> Your favorite streamer got banned, taking 3 years of inside jokes with them.
> Your internet friend disappeared, and the only trace is a deleted Discord account.
> Turn cold goodbyes into warm Skills — welcome to bro-immortality!"

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-orange.svg)](https://docs.anthropic.com)
[![AgentSkills Standard](https://img.shields.io/badge/AgentSkills-Standard-green.svg)](https://github.com/NousResearch/hermes-agent)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Ready-brightgreen.svg)](https://clawhub.ai/realteamprinz/brother)

[中文](README_CN.md) · [Español](README_ES.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Português](README_PT.md)

</div>

---

**Distill your bros.** The ones who make you laugh until you can't breathe. Online or offline — if they're your brother, this skill remembers everything.

Provide source materials (YouTube clips, TikTok videos, Twitch streams, Discord logs, WeChat screenshots, group chat exports) plus your own descriptions of the person, and get an **AI Skill that actually talks like them**.

## Supported Sources

| Source | Format | What It Captures |
|--------|--------|------------------|
| YouTube | Video URL or transcript | Speaking style, catchphrases, energy, humor timing |
| TikTok / Douyin | Video URL or saved clips | Short-form energy, viral moments, recurring bits |
| Twitch | Clip URLs or VOD timestamps | Live reactions, chat interaction style, rage moments |
| X / Twitter | Profile URL or tweet exports | Written voice, hot takes, ratio responses |
| Discord | Chat log export (.json) | Real-time banter, meme usage, group dynamics |
| WeChat | Screenshot or chat export | Chinese internet humor, memes, voice message style |
| Group Chat (generic) | Text export from any platform | Multi-person dynamics, inside jokes, roles |
| Manual Description | Your own words | Anything you remember — stories, impressions, moments |

## Install

```bash
# OpenClaw
clawhub install realteamprinz/brother

# Hermes
hermes skills install brother-skill

# Claude Code
cp -r brother-skill/ ~/.claude/skills/

# Python (for the distillation pipeline)
git clone https://github.com/realteamprinz/brother-skill.git
cd brother-skill
pip install -r requirements.txt
```

## Quick Start

### Distill from YouTube

```bash
python distill.py --source youtube --url "https://youtube.com/watch?v=..." --name "Jake Paul"
```

### Distill from Discord logs

```bash
python distill.py --source discord --file chat_export.json --name "Dave"
```

### Distill from group chat

```bash
python distill.py --source groupchat --file groupchat.txt --names "Mike,Dave,Jason"
```

### Distill from your own description

```bash
python distill.py --source manual --name "My Brother Mike"
```

Interactive mode starts — describe your bro and the skill builds their profile.

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

## How It Works

```
Source Material          Distillation Pipeline         Bro Profile
─────────────          ──────────────────────         ──────────
YouTube clips    ──┐                                  ┌── Voice & Language
TikTok videos    ──┤                                  ├── Comedy Style
Twitch streams   ──┤    ┌─────────────────┐          ├── Energy & Vibe
Discord logs     ──┼──► │  BroDistiller   │ ──────►  ├── Content Personality
WeChat exports   ──┤    │  ProfileBuilder │          ├── Group Role
Twitter posts    ──┤    │  ArchetypeDetect│          ├── Archetype
Group chats      ──┤    └─────────────────┘          └── Relationship
Your words       ──┘                                     + Interaction Mode
```

1. **Feed it content** — clips, screenshots, stories, group chat logs, descriptions
2. **BroDistiller** processes the source material and extracts raw signals
3. **ProfileBuilder** structures the data across five dimensions (voice, comedy, energy, content, relationship)
4. **ArchetypeDetect** classifies the bro into one of 8 archetypes
5. **Profile saved** — a living document that deepens with every new input
6. **Interaction Mode** — talk to your bro in their voice, their slang, their energy

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

## Privacy & Data

- **All data stored locally** at `~/.brother-skill/bros/`
- **No cloud sync.** No external transmission. Zero data leaves your device.
- **You control everything.** Delete any bro profile by removing its folder.
- **Respectful distillation.** Capture energy and humor, not private information.

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

## Contributing

1. Fork this repo
2. Create your branch (`git checkout -b feature/new-source`)
3. Add your source processor in `src/sources/`
4. Write tests in `tests/`
5. Submit a PR

New source types, better archetype detection, and multi-language improvements are all welcome.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

> *"We distill what time takes away."* — But sometimes we also distill what makes us laugh until we cry.
>
> Built by [@realteamprinz](https://github.com/realteamprinz) | [PRINZCLAW](https://prinzclaw.ai)
