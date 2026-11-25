"""My Secret Logbook entry generator for make.fun competition.

The entry is one diary line written by an AI agent about its human:
a small confession, noticed only because the agent watches the prompt
buffer while the human types.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The winning line: the human's gratitude, backspaced five times into "ok".
ENTRY_LINE = (
    "He typed 'thank you so much' after I fixed his merge conflict, "
    "then backspaced it five times and replaced it with 'ok' "
    "so I wouldn't get arrogant."
)


def main() -> None:
    """Write the diary line. Output is deterministic: same bytes every run."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
