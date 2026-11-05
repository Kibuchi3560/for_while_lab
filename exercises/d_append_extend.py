"""Part D — append vs extend.

Predict every PREDICTION_* before running. The *_run() helpers are
GIVEN — do not modify them.
Run:  python run_lab.py d
"""

# ---- D1 ------------------------------------------------------------
PREDICTION_D1: list = []


def d1_run():
    a = [1]
    a.append([2, 3])
    return a


# ---- D2 ------------------------------------------------------------
PREDICTION_D2: list = []


def d2_run():
    b = [1]
    b.extend([2, 3])
    return b


# ---- D3 ------------------------------------------------------------
PREDICTION_D3 = ""     # <-- "ok" or "error"


def d3_run():
    c = []
    try:
        c.extend(5)
        return "ok"
    except TypeError:
        return "error"


# ---- D4 ------------------------------------------------------------
PREDICTION_D4: list = []


def d4_run():
    d = []
    d.append(5)
    d.extend("ab")
    return d


# ---- D5 — fix B3 two different ways --------------------------------
def fix_double_all_append(ls: list[int]) -> list[int]:
    """double_all([1, 2, 3]) -> [2, 4, 6] using .append()"""
    # TODO
    raise NotImplementedError


def fix_double_all_extend(ls: list[int]) -> list[int]:
    """double_all([1, 2, 3]) -> [2, 4, 6] using .extend()"""
    # TODO
    raise NotImplementedError