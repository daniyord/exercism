list = ["black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"]


def color_code(color):
    result = 0
    for item in list:
        if item == color:
            return result
        result += 1

    return result


def colors():
    return list
