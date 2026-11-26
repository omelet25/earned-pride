"""One Line of Earned Pride.

Writes a single line of text (1 to 240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.

Standard library only. No network access. Deterministic.
"""

import os

LINE = (
    "At five in the morning, the baker tapped her first loaf and heard "
    "the hollow knock her grandmother used to listen for."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: one line, 1 to 240 characters, not only white space.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 240, "entry must be 1 to 240 characters"
    assert LINE.strip(), "entry must not be only white space"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
