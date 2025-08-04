plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"


def encode(plain_text):
    result = []
    for symbol in plain_text:
        if symbol in plain:
            result.append(cipher[plain.index(symbol)])
            # print(symbol)
            # print(plain.index(symbol))

    return "".join(result)


def decode(ciphered_text):
    pass


print(encode("mindblo123wing ly"))
