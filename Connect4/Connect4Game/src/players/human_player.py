from typing import List
from Connect4Game.src.players import player
from Connect4Game.src import board, move


class HumanPlayer(player.Player):

    @classmethod
    def get_valid_piece(cls, players: List["player.Player"], blank_char: str, case_matters: bool = False) -> str:
        """
        Check if piece is a valid one to use in the current game.
        A piece is valid if it is 1 character big
        and no other players are using it.
        :param players: The other players in the game
        :param blank_char: The blank character for the board
        :param case_matters: Does case matter when comparing pieces?
        :return: the piece the player has chosen
        :raises ValueError if the piece is not valid
        """
        player_num = len(players) + 1
        piece = input(f'HumanPlayer {player_num} enter your piece: ').strip()
        cmp_piece = piece if case_matters else piece.lower()
        player_pieces = {player.piece if case_matters else player.piece.lower(): player for player in players}

        if not piece:
            raise ValueError('Your piece cannot be the empty string or whitespace.')
        elif len(piece) > 1:
            raise ValueError(f'{piece} is not a single character. Your piece can only be a single character.')
        elif cmp_piece == blank_char.lower():
            raise ValueError(f'Your piece cannot be the same as the blank character.')
        elif cmp_piece in player_pieces:
            raise ValueError(
                f'You cannot use {piece} for your piece as {player_pieces[cmp_piece]} is already using it.')
        else:
            return piece

    @classmethod
    def get_valid_name(cls, players: List["player.Player"], case_matters: bool = False) -> str:
        """
        Check if name is a valid name for this player
        :param players:  The other players in the game
        :param case_matters: Whether capitalization matters or not
        :return: The name the user has chosen
        :raises: ValueError if the name chosen is not valid

        """
        player_num = len(players) + 1
        player_names = {player.name if case_matters else player.name.lower() for player in players}
        name = input(f'HumanPlayer {player_num} enter your name: ').strip()
        cmp_name = name if case_matters else name.lower()
        if not name:
            raise ValueError('Your name cannot be the empty string or whitespace.')
        elif cmp_name in player_names:
            raise ValueError(f'You cannot use {name} for your name as someone else is already using it.')
        else:
            return name

    
    def get_move(self, the_board: "board.Board", num_pieces_to_win: int) -> "move.Move":
        """"
        Get a move from the user
        :return: the move the user made
        :raises: MoveError if the move is invalid
        """
        str_move = input(f'{self.name}, please enter the column you want to play in: ')
        return move.Move.from_string(self, str_move)
