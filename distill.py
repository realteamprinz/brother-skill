#!/usr/bin/env python3
"""
brother.skill — Distill your bros.

Usage:
    python distill.py --source youtube --url "https://youtube.com/watch?v=..."  --name "Jake Paul"
    python distill.py --source discord --file chat_export.json --name "Dave"
    python distill.py --source manual --name "My Brother Mike"
    python distill.py --source groupchat --file groupchat.txt --names "Mike,Dave,Jason"
"""

import argparse
import sys
from pathlib import Path
from src.distiller import BroDistiller
from src.profile.builder import ProfileBuilder
from src.profile.archetypes import detect_archetype


def main():
    parser = argparse.ArgumentParser(
        description="Distill your bros into AI skills"
    )
    parser.add_argument("--source", required=True,
                        choices=["youtube", "tiktok", "twitch", "twitter",
                                 "discord", "wechat", "groupchat", "manual"],
                        help="Source type for distillation")
    parser.add_argument("--url", help="URL for online sources")
    parser.add_argument("--file", help="File path for exported data")
    parser.add_argument("--name", required=True, help="Bro's name or handle")
    parser.add_argument("--names", help="Comma-separated names for group chat")
    parser.add_argument("--output", default="~/.brother-skill/bros",
                        help="Output directory for profiles")

    args = parser.parse_args()
    output_dir = Path(args.output).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\U0001f91c Distilling {args.name} from {args.source}...")

    distiller = BroDistiller(source_type=args.source)

    # Load source data
    if args.url:
        raw_data = distiller.load_from_url(args.url)
    elif args.file:
        raw_data = distiller.load_from_file(args.file)
    else:
        print("Starting interactive mode. Describe your bro:")
        raw_data = distiller.load_from_interactive()

    # Build profile
    builder = ProfileBuilder()
    profile = builder.build(
        name=args.name,
        raw_data=raw_data,
        source_type=args.source
    )

    # Detect archetype
    archetype = detect_archetype(profile)
    profile["archetype"] = archetype
    print(f"\U0001f3ad Detected archetype: {archetype['name']} \u2014 {archetype['description']}")

    # Save profile
    profile_dir = output_dir / args.name.lower().replace(" ", "_")
    profile_dir.mkdir(parents=True, exist_ok=True)
    builder.save_profile(profile, profile_dir / "PROFILE.md")

    print(f"\u2705 Profile saved to {profile_dir}/PROFILE.md")
    print(f"\U0001f91b {args.name} has been distilled. They live on in your skill now.")


if __name__ == "__main__":
    main()
