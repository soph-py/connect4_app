import random
from typing import List
from Connect4Game.src.board import Board
from Connect4Game.src.players import player
from .. import move


class RandomAi(player.Player):

    @classmethod
    def get_valid_piece(cls, players: List["player.Player"], blank_char: str, case_matters: bool = False) -> str:
        VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
        illegal_pieces = {other_player.piece for other_player in players} # set comprehension so look ups are done with hashtables and hashing
        illegal_pieces.add(blank_char)
        while True:
            piece_choice = random.choice(VISIBLE_CHARACTERS)
            if piece_choice not in illegal_pieces:
                return piece_choice

    @classmethod
    def get_valid_name(cls, players: List["player.Player"], case_matters: bool = False) -> str:
        return f'RandomAi {len(players) + 1}'

    def get_move(self, the_board: Board, num_pieces_to_win: int) -> "move.Move":
        """
        Generate a random move from the RandomAi player
        :return: the move the RandomAi player made
        :raises: MoveError if the move is invalid
        RandomAi will not be using "the_board" argument, but he doesn't need to use it, it's optional
        """
        # generate a list of the columns that are not full, and then randomly pick one
        not_full_columns = [column for column in range(the_board.num_cols) if not the_board.is_column_full(column)]
        return move.Move(self, random.choice(not_full_columns))
