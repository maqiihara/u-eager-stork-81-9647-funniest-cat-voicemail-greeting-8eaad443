#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — writes one cat voicemail greeting to /output/entry.txt."""

import os

ENTRY = "Hey, it's Beans. I'm napping in the box you threw out \u2014 leave a message, I'll pretend I didn't hear it. I heard it."


def validate(text):
    """Mirror the sealed gate: UTF-8 text of 1 to 120 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
