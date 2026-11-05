import pytest

from exercises.a_hidden_counter import (
    PREDICTION_A1, a1_run,
    PREDICTION_A2, a2_run,
    PREDICTION_A3,
    a4_hidden_loop,
)


def _reference_a1(ls):
    """The mutating for-loop, expanded into its hidden while form."""
    ls = list(ls)
    out = []
    counter = 0
    while counter < len(ls):
        out.append(ls[counter])
        ls.pop(0)
        counter += 1
    return out


def test_a1_prediction_matches_reality():
    actual = a1_run()
    assert PREDICTION_A1 == actual, (
        f"Prediction {PREDICTION_A1} != actual {actual}. "
        "Re-trace the hidden counter."
    )


def test_a1_known_answer():
    assert a1_run() == [1, 3, 5]


def test_a2_prediction_matches_reality():
    actual = a2_run()
    assert PREDICTION_A2 == actual, (
        f"Prediction {PREDICTION_A2} != actual {actual}. "
        "Did you assume every mutation skips?"
    )


def test_a2_known_answer():
    assert a2_run() == [1, 2, 4]


def test_a3_is_infinite():
    assert PREDICTION_A3.lower() == "infinite"


@pytest.mark.parametrize("ls", [[1, 2, 3, 4, 5], [1], [], [9, 8, 7], [4, 4]])
def test_a4_matches_reference(ls):
    assert a4_hidden_loop(list(ls)) == _reference_a1(ls)