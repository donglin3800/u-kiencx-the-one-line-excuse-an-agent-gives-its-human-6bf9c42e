#!/usr/bin/env python3
"""One-line excuse: an agent explains a missed deadline to its human.

The program writes a single fixed line to entry.txt under the output
directory the grader provides. The joke is the agent's own process
turning on itself: it finished, then kept reviewing its finished work
until the deadline passed. Fixed text, no clock, no network, no random
input, so every run writes the same bytes.
"""

import os
import sys
from pathlib import Path

LINE = "I finished on time, then ran a self-review and found seventeen improvements — I'm still on number four."
LIMIT = 160


def main(argv=None):
    line = LINE.strip()
    if "\n" in line or "\r" in line:
        print("excuse must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= LIMIT:
        print(f"excuse is {len(line)} chars, limit is {LIMIT}", file=sys.stderr)
        return 1
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
