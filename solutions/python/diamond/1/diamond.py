def rows(letter):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result_start = []
    result_end = []

    for curr_letter in letters:
        if curr_letter == "A":
            pattern = "A"
        else:
            pattern = f"{curr_letter}{pattern}{curr_letter}"

        if letter == curr_letter:
            print(pattern)
            break

    for curr_letter in letters:
        mod_pattern = ""

        for part in pattern:
            if part == curr_letter:
                mod_pattern += part
            else:
                mod_pattern += " "

        result_start.append(mod_pattern)

        if letter == curr_letter:
            break

        result_end.insert(0, mod_pattern)

    return result_start + result_end
