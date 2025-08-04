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

        for allergen in ALLERGENS:
            if allergen & score > 0:
                self.allergies.append(ALLERGENS[allergen])     

    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies
