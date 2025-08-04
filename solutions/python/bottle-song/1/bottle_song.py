input = {
    10: ("Ten", "bottles", "nine", "bottles"),
    9: ("Nine", "bottles", "eight", "bottles"),
    8: ("Eight", "bottles", "seven", "bottles"),
    7: ("Seven", "bottles", "six", "bottles"),
    6: ("Six", "bottles", "five", "bottles"),
    5: ("Five", "bottles", "four", "bottles"),
    4: ("Four", "bottles", "three", "bottles"),
    3: ("Three", "bottles", "two", "bottles"),
    2: ("Two", "bottles", "one", "bottle"),
    1: ("One", "bottle", "no", "bottles")
}


def recite(start, take=1):
    result = []

    num = start
    while take > 0:
        result += recite_verse(num)
        num -= 1
        take -= 1

        if take > 0:
            result.append("")

    return result


def recite_verse(num):
    return [
        f"{input[num][0]} green {input[num][1]} hanging on the wall,",
        f"{input[num][0]} green {input[num][1]} hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        f"There'll be {input[num][2]} green {input[num][3]} hanging on the wall."]
