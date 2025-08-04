def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    numbers = []

    for symbol in isbn[:-1]:
        if symbol.isdigit():
            numbers.append(int(symbol))
        else:
            return False

    if isbn[-1].isdigit():
        numbers.append(int(isbn[-1]))
    elif isbn[-1] == "X":
        numbers.append(10)
    else:
        return False

    sum = 0
    multy = 10

    for number in numbers:
        sum += number * multy
        multy -= 1

    return sum % 11 == 0
