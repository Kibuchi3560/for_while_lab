# for-while-lab

A self-grading Python lab on `for` vs `while`, list mutation during
iteration, `append` vs `extend`, copy semantics, and `try`/`except`.

## Quick start

    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

    python run_lab.py                # run every part
    python run_lab.py a              # run one part

Tests are red on purpose. Fix the code in `exercises/`, not `tests/`.

## What each part teaches

| Part | Topic |
|------|-------|
| A | The hidden counter inside `for` — and when it desyncs |
| B | Four functions that run but return wrong answers |
| C | One problem, three implementations, none mutating the input |
| D | `append` vs `extend` |
| E | `a = b` vs `a = b[:]` vs shallow copy |
| F | Specific `except`, `else`, `finally` |
| G | Capstone: same shape, new problems |

## Definition of done

    pytest -v     # all green