import unittest
from DartsGame import DartsGame
from Player import Player





class TestDartsGame(unittest.TestCase):
    def test_generate_players(self):
        game = DartsGame()
        game.generate_players(3, ["Edward","Rebecca","Raymond"])
        self.assertEqual(game.player_list[0].get_name(), "Rebecca")



if __name__ == "__main__":
    unittest.main()
