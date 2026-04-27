"""Module for system logic validation."""

# Named constants to avoid PLR2004 (Magic Value) errors
MIN_SCORE = 0
MAX_SCORE = 100


def validate_score(score: int) -> bool:
    """Check if a score is within acceptable bounds.

    Returns the condition directly to satisfy SIM103.
    """
    return MIN_SCORE <= score <= MAX_SCORE
