"""Good logic module with some simple business rules."""

def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

def test_add_numbers() -> None:
    """Test adding numbers."""
    assert add_numbers(1, 2) == 3  # noqa: S101

def complex_business_logic(x: int) -> str:
    """Execute complex business logic based on a number."""
    if x > 100:
        return "Large"
    if x > 50:
        return "Medium"
    for i in range(x):
        print(f"Counting {i}")  # noqa: T201
    return "Small"