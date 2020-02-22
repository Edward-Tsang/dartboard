from Dartboard import Dartboard
from Player import Player
from typing import List


class DartsGame:
    def __init__(self):
        self.player_list:List[Player] = []
        self.board = Dartboard()

    def generate_players(self, player_num, player_names):
        for p in range(0, player_num - 1):
            self.player_list.append(Player(player_names[p]))

    def calc_player_score(self):
        winner = 0
        while winner == 0:
            for p in self.player_list:
                p.deduct_score(self.board.calc_score())
                if p.get_score() <= 0:
                    print(p.get_name() + " has won the game")
                    break


