"""Part A — the hidden counter.

Fill in every PREDICTION_* BEFORE running the tests.
Then run:  python run_lab.py a
"""

# --------------------------------------------------------------------
# A1 — the classic skip.  a1_run() is GIVEN, do not modify it.
# --------------------------------------------------------------------
PREDICTION_A1: list[int] = []   # <-- the numbers you expect to be printed


def a1_run() -> list[int]:
    ls = [1, 2, 3, 4, 5]
    out = []
    for i in ls:
        out.append(i)
        ls.pop(0)
    return out


# --------------------------------------------------------------------
# A2 — the trap that does NOT skip.  a2_run() is GIVEN, do not modify.
# --------------------------------------------------------------------
PREDICTION_A2: list[int] = []   # <-- the numbers you expect to be printed


def a2_run() -> list[int]:
    ls = [1, 2, 3, 4]
    out = []
    for i in ls:
        out.append(i)
        if i == 2:
            ls.remove(3)
    return out


# --------------------------------------------------------------------
# A3 — DO NOT RUN THIS. Predict on paper.
#
#     ls = [1, 2, 3]
#     for i in ls:
#         ls.append(i)
#
# --------------------------------------------------------------------
PREDICTION_A3 = ""   # <-- "finite" or "infinite"
WHY_A3 = ""          # <-- one sentence


# --------------------------------------------------------------------
# A4 — rewrite A1 using the hidden-counter `while` form.
# Must produce EXACTLY the same output as a1_run() for any input.
# --------------------------------------------------------------------
def a4_hidden_loop(ls: list[int]) -> list[int]:
    """Return the values the mutating for-loop from A1 would print."""
    out: list[int] = []
    # TODO:
    #   _counter = 0
    #   while _counter < len(ls):
    #       ...
    #       _counter += 1
    return out