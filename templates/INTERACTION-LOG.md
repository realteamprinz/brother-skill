# Interaction Log Format

Each entry in `interaction-log.jsonl` is a JSON object on a single line:

```json
{
  "timestamp": "2026-04-10T12:00:00.000000",
  "source_type": "manual",
  "input_type": "description",
  "content_summary": "User described bro's catchphrases and energy level",
  "dimensions_updated": ["voice", "energy"],
  "data_point_number": 5
}
```

## Fields

| Field | Type | Description |
|---|---|---|
| timestamp | string | ISO 8601 UTC timestamp |
| source_type | string | youtube, tiktok, twitch, twitter, discord, wechat, groupchat, manual |
| input_type | string | video, short_video, stream, posts, chat, description |
| content_summary | string | Brief summary of what was provided |
| dimensions_updated | list | Which profile dimensions were affected |
| data_point_number | int | Running count of inputs for this bro |

## Rules

- **Never overwrite** — always append new entries
- **Every input gets logged** — even if it doesn't change the profile
- **Track what changed** — so profile evolution is visible
