"""Tests for business logic."""

from trying.logic import calculate_status


def test_calculate_status_healthy() -> None:
    """Test healthy score."""
    assert calculate_status(100) == "Healthy"


def test_calculate_status_warning() -> None:
    """Test warning score."""
    assert calculate_status(10) == "Warning"
