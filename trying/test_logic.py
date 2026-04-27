"""Tests for the logic module."""

from trying.good_logic import complex_business_logic
from trying.logic import validate_score


def test_validate_score_valid() -> None:
    """Test that valid scores return True."""
    assert validate_score(50) is True  # noqa: S101


def test_validate_score_invalid() -> None:
    """Test that out-of-bounds scores return False."""
    assert validate_score(150) is False  # noqa: S101


def test_complex_business_logic_large() -> None:
    """Test logic for Large."""
    assert complex_business_logic(150) == "Large"  # noqa: S101


def test_complex_business_logic_medium() -> None:
    """Test logic for Medium."""
    assert complex_business_logic(75) == "Medium"  # noqa: S101


def test_complex_business_logic_small() -> None:
    """Test logic for Small."""
    assert complex_business_logic(2) == "Small"  # noqa: S101

