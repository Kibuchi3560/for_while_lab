"""Part D — append vs extend.

═══════════════════════════════════════════════════════════════════════
  HOW TO WORK THIS FILE
  Predict, then run. The *_run() helpers are GIVEN — do not modify.
  Set each PREDICTION_D* to what you expect, THEN run:

      python3 -m pytest -v tests/test_d_append_extend.py

  If a prediction is wrong, the test message tells you the actual
  value. Do NOT update the prediction to match reality — instead,
  re-trace on paper and understand WHY it was different.
═══════════════════════════════════════════════════════════════════════

THE RULE:
    lst.append(x)        adds x as ONE item → list grows by 1
    lst.extend(iterable) unpacks iterable → list grows by many
    lst.extend(5)        ERROR — 5 is not iterable
    lst.extend("ab")     adds 'a' and 'b' as TWO items (a string IS
                         iterable — its characters are the items)
"""

# ════════════════════════════════════════════════════════════════════════
# D1 — append a list
# ════════════════════════════════════════════════════════════════════════
# Predict the return value of d1_run() below. The result is a list.
PREDICTION_D1: list = []


def d1_run():
    """GIVEN. Do not modify."""
    a = [1]
    a.append([2, 3])
    return a


# ════════════════════════════════════════════════════════════════════════
# D2 — extend with a list
# ════════════════════════════════════════════════════════════════════════
# Predict the return value of d2_run() below.
PREDICTION_D2: list = []


def d2_run():
    """GIVEN. Do not modify."""
    b = [1]
    b.extend([2, 3])
    return b


# ════════════════════════════════════════════════════════════════════════
# D3 — extend with a NON-iterable
# ════════════════════════════════════════════════════════════════════════
# Predict whether d3_run() returns "ok" or "error".
#   Set PREDICTION_D3 to the literal string  "ok"  or  "error"
PREDICTION_D3 = ""


def d3_run():
    """GIVEN. Do not modify."""
    c = []
    try:
        c.extend(5)
        return "ok"
    except TypeError:
        return "error"


# ════════════════════════════════════════════════════════════════════════
# D4 — append then extend a STRING
# ════════════════════════════════════════════════════════════════════════
# Predict the return value of d4_run() below.
#   Reminder: "ab" is a string — an iterable of characters.
PREDICTION_D4: list = []


def d4_run():
    """GIVEN. Do not modify."""
    d = []
    d.append(5)
    d.extend("ab")
    return d


# ════════════════════════════════════════════════════════════════════════
# D5 — fix B3 TWO different ways
# ════════════════════════════════════════════════════════════════════════
# The buggy double_all() in Part B used .extend(x * 2) and crashed.
# Fix it here TWICE — once using append, once using extend.

def fix_double_all_append(ls: list[int]) -> list[int]:
    """Return a new list with each element doubled — using .append() only.

    WHAT TO DO:
        Loop over ls, compute x * 2 for each, and add it to the result
        using .append(). Do not use .extend() in this function.

    EXAMPLES:
        fix_double_all_append([1, 2, 3])  →  [2, 4, 6]
        fix_double_all_append([])         →  []
        fix_double_all_append([0])        →  [0]
        fix_double_all_append([-1, -2])   →  [-2, -4]

    CONSTRAINT: do not mutate `ls`.

    RUN THIS:  python3 -m pytest -v tests/test_d_append_extend.py -k append
    """
    raise NotImplementedError


def fix_double_all_extend(ls: list[int]) -> list[int]:
    """Return a new list with each element doubled — using .extend() only.

    WHAT TO DO:
        Same output as fix_double_all_append, but every addition to
        the result must go through .extend(). Do not use .append().

    HINT: .extend() needs an ITERABLE. What's a one-element iterable
          you can wrap x * 2 in?

    EXAMPLES:
        fix_double_all_extend([1, 2, 3])  →  [2, 4, 6]
        fix_double_all_extend([])         →  []
        fix_double_all_extend([0])        →  [0]
        fix_double_all_extend([-1, -2])   →  [-2, -4]

    CONSTRAINT: do not mutate `ls`.

    RUN THIS:  python3 -m pytest -v tests/test_d_append_extend.py -k extend
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════
# SELF-CHECK before running pytest
# ════════════════════════════════════════════════════════════════════════
# [ ] I can state the difference between append and extend in ONE line.
# [ ] I predicted D3 correctly by remembering 5 is not iterable.
# [ ] I predicted D4 correctly — string elements are single chars.
# [ ] fix_double_all_append uses ONLY .append().
# [ ] fix_double_all_extend uses ONLY .extend().
# [ ] I have NOT run pytest yet. Do that now.
# ════════════════════════════════════════════════════════════════════════