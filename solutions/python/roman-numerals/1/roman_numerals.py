input = [
    ("I", "V", "X"),
    ("X", "L", "C"),
    ("C", "D", "M"),
    ("M", "-", "-")
]


def roman(number):
    digits = []

    while number > 0:
        digits.append(number % 10)
        number = number // 10

    result = ""
    for index, digit in enumerate(digits):
        input_data = input[index]

        match digit:
            case 0:
                roman_digit = ""
            case 1:
                roman_digit = f"{input_data[0]}"
            case 2:
                roman_digit = f"{input_data[0]}{input_data[0]}"
            case 3:
                roman_digit = f"{input_data[0]}{input_data[0]}{input_data[0]}"
            case 4:
                roman_digit = f"{input_data[0]}{input_data[1]}"
            case 5:
                roman_digit = f"{input_data[1]}"
            case 6:
                roman_digit = f"{input_data[1]}{input_data[0]}"
            case 7:
                roman_digit = f"{input_data[1]}{input_data[0]}{input_data[0]}"
            case 8:
                roman_digit = f"{input_data[1]}{input_data[0]}{input_data[0]}{input_data[0]}"
            case 9:
                roman_digit = f"{input_data[0]}{input_data[2]}"

        result = roman_digit + result

    return result
