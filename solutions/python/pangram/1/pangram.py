def is_pangram(sentence):
    used = set()

    for symbol in sentence:
        if symbol.isalpha():
            used.add(symbol.lower())

    return len(used) == 26
