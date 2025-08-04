plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"


def encode(plain_text):
    result = []
    for symbol in plain_text.lower():
        if symbol.isdigit():
            result.append(symbol)
        if symbol in plain:
            result.append(cipher[plain.index(symbol)])

    result_str = "".join(result)

    result = []
    while result_str:
        result.append(result_str[0:5])
        result_str = result_str[5:]

    return " ".join(result)


def decode(ciphered_text):
    result = []

    for symbol in ciphered_text.lower():
        if symbol.isdigit():
            result.append(symbol)
        if symbol in cipher:
            result.append(plain[cipher.index(symbol)])

    return "".join(result)
