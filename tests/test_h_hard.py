import pytest

from exercises.h_hard import (
    rotate_left_in_place,
    sliding_window_max,
    flatten_deeply,
)


# ════════════════════════════════════════════════════════════════════════
# H1 — rotate_left_in_place
# ════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize(
    "initial,k,expected",
    [
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([1, 2, 3], 1, [2, 3, 1]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3], 5, [3, 1, 2]),          # k > len → 5 % 3 == 2 → left by 2
        ([1, 2, 3], -1, [3, 1, 2]),         # negative k rotates right
        ([1, 2, 3], -4, [3, 1, 2]),         # -4 % 3 == 2 → left by 2
        ([1], 0, [1]),
        ([1], 1, [1]),
        ([1], 17, [1]),
        ([], 0, []),
        ([], 5, []),                        # empty: any k → unchanged
    ],
)
def test_rotate_left_in_place_mutates_caller(initial, k, expected):
    nums = list(initial)                    # fresh copy for the test
    original_id = id(nums)

    result = rotate_left_in_place(nums, k)

    assert id(nums) == original_id, (
        "The list object was REBOUND, not mutated in place. "
        "The caller's list is the same object as before the call."
    )
    assert nums == expected, (
        f"After rotation by k={k}, expected {expected}, got {nums}. "
        "Did you forget to normalize k with k % len(ls)?"
    )
# ════════════════════════════════════════════════════════════════════════
# H2 — sliding_window_max
# ════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize(
    "ls,k,expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1, 2, 3], 1, [1, 2, 3]),
        ([1, 2, 3], 2, [2, 3]),
        ([1, 2, 3], 3, [3]),
        ([5], 1, [5]),
        ([-1, -2, -3], 1, [-1, -2, -3]),
        ([4, 4, 4, 4], 2, [4, 4, 4]),
        ([2, 1, 3, 1, 2], 3, [3, 3, 3]),
    ],
)
def test_sliding_window_max_normal(ls, k, expected):
    assert sliding_window_max(list(ls), k) == expected


def test_sliding_window_max_k_too_big():
    assert sliding_window_max([1, 2, 3], 5) == []


def test_sliding_window_max_empty():
    assert sliding_window_max([], 1) == []
    assert sliding_window_max([], 5) == []


@pytest.mark.parametrize("bad_k", [0, -1, -100])
def test_sliding_window_max_bad_k_raises(bad_k):
    with pytest.raises(ValueError):
        sliding_window_max([1, 2, 3], bad_k)


def test_sliding_window_max_does_not_mutate_input():
    nums = [1, 3, -1, -3, 5]
    sliding_window_max(nums, 2)
    assert nums == [1, 3, -1, -3, 5]


# ════════════════════════════════════════════════════════════════════════
# H3 — flatten_deeply
# ════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize(
    "nested,expected",
    [
        # Basics
        ([1, 2, 3], [1, 2, 3]),
        ([1, [2, 3], 4], [1, 2, 3, 4]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
        ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
        ([[1, 2], [3, [4, [5, 6]]], 7], [1, 2, 3, 4, 5, 6, 7]),
        # Empty / nested empties
        ([], []),
        ([[], [[]], [[[]]]], []),
        ([1, [], [[2]], [[]], 3], [1, 2, 3]),
        # Strings are SCALARS — do not iterate chars
        ([1, "abc", [2, "def"]], [1, "abc", 2, "def"]),
        (["a", ["b", ["c"]]], ["a", "b", "c"]),
        ([[""], [""]], ["", ""]),
        # Tuples are SCALARS — do not unpack them
        ([1, (2, 3)], [1, (2, 3)]),
        ([(1, 2), [3, (4, 5)]], [(1, 2), 3, (4, 5)]),
        # Mixed scalars
        ([None, [True, [1.5, [False]]]], [None, True, 1.5, False]),
        ([{"a": 1}, [{2}, [frozenset()]]], [{"a": 1}, {2}, frozenset()]),
    ],
)
def test_flatten_deeply(nested, expected):
    assert flatten_deeply(nested) == expected


def test_flatten_deeply_does_not_mutate():
    original_inner = [2, [3]]
    nested = [1, original_inner]
    nested_copy = [1, original_inner]

    flatten_deeply(nested)
    # Our input wasn't touched
    assert nested == nested_copy
    assert original_inner == [2, [3]]


def test_flatten_deeply_returns_new_list():
    nested = [1, 2, 3]
    result = flatten_deeply(nested)
    assert result is not nested
    result.append(99)
    assert nested == [1, 2, 3]      # caller's list unaffected