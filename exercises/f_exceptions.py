"""Part F — try / except.

═══════════════════════════════════════════════════════════════════════
  HOW TO WORK THIS FILE
  1. F1: predict exception names on paper, THEN run.
  2. F2: fix get_len — one specific `except`, not bare.
  3. F3: implement f() to a written spec.
  4. F4: write one sentence about why bare except is dangerous.
  Run:  python3 -m pytest -v tests/test_f_exceptions.py
═══════════════════════════════════════════════════════════════════════

KEY RULE:
    except:                  ← catches EVERYTHING (including typos)
    except Exception:        ← also too broad
    except ValueError:       ← correct: one specific exception
    except (ValueError, KeyError):  ← correct: multiple specific ones
"""

# ════════════════════════════════════════════════════════════════════════
# F1 — name the exception
# ════════════════════════════════════════════════════════════════════════
# For each expression below, predict which exception class gets raised.
# Fill in the PREDICTION_F1 dict with the EXCEPTION CLASS NAME, as a
# string (e.g. "ValueError", "IndexError", ...). Do NOT run first.
#
#   int("abc")              →  ?
#   [1, 2][5]               →  ?
#   {"a": 1}["b"]           →  ?
#   10 / 0                  →  ?
#   "a" + 1                 →  ?
#
PREDICTION_F1: dict[str, str] = {
    "int_abc": "ValueError",
    "index": "IndexError",
    "key": "KeyError",
    "zero": "ZeroDivisionError",
    "add": "TypeError",
}


def f1_run() -> dict[str, str]:
    """GIVEN. Do not modify. Returns the actual exception names."""
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


# ════════════════════════════════════════════════════════════════════════
# F2 — fix get_len
# ════════════════════════════════════════════════════════════════════════
# The B-part get_len is back, and this time the tests are stricter:
# it must catch ONLY the exception len() raises for an unsized object.
#
def get_len(obj) -> int:
    """Return len(obj) for anything sized, else 0.

    WHAT TO DO:
        Fix it. Use len(), not .size (that's not a Python list attr).
        Wrap the len() call in try/except, catching exactly ONE
        exception type.

    EXAMPLES:
        get_len([1, 2, 3])  →  3
        get_len("abc")      →  3
        get_len([])         →  0
        get_len(42)         →  0
        get_len(None)       →  0

    CONSTRAINTS:
        • Do NOT use bare `except:`.
        • Do NOT use `except Exception`.
        • Name the specific exception type that len() raises when
          called on a non-sized object.

    HINT: what exception does len(42) raise? Try it in a REPL:
          >>> len(42)

    RUN THIS:  python3 -m pytest -v tests/test_f_exceptions.py -k get_len
    """
    try:
        return len(obj)
    except TypeError:
        return 0
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════
# F3 — implement f() to a written spec
# ════════════════════════════════════════════════════════════════════════
def f(x):
    """Return 10 / x, with careful try/except/else/finally behavior.

    WHAT TO DO:
        Implement this function so that:

        • On ZeroDivisionError:
            print "caught"
            return -1

        • Otherwise (no exception):
            print "no error"
            return the division result (10 / x)

        • In ALL cases (success OR failure):
            print "cleanup" as the LAST thing that happens

    MUST USE:
        try, except, else, finally — no bare except.

    WHY `else` AND `finally`:
        `else` runs only if the try block succeeded — it's where you
        put code that should NOT trigger the except path.
        `finally` runs whether or not anything failed — good for
        cleanup, closing files, releasing locks. It runs even after
        a `return`.

    EXAMPLES (expected stdout, then return value):
        f(2)  → prints "no error" then "cleanup", returns 5.0
        f(0)  → prints "caught"   then "cleanup", returns -1

    WHAT THE TESTS CHECK:
        Exact printed output. Exact return value. Order matters.
        "caught\ncleanup\n" and "no error\ncleanup\n" — nothing more,
        nothing less, nothing reordered.

    RUN THIS:  python3 -m pytest -v tests/test_f_exceptions.py -k "f3 or f_success or f_zero"
    """
    try:
        result = 10 / x
    except ZeroDivisionError:       
        print("caught")
        return -1
    else:
        print("no error")
        return result
    finally:
        print("cleanup")      
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════
# F4 — why bare except is dangerous (written answer)
# ════════════════════════════════════════════════════════════════════════
# WHAT TO DO:
#   In one or two sentences, name a CONCRETE bug that a bare
#   `except:` would silently hide inside a function like parts_sums.
#
#   Not graded by pytest — write it for your own learning. Something
#   like "a typo in a variable name raises NameError, which a bare
#   except would swallow and turn into a silent wrong return."
#
F4_WHY_BARE_EXCEPT_IS_BAD = " A bare except can catch unexpected exceptions, such as typos or logic errors, which can lead to silent failures and make debugging difficult."


# ════════════════════════════════════════════════════════════════════════
# SELF-CHECK before running pytest
# ════════════════════════════════════════════════════════════════════════
# [ ] I filled PREDICTION_F1 WITHOUT running f1_run first.
# [ ] get_len catches exactly one specific exception.
# [ ] f() uses try/except/else/finally — no bare except.
# [ ] My f() returns float on success (10 / 2 → 5.0, not 5).
# [ ] "cleanup" prints LAST in BOTH cases (success and failure).
# [ ] I wrote F4_WHY_BARE_EXCEPT_IS_BAD as a real sentence.
# [ ] I have NOT run pytest yet. Do that now.
# ════════════════════════════════════════════════════════════════════════