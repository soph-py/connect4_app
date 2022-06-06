from typing import List, Optional
from .board import Board
from Connect4Game.src.players import human_player, player, random_ai, simple_ai


class Game(object):

    @staticmethod
    def create_game_from_file(path_to_file: str) -> "Game":
        """
        create a game from the specified configuration file
        :param path_to_file: the follow holding the configuration
        :return: a game setup up based on the configuration file
        """
        with open(path_to_file) as config_file:
            config = {}
            for line in config_file:
                line = line.strip()
                if line:
                    var, value = line.split(':')
                    var = var.strip()
                    value = value.strip()
                    try:
                        value = int(value)  # type: ignore[assignment]
                    except ValueError:
                        pass
                    config[var] = value
            board = Board(config['num_rows'], config['num_cols'], config['blank_char'])
            return Game(board, config['num_pieces_to_win'])  # type: ignore[arg-type]

    def __init__(self, board: Board, num_pieces_to_win: int,
                 players: Optional[List["player.Player"]] = None) -> None:
        self.cur_player_turn = 0
        self.board = board
        self.num_pieces_to_win = num_pieces_to_win
        self.someone_won: bool = False
        if players is not None:
            self.players: List[player.Player] = players
        else:
            self.players = []
            self.setup_players()

    @property
    def cur_player(self) -> "player.Player":
        """
        :return: the player whoose turn it is
        """
        return self.players[self.cur_player_turn]

    @property
    def num_players(self) -> int:
        """
        :return: The number of players in the game
        """
        return len(self.players)

    @property
    def is_tie_game(self) -> bool:
        """
        Check if the game ended ina tie.
        Can only be safely called after checking if someone won the game
        :return: if the game ended in a tie
        """
        return self.board.is_full

    @staticmethod
    def get_valid_player_type_from_user(player_num: int) -> str:
        legal_player_types = ('human', 'random', 'simple')
        while True:
            print(f'Choose the type for Player {player_num + 1}')
            player_type_input = input('Enter Human or Random or Simple: ')
            player_type = player_type_input.strip().lower()
            for legal_player_type in legal_player_types:
                if legal_player_type.startswith(player_type) and player_type != '':
                    return legal_player_type
            else:
                print(f'{player_type} is not one of Human or Random or Simple. Please try again.')
                

    def setup_players(self) -> None:
        """
        Create the players for this game
        :return: None
        """
        num_players = 2
        for i in range(num_players):
            player_type = self.get_valid_player_type_from_user(player_num=i)
            if player_type == 'human':
                new_player = human_player.HumanPlayer.create_for_game(self.players, self.board.blank_char)
            elif player_type == 'random':
                new_player = random_ai.RandomAi.create_for_game(self.players, self.board.blank_char)
            else:
                new_player = simple_ai.SimpleAi.create_for_game(self.players, self.board.blank_char)
            self.players.append(new_player)
        # player 1 points to the opponent object
        self.players[0].opponent = self.players[1] # player 1 - point object to refer to each other
        self.players[1].opponent = self.players[0]

    def play(self) -> None:
        """
        Play a game of Connect4 to completion
        :return: None
        """
        while True:
            print(self.board)
            player_move = self.cur_player.take_turn(self.board, self.num_pieces_to_win)
            if player_move.ends_game(self):
                self.someone_won = self.is_part_of_win(player_move.row, player_move.column)
                break
            self.change_turn()
        self.declare_winner_or_tie()

    def is_game_over(self) -> bool:
        """
        :return: whether the game is over
        """
        return self.someone_won or self.is_tie_game

    def is_part_of_win(self, row: int, column: int) -> bool:
        """
        Check if the given piece is part of a win
        :param row:
        :param column:
        :return:
        :side effect: modifies someone_won
        """
        if self.board.contains_blank_character(row, column):
            raise ValueError(f'{row},{column} contains a blank space')

        return self.board.count_max_matches(row, column) >= self.num_pieces_to_win

    def change_turn(self) -> None:
        """
        Change the turn to the next player in line
        :return:
        """
        self.cur_player_turn = (self.cur_player_turn + 1) % self.num_players

    def declare_winner_or_tie(self) -> None:
        """
        Print out who won the game or if it was a tie
        :return:
        """
        print(self.board)
        if self.someone_won:
            print(f'{self.cur_player} won the game!')
        else:
            print('Tie Game.')
