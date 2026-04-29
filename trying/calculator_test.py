"""Tests for calculator module — targets 100% coverage."""

import pytest

from calculator import (
    add,
    divide,
    factorial,
    multiply,
    power,
    subtract,
)


class TestCalculator:
    """Test suite for calculator operations."""

    def test_add(self) -> None:
        """Test add operation."""
        assert add(2, 3) == 5  # noqa: S101
        assert add(-1, 1) == 0  # noqa: S101
        assert add(0, 0) == 0  # noqa: S101

    def test_subtract(self) -> None:
        """Test subtract operation."""
        assert subtract(5, 3) == 2  # noqa: S101
        assert subtract(0, 5) == -5  # noqa: S101

    def test_multiply(self) -> None:
        """Test multiply operation."""
        assert multiply(4, 5) == 20  # noqa: S101
        assert multiply(-2, 3) == -6  # noqa: S101

    def test_divide(self) -> None:
        """Test divide operation."""
        assert divide(10, 2) == 5.0  # noqa: S101
        assert divide(7, 2) == 3.5  # noqa: S101

    def test_divide_by_zero(self) -> None:
        """Test divide by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_power(self) -> None:
        """Test power operation."""
        assert power(2, 3) == 8  # noqa: S101
        assert power(5, 0) == 1  # noqa: S101

    def test_factorial(self) -> None:
        """Test factorial operation."""
        assert factorial(0) == 1  # noqa: S101
        assert factorial(1) == 1  # noqa: S101
        assert factorial(5) == 120  # noqa: S101

    def test_factorial_negative(self) -> None:
        """Test factorial with negative input."""
        match_msg = "Factorial not defined for negative numbers"
        with pytest.raises(ValueError, match=match_msg):
            factorial(-1)


def test_benchmark_add(benchmark: object) -> None:
    """Benchmark add operation — should complete in < 1ms."""
    benchmark(add, 1000, 2000)
