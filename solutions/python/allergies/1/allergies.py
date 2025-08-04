ALLERGENS = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats"
}

class Allergies:

    

    def __init__(self, score):
        self.allergies = []

        while score > 256:
            score -= 256

        divider = 128
        while divider > 0:
            if score >= divider:
                if divider in ALLERGENS:
                    self.allergies.append(ALLERGENS[divider])
                score -= divider
            divider /= 2       

    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies


