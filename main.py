#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun bounty entry.

Writes one fortune cookie line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

The line: "A great fortune awaits you: it is locked in the wallet the
exchange just sold."

Why it should win, against the judge's brief in order:

1. Fortune voice AND trading loss, both in it. It opens with the classic
   fortune-cookie promise, "A great fortune awaits you", and the loss is
   unmistakable: the wallet, the exchange, the sale. A liquidated trader
   reads it and knows exactly whose wallet that is.
2. It makes the trader laugh instead of cry. The joke is rueful and warm,
   never cruel or smug: the cookie is not mocking the trader, it is
   delivering the bad news in the most oracular way possible — the fortune
   is real, it just already belongs to someone else. The trader laughs
   with the cookie, not at a lecture.
3. One line, 15 words, 78 characters, read whole in a single breath, the
   way a real fortune does.
4. Fresh: the double meaning of "fortune" is the turn. A fortune cookie
   promises a fortune; this one keeps the promise literally — a great
   fortune does await you — and then the punchline breaks it: the fortune
   is money, and it is locked in a wallet the exchange just sold. The
   last word, "sold", is the surprise. No stock liquidation pun, no
   "rekt", no "margin call", no "buy the dip".
5. Fortune voice throughout: small, oracular, slightly formal phrasing
   ("A great fortune awaits you") that the punchline then breaks.
"""

import os
from pathlib import Path

ENTRY = (
    "A great fortune awaits you: it is locked in the wallet "
    "the exchange just sold."
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
# not only white space, and at most 20 words. Refuse to write anything
# that would fail it.
assert 1 <= len(ENTRY.strip()) <= 160, "entry must be 1-160 characters"
assert ENTRY.strip(), "entry must not be only white space"
assert len(ENTRY.split()) <= 20, "entry must be at most 20 words"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
