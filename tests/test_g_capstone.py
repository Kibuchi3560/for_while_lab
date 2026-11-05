"""Part G — capstone: same shape, new problems.

═══════════════════════════════════════════════════════════════════════
  HOW TO WORK THIS FILE
  1. Each function is a NEW problem, but the underlying pattern is the
     one you've been using: compute a whole-list aggregate, then keep
     updating as you "walk" through the elements.
  2. NONE of these may mutate the caller's list. The tests check it.
  3. Run:  python3 -m pytest -v tests/test_g_capstone.py
═══════════════════════════════════════════════════════════════════════

IMPORTANT — COUNT YOUR OUTPUTS FIRST:
    Some of these output n+1 items, others n items. Read carefully.
    (This is the "output shape" lesson from the checklist.)
"""


def parts_sums_reverse(ls: list[int]) -> list[int]:
    """Sum of whole list, then after dropping the LAST, then again → 0.

    WHAT TO DO:
        Same idea as parts_sums, but stripping from the BACK, not front.

    EXAMPLES:
        parts_sums_reverse([1, 2, 3])  →  [6, 3, 1, 0]
                                           ^  ^  ^  ^
                                           |  |  |  └─ empty
                                           |  |  └──── after dropping 3
                                           |  └─────── after dropping 3 and 2
                                           └────────── whole list
        parts_sums_reverse([])         →  [0]
        parts_sums_reverse([5])        →  [5, 0]

    CONSTRAINTS:
        • len(ls) + 1 outputs.
        • Do NOT mutate `ls`.

    HINT: `reversed(ls)` gives you the elements back-to-front without
          copying. Subtract those from the total.

    RUN THIS:  python3 -m pytest -v tests/test_g_capstone.py -k reverse
    """
    raise NotImplementedError


def parts_products(ls: list[int]) -> list[int]:
    """Product of whole list, then after dropping FRONT, then again → 1.

    WHAT TO DO:
        Same shape as parts_sums, but PRODUCT instead of sum.
        The empty-list product is 1, not 0.

    EXAMPLES:
        parts_products([2, 3, 4])  →  [24, 12, 4, 1]
        parts_products([0, 5])     →  [0, 5, 1]
        parts_products([])         →  [1]

    CONSTRAINTS:
        • len(ls) + 1 outputs.
        • Do NOT mutate `ls`.
        • Must work correctly when the list CONTAINS ZERO.
          (This is the gotcha — see below.)

    THE ZERO GOTCHA:
        The "subtract-style" trick for products (`p //= x`) CRASHES
        with ZeroDivisionError if any element is 0, and gives wrong
        results if there are multiple zeros. Don't try that trick.
        Instead, recompute the product of ls[i:] for each i —
        O(n²) but correct.

    HINT:
        for i in range(len(ls) + 1):
            p = 1
            for x in ls[i:]:
                p *= x
            out.append(p)

    RUN THIS:  python3 -m pytest -v tests/test_g_capstone.py -k products
    """
    raise NotImplementedError


def running_max(ls: list[int]) -> list[int]:
    """For each element, the max of everything up to and including it.

    WHAT TO DO:
        Walk left to right. After each element, append the maximum
        you've seen so far.

    EXAMPLES:
        running_max([3, 1, 4, 1, 5])  →  [3, 3, 4, 4, 5]
                                           ^  ^  ^  ^  ^
                                           |  |  |  |  └─ max(3,1,4,1,5)=5
                                           |  |  |  └──── still 4
                                           |  |  └─────── new max 4
                                           |  └────────── still 3
                                           └───────────── 3
        running_max([])               →  []
        running_max([7])              →  [7]

    ⚠️  OUTPUT SHAPE IS DIFFERENT:
        n inputs → n outputs. NOT n+1. There is no trailing element.
        (The "count your outputs" lesson — this is a different problem.)

    CONSTRAINTS:
        • Do NOT mutate `ls`.

    RUN THIS:  python3 -m pytest -v tests/test_g_capstone.py -k running_max
    """
    raise NotImplementedError


def remaining_counts_while(ls: list[int]) -> list[int]:
    """Count of elements left at each stage, using while + pop on a copy.

    WHAT TO DO:
        Same "strip the front" pattern, but the output is COUNTS, not
        sums. Empty-list count is 0.

    EXAMPLES:
        remaining_counts_while([1, 2, 3])  →  [3, 2, 1, 0]
        remaining_counts_while([])         →  [0]

    CONSTRAINTS:
        • Use while True + pop(0) on a COPY (like parts_sums_safe).
        • Do NOT mutate `ls`.
        • len(ls) + 1 outputs.

    RUN THIS:  python3 -m pytest -v tests/test_g_capstone.py -k "while"
    """
    raise NotImplementedError


def remaining_counts_math(ls: list[int]) -> list[int]:
    """Same output as remaining_counts_while, but with NO data loop.

    WHAT TO DO:
        Produce [len(ls), len(ls) - 1, ..., 1, 0] using plain
        arithmetic — no iteration over the elements themselves.

    EXAMPLES:
        remaining_counts_math([1, 2, 3])  →  [3, 2, 1, 0]
        remaining_counts_math([])         →  [0]

    CONSTRAINTS:
        • Do NOT mutate `ls`.
        • Don't build a copy. Don't pop anything. Just arithmetic.

    HINT: a list comprehension over range() does it in one line.

    COMPLEXITY:
        O(n) — the while version was O(n²) because each pop(0) is
        O(n). This one never touches the elements at all.

    RUN THIS:  python3 -m pytest -v tests/test_g_capstone.py -k "math"
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════
# SELF-CHECK before running pytest
# ════════════════════════════════════════════════════════════════════════
# [ ] parts_sums_reverse: n+1 outputs, uses reversed(ls), no mutation.
# [ ] parts_products: handles zeros, does NOT use p //= x.
# [ ] running_max: n outputs (not n+1). I counted before writing.
# [ ] remaining_counts_while: n+1 outputs, uses while + pop on a copy.
# [ ] remaining_counts_math: no loop over elements, one comprehension.
# [ ] I can name the complexity of each.
# [ ] I have NOT run pytest yet. Do that now.
# ════════════════════════════════════════════════════════════════════════