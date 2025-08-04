def saddle_points(matrix: list[list[int]]):
    row_len = len(matrix)
    if row_len == 0:
        return []

    col_len = len(matrix[0])
    if col_len == 0:
        raise ValueError("irregular matrix")

    result = []

    for row_index, row in enumerate(matrix):
        if len(row) != col_len:
            raise ValueError("irregular matrix")

        max_in_row = max(row)

        for column_index, cell in enumerate(row):
            if max_in_row != cell:
                continue

            is_valid = True
            for i in range(0, row_len):
                if matrix[i][column_index] < cell:
                    is_valid = False
                    break

            if is_valid:
                result.append({"row": row_index + 1, "column": column_index + 1})

    return result
