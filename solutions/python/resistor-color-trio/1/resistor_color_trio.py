values = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]


def label(colors):
    digit_10 = values.index(colors[0])
    digit_1 = values.index(colors[1])

    exponent = values.index(colors[2])

    value = (digit_10 * 10 + digit_1) * (10 ** exponent)

    measure = "ohms"

    if value > 1_000_000_000:
        measure = "gigaohms"
        value = value // 1_000_000_000

    if value > 1_000_000:
        measure = "megaohms"
        value = value // 1_000_000

    if value > 1_000:
        measure = "kiloohms"
        value = value // 1_000

    return f"{value} {measure}"
