import random
options = [1, 2, 3, 4, 5, 6]


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dice = [
            random.choice(options),
            random.choice(options),
            random.choice(options),
            random.choice(options)]

        selected_dice = sorted(dice)[1:]

        return sum(selected_dice)


def modifier(value):
    return (value - 10) // 2
