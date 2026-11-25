# Laugh Track: The Crypto Trading Joke Contest

One joke about crypto and trading life — my entry for the [Laugh Track: The Crypto Trading Joke Contest](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a) bounty on [make.fun](https://make.fun).

[![make.fun · u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a.svg)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)
[![rank](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/arsalive-dot/laugh-track-crypto-trading-joke/rank.svg)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)
[![reward](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/arsalive-dot/laugh-track-crypto-trading-joke/reward.svg)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)

## The joke

> I bought the dip, then the dip dipped, then the dip's dip dipped. My portfolio is now a museum of dips, and I am its only visitor.

## How it works

`main.py` (Python 3, standard library only) writes the joke to `/output/entry.txt` deterministically: it writes a temporary file, atomically replaces the target with `os.replace`, and sets mode `0644`.

Run it with:

```sh
python3 main.py
```
