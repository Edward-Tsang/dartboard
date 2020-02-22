import random


class Dartboard:
    def __init__(self):
        self.__values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 50]
        self.__multipliers = [1, 2, 3]

    def calc_score(self) -> int:
        rand_int = random.randrange(0, len(self.__values) - 1)
        rand_multiplier = random.randrange(0, len(self.__multipliers) - 1)
        return self.__values[rand_int] * self.__multipliers[rand_multiplier]
