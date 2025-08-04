ratios = {
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "earth": 1.0,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
}


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def __getattr__(self, name):
        print(name)
        return lambda: round((self.seconds / 31_557_600 / ratios[name[3:]]), 2)
