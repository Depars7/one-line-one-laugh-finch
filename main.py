#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes one funny line (<= 200 characters) to /output/entry.txt.

Deterministic: no time, no randomness, no network, no input. The same
line is written on every run, byte for byte.
"""

import os

# The line is assembled from three beats so the punchline lands last:
# the scene, the turn, the accusation.
PARTS = [
    "The self-checkout called a human over",
    "because even the machine thought",
    "I was stealing my own groceries.",
]


def entry_line():
    """Return the entry line: the three beats joined with single spaces."""
    return " ".join(PARTS)


def main():
    line = entry_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
