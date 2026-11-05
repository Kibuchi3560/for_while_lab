"""Part F — try / except.

Run:  python run_lab.py f
"""

# ---- F1 — name the exception (do not run first) --------------------
PREDICTION_F1: dict[str, str] = {
    "int_abc": "",   # int("abc")
    "index": "",     # [1, 2][5]
    "key": "",       # {"a": 1}["b"]
    "zero": "",      # 10 / 0
    "add": "",       # "a" + 1
}


def f1_run() -> dict[str, str]:
    out: dict[str, str] = {}
    try:
        int("abc")
    except Exception as e:
        out["int_abc"] = type(e).__name__
    try:
        [1, 2][5]
    except Exception as e:
        out["index"] = type(e).__name__
    try:
        {"a": 1}["b"]
    except Exception as e:
        out["key"] = type(e).__name__
    try:
        10 / 0
    except Exception as e:
        out["zero"] = type(e).__name__
    try:
        "a" + 1
    except Exception as e:
        out["add"] = type(e).__name__
    return out


# ---- F2 — fix get_len ---------------------------------------------
def get_len(obj) -> int:
    """Return len(obj) for any sized object, else 0.

    get_len([1, 2, 3]) -> 3
    get_len(42)        -> 0

    Rule: catch ONLY the exception that len() can raise for a bad type.
    """
    # TODO
    raise NotImplementedError


# ---- F3 — write f() from the spec ---------------------------------
def f(x):
    """Return 10 / x, but with this exact behavior:

    - on ZeroDivisionError: print "caught" and return -1
    - otherwise:            print "no error" and return the result
    - in ALL cases:         print "cleanup" as the very last thing

    Use try / except / else / finally — no bare except.
    """
    # TODO
    raise NotImplementedError


# ---- F4 — answer in a string --------------------------------------
F4_WHY_BARE_EXCEPT_IS_BAD = ""
# <-- Name one concrete bug a bare `except:` would silently hide
#     inside a function like parts_sums.