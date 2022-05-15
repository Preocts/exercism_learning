"""Grains problem."""


def square(number: int) -> int:
    """Calculate number of grains on a given square."""
    if 0 >= number or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Calculate total number of grains on chessboard."""
    return sum((square(num) for num in range(1, 65)))
