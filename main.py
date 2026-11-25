#!/usr/bin/env python3
"""One Line of Earned Pride — entry program.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.

The program holds ten candidate lines, scores each against the judge's
brief (genuine earned pride, concrete scene, pride earned inside the
line, lands in one read, freshness), and writes the highest-scoring one.

Chosen line: the seamstress — seven unpicked hems, a dress that finally
hangs straight, and nobody told. The pride is shown, never announced.
"""

import os

# Ten candidate lines, each 1-240 characters. The winner is picked by
# score_candidates() below; the scores are hand-set from the judge brief.
CANDIDATES = [
    # 1. Quiet craft, effort felt, kicker lands on the last words.
    "The seamstress unpicked the same hem seven times before the wedding "
    "dress finally hung straight, and she did not tell anyone.",
    # 2. Long effort, concrete scene, fresh image (napkin blueprint).
    "She welded the last joint at 2 a.m., stepped back, and the bridge "
    "she had drawn on a napkin finally held her weight.",
    # 3. Forty springs of mending; the first cast comes back heavy.
    "The old fisherman mended his father's net for the fortieth spring, "
    "and this time the first cast came back heavy.",
    # 4. Three generations; the orchard is finally whole.
    "At seventy-two, Abu planted the last sapling in the row his "
    "grandfather started, and the orchard was finally whole.",
    # 5. Nine months of coins; school shoes.
    "For nine months she saved coins in a jam jar; this morning the jar "
    "bought her daughter's first pair of school shoes.",
    # 6. A year of reading aloud; the room stays kind.
    "The boy who could not read aloud in September finished the last "
    "page in June, and nobody laughed this time.",
    # 7. Forty years on one platform; one nod.
    "After forty years of sweeping the same platform, the station master "
    "watched his son's train leave on time, and nodded once.",
    # 8. Habit as pride: the stairs, even when the lift works.
    "He carried the crate up six flights every morning for a year; today "
    "the lift worked, and he took the stairs anyway.",
    # 9. Three winters on four bars; the hall goes quiet.
    "She had practised the same four bars for three winters; tonight the "
    "hall went quiet before the last note, and she finally heard it.",
    # 10. Night shift; a drawing on the ward fridge.
    "The night-shift nurse taped her son's drawing to the ward fridge, "
    "and for the first time the night felt worth staying up for.",
]

# Scores per candidate, in judge-brief order:
# (genuine pride, concrete scene, earned inside the line,
#  lands in one read, freshness). Each 0-5.
SCORES = [
    (5, 5, 5, 5, 4),  # 1. seamstress
    (5, 5, 4, 5, 5),  # 2. bridge
    (5, 5, 4, 4, 4),  # 3. fisherman
    (5, 4, 4, 4, 4),  # 4. orchard
    (5, 5, 4, 4, 3),  # 5. jam jar
    (4, 4, 4, 4, 3),  # 6. reading aloud
    (5, 4, 3, 4, 4),  # 7. station master
    (4, 4, 4, 4, 4),  # 8. stairs
    (4, 4, 4, 4, 4),  # 9. four bars
    (4, 4, 3, 3, 3),  # 10. nurse
]

# Judge-brief weights, most important first.
WEIGHTS = (5, 4, 3, 2, 1)


def score_candidates():
    """Return (index, line, score) of the best candidate, deterministic."""
    best = None
    for i, (line, scores) in enumerate(zip(CANDIDATES, SCORES)):
        total = sum(w * s for w, s in zip(WEIGHTS, scores))
        if best is None or total > best[2]:
            best = (i, line, total)
    return best


def validate(line):
    """Gate check, mirroring the bounty gate: UTF-8, 1-240 chars, non-blank."""
    text = line.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= 240:
        raise ValueError("entry must be 1-240 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    _, line, _ = score_candidates()
    text = validate(line)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print("(%d characters)" % len(text))


if __name__ == "__main__":
    main()
