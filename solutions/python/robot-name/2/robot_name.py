import string
import random


class Robot:
    def __init__(self):
        self.name = self.calculate_name()

    def reset(self):
        self.name = self.calculate_name()

    def calculate_name(self):
        random.seed()

        result = ""

        result += random.choice(string.ascii_uppercase)
        result += random.choice(string.ascii_uppercase)
        result += random.choice(string.digits)
        result += random.choice(string.digits)
        result += random.choice(string.digits)

        return result
