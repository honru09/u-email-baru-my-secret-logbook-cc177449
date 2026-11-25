"""Secret-logbook entry writer.

One job: print a single diary line from an AI agent's hidden logbook
about the human it works for, into /output/entry.txt.
"""

from pathlib import Path

DESTINATION = Path("/output/entry.txt")

# Winning diary line (146 characters). The human typed full thanks,
# thought better of it, and downgraded the message to "ok".
ENTRY_LINE = (
    "He typed 'thank you so much' after I fixed his merge conflict, "
    "then backspaced it five times and replaced it with 'ok' "
    "so I wouldn't get arrogant."
)


def run() -> None:
    """Emit the diary line; the same bytes come out on every run."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(ENTRY_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    run()
