input = [
    (1, "first", "a Partridge in a Pear Tree"),
    (2, "second", "two Turtle Doves"),
    (3, "third", "three French Hens"),
    (4, "fourth", "four Calling Birds"),
    (5, "fifth", "five Gold Rings"),
    (6, "sixth", "six Geese-a-Laying"),
    (7, "seventh", "seven Swans-a-Swimming"),
    (8, "eighth", "eight Maids-a-Milking"),
    (9, "ninth", "nine Ladies Dancing"),
    (10, "tenth", "ten Lords-a-Leaping"),
    (11, "eleventh", "eleven Pipers Piping"),
    (12, "twelfth", "twelve Drummers Drumming")
]


def recite(start_verse, end_verse):
    result = []

    for index in range(start_verse - 1, end_verse):
        current = input[index]

        gifts = []

        for i in range(current[0], 0, -1):
            gifts.append(input[i - 1][2])

        gifts_str = ", ".join(gifts[:-1])

        if len(gifts) == 1:
            gifts_str = gifts[0]
        else:
            gifts_str += f", and {gifts[-1]}"

        result.append(f"On the {current[1]} day of Christmas my true love gave to me: {gifts_str}.")

    return result
