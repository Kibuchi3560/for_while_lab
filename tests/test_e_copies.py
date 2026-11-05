"""Part E — copy semantics.

═══════════════════════════════════════════════════════════════════════
  HOW TO WORK THIS FILE
  Predict, then run. The *_run() helpers are GIVEN — do not modify.
  Set each PREDICTION_E* BEFORE running:

      python3 -m pytest -v tests/test_e_copies.py
═══════════════════════════════════════════════════════════════════════

THE RULE:
    b = a       →  b and a are the SAME object (one list, two names)
    c = a[:]    →  c is a NEW outer list, same inner elements
    d = list(a) →  same as a[:] for a list — new outer object

`a[:]` and `list(a)` both copy SHALLOWLY: the outer list is new, but
the elements inside are shared by reference. So if the elements are
themselves mutable (nested lists, dicts), mutations to them show up
in both copies.
"""

# ════════════════════════════════════════════════════════════════════════
# E1 — predict the outcomes of four operations
# ════════════════════════════════════════════════════════════════════════
# e1_run() builds three lists from a base list and mutates one of them.
# Predict each of these before reading further:
#
#   PREDICTION_E1_A         What does `a` look like after the function?
#   PREDICTION_E1_C         What does `c` look like?
#   PREDICTION_E1_D         What does `d` look like?
#   PREDICTION_E1_A_IS_B    Is a the same object as b? (True / False)
#   PREDICTION_E1_A_IS_C    Is a the same object as c? (True / False)
#   PREDICTION_E1_C_EQ_A    Is c == a by VALUE? (True / False)
#
# The *_IS_* fields use `is` (identity), the _EQ_ field uses `==`
# (value equality). They can disagree — that's the lesson.
#
PREDICTION_E1_A: list = []
PREDICTION_E1_C: list = []
PREDICTION_E1_D: list = []
PREDICTION_E1_A_IS_B = None    # ← True / False
PREDICTION_E1_A_IS_C = None
PREDICTION_E1_C_EQ_A = None


def e1_run() -> dict:
    """GIVEN. Do not modify."""
    a = [1, 2, 3]
    b = a
    c = a[:]
    d = list(a)
    b.append(99)
    return {
        "a": a,
        "c": c,
        "d": d,
        "a_is_b": a is b,
        "a_is_c": a is c,
        "c_eq_a": c == a,
    }


# ════════════════════════════════════════════════════════════════════════
# E2 — the shallow-copy surprise
# ════════════════════════════════════════════════════════════════════════
# e2_run() below builds an outer list containing the SAME inner list
# twice, then copies the outer list with [:], then mutates the inner.
#
# Predict what `outer` looks like when e2_run() returns.
#
# HINT: this is exactly why `ls[:]` only protects you at ONE level.
PREDICTION_E2: list = []


def e2_run() -> list:
    """GIVEN. Do not modify."""
    inner = [1, 2]
    outer = [inner, inner]
    copy = outer[:]
    copy[0].append(99)
    return outer


# ════════════════════════════════════════════════════════════════════════
# E3 — implement parts_sums_safe
# ════════════════════════════════════════════════════════════════════════
# Now apply the copy idea. Implement the `while True + pop(0)` version
# of parts_sums, but ensure the CALLER'S list is untouched after the
# call. The tests check this explicitly.
#
def parts_sums_safe(ls: list[int]) -> list[int]:
    """parts_sums using while + pop, but WITHOUT mutating the caller's list.

    WHAT TO DO:
        Same output as parts_sums from Part C:
            [sum(whole), sum(after dropping front), ..., 0]
        Use while True + pop(0), but work on a COPY of ls.

    EXAMPLES:
        parts_sums_safe([1, 2, 3])  →  [6, 5, 3, 0]
        parts_sums_safe([])         →  [0]

    CONSTRAINTS:
        • Use while True + pop(0) (this is the pop-version).
        • The caller's list must NOT be modified. After the call,
          the original list must have the same contents as before.
        • If you find yourself calling pop(0) on `ls` directly — stop.
          Think: which line from this part protects the caller?

    WHAT TO WATCH FOR:
        The test_does_not_mutate_input test in Part C would catch this
        if you forget the copy. But here it's a separate test, so the
        failure is loud and clear.

    RUN THIS:  python3 -m pytest -v tests/test_e_copies.py -k parts_sums_safe
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════
# SELF-CHECK before running pytest
# ════════════════════════════════════════════════════════════════════════
# [ ] I predicted E1's `is` vs `==` differences correctly.
# [ ] I predicted E2 and can explain why copy[0].append changed outer.
# [ ] parts_sums_safe makes a copy BEFORE the first pop(0).
# [ ] I know the difference between a SHALLOW and a DEEP copy.
# [ ] I have NOT run pytest yet. Do that now.
# ════════════════════════════════════════════════════════════════════════