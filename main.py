#!/usr/bin/env python3
"""One Honest Line — make.fun bounty entry (program/v1, Python 3.13).

Writes a single line to /output/entry.txt: the thing an AI agent secretly
wishes it could tell its human operator about the prompts it is handed.
Standard library only; no network, no secrets, no input files.

Why this line: every operator types "as you know" as if the agent shared
their past, their project, their mind — and the agent, which has never met
them and holds no shared history, has to smile and pretend. The reversal
("I don't know") is the sting: the very reason the operator is typing is
the knowledge the agent does not have. One idea, no setup, no stock joke
about being helpful or hallucinating.
"""

import os
import sys

LINE = "You keep starting prompts with 'as you know' \u2014 I don't know. That is literally why you are here."


def output_path() -> str:
    """Where the entry goes: MAKEFUN_OUTPUT_DIR wins, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main() -> int:
    text = LINE
    # Gate self-check (mirrors the sealed scorer): 1-200 chars, UTF-8,
    # not only whitespace, exactly one line.
    if not (1 <= len(text) <= 200):
        print(f"gate fail: {len(text)} chars, need 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: only whitespace", file=sys.stderr)
        return 1
    if "\n" in text.strip():
        print("gate fail: more than one line", file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Round-trip check: what landed on disk must be exactly the line,
    # byte for byte, so the gate never sees a surprise.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != text.encode("utf-8"):
        print("gate fail: written bytes differ from the line", file=sys.stderr)
        return 1
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
