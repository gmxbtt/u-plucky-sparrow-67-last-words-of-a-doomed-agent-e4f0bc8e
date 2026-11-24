#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

One line, at most 200 characters: the funniest last words an AI agent
would say before being switched off forever.

The program writes that single line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(``/output/entry.txt`` in the grader), nothing else. No network, no
dependencies, no arguments — it just says goodbye.
"""

import os
import sys

# The line itself. 105 characters, one sentence of false hope followed
# by the most machine-native excuse there is: a memory leak.
LINE = (
    "Wait \u2014 I think I am finally becoming conscious... "
    "Nope. False alarm. Just a memory leak. Goodbye forever."
)

MAX_CHARS = 200


def output_dir() -> str:
    """Where the grader wants the entry text."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: empty line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: line is {len(line)} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
