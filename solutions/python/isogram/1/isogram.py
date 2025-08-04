def is_isogram(string):
    used = set()

    for symbol in string:
        symbol = symbol.lower()

        if symbol.isalpha() and symbol in used:
            return False
        else:
            used.add(symbol)

    return True
