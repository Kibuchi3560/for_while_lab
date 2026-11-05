"""Part A — the hidden counter.

═══════════════════════════════════════════════════════════════════════
  HOW TO WORK THIS FILE
  1. Read every section below in order. Don't skip A3.
  2. Do NOT run any code yet. Write your prediction on paper FIRST.
  3. Set the PREDICTION_* constants to what you expect.
  4. Run:  python3 -m pytest -v tests/test_a_hidden_counter.py
  5. If red, the assertion message tells you your prediction was wrong —
     go back to the trace, find the missed step, update, rerun.
═══════════════════════════════════════════════════════════════════════

A `for` loop doesn't "walk the list." It walks a hidden counter:

    _counter = 0
    while _counter < len(ls):
        i = ls[_counter]     # reads ONE element at _counter
        ...body...
        _counter += 1         # ALWAYS +1, no matter what

Mutation like `ls.pop(0)` shifts the list LEFT while the counter moves
RIGHT. The two can cross and skip elements. This part makes that real.
"""

# ════════════════════════════════════════════════════════════════════════
# A1 — The classic skip
# ════════════════════════════════════════════════════════════════════════
# WHAT TO DO:
#   a1_run() below is GIVEN — do not modify it. It runs this loop:
#
#       ls = [1, 2, 3, 4, 5]
#       for i in ls:
#           print(i)
#           ls.pop(0)
#
#   On paper, trace it with the hidden counter exposed. Write down, in
#   order, every number you think gets printed. Put them here:
#
#   Expected format: a list of ints, e.g. [4, 5, 6]
#
# NOTE: the function returns what it "prints" instead of printing, so
#       the tests can compare. The behavior is identical.
#
PREDICTION_A1: list[int] = []   # ← your prediction goes here


def a1_run() -> list[int]:
    """GIVEN. Do not modify."""
    ls = [1, 2, 3, 4, 5]
    out = []
    for i in ls:
        out.append(i)
        ls.pop(0)
    return out


# ════════════════════════════════════════════════════════════════════════
# A2 — The trap that does NOT skip
# ════════════════════════════════════════════════════════════════════════
# WHAT TO DO:
#   a2_run() below is GIVEN — do not modify it. It runs:
#
#       ls = [1, 2, 3, 4]
#       for i in ls:
#           print(i)
#           if i == 2:
#               ls.remove(3)
#
#   Predict what gets printed, in order, and put it here.
#
#   This is the *contrast* to A1. The list still shrinks — but does an
#   element get skipped? If not, why not? (Answer in your head; A2 is
#   about noticing that not every mutation breaks a loop.)
#
PREDICTION_A2: list[int] = []   # ← your prediction goes here


def a2_run() -> list[int]:
    """GIVEN. Do not modify."""
    ls = [1, 2, 3, 4]
    out = []
    for i in ls:
        out.append(i)
        if i == 2:
            ls.remove(3)
    return out


# ════════════════════════════════════════════════════════════════════════
# A3 — The infinite loop  ·  ⚠️  DO NOT RUN THIS  ⚠️
# ════════════════════════════════════════════════════════════════════════
# WHAT TO DO:
#   Look at this snippet. Do NOT run it. Predict on paper:
#
#       ls = [1, 2, 3]
#       for i in ls:
#           ls.append(i)
#
#   Question 1: does the loop terminate?
#       Set PREDICTION_A3 to the literal string "finite" or "infinite"
#   Question 2: in ONE sentence, WHY? (Set WHY_A3 — not graded, but
#       write it; it's the lesson of the part.)
#
PREDICTION_A3 = ""   # ← "finite" or "infinite"
WHY_A3 = ""          # ← one sentence


# ════════════════════════════════════════════════════════════════════════
# A4 — Rewrite A1 as a hidden-counter `while`
# ════════════════════════════════════════════════════════════════════════
# WHAT TO DO:
#   Implement a4_hidden_loop(ls) so it returns EXACTLY what a1_run()
#   returns for any list. Use the hidden-counter `while` form:
#
#       _counter = 0
#       while _counter < len(ls):
#           ...
#           _counter += 1
#
# EXAMPLES:
#   a4_hidden_loop([1, 2, 3, 4, 5])  →  same as a1_run() → [1, 3, 5]
#   a4_hidden_loop([1])              →  [1]
#   a4_hidden_loop([])               →  []
#   a4_hidden_loop([9, 8, 7])        →  [9, 7]   ← trace it; check
#   a4_hidden_loop([4, 4])           →  [4]      ← trace it; check
#
# CONSTRAINTS:
#   • Use `while`, not `for`. This is the point of the exercise.
#   • You MAY mutate the `ls` parameter (the tests pass you a fresh
#     copy of the caller's list, so no harm).
#   • Don't call a1_run() — reimplement the logic. Copy-pasting defeats
#     the exercise.
#   • The final result must match a1_run() for every input, including
#     the edge cases above.
#
# EDGE CASES the grader checks:
#   empty list  ·  1-element list  ·  all-equal elements
#
# RUN THIS:  python3 -m pytest -v tests/test_a_hidden_counter.py
#
def a4_hidden_loop(ls: list[int]) -> list[int]:
    """Return the values the mutating for-loop from A1 would produce."""
    out: list[int] = []
    # TODO:
    #   _counter = 0
    #   while _counter < len(ls):
    #       ...
    #       _counter += 1
    return out


# ════════════════════════════════════════════════════════════════════════
# SELF-CHECK before running pytest
# ════════════════════════════════════════════════════════════════════════
# [ ] A1 prediction: I traced the hidden counter step by step, not by
#     eyeballing the loop.
# [ ] A2 prediction: I noticed whether the removal caused a skip or not.
# [ ] A3: I did not run it. I know "finite" or "infinite" and I know why.
# [ ] A4: I used `while` with an explicit counter, not `for`.
# [ ] A4: I traced [9, 8, 7] and [4, 4] by hand and my code matches.
# [ ] I have NOT run `pytest` yet. Do that now.
# ════════════════════════════════════════════════════════════════════════