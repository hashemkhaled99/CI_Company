"""A simple calculator module with 100% coverage-friendly code."""

Number = int | float


def add(a: Number, b: Number) -> Number:
    """Add two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers."""
    return a * b


_DIVIDE_BY_ZERO_MSG = "Cannot divide by zero"


def divide(a: Number, b: Number) -> Number:
    """Divide a by b."""
    if b == 0:
        raise ValueError(_DIVIDE_BY_ZERO_MSG)
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """Raise base to the power of exponent."""
    return base**exponent


_FACTORIAL_NEGATIVE_MSG = "Factorial not defined for negative numbers"


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError(_FACTORIAL_NEGATIVE_MSG)
    if n in {0, 1}:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
