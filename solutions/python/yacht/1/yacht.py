# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score_yacht(dice: list[int]):
    if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
        return 50
    return 0


def score_full_house(dice: list[int]):
    die_counts = {}

    for die in dice:
        die_counts.setdefault(die, 0)
        die_counts[die] += 1

    values = sorted(die_counts.values())

    if len(values) == 2 and values[0] == 2 and values[1] == 3:
        return sum(dice)

    return 0


def score_four_of_a_kind(dice: list[int]):
    die_counts = {}

    for die in dice:
        die_counts.setdefault(die, 0)
        die_counts[die] += 1

    for die_count in die_counts:
        if die_counts[die_count] >= 4:
            return 4 * die_count

    return 0


def score_little_straight(dice: list[int]):
    for index, die in enumerate(sorted(dice)):
        if index + 1 != die:
            return 0

    return 30


def score_big_straight(dice: list[int]):
    for index, die in enumerate(sorted(dice)):
        if index + 2 != die:
            return 0

    return 30


def score_for_value(dice: list[int], value: int):
    result = 0
    for die in dice:
        if die == value:
            result += value
    return result


def score(dice: list[int], category):
    if category == YACHT:
        return score_yacht(dice)
    if category == FULL_HOUSE:
        return score_full_house(dice)
    if category == FOUR_OF_A_KIND:
        return score_four_of_a_kind(dice)
    if category == LITTLE_STRAIGHT:
        return score_little_straight(dice)
    if category == BIG_STRAIGHT:
        return score_big_straight(dice)
    if category == CHOICE:
        return sum(dice)
    if category == ONES:
        return score_for_value(dice, 1)
    if category == TWOS:
        return score_for_value(dice, 2)
    if category == THREES:
        return score_for_value(dice, 3)
    if category == FOURS:
        return score_for_value(dice, 4)
    if category == FIVES:
        return score_for_value(dice, 5)
    if category == SIXES:
        return score_for_value(dice, 6)
