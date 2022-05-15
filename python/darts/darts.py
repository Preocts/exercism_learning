"Calculate dart score."
from math import sqrt


def score(x: float, y: float) -> int:
    """Calulate score of throw based on dart location."""
    # If the dart lands outside the target, player earns no points (0 points).
    # If the dart lands in the outer circle of the target, player earns 1 point.
    # If the dart lands in the middle circle of the target, player earns 5 points.
    # If the dart lands in the inner circle of the target, player earns 10 points.
    # Outter circle radius = 10
    # Middle circle radius = 5
    # Inner circle radius = 1
    dist = sqrt(x**2 + y**2)

    if 0 <= dist <= 1:
        return 10
    elif 1 <= dist <= 5:
        return 5
    elif 5 <= dist <= 10:
        return 1

    return 0
