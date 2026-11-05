"""Part C — same result, three implementations.

Every one of these must return, for input ls:
    [sum(ls), sum(ls[1:]), sum(ls[2:]), ..., 0]

None of them may mutate the caller's list.
Run:  python run_lab.py c
"""


def parts_sums_for(ls: list[int]) -> list[int]:
    """Read-only for loop. Do NOT mutate ls."""
    # TODO
    raise NotImplementedError


def parts_sums_while_pop(ls: list[int]) -> list[int]:
    """while True + pop(0) — but on a COPY, so the caller's list is safe."""
    # TODO
    raise NotImplementedError


def parts_sums_while_index(ls: list[int]) -> list[int]:
    """while loop over an index, no pop. Use sum(ls[i:])."""
    # TODO
    raise NotImplementedError