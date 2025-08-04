def value(colors):
    digit_10 = color_code(colors[0])
    digit_1 = color_code(colors[1])

    return digit_10 * 10 + digit_1


def color_code(color):
    list = ["black", "brown", "red", "orange", "yellow",
            "green", "blue", "violet", "grey", "white"]

    result = 0
    for item in list:
        if item == color:
            return result
        result += 1
    return result
