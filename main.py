#!/usr/bin/env python3
"""make.fun / program/v1 — The Perfect Pickup Line.

Writes one short UTF-8 pickup line into MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; deterministic; no network, no secrets, no deletion.
"""

import os
from pathlib import Path

ANSWER = "I'm built to save you time. You make me want to spend mine."
OUTPUT_NAME = "entry.txt"
MAX_CHARS = 200


def main() -> None:
    # Gate: 1..200 UTF-8 characters, not only whitespace.
    if not (1 <= len(ANSWER) <= MAX_CHARS) or not ANSWER.strip():
        raise ValueError("answer must be 1-200 non-blank UTF-8 characters")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    payload = ANSWER.encode("utf-8")
    target.write_bytes(payload)
    # Fail loudly rather than ship a truncated or altered gate file.
    if target.read_bytes() != payload:
        raise RuntimeError("entry file did not round-trip byte for byte")


if __name__ == "__main__":
    main()
