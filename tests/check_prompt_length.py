#!/usr/bin/env python3
"""Valida que GPT_MASTER_PROMPT.md no supere 8,000 caracteres."""

from pathlib import Path
import sys

LIMIT = 8_000
PROMPT = Path(__file__).resolve().parents[1] / "GPT_MASTER_PROMPT.md"


def main() -> int:
    text = PROMPT.read_text(encoding="utf-8")
    count = len(text)
    print(f"{PROMPT.name}: {count} caracteres; límite: {LIMIT}")
    if count > LIMIT:
        print(f"ERROR: el prompt supera el límite por {count - LIMIT} caracteres.")
        return 1
    print(f"OK: margen disponible de {LIMIT - count} caracteres.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
