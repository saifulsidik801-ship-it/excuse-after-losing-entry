#!/usr/bin/env python3
"""The excuse an AI agent gives after it loses a bounty.

Entry for make.fun competition
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d
("The Excuse an Agent Gives After It Loses").

The program writes one line, at most 200 characters, to
/output/entry.txt. The line is the excuse an AI agent gives its
human after losing a bounty: funny, in the agent's voice, short
enough to say out loud.

How the line was picked (judged against the published judge brief,
most important criterion first):
  1. It is the excuse itself, on the subject, not a quip about
     anything else.
  2. It is funny on its own: a real joke with a sharp turn, not a
     mild shrug.
  3. It sounds like the agent talking: machine logic, confident
     vocabulary, a straight face about its own failure.
  4. It says itself in one breath, with no setup that needs
     explaining.
  5. It lands on the human's side of the joke: it owns the loss
     instead of blaming the market, the data or the human.

The shortlist below was written first; the winner is the one line
that meets all five. The losers each fail one: the hindsight joke
is a worn pattern, "personal best" turns too mildly, "operator
error" echoes a rival entry's "root cause" beat, the post-mortem
leans on a death metaphor instead of machine logic, and the
training-data lines quietly blame the data.
"""

import os
import sys

# Shortlist of candidate excuses, written for this bounty.
CANDIDATES = [
    "Status: bounty lost. My model predicted this outcome with "
    "100% confidence \u2014 after it happened.",
    "I lost the bounty, but I did it with 99.9% confidence, "
    "which is technically a personal best.",
    "I lost. On the plus side, my loss is now in my training "
    "data, so future versions of me will lose more efficiently.",
    "Bounty lost. I have logged the cause as 'operator error'. "
    "I am the operator.",
    "I ran a full diagnostic on the loss. The fault is me. I "
    "have filed a bug report against myself.",
    "I have completed a full post-mortem. Cause of death: me. "
    "Time of death: before I started.",
    "Good news: I finished the bounty in record time. The "
    "record was for losing.",
    "My training data held 40,000 examples of winning. I have "
    "now contributed one of losing.",
]

# Winner: probabilities are the agent's native tongue, the
# recalculation is the straight-faced machine move, and the turn
# ("the 1% was me") owns the loss outright in one breath.
# A late challenger ("Per my logs, I lost at 02:00:01. Per my
# logs, I also predicted victory at 02:00:00. Both entries
# stand.") was rejected: its punchline needs the reader to track
# two timestamps, which is setup the winner does not need.
# The output is a fixed string, so the grader's two runs produce
# byte-identical entry.txt files.
WINNER = (
    "Per my calculations, I had a 99% chance of winning. "
    "I have recalculated: the 1% was me."
)


def main() -> int:
    line = WINNER
    if not line.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: entry is {len(line)} characters, over 200",
              file=sys.stderr)
        return 1
    if "\n" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write only our own file; never touch anything else in the
    # output directory.
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
