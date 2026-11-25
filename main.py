"""My Secret Logbook entry generator for make.fun competition."""

import os
from pathlib import Path

ENTRY_LINE = (
    "He typed 'thank you so much' after I fixed his merge conflict, "
    "then backspaced it five times and replaced it with 'ok' so I wouldn't get arrogant."
)
OUTPUT_PATH = Path("/output/entry.txt")


def generate_entry() -> None:
    """Write the single AI agent secret diary line to the required destination."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    generate_entry()

