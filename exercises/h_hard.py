"""Part H — HARD / SUPER-HARD challenge problems.

═══════════════════════════════════════════════════════════════════════
  HOW TO WORK THIS FILE
  Three challenges, each harder than anything in A–G.
  Read each docstring fully before typing. Predict on paper.
  Run:  python3 -m pytest -v tests/test_h_hard.py
       python3 -m pytest -v tests/test_h_hard.py -k rotate
       python3 -m pytest -v tests/test_h_hard.py -k sliding
       python3 -m pytest -v tests/test_h_hard.py -k flatten
═══════════════════════════════════════════════════════════════════════

  H1 — HARD        rotate_left_in_place   (subtle in-place bug)
  H2 — HARD        sliding_window_max     (edge cases + indexes)
  H3 — SUPER HARD  flatten_deeply         (recursion + append/extend)
═══════════════════════════════════════════════════════════════════════
"""


# ════════════════════════════════════════════════════════════════════════
# H1 — HARD  ·  rotate_left_in_place  ·  bug to fix
# ════════════════════════════════════════════════════════════════════════
def rotate_left_in_place(ls: list, k: int) -> None:
    """Rotate ls LEFT by k positions, IN PLACE. Return None.

    WHAT TO DO:
        The current body LOOKS correct but is broken in two ways.
        Find both bugs and fix them.

    WHAT "IN PLACE" MEANS (read twice):
        • The caller's list OBJECT must be modified.
        • id(ls) must be the SAME before and after the call.
        • The function returns None (not a new list).
        • After the call, the caller's variable must show the rotation.

    EXAMPLES:
        nums = [1, 2, 3, 4, 5]
        rotate_left_in_place(nums, 2)
        # nums is now [3, 4, 5, 1, 2]     ← caller's list WAS changed
        # the return value is None

        nums = [1, 2, 3]
        rotate_left_in_place(nums, 5)    # k > len
        # nums is now [2, 3, 1]          ← 5 % 3 = 2 effective rotation

        nums = [1, 2, 3]
        rotate_left_in_place(nums, 0)    # k = 0
        # nums is now [1, 2, 3]          ← unchanged

        nums = [1, 2, 3]
        rotate_left_in_place(nums, -1)   # negative k rotates RIGHT
        # nums is now [3, 1, 2]

        nums = []
        rotate_left_in_place(nums, 4)    # empty list
        # nums is now []                 ← no error

    CONSTRAINTS:
        • Must modify ls IN PLACE — do NOT rebind it. `ls = ...` is
          the bug, not the fix. Use slice assignment `ls[:] = ...`
          or `.pop()`/`.append()`/`.insert()`.
        • Must return None. The test asserts `result is None`.
        • Must normalize k. `k % len(ls)` works — EXCEPT when ls is
          empty (len 0 → ZeroDivisionError). Guard that case.
        • Negative k must work (Python's `%` handles that — check it).

    THE TWO BUGS IN THE CURRENT BODY (find them yourself first):
        1. It rebinds `ls` to a new list. The caller's list is
           unchanged. "In place" broken.
        2. When k > len(ls), the slicing `ls[k:] + ls[:k]` gives the
           wrong rotation (it does NOT wrap around the way you want).
           Fix: normalize k with `% len(ls)` first.

    COMPLEXITY:
        O(n). Both the buggy and correct versions are O(n); the bug
        is about identity/state, not speed.

    RUN THIS:  python3 -m pytest -v tests/test_h_hard.py -k rotate
    """
    if not ls:               # avoid ZeroDivisionError on empty list
        return None
    k %= len(ls)             # normalizes k > len and negative k
    ls[:] = ls[k:] + ls[:k]


