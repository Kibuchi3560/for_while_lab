"""Part G — same shape, new problems.

No function here may mutate the caller's list.
Run:  python run_lab.py g
"""


def parts_sums_reverse(ls: list[int]) -> list[int]:
    """Sum of the whole list, then after dropping the LAST element, ...

    parts_sums_reverse([1, 2, 3]) -> [6, 3, 1, 0]
    parts_sums_reverse([])        -> [0]
    """
    # TODO
    raise NotImplementedError


def parts_products(ls: list[int]) -> list[int]:
    """Product of the whole list, then after dropping the FRONT, ...

    parts_products([2, 3, 4]) -> [24, 12, 4, 1]
    parts_products([0, 5])    -> [0, 5, 1]
    parts_products([])        -> [1]
    """
    # TODO
    raise NotImplementedError


def running_max(ls: list[int]) -> list[int]:
    """Max value seen so far, for each element.

    running_max([3, 1, 4, 1, 5]) -> [3, 3, 4, 4, 5]
    running_max([])              -> []
    """
    # TODO
    raise NotImplementedError


def remaining_counts_while(ls: list[int]) -> list[int]:
    """Count of elements left at each stage, using while + pop on a COPY.

    remaining_counts_while([1, 2, 3]) -> [3, 2, 1, 0]
    remaining_counts_while([])        -> [0]
    """
    # TODO
    raise NotImplementedError


def remaining_counts_math(ls: list[int]) -> list[int]:
    """Same output, but with NO loop over the data — plain arithmetic."""
    # TODO
    raise NotImplementedError