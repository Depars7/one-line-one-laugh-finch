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
    # Gate check before anything is written: the sealed scorer only
    # accepts UTF-8 text of 1-200 characters, not only whitespace.
    if not line.strip() or not 1 <= len(line) <= 200:
        raise SystemExit("entry line fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    # Atomic write: temp file in the same directory, world-readable
    # (the grader collects outputs as another user), then rename.
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
