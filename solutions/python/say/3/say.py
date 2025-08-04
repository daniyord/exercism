def digit_to_text(digit):
    digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return digits[digit]


def digit_to_10_19(digit):
    numbers = ["ten", "elevem", "twelve", "thirteen", "fourteen",
               "fiveteen", "sixteen", "seventeen", "eightteen", "nineteen"]
    return numbers[digit]


def digit_to_nty(digit):
    nty = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    return nty[digit]


def part_to_text(part_index):
    parts = ["", " thousand", " million", " billion"]
    return parts[part_index]


def process_part(part):
    result = ""

    if len(part) > 2 and part[2] > 0:
        result += f"{digit_to_text(part[2])} hundred "

    if len(part) > 1 and part[1] > 1 and part[0] > 0:
        result += f"{digit_to_nty(part[1])}-"
    if len(part) > 1 and part[1] > 1 and part[0] == 0:
        result += f"{digit_to_nty(part[1])}"

    if len(part) > 1 and part[1] == 1:
        result += f"{digit_to_10_19(part[0])}"
    elif part[0] > 0:
        result += f"{digit_to_text(part[0])}"

    return result


def say(number):
    if number == 0:
        return "zero"

    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    parts = []
    current = []

    while number > 0:
        current.append(number % 10)
        number = number // 10

        if len(current) == 3:
            parts.append(current)
            current = []

    if len(current) < 3 and len(current) > 0:
        parts.append(current)

    result = ""
    for part_index, part in enumerate(parts):
        if any([p > 0 for p in part]):
            result = process_part(part) + part_to_text(part_index) + " " + result

    return result.strip()
