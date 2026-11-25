#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh entry.

Writes one original roast of a smart fridge to /output/entry.txt.
The line is kept in a single constant so the output is exactly one line,
well inside the 200-character limit.
"""

import os

LINE = (
    "My smart fridge updated its firmware overnight, and now the ice "
    "maker will not dispense until I accept the new terms — I came "
    "for a sandwich, not a software license."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert "\n" not in line, "line must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
