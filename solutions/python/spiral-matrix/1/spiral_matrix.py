RIGHT = "RIGHT"
DOWN = "DOWN"
LEFT = "LEFT"
UP = "UP"


def spiral_matrix(size):
    if size == 0:
        return []

    matrix = list()

    for i in range(0, size):
        matrix.append([])
        for j in range(0, size):
            matrix[i].append(None)

    direction = RIGHT
    left_border = 0
    right_border = size - 1
    top_border = 0
    down_border = size - 1

    index = 1

    while left_border != right_border or top_border != down_border:
        if direction == RIGHT:
            for i in range(left_border, right_border + 1, 1):
                matrix[top_border][i] = index
                index += 1
            direction = DOWN
            top_border += 1
        elif direction == DOWN:
            for j in range(top_border, down_border + 1, 1):
                matrix[j][right_border] = index
                index += 1
            direction = LEFT
            right_border -= 1
        elif direction == LEFT:
            for i in range(right_border, left_border - 1, -1):
                matrix[down_border][i] = index
                index += 1
            direction = UP
            down_border -= 1
        elif direction == UP:
            for j in range(down_border, top_border - 1, -1):
                matrix[j][left_border] = index
                index += 1
            direction = RIGHT
            left_border += 1

    matrix[top_border][left_border] = index

    return matrix
