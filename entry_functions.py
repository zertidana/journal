"""Functions to manage entries."""

from json import load, dump

from uuid import uuid4
from datetime import datetime


def load_all_entries(filename: str = "entries.json") -> list[dict]:
    """Returns entries from a data file."""

    with open(filename, "r", encoding="utf-8") as f:
        entries = load(f)
        return entries


def is_valid_entry(entry: dict) -> bool:
    """Returns if an entry is valid."""
    return all(key.lower() in entry for key in ["body", "author"])


def save_entry(entry: dict) -> dict:
    """Saves an entry to a data file."""

    entries = load_all_entries

    entry["id"] = str(uuid4())
    if "title" not in entry:
        entry["title"] = None

    entry["created_at"] = datetime.now().isoformat()
    entries.append(entry)

    with open("entries.json", "w", encoding="utf-8") as f:
        dump(entry, f, indent=2)

    return entry
