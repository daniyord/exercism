def convert_letter(cell):
    digits = {
        "1": ['   ', '  |', '  |', '   '],
        "2": [' _ ', ' _|', '|_ ', '   '],
        "3": [' _ ', ' _|', ' _|', '   '],
        "4": ['   ', '|_|', '  |', '   '],
        "5": [' _ ', '|_ ', ' _|', '   '],
        "6": [' _ ', '|_ ', '|_|', '   '],
        "7": [' _ ', '  |', '  |', '   '],
        "8": [' _ ', '|_|', '|_|', '   '],
        "9": [' _ ', '|_|', ' _|', '   '],
        "0": [" _ ", "| |", "|_|", "   "]
    }

    for digit in digits:
        digit_list = digits[digit]

        if digit_list[0] == cell[0] and digit_list[1] == cell[1] and digit_list[2] == cell[2] and digit_list[3] == cell[3]:
            return digit

    return "?"


def convert(input_grid):
    rows = []

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    for index, row in enumerate(input_grid):
        if len(row) % 3 != 0:
            raise ValueError(
                "Number of input columns is not a multiple of three")

        if index % 4 == 0:
            new_row = []
            rows.append(new_row)

        for i in range(0, len(row), 3):
            if index % 4 == 0:
                new_row.append([])
            new_row[i // 3].append(row[i:i + 3])

    result = []
    for row in rows:
        result_row = []
        result.append(result_row)

        for cell in row:
            result_row.append(convert_letter(cell))

    for i in range(0, len(result)):
        result[i] = "".join(result[i])

    return ",".join(result)
