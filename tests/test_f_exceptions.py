import contextlib
import io

from exercises.f_exceptions import (
    PREDICTION_F1, f1_run,
    get_len,
    f,
)


def test_f1():
    assert PREDICTION_F1 == f1_run()


def test_get_len():
    assert get_len([1, 2, 3]) == 3
    assert get_len("abc") == 3
    assert get_len(42) == 0
    assert get_len(None) == 0


def _capture(fn, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = fn(*args)
    return result, buf.getvalue()


def test_f3_success_path():
    ret, out = _capture(f, 2)
    assert ret == 5.0
    assert out == "no error\ncleanup\n"


def test_f3_zero_division_path():
    ret, out = _capture(f, 0)
    assert ret == -1
    assert out == "caught\ncleanup\n"