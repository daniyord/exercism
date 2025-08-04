def is_paired(input_string):
    opening_symbols = "[{("
    closing_symbols = "]})"

    dict = {
        "[": "]",
        "{": "}",
        "(": ")",
    }

    stack = []

    for symbol in input_string:
        if symbol in opening_symbols:
            stack.append(symbol)
        if symbol in closing_symbols:
            if len(stack) == 0:
                return False

            last = stack.pop()
            if dict[last] != symbol:
                return False

    return len(stack) == 0
