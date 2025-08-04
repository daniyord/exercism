def is_armstrong_number(number):
    number_str = str(number)
    degree = len(number_str)

    total = 0
    for digit in number_str:
        total += int(digit) ** degree

    return total == number


print(is_armstrong_number(153))
