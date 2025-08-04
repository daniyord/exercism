def is_armstrong_number(number):
    digits = []
    number_mod = number

    while number_mod > 0:
        digits.append(number_mod % 10)
        number_mod = number_mod // 10

    degree = len(digits)

    total = 0
    for digit in digits:
        total += digit ** degree

    print(total)

    return total == number
