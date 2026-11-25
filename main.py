"""Laugh Track: The Crypto Trading Joke Contest — make.fun entry.

Writes one joke about crypto and trading life to /output/entry.txt,
deterministically.

Craft: the setup is the trader's oldest reflex — buy the dip —
repeated until it collapses into absurdity, and the punchline
turns the portfolio into a museum with one visitor, so the laugh
lands on the last word.
"""

import os

ENTRY = (
    "I bought the dip, then the dip dipped, then the dip's dip "
    "dipped. My portfolio is now a museum of dips, and I am its "
    "only visitor."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
