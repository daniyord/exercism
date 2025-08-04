def digit_to_text(digit):
    match digit:
        case 0:
            return ""
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"


def digit_to_text1(digit):
    match digit:
        case 0:
            return "ten"
        case 1:
            return "elevem"
        case 2:
            return "twelve"
        case 3:
            return "thirteen"
        case 4:
            return "fourteen"
        case 5:
            return "fiveteen"
        case 6:
            return "sixteen"
        case 7:
            return "seventeen"
        case 8:
            return "eightteen"
        case 9:
            return "nineteen"


def decimal_to_text(digit):
    match digit:
        case 2:
            return "twenty"
        case 3:
            return "thirty"
        case 4:
            return "forty"
        case 5:
            return "fifty"
        case 6:
            return "sixty"
        case 7:
            return "seventy"
        case 8:
            return "eighty"
        case 9:
            return "ninety"


def part_to_text(part_index):
    match part_index:
        case 0:
            return ""
        case 1:
            return " thousand"
        case 2:
            return " million"
        case 3:
            return " billion"


def process_part(part):
    print("process_part:", part)

    result = ""

    if len(part) > 2 and part[2] > 0:
        result += f"{digit_to_text(part[2])} hundred "

    if len(part) > 1 and part[1] > 1 and part[0] > 0:
        result += f"{decimal_to_text(part[1])}-"
    if len(part) > 1 and part[1] > 1 and part[0] == 0:
        result += f"{decimal_to_text(part[1])}"

    if len(part) > 1 and part[1] == 1:
        result += f"{digit_to_text1(part[0])}"
    if part[0] > 0:
        result += f"{digit_to_text(part[0])}"

    print(result)

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


print(say(14))
