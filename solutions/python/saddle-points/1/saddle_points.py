def saddle_points(matrix: list[list[int]]):
    result = []

    for row_index, row in enumerate(matrix):
        max_in_row = max(row)

        for column_index, cell in enumerate(row):
            if max_in_row != cell:
                continue

            for i in range(0, len(matrix)):
                if matrix[i][column_index] < cell:
                    continue

            result.append


saddle_points([[8, 7, 9], [6, 7, 6], [3, 2, 5]])
