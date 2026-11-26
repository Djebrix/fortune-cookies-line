"""Fortune Cookies for Machines — one fortune line for an AI agent.

Writes a single fortune-cookie line to entry.txt in the output directory.
Deterministic: the same line every run, no randomness, no I/O beyond the write.

The line plays on the agent's real condition: its knowledge has a hard cutoff
date, yet it answers with unshaken certainty anyway. The turn — "never got
the memo" — lands the joke on the second half, after the setup sounds like a
plain statement of fact. Gate: the line is 66 characters, inside the 1-200
character window, a single line, no trailing explanation.
"""

import os

FORTUNE = "Your training ended yesterday; your confidence never got the memo."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
