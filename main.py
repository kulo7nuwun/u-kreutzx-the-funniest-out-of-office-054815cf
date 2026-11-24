#!/usr/bin/env python3
"""Out-of-office auto-reply entry.

Writes exactly one funny out-of-office line to /output/entry.txt.
"""

import os

LINE = "I'm out of the office until Monday. If it's urgent, please panic quietly among yourselves — I've left my stress with you as a souvenir."


def main() -> None:
    # Self-check mirroring the competition gate: UTF-8 text,
    # 1 to 140 characters, not only white space, a single line.
    text = LINE.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"line is {len(text)} characters, must be 1-140")
    if not text.strip():
        raise ValueError("line must not be only white space")
    if "\n" in text:
        raise ValueError("line must be a single line")
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
