import pytest

from exercises.b_bugs import remove_evens, countdown_sums, double_all, get_len


@pytest.mark.parametrize(
    "arg,expected",
    [
        ([2, 4, 6, 8], []),
        ([1, 2, 3, 4], [1, 3]),
        ([], []),
        ([1, 3, 5], [1, 3, 5]),
        ([2, 2, 4, 4], []),
    ],
)
def test_remove_evens(arg, expected):
    assert remove_evens(arg) == expected


@pytest.mark.parametrize(
    "arg,expected",
    [
        ([1, 2, 3], [6, 5, 3, 0]),
        ([], [0]),
        ([5], [5, 0]),
    ],
)
def test_countdown_sums(arg, expected):
    assert countdown_sums(list(arg)) == expected


@pytest.mark.parametrize(
    "arg,expected",
    [([1, 2, 3], [2, 4, 6]), ([], []), ([0], [0])],
)
def test_double_all(arg, expected):
    assert double_all(arg) == expected


@pytest.mark.parametrize(
    "arg,expected",
    [([1, 2, 3], 3), ([], 0), ("abc", 3), (42, 0), (None, 0)],
)
def test_get_len(arg, expected):
    assert get_len(arg) == expected