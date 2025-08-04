def decode(string):
    result = []

    count_digits = []

    for symbol in string:
        if symbol.isdigit():
            count_digits.append(symbol)
        else:
            for _ in range(int("".join(count_digits) if len(count_digits) > 0 else 1)):
                result.append(symbol)
            count_digits = []

    return "".join(result)


def encode(string):
    if len(string) == 0:
        return ""

    current_symbol = string[0]
    current_count = 0

    result = ""

    for symbol in string:
        if current_symbol == symbol:
            current_count += 1
        else:
            result += f"{current_count}{current_symbol}" if current_count > 1 else current_symbol
            current_count = 1
            current_symbol = symbol

    result += f"{current_count}{current_symbol}" if current_count > 1 else current_symbol

    return result
