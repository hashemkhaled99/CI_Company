"""Minimal tests for bad_code.py — coverage will still fail (< 40%)."""

try:
    from bad_code import bad_function, slow_function
except ImportError:
    from trying.bad_code import bad_function, slow_function


def test_bad_function() -> None:
    """Test bad_function."""
    assert bad_function(3, 2) == 3  # noqa: S101


def test_slow_benchmark(benchmark: object) -> None:
    """FAIL: This benchmark will exceed 1000ms threshold."""
    benchmark(slow_function)
    