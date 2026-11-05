import pytest

from exercises.c_three_ways import (
    parts_sums_for,
    parts_sums_while_pop,
    parts_sums_while_index,
)

IMPLEMENTATIONS = [parts_sums_for, parts_sums_while_pop, parts_sums_while_index]

CASES = [
    ([1, 2, 3, 4], [10, 9, 7, 4, 0]),
    ([], [0]),
    ([5], [5, 0]),
    ([1, 1, 1], [3, 2, 1, 0]),
]


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
@pytest.mark.parametrize("ls,expected", CASES)
def test_parts_sums(fn, ls, expected):
    assert fn(list(ls)) == expected


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_does_not_mutate_input(fn):
    nums = [1, 2, 3, 4]
    fn(nums)
    assert nums == [1, 2, 3, 4], f"{fn.__name__} mutated the caller's list"