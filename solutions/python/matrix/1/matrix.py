class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []

        for row in matrix_string.split("\n"):
            self.matrix.append([])

            for cell in row.split(" "):
                self.matrix[-1].append(int(cell))

        print(self.matrix)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        result = []

        for row in self.matrix:
            result.append(row[index - 1])

        return result
