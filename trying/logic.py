"""Business logic module."""

HEALTHY_THRESHOLD = 50


def calculate_status(score: int) -> str:
    """Evaluate system health."""
    if score > HEALTHY_THRESHOLD:
        return "Healthy"
    return "Warning"
