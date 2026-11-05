"""Part E — copy semantics.

Predict before running. The *_run() helpers are GIVEN.
Run:  python run_lab.py e
"""

# ---- E1 ------------------------------------------------------------
PREDICTION_E1_A: list = []
PREDICTION_E1_C: list = []
PREDICTION_E1_D: list = []
PREDICTION_E1_A_IS_B = None    # <-- True / False
PREDICTION_E1_A_IS_C = None
PREDICTION_E1_C_EQ_A = None


def e1_run() -> dict:
    a = [1, 2, 3]
    b = a
    c = a[:]
    d = list(a)
    b.append(99)
    return {
        "a": a,
        "c": c,
        "d": d,
        "a_is_b": a is b,
        "a_is_c": a is c,
        "c_eq_a": c == a,
    }


# ---- E2 ------------------------------------------------------------
PREDICTION_E2: list = []    # <-- outer after copy[0].append(99)


def e2_run() -> list:
    inner = [1, 2]
    outer = [inner, inner]
    copy = outer[:]
    copy[0].append(99)
    return outer


# ---- E3 ------------------------------------------------------------
def parts_sums_safe(ls: list[int]) -> list[int]:
    """while True + pop(0) version that must NOT mutate the caller's list.

    parts_sums_safe([1, 2, 3]) -> [6, 5, 3, 0]

    After the call, the caller's list must be unchanged.
    """
    # TODO
    raise NotImplementedError