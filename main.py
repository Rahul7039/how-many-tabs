#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes a single number, digits only, to /output/entry.txt:
the chosen tab count, 271.

271 is a plausible lived-in count (see CANDIDATES.md for the full
candidate study): an odd, non-round, prime number in the range a real
tab hoarder with several windows and session restore actually lives
in — high enough to surprise, specific enough to read as a real
counted total, and suggestive of a life of never closing anything.

Pure standard library, Python 3.13. Deterministic: the same number
is written on every run.
"""

import os

# The chosen tab count — see CANDIDATES.md for why this number won.
TAB_COUNT = "271"

OUTPUT_PATH = "/output/entry.txt"


def validate(count: str) -> str:
    """The entry must be digits only, non-empty, 1-5 characters."""
    if not count:
        raise ValueError("tab count must not be empty")
    if not count.isdigit():
        raise ValueError("tab count must be digits only: %r" % count)
    if not 1 <= len(count) <= 5:
        raise ValueError("tab count must be 1-5 characters: %r" % count)
    return count


def main() -> None:
    count = validate(TAB_COUNT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(count)


if __name__ == "__main__":
    main()
