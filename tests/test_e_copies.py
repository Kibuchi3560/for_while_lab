from exercises.e_copies import (
    PREDICTION_E1_A, PREDICTION_E1_C, PREDICTION_E1_D,
    PREDICTION_E1_A_IS_B, PREDICTION_E1_A_IS_C, PREDICTION_E1_C_EQ_A,
    e1_run,
    PREDICTION_E2, e2_run,
    parts_sums_safe,
)


def test_e1():
    r = e1_run()
    assert PREDICTION_E1_A == r["a"]
    assert PREDICTION_E1_C == r["c"]
    assert PREDICTION_E1_D == r["d"]
    assert PREDICTION_E1_A_IS_B == r["a_is_b"]
    assert PREDICTION_E1_A_IS_C == r["a_is_c"]
    assert PREDICTION_E1_C_EQ_A == r["c_eq_a"]


def test_e2():
    assert PREDICTION_E2 == e2_run()
    assert e2_run() == [[1, 2, 99], [1, 2, 99]]


def test_parts_sums_safe_correct():
    assert parts_sums_safe([1, 2, 3]) == [6, 5, 3, 0]
    assert parts_sums_safe([]) == [0]


def test_parts_sums_safe_does_not_mutate():
    nums = [1, 2, 3]
    parts_sums_safe(nums)
    assert nums == [1, 2, 3]