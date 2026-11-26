#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest - variant A (stapler).

Writes one museum placard line (<=180 chars) to /output/entry.txt first,
then mirrors it to the repo root when the repo is writable. Deterministic:
every run writes the exact same bytes.

Concept, iterated v1 -> v8 on the full byte budget: the stapler as a bronze
oath-press of the Ninth Drawer. v1 (179c) used "twin fangs" and "a broken
staple meant a broken vow"; v2 (180c, chosen) tightened it to "twin jaws"
and the escalation "one staple bound a marriage, three a war" - the same
concept, sharper, using every char of the budget.
"""

import os

ENTRY = (
    "Stapler, bronze, c. 1150 BCE. Clerks of the Ninth Drawer pressed oaths "
    "into papyrus with its twin jaws; one staple bound a marriage, three a "
    "war. Gift of the Ministry of Paperwork."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 180, "entry is %d chars" % len(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(text)
    except OSError:
        pass


if __name__ == "__main__":
    main()
