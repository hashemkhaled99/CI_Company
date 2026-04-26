"""A compliant Python module."""

TARGET_SUM = 14


def calculate_things(x: int, y: int) -> bool:
    """Calculate if the sum equals the target.

    Args:
        x: First integer.
        y: Second integer.

    Returns:
        True if matches target.
    """
    return x + y == TARGET_SUM
