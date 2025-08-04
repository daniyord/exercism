EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction
        pass

    def move(self, instructions):
        for instruction in instructions:
            match instruction:
                case "R":
                    self.turn_right()
                case "L":
                    self.turn_left()
                case "A":
                    self.advance()

    def turn_right(self):
        new_direction = None

        if self.direction == EAST:
            new_direction = SOUTH
        if self.direction == NORTH:
            new_direction = EAST
        if self.direction == WEST:
            new_direction = NORTH
        if self.direction == SOUTH:
            new_direction = WEST

        self.direction = new_direction

    def turn_left(self):
        new_direction = None

        if self.direction == EAST:
            new_direction = NORTH
        if self.direction == NORTH:
            new_direction = WEST
        if self.direction == WEST:
            new_direction = SOUTH
        if self.direction == SOUTH:
            new_direction = EAST

        self.direction = new_direction

    def advance(self):
        if self.direction == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
        if self.direction == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        if self.direction == WEST:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
        if self.direction == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
