class Player:

    def __init__(self, name):
        self.__name = name
        self.__score = 501

    def get_score(self):
        return self.__score

    def deduct_score(self, score):
        self.__score -= score

    def get_name(self):
        return self.__name
