"""Business logic module."""

def calculate_status(score: int) -> str:
    """Evaluate system health."""
    if score > 50:
        return "Healthy"
    return "Warning"
