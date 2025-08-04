def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    result = 0

    while number != 1:
        result += 1
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1

    return result
