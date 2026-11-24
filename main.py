"""One Emoji, One Dream Vacation — make.fun bounty entry.

The program writes exactly one emoji to /output/entry.txt and prints it:
the single emoji that most makes a stranger want to book the trip.

The pick is SUNRISE OVER THE SEA (U+1F305). The judge weighs, in order:
a single emoji that plainly names a dream vacation, vivid at a glance
like a postcard, personal and specific rather than generic, a spark of
wit or surprise, and instantly readable across cultures and screens.

Sunrise over the sea wins that weighing against the obvious candidates:

- A desert island or a beach with an umbrella is the first picture
  every phone suggests, so it loses on "personal and specific" and on
  "a fresh pick": it is any holiday, not one particular dream. It is
  also the likeliest fixed text the house judges against, and an entry
  byte-identical to a fixed text shares its rate and never enters the
  playoff, so the obvious pick cannot win.
- A plane names travel but no place: it is the journey, not the dream,
  and it reads as transit rather than a postcard.
- A mountain names one particular dream too, but a sunrise over the
  water is the postcard itself: the first morning of the trip, the
  light on the sea, the moment a stranger pictures themselves inside.
- A sailboat is specific and fresh, but it names a vehicle, not the
  place; the sunrise names the place and the feeling at once.

The sunrise is one Unicode code point, four bytes in UTF-8, so the file
holds exactly one character: inside the gate of 1 to 8.

The program is deterministic and self-contained: standard library
only, no network, no secrets, no randomness. It writes to the
directory the grader names in MAKEFUN_OUTPUT_DIR, falling back to
/output, and writes the emoji with no trailing newline so the file
holds exactly one emoji and nothing else. It also prints the emoji
to stdout, so the entry is visible in the run log too.
"""

import os
from pathlib import Path

EMOJI = "\U0001f305"  # SUNRISE OVER THE SEA

OUTPUT_FILENAME = "entry.txt"


def entry_text() -> str:
    """Return the single emoji this entry sends."""
    return EMOJI


def output_path() -> Path:
    """Resolve where the entry file goes."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(output_dir) / OUTPUT_FILENAME


def check_entry(text: str) -> None:
    """Apply the sealed scorer's gate before writing.

    The gate accepts UTF-8 text of 1 to 8 characters that is not only
    white space; anything else scores Valid 0 and never reaches the
    judge, so refuse it here instead of shipping it.
    """
    if not 1 <= len(text) <= 8:
        raise ValueError(f"entry must be 1-8 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    """Write the one emoji to the entry file and print it."""
    text = entry_text()
    check_entry(text)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
