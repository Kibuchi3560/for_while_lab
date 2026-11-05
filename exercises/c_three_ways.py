"""Part C — same result, three implementations.

═══════════════════════════════════════════════════════════════════════
  HOW TO WORK THIS FILE
  1. Each function must compute the SAME output: parts_sums.
  2. Each uses a DIFFERENT technique — that's the point.
  3. Run:  python3 -m pytest -v tests/test_c_three_ways.py
═══════════════════════════════════════════════════════════════════════

THE PROBLEM (all three functions):
    For an input list ls, return:
        [ sum(ls), sum(ls[1:]), sum(ls[2:]), ..., sum([]) ]
    In words: sum of the whole list, then sum after dropping the
    front, then again, ending with 0.

EXAMPLES:
    parts_sums([1, 2, 3, 4])  →  [10, 9, 7, 4, 0]
    parts_sums([])            →  [0]
    parts_sums([5])           →  [5, 0]
    parts_sums([1, 1, 1])     →  [3, 2, 1, 0]

HARD CONSTRAINT on ALL THREE:
    ★ Do NOT mutate the caller's list.  ★
    The tests check that ls is unchanged after the call. If you use
    .pop(), .remove(), .append() etc. on `ls` itself → test fails.
    (You may mutate a COPY: `new_ls = ls[:]`.)
"""


def parts_sums_for(ls: list[int]) -> list[int]:
    """Implementation 1 — READ-ONLY `for` loop.

    WHAT TO DO:
        Use a `for` loop that iterates ls but NEVER modifies it.
        Track a running total in a variable, subtract each element,
        append after each subtraction.

    TECHNIQUE:
        n = sum(ls)          # compute total once
        out = [n]            # seed the result with the total
        for x in ls:
            n -= x           # running total goes DOWN
            out.append(n)
        return out

    (Yes, that's the answer written as pseudo-code — implement it.
     The point of C is that ALL THREE must produce the same output,
     so here you can be literal.)

    WHY `for` IS SAFE HERE:
        You only READ from `ls`. Never `pop`, `remove`, `append`,
        `insert` on it. The hidden counter and the list never move
        relative to each other → no skips.

    COMPLEXITY:
        O(n) — one sum pass, one loop pass.

    RUN THIS:  python3 -m pytest -v tests/test_c_three_ways.py -k parts_sums_for
    """
    raise NotImplementedError


def parts_sums_while_pop(ls: list[int]) -> list[int]:
    """Implementation 2 — `while True` + pop(0) on a COPY.

    WHAT TO DO:
        Copy ls first:      new_ls = ls[:]
        Loop forever:
            append sum(new_ls) to out
            if new_ls is empty, break
            new_ls.pop(0)
        return out.

    TECHNIQUE:
        while True:
            out.append(sum(new_ls))
            if not new_ls:
                break
            new_ls.pop(0)

    WHY `while` AND NOT `for` HERE:
        The loop's exit depends on new_ls becoming empty, which
        CHANGES on every pass. `while` re-checks each time. A `for`
        loop would freeze the length at the start and stop early
        (this is exactly the A1 bug).

    WHY WE COPY:
        `pop(0)` destroys the list it's called on. Without the copy,
        calling parts_sums would leave the CALLER's list empty.

    COMPLEXITY:
        O(n²) — pop(0) is O(n) and sum() is O(n), each done ~n times.
        Slower than the `for` version. That's fine — you're learning
        the pattern, not optimizing.

    RUN THIS:  python3 -m pytest -v tests/test_c_three_ways.py -k while_pop
    """
    raise NotImplementedError


def parts_sums_while_index(ls: list[int]) -> list[int]:
    """Implementation 3 — `while` over an INDEX, no pop, use slicing.

    WHAT TO DO:
        Start i = 0. While i <= len(ls):
            append sum(ls[i:]) to out
            i += 1
        return out.

    TECHNIQUE:
        i = 0
        while i <= len(ls):        # note: <=, not <
            out.append(sum(ls[i:]))  # ls[i:] is a fresh slice — safe
            i += 1

    TWO THINGS TO NOTICE:
        1. `<=`, not `<`. You need n+1 iterations to hit the empty
           slice at the end (which sums to 0).
        2. `ls[i:]` creates a NEW list each time — so this function
           never mutates `ls`. Slicing is read-only.

    COMPLEXITY:
        O(n²) — each slice is O(n) and sum over it is O(n).

    RUN THIS:  python3 -m pytest -v tests/test_c_three_ways.py -k while_index
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════
# SELF-CHECK before running pytest
# ════════════════════════════════════════════════════════════════════════
# [ ] All three return the SAME list for every input I tried on paper.
# [ ] None of them do pop / remove / append / insert / del on `ls`.
# [ ] parts_sums_for uses `for`, the other two use `while`.
# [ ] parts_sums_while_pop makes a copy before any pop(0).
# [ ] parts_sums_while_index uses `<=` (n+1 iterations, not n).
# [ ] I can rank the three by complexity and say why.
# [ ] I have NOT run pytest yet. Do that now.
# ════════════════════════════════════════════════════════════════════════