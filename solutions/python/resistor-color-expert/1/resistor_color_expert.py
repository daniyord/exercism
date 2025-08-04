values = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]

tolerances = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}


def resistor_label(colors):
    print(colors)
    value_1 = values.index(colors[0])
    value_2 = values.index(colors[1])

    if len(colors) == 4:
        exponent = values.index(colors[2])
        tolerance = tolerances[colors[3]]

        value = (value_1 * 10 + value_2) * (10 ** exponent)

    if len(colors) == 5:
        value_3 = values.index(colors[2])
        exponent = values.index(colors[3])
        tolerance = tolerances[colors[4]]

        value = (value_1 * 100 + value_2 * 10 + value_3) * (10 ** exponent)

    measure = "ohms"

    if value > 1_000_000_000:
        measure = "gigaohms"
        value = value / 1_000_000_000

    if value > 1_000_000:
        measure = "megaohms"
        value = value / 1_000_000

    if value > 1_000:
        measure = "kiloohms"
        value = value / 1_000

    return f"{value:g} {measure} ±{tolerance}%"
