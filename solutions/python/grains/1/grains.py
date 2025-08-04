def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    total = 0

    for index in range(0, 64):
        total += 2 ** index
        print(total)

    return total
