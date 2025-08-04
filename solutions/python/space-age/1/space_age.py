info = {
    "Mercury": 0.2408467,
    "Venus": 0.61519726,
    "Earth": 1.0,
    "Mars": 1.8808158,
    "Jupiter": 11.862615,
    "Saturn": 29.447498,
    "Uranus": 84.016846,
    "Neptune": 164.79132,
}


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return self.__calculate__("Earth")

    def on_mercury(self):
        return self.__calculate__("Mercury")

    def on_venus(self):
        return self.__calculate__("Venus")

    def on_mars(self):
        return self.__calculate__("Mars")

    def on_jupiter(self):
        return self.__calculate__("Jupiter")

    def on_saturn(self):
        return self.__calculate__("Saturn")

    def on_uranus(self):
        return self.__calculate__("Uranus")

    def on_neptune(self):
        return self.__calculate__("Neptune")

    def __calculate__(self, planet):
        return round((self.seconds / 31_557_600 / info[planet]), 2)
