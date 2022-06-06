import random
from Connect4Game.src.game import Game

# runtime command line arguments:
# python3 main.py config_files/connect4.txt 25

def main(game_config: str = 'config_files/connect4.txt') -> None:
    """
    Run the program
    :return:
    """
    random.seed(random.randint(0, 1000)) # set random seed
    Connect4 = Game.create_game_from_file(game_config) # board config for connect 4
    Connect4.play() # initiate the game

if __name__ == '__main__':
    main()