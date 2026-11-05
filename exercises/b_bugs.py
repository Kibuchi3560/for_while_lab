"""Part B — every function below RUNS but is WRONG.

Fix each one. Do not change the function name or signature.
Run:  python run_lab.py b
"""


def remove_evens(nums: list[int]) -> list[int]:
    """Return nums with all even numbers removed.
    remove_evens([2, 4, 6, 8]) -> []
    remove_evens([1, 2, 3, 4]) -> [1, 3]
    """
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)
    return nums


def countdown_sums(ls: list[int]) -> list[int]:
    """Sum of the whole list, then sum after dropping the front, ...
    countdown_sums([1, 2, 3]) -> [6, 5, 3, 0]
    countdown_sums([])        -> [0]
    """
    sums = []
    for x in ls:
        sums.append(sum(ls))
        ls.pop(0)
    return sums


def double_all(ls: list[int]) -> list[int]:
    """double_all([1, 2, 3]) -> [2, 4, 6]"""
    out = []
    for x in ls:
        out.extend(x * 2)
    return out


def get_len(obj) -> int:
    """Return len(obj) for any sized object, else 0.
    get_len([1, 2, 3]) -> 3
    get_len(42)        -> 0
    """
    try:
        return obj.size
    except Exception:
        return 0