from DartsGame import DartsGame
def main():
    player_names = []
    player_num = int(input("Please enter the number of players: "))
    for p in range(0, player_num - 1):
        name = input("Please enter the name of the player: ")
        player_names.append(name)

