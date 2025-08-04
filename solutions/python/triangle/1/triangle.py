def equilateral(sides):
    return is_triangle(sides) and (sides[0] == sides[1] == sides[2])


def isosceles(sides):
    return is_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])


def scalene(sides):
    return is_triangle(sides) and (sides[0] != sides[1] != sides[2] != sides[0])


def is_triangle(sides):
    if 0 in sides:
        return False

    if sides[0] > sides[1] + sides[2]:
        return False

    if sides[1] > sides[0] + sides[2]:
        return False

    if sides[2] > sides[0] + sides[1]:
        return False

    return True