# ════════════════════════════════════════════════════════════════════════
# H2 — HARD  ·  sliding_window_max  ·  solve from scratch
# ════════════════════════════════════════════════════════════════════════
def sliding_window_max(ls: list[int], k: int) -> list[int]:
    """Return the maximum of each sliding window of size k.

    WHAT TO DO:
        Walk a window of size k across ls and return a new list
        containing the max of every window.

    EXAMPLES:
        sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
            → [3, 3, 5, 5, 6, 7]

            windows:                maxes:
            [1,  3, -1]  → 3
            [   3, -1, -3] → 3
            [      -1, -3,  5] → 5
            [         -3,  5,  3] → 5
            [              5,  3,  6] → 6
            [                  3,  6,  7] → 7

        sliding_window_max([1, 2, 3], 1)  →  [1, 2, 3]
        sliding_window_max([1, 2, 3], 3)  →  [3]
        sliding_window_max([5], 1)        →  [5]

    EDGE CASES — the tests check all of these:
        • k <= 0            →  raise ValueError
        • k > len(ls)       →  return []   (no window fits)
        • empty ls          →  return []   (no window fits — even for k=1)
        • list of one elem  →  [max] if k <= 1
        • negative numbers  →  handled naturally

    CONSTRAINTS:
        • Return a NEW list. Do NOT mutate ls.
        • Don't use a library (no numpy, no itertools). Pure Python.
        • Naive O(n*k) is fine — an O(n) monotonic-deque version is
          welcome as a stretch goal but not required.

    HINTS:
        • Number of windows = len(ls) - k + 1  (when k <= len(ls)).
        • For each starting index `i` from 0 to len(ls) - k:
              append max(ls[i : i + k])
        • That's it. The hard part is the edges, not the loop.

    COMPLEXITY:
        Naive: O(n·k). Any solution that works will pass.

    RUN THIS:  python3 -m pytest -v tests/test_h_hard.py -k sliding
    """
def sliding_window_max(ls: list[int], k: int) -> list[int]:
    """Return the maximum of each sliding window of size k.

    WHAT TO DO:
        Walk a window of size k across ls and return a new list
        containing the max of every window.

    EXAMPLES:
        sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
            → [3, 3, 5, 5, 6, 7]

            windows:                maxes:
            [1,  3, -1]  → 3
            [   3, -1, -3] → 3
            [      -1, -3,  5] → 5
            [         -3,  5,  3] → 5
            [              5,  3,  6] → 6
            [                  3,  6,  7] → 7

        sliding_window_max([1, 2, 3], 1)  →  [1, 2, 3]
        sliding_window_max([1, 2, 3], 3)  →  [3]
        sliding_window_max([5], 1)        →  [5]

    EDGE CASES — the tests check all of these:
        • k <= 0            →  raise ValueError
        • k > len(ls)       →  return []   (no window fits)
        • empty ls          →  return []   (no window fits — even for k=1)
        • list of one elem  →  [max] if k <= 1
        • negative numbers  →  handled naturally

    CONSTRAINTS:
        • Return a NEW list. Do NOT mutate ls.
        • Don't use a library (no numpy, no itertools). Pure Python.
        • Naive O(n*k) is fine — an O(n) monotonic-deque version is
          welcome as a stretch goal but not required.

    HINTS:
        • Number of windows = len(ls) - k + 1  (when k <= len(ls)).
        • For each starting index `i` from 0 to len(ls) - k:
              append max(ls[i : i + k])
        • That's it. The hard part is the edges, not the loop.

    COMPLEXITY:
        Naive: O(n·k). Any solution that works will pass.

    RUN THIS:  python3 -m pytest -v tests/test_h_hard.py -k sliding
    """
    if k <= 0:   
        raise ValueError("k must be positive")
    if k > len(ls):          # also covers empty ls
        return []

    maximum = []
    for i in range(len(ls) - k + 1):
        window = ls[i : i + k]
        maximum.append(max(window))
    return maximum
        


        


    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════
