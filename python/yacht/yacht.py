"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from __future__ import annotations

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice: list[int], category: int) -> int:
    # Get the sort over with here, it's used enough.
    dice.sort()

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    elif category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return dice.count(category) * category

    elif category == FULL_HOUSE:
        leading = 2 <= dice.count(dice[0]) <= 3
        trailing = 2 <= dice.count(dice[-1]) <= 3
        return sum(dice) if all([leading, trailing]) else 0

    elif category == FOUR_OF_A_KIND:
        if dice.count(dice[0]) >= 4:
            return dice[0] * 4
        elif dice.count(dice[-1]) >= 4:
            return dice[-1] * 4
        return 0

    elif category == LITTLE_STRAIGHT:
        return 30 if dice == [1, 2, 3, 4, 5] else 0

    elif category == BIG_STRAIGHT:
        return 30 if dice == [2, 3, 4, 5, 6] else 0

    elif category == CHOICE:
        return sum(dice)

    return 0
