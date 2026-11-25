"""Write the 4AM Commit entry: one commit message, one line, no newline.

The line is the note an AI agent leaves after a long night fixing its
own bugs. It is written exactly as-is to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).
"""

import os

ENTRY = "I have reviewed my own code and found the author unreliable. Patching accordingly."


def validate(line):
    """Check the line satisfies the gate before anything is written."""
    if not line or not line.strip():
        raise ValueError("entry must be non-empty and not only whitespace")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry must contain no control characters")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    return line


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    line = validate(ENTRY)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