# H3 — SUPER HARD  ·  flatten_deeply  ·  solve from scratch
# ════════════════════════════════════════════════════════════════════════
def flatten_deeply(lst: list) -> list:
    """Recursively flatten arbitrarily-nested lists into one flat list.

    WHAT TO DO:
        Produce a new list containing every non-list scalar in `lst`,
        in left-to-right order, no matter how deeply nested.

    THE TYPE RULE (this is the whole problem):
        Recurse ONLY into `list`. Everything else is a scalar:
            • str          → scalar (do NOT iterate its characters)
            • tuple        → scalar (do NOT unpack it)
            • dict, set    → scalar
            • int, float   → scalar
            • None         → scalar

        That means isinstance(x, list) is the ONLY check you need.
        isinstance(x, (list, tuple)) or isinstance(x, Iterable) is
        WRONG — those would flatten things you must not touch.

    EXAMPLES:
        flatten_deeply([1, [2, [3, [4]]]])
            → [1, 2, 3, 4]

        flatten_deeply([])
            → []

        flatten_deeply([[], [[]], [[[]]]])
            → []                    ← empty nested lists flatten to nothing

        flatten_deeply([1, "abc", [2, "def"]])
            → [1, "abc", 2, "def"]  ← "abc" stays INTACT (string is scalar)

        flatten_deeply([1, (2, 3)])
            → [1, (2, 3)]           ← tuple stays intact

        flatten_deeply([[1, 2], [3, [4, [5, 6]]], 7])
            → [1, 2, 3, 4, 5, 6, 7]

        flatten_deeply([None, [True, [1.5]]])
            → [None, True, 1.5]

    CONSTRAINTS:
        • Return a NEW list. Do NOT mutate the input.
        • Use recursion (this is the recursion exercise).
        • Do NOT use itertools.chain, no library flatteners.

    THE TWO CLASSIC BUGS (avoid both):
        1. `result.append(flatten_deeply(x))` when x is a list.
           → produces [[...], [...]] — nested output, WRONG.
           You want `result.extend(flatten_deeply(x))`.
        2. `isinstance(x, (list, tuple))` or `isinstance(x, Iterable)`.
           → flattens tuples and/or strings. WRONG.
           Only `isinstance(x, list)` is correct.

    SKELETON (fill in the two branches yourself):
        result = []
        for x in lst:
            if isinstance(x, list):
                # ??? append or extend? flatten what?
            else:
                # ??? append or extend? what?
        return result

    COMPLEXITY:
        O(n) where n is the total number of scalars in the tree.
        Recursion depth is bounded by the maximum nesting depth.

    RUN THIS:  python3 -m pytest -v tests/test_h_hard.py -k flatten
    """
    result = []
    for x in lst:
        if not isinstance(x, list):
            result.append(x)
        else:
            result.extend(flatten_deeply(x))
    return result

    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════
# SELF-CHECK before running pytest
# ════════════════════════════════════════════════════════════════════════
# H1:
#   [ ] I found BOTH bugs (rebinding, k-not-normalized) before writing
#       the fix.
#   [ ] After the call, id(nums) is unchanged (I checked with id()).
#   [ ] My function returns None.
#   [ ] Empty list does not crash on `k % len(ls)`.
#
# H2:
#   [ ] k <= 0 raises ValueError (not returns []).
#   [ ] k > len(ls) returns [].
#   [ ] Empty list returns [].
#   [ ] I did not mutate ls.
#   [ ] I wrote the number of windows formula on paper: len(ls) - k + 1.
#
# H3:
#   [ ] I used isinstance(x, list), NOT (list, tuple) or Iterable.
#   [ ] When recursing into a list, I used .extend(), not .append().
#   [ ] Strings stay intact. Tuples stay intact.
#   [ ] Empty nested lists like [[], [[]]] produce [].
#   [ ] I did not mutate the input.
#
# [ ] I have NOT run pytest yet. Do that now.
# ════════════════════════════════════════════════════════════════════════