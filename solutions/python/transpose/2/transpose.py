def transpose(text):
    max = 0
    lines = []
    matrix = []

    for index, line in enumerate(text.split("\n")):
        lines.append(line)

        if len(line) > max:
            max = len(line)

    for _ in range(0, max):
        matrix.append("")

    for line in lines:
        index = 0
        for symbol in line:
            matrix[index] += symbol
            index += 1

        for i in range(index, max):
            matrix[i] += "#"

    for index, row in enumerate(matrix):
        matrix[index] = row.rstrip("#")

    result = "\n".join(matrix).replace("#", " ")

    return result
