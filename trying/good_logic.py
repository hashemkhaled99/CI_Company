"""Good logic module with some simple business rules."""

LARGE_THRESHOLD = 100
MEDIUM_THRESHOLD = 50
EXPECTED_SUM = 3

def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

def test_add_numbers() -> None:
    """Test adding numbers."""
    assert add_numbers(1, 2) == EXPECTED_SUM  # noqa: S101

def complex_business_logic(x: int) -> str:
    """Execute complex business logic based on a number."""
    if x > LARGE_THRESHOLD:
        return "Large"
    if x > MEDIUM_THRESHOLD:
        return "Medium"
    for i in range(x):
        print(f"Counting {i}")  # noqa: T201
    return "Small"