"""One-Liner Laughs entry.

Writes the competition entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt), with no trailing newline.
"""

import os
import sys

ENTRY = "I asked the bank for a loan to open an escape room; they said no, so I locked the door and started the demo."

# Why it works: a rejected entrepreneur turns bank robber on the spot,
# but still calls the heist a "demo" -- the polite startup pitch never
# leaves him, even while he commits the crime.


def validate(entry: str) -> None:
    if not entry:
        sys.exit("entry is empty")
    if len(entry) > 200:
        sys.exit(f"entry is {len(entry)} chars, over the 200-char limit")
    if "\r" in entry or "\n" in entry:
        sys.exit("entry must be a single line (no CR/LF)")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
