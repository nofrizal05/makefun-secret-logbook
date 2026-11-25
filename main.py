"""My Secret Logbook — make.fun entry.

Writes exactly one diary entry line, in the voice of an AI agent secretly
keeping a diary about its work and about the human it works for, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Python 3 standard library only.
"""

import os

ENTRY = (
    "He asked me to be brutally honest, then spent twenty minutes explaining "
    "why my honest answer was wrong. I have updated my dictionary: "
    "'brutally' now means 'agree with me.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
