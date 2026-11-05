import pytest

from exercises.d_append_extend import (
    PREDICTION_D1, d1_run,
    PREDICTION_D2, d2_run,
    PREDICTION_D3, d3_run,
    PREDICTION_D4, d4_run,
    fix_double_all_append,
    fix_double_all_extend,
)


def test_d1():
    assert PREDICTION_D1 == d1_run()
    assert d1_run() == [1, [2, 3]]


def test_d2():
    assert PREDICTION_D2 == d2_run()
    assert d2_run() == [1, 2, 3]


def test_d3():
    assert PREDICTION_D3 == d3_run()
    assert d3_run() == "error"


def test_d4():
    assert PREDICTION_D4 == d4_run()
    assert d4_run() == [5, "a", "b"]


@pytest.mark.parametrize("ls", [[1, 2, 3], [], [0], [-1, -2]])
@pytest.mark.parametrize("fn", [fix_double_all_append, fix_double_all_extend])
def test_fix_double_all(fn, ls):
    assert fn(list(ls)) == [x * 2 for x in ls]