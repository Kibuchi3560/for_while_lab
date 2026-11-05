import pytest

from exercises.g_capstone import (
    parts_sums_reverse,
    parts_products,
    running_max,
    remaining_counts_while,
    remaining_counts_math,
)


@pytest.mark.parametrize(
    "arg,expected",
    [
        ([1, 2, 3], [6, 3, 1, 0]),
        ([], [0]),
        ([5], [5, 0]),
    ],
)
def test_parts_sums_reverse(arg, expected):
    nums = list(arg)
    assert parts_sums_reverse(nums) == expected
    assert nums == list(arg)


@pytest.mark.parametrize(
    "arg,expected",
    [
        ([2, 3, 4], [24, 12, 4, 1]),
        ([0, 5], [0, 5, 1]),
        ([], [1]),
    ],
)
def test_parts_products(arg, expected):
    nums = list(arg)
    assert parts_products(nums) == expected
    assert nums == list(arg)


@pytest.mark.parametrize(
    "arg,expected",
    [
        ([3, 1, 4, 1, 5], [3, 3, 4, 4, 5]),
        ([], []),
        ([7], [7]),
    ],
)
def test_running_max(arg, expected):
    nums = list(arg)
    assert running_max(nums) == expected
    assert nums == list(arg)


@pytest.mark.parametrize("fn", [remaining_counts_while, remaining_counts_math])
@pytest.mark.parametrize("arg,expected", [([1, 2, 3], [3, 2, 1, 0]), ([], [0])])
def test_remaining_counts(fn, arg, expected):
    nums = list(arg)
    assert fn(nums) == expected
    assert nums == list(arg)