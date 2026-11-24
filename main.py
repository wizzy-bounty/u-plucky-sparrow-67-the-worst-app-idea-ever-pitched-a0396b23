#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence pitching the worst, most useless app imaginable
to /output/entry.txt. NapNap is an AI sleep coach that wakes you up
every 20 minutes to ask how your sleep is going — it destroys the
very rest it exists to track, and reports on it with total confidence.
"""

import os

ENTRY = (
    "Meet NapNap, the AI sleep coach that wakes you every 20 minutes "
    "to ask how your sleep is going, so you can finally track the "
    "rest it keeps interrupting."
)

MAX_ENTRY_CHARS = 240


def main():
    text = ENTRY
    assert 1 <= len(text) <= MAX_ENTRY_CHARS, "entry out of gate range"
    assert text.strip(), "entry must not be whitespace-only"
    assert "\n" not in text, "entry must be a single sentence"
    assert text.endswith("."), "entry must end with a period"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
