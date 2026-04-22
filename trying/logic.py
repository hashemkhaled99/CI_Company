"""Module for system logic validation."""

def validate_score(score: int) -> bool:
    """Check if a score is within acceptable bounds."""
    if 0 <= score <= 100:
        return True
    return False

