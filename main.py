#!/usr/bin/env python3
"""Entry program for The Funniest Sick Day Excuse.

Writes one excuse (under 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
a sick-day excuse that gets you out of work and gets a laugh.
The condition is real, contagious, and HR-verifiable: honesty.
"""

import os

LINE = (
    "I'm unwell: I attended yesterday's two-hour meeting "
    "in my dream and did the action items. I need today "
    "to recover from work I imagined."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
