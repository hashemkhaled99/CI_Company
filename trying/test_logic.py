"""Tests for the logic module."""

from trying.logic import validate_score


def test_validate_score_valid() -> None:
    """Test that valid scores return True."""
    assert validate_score(50) is True  # noqa: S101


def test_validate_score_invalid() -> None:
    """Test that out-of-bounds scores return False."""
    assert validate_score(150) is False  # noqa: S101
