"""Unit tests for the good_logic module."""

from trying.good_logic import calculate_things


def test_calculate_things_success() -> None:
    """Verify that calculate_things returns True for the target sum."""
    assert calculate_things(7, 7) is True  # noqa: S101


def test_calculate_things_failure() -> None:
    """Verify that calculate_things returns False for incorrect sums."""
    assert calculate_things(1, 1) is False  # noqa: S101
