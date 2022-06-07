from typing import List
import copy
from Connect4Game.src.players import player, random_ai
from .. import move, board

class BasicAi(random_ai.RandomAi):

    @classmethod
    def get_valid_name(cls, players: List["player.Player"], case_matters: bool = False) -> str:
        return f'BasicAi {len(players) + 1}'

    def get_move(self, the_board: board.Board, num_pieces_to_win: int) -> "move.Move":
        ## check for a winning position
        not_full_columns = [column for column in range(the_board.num_cols) if not the_board.is_column_full(column)]
        for col in not_full_columns:
            board_copy = copy.deepcopy(the_board)
            row = board_copy.add_piece_to_column(self.piece, col)
            if board_copy.count_max_matches(row, col) >= num_pieces_to_win:
                return move.Move(self, col)
            else:
                board_copy.remove_piece_from_position(row, col)

        for col in not_full_columns:
            board_copy = copy.deepcopy(the_board)
            opp_row = board_copy.add_piece_to_column(self.opponent.piece, col)
            if board_copy.count_max_matches(opp_row, col) >= num_pieces_to_win:
                return move.Move(self, col)
            else:
                board_copy.remove_piece_from_position(opp_row, col)

        else:
            return super().get_move(the_board, num_pieces_to_win)
