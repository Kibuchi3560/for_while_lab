"""Part B — every function below RUNS but is WRONG.

═══════════════════════════════════════════════════════════════════════
  HOW TO WORK THIS FILE
  1. Read each function's docstring. It says the truth (input → output).
  2. Look at the body. It doesn't match the docstring.
  3. Figure out WHY — write down the reason (mutating while iterating,
     wrong method, wrong exception, etc.).
  4. Fix the body. Do NOT change the name, signature, or docstring.
  5. Run:  python3 -m pytest -v tests/test_b_bugs.py
═══════════════════════════════════════════════════════════════════════

Every fix here is small — usually 1 line. The point is learning to
SPOT the pattern, not writing clever code.
"""


def remove_evens(nums: list[int]) -> list[int]:
    """Return nums with all even numbers removed.

    WHAT TO DO:
        Fix the body so this function returns the list with evens gone.
        The docstring below is the truth — the body disagrees with it.

    EXAMPLES:
        remove_evens([2, 4, 6, 8])   →  []
        remove_evens([1, 2, 3, 4])   →  [1, 3]
        remove_evens([])             →  []
        remove_evens([1, 3, 5])      →  [1, 3, 5]   (nothing removed)
        remove_evens([2, 2, 4, 4])   →  []

    CONSTRAINTS:
        • Fix it however you like (list comprehension, new list, while,
          etc.) — the tests only check the return value.
        • Don't mutate `nums` — the tests pass you a fresh copy, but
          good habit is to return a new list.

    EDGE CASES the grader checks:
        empty list  ·  all even  ·  all odd  ·  adjacent duplicates

    HINT: `list.remove(x)` deletes the FIRST matching VALUE, not an
          index. What does that do to a loop that's iterating the list?

    RUN THIS:  python3 -m pytest -v tests/test_b_bugs.py::test_remove_evens
    """
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)
    return nums


def countdown_sums(ls: list[int]) -> list[int]:
    """Sum of whole list, then after dropping FRONT, then again, ... → 0.

    WHAT TO DO:
        Fix the body. The output is the "Sums of Parts" pattern:
        one value per state of the list, starting from "whole list"
        and ending with "empty list" (which sums to 0).
        That means len(ls) + 1 outputs total.

    EXAMPLES:
        countdown_sums([1, 2, 3])  →  [6, 5, 3, 0]
                                      ^  ^  ^  ^
                                      |  |  |  └── sum of empty
                                      |  |  └───── sum after dropping 1
                                      |  └──────── sum after dropping 1 and 2
                                      └─────────── sum of whole list
        countdown_sums([])         →  [0]
        countdown_sums([5])        →  [5, 0]

    CONSTRAINTS:
        • Do NOT mutate the caller's `ls`. (Use ls[:], or build a new
          result list without mutating anything.)
        • The tests check that ls is unchanged after the call.

    EDGE CASES the grader checks:
        empty list  ·  single element  ·  a 3-element list

    HINT: same bug family as A1 — a `for` loop over a shrinking list
          can't reach all the states you need. Two fixes are possible:
          (a) `while` on a COPY, or (b) never mutate at all and just
          track a running total. Both work — pick one.

    RUN THIS:  python3 -m pytest -v tests/test_b_bugs.py::test_countdown_sums
    """
    sums = []
    for x in ls:
        sums.append(sum(ls))
        ls.pop(0)
    return sums


def double_all(ls: list[int]) -> list[int]:
    """Return a NEW list with every element doubled.

    WHAT TO DO:
        Fix the body so every element becomes 2 * x. Currently it
        doesn't even run — it raises.

    EXAMPLES:
        double_all([1, 2, 3])  →  [2, 4, 6]
        double_all([])         →  []
        double_all([0])        →  [0]
        double_all([-1, -2])   →  [-2, -4]

    CONSTRAINTS:
        • Return a new list; do not mutate `ls`.
        • List comprehension OR a for loop, both fine.

    HINT: `list.append(x)` adds one item. `list.extend(iterable)`
          unpacks the iterable and adds each element. Which one wants
          an INT and which one wants an ITERABLE?

    RUN THIS:  python3 -m pytest -v tests/test_b_bugs.py::test_double_all
    """
    out = []
    for x in ls:
        out.extend(x * 2)
    return out


def get_len(obj) -> int:
    """Return len(obj) for anything that has a length, else 0.

    WHAT TO DO:
        Fix the body. This function must return the length of ANY
        sized object (list, string, tuple, ...), and 0 for objects
        that can't be sized (int, None, ...).

    EXAMPLES:
        get_len([1, 2, 3])  →  3
        get_len([])         →  0
        get_len("abc")      →  3
        get_len(42)         →  0
        get_len(None)       →  0

    CONSTRAINTS:
        • Catch ONLY the specific exception that len() raises for an
          unsized object. Do NOT use bare `except:` or `except Exception`.
        • Use len(), not `.size` — Python lists don't have `.size`.
          (Hint: if the current code misuses an attribute, that's the
          first bug. Fix that, THEN decide if you still need try/except.)

    EDGE CASES the grader checks:
        list  ·  empty list  ·  string  ·  int  ·  None

    RUN THIS:  python3 -m pytest -v tests/test_b_bugs.py::test_get_len
    """
    try:
        return obj.size
    except Exception:
        return 0


# ════════════════════════════════════════════════════════════════════════
# SELF-CHECK before running pytest
# ════════════════════════════════════════════════════════════════════════
# [ ] For each function, I can name the bug in ONE sentence. E.g.
#     "remove_evens mutates the list while iterating it."
# [ ] I didn't just re-run the tests until they went green — I can
#     explain WHY the fix works.
# [ ] My get_len catches exactly ONE exception type, not all of them.
# [ ] I have NOT run pytest yet. Do that now.
# ════════════════════════════════════════════════════════════════════════