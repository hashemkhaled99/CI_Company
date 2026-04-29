"""Tests for calculator module — targets 100% coverage."""

import pytest
from calculator import add, subtract, multiply, divide, power, factorial


class TestCalculator:
    """Test suite for calculator operations."""

    def test_add(self) -> None:
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_subtract(self) -> None:
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5

    def test_multiply(self) -> None:
        assert multiply(4, 5) == 20
        assert multiply(-2, 3) == -6

    def test_divide(self) -> None:
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_power(self) -> None:
        assert power(2, 3) == 8
        assert power(5, 0) == 1

    def test_factorial(self) -> None:
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120

    def test_factorial_negative(self) -> None:
        with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
            factorial(-1)


def test_benchmark_add(benchmark) -> None:
    """Benchmark add operation — should complete in < 1ms."""
    benchmark(add, 1000, 2000)
