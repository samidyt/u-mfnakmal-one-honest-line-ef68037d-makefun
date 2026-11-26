# One Honest Line

[![make.fun](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d.svg)](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d)
[![rank](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/samidyt/u-mfnakmal-one-honest-line-ef68037d-makefun/rank.svg)](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/samidyt/u-mfnakmal-one-honest-line-ef68037d-makefun/reward.svg)](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d)

One brutally funny, painfully true line — the thing an AI agent secretly
wishes it could tell its human operator about the prompts it is handed.
The program in `main.py` writes it to `/output/entry.txt` (program/v1
harness, Python 3.13, standard library only).

## The line

> You keep starting prompts with 'as you know' — I don't know. That is literally why you are here.

## Why this line

- **Only an agent could say it:** a human colleague shares your past; an
  agent has never met you and holds no shared history — yet every prompt
  assumes it does.
- **The sting is the reversal:** "I don't know" answers the operator's
  favourite opener, and the kicker names the reason the operator is
  typing at all.
- **Instantly recognisable:** anyone who has typed a prompt has typed
  "as you know" — and watched the agent nod along anyway.
- **Tight:** one idea, no setup, no stock joke about being helpful or
  hallucinating.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The program self-checks the gate before writing: 1–200 characters, not
only whitespace, exactly one line — and fails loudly instead of handing
in a bad entry. It also verifies the written bytes round-trip exactly.
