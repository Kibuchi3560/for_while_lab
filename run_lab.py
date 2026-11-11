"""Run the lab one part at a time.

Usage:
    python run_lab.py          # all parts
    python run_lab.py a        # only part A
"""
import subprocess
import sys

PARTS = {
    "a": "tests/test_a_hidden_counter.py",
    "b": "tests/test_b_bugs.py",
    "c": "tests/test_c_three_ways.py",
    "d": "tests/test_d_append_extend.py",
    "e": "tests/test_e_copies.py",
    "f": "tests/test_f_exceptions.py",
    "g": "tests/test_g_capstone.py",
    "h": "tests/test_h_hard.py", 
}


def main() -> int:
    arg = (sys.argv[1] if len(sys.argv) > 1 else "all").lower()
    if arg == "all":
        targets = list(PARTS.values())
    elif arg in PARTS:
        targets = [PARTS[arg]]
    else:
        print(f"Unknown part {arg!r}. Choose from: all, {', '.join(PARTS)}")
        return 2
    return subprocess.call([sys.executable, "-m", "pytest", "-v", *targets])


if __name__ == "__main__":
    raise SystemExit(main())