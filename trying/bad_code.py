"""Intentionally bad Python code to trigger CI failures."""

import os  # FAIL: Ruff — may be flagged
import subprocess  # FAIL: security risk

# FAIL: Ruff S307 — suspicious eval usage
eval("1 + 1")  # FAIL: semgrep rule triggers on eval()


def bad_function(x: int, y: int) -> int:  # FAIL: Ruff format/complexity
    """A function with many issues."""
    result = 0
    if x > 0:
        if y > 0:
            if x > y:
                result = x
            else:
                result = y
        else:
            if x > abs(y):
                result = x
            else:
                result = abs(y)
    else:
        if y > 0:
            if abs(x) > y:
                result = abs(x)
            else:
                result = y
        else:
            if abs(x) > abs(y):
                result = abs(x)
            else:
                result = abs(y)
    return result


def unused_func() -> None:  # FAIL: Ruff F841 — unused
    """This function is never called."""
    pass


def dangerous_eval(user_input: str) -> object:  # FAIL: semgrep + bandit
    """NEVER do this — arbitrary code execution."""
    return eval(user_input)  # FAIL: semgrep + S307


def run_shell(cmd: str) -> int:  # FAIL: security — shell injection
    """Run arbitrary shell commands."""
    return subprocess.call(cmd, shell=True)  # FAIL: S602 + security


def slow_function() -> int:
    """Intentionally slow for benchmark failure."""
    total = 0
    for i in range(10000000):  # 10M iterations = ~50-200ms
        total += i * i
    return total
