def annotate(minefield):
    if len(minefield) == 0:
        return []

    result = []

    row_count = len(minefield)
    col_count = len(minefield[0])

    for i, row in enumerate(minefield):
        if (len(minefield[i]) != col_count):
            raise ValueError("The board is invalid with current input.")

        new_row = ""

        for j, cell in enumerate(row):
            if cell not in " *":
                raise ValueError("The board is invalid with current input.")

            if cell == "*":
                new_row += "*"
                continue

            adj_bombs = 0

            if i-1 >= 0 and j-1 >= 0 and minefield[i-1][j-1] == "*":
                adj_bombs += 1

            if i-1 >= 0 and minefield[i-1][j] == "*":
                adj_bombs += 1

            if i-1 >= 0 and j+1 < col_count and minefield[i-1][j+1] == "*":
                adj_bombs += 1

            if j-1 >= 0 and minefield[i][j-1] == "*":
                adj_bombs += 1

            if j+1 < col_count and minefield[i][j+1] == "*":
                adj_bombs += 1

            if i+1 < row_count and j-1 >= 0 and minefield[i+1][j-1] == "*":
                adj_bombs += 1

            if i+1 < row_count and minefield[i+1][j] == "*":
                adj_bombs += 1

            if i+1 < row_count and j+1 < col_count and minefield[i+1][j+1] == "*":
                adj_bombs += 1

            if adj_bombs > 0:
                new_row += str(adj_bombs)
            else:
                new_row += " "

        result.append(new_row)

    return result
