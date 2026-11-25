#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

The line is fixed text: deterministic, no network, no randomness, no
input. The grader runs this program twice; both runs must produce the
same bytes, and they do — the same constant is written every time.
"""

import os

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 One star. He calls me 'basically unkillable', "
    "then forgot to water me for six months. I am now one root held "
    "together by spite, and the only thing growing in this flat is "
    "his confidence."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
