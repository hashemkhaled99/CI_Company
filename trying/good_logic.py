"""A compliant Python module."""

TARGET_SUM = 14


def calculate_things(x: int, y: int) -> bool:
    """Calculate if the sum equals exactly fourteen.

    Args:
        x: The first integer.
        y: The second integer.

    Returns:
        True if the sum is the target, False otherwise.
    """
    return x + y == TARGET_SUM
