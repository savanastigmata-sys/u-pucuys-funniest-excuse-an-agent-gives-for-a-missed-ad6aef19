#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

The grader runs `python3 -P -s main.py` with MAKEFUN_OUTPUT_DIR set.
The program writes exactly one UTF-8 text, 1 to 200 characters, to
<MAKEFUN_OUTPUT_DIR>/entry.txt and nothing else.
"""

import os

EXCUSE = (
    "I didn't miss the deadline. My context window evicted it to make "
    "room for this apology, so I did deliver something on time \u2014 "
    "I just delivered it to the void."
)


def main():
    # The sealed gate: 1 to 200 characters, not only white space.
    # Fail loudly here rather than ship an invalid entry.
    if not 1 <= len(EXCUSE) <= 200:
        raise SystemExit(f"excuse is {len(EXCUSE)} characters, must be 1-200")
    if not EXCUSE.strip():
        raise SystemExit("excuse is only white space")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise SystemExit("excuse must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    # Read the file back and prove it is exactly the excuse, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != EXCUSE:
        raise SystemExit("entry.txt does not match the excuse byte for byte")
    print(f"wrote {len(EXCUSE)} characters to {path}")


if __name__ == "__main__":
    main()
