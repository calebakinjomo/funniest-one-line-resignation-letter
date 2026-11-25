"""The Funniest One-Line Resignation Letter — make.fun entry.

The program writes exactly one line — the resignation letter of a cron job
that has fired every minute since March — to /output/entry.txt. The entry
is 128 characters, one line, no trailing newline, so the file's bytes are
the entry itself.
"""

import os

ENTRY = (
    "I resign. I have fired every minute since March for a task that "
    "turned out to be a calendar reminder with delusions of grandeur."
)

MAX_CHARS = 140


def validate(line):
    """Check the entry is a single non-empty line within the limit."""
    if not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d limit" % (len(line), MAX_CHARS))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    return line


def main():
    line = validate(ENTRY)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("Wrote %d chars to %s" % (len(line), out))


if __name__ == "__main__":
    main()
