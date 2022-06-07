import unittest
from unittest.mock import patch
from Connect4Game.src import move, board
from Connect4Game.src.players import human_player


class TestHumanPlayer(unittest.TestCase):

    def test_name(self):
        human_test = human_player.HumanPlayer('Billy', '~')
        self.assertEqual(human_test.name, 'Billy')

    def test_get_move(self):
        user_input = ['1']
        human_test1 = human_player.HumanPlayer('Bob', '!')
        board_test = board.Board(3, 3, '*')
        move_test = move.Move.from_string(human_test1, '1')
        with patch('Connect4Game.src.players.human_player.input', side_effect = user_input):
            move_object = human_test1.get_move(board_test, 3)
            self.assertEqual(move_test, move_object)

    def test_get_valid_piece(self):
        test_human = human_player.HumanPlayer("Bob", "!")
        test_opponent = human_player.HumanPlayer("Billy", "~")
        self.assertNotEqual(test_human.piece, test_opponent.piece)


if __name__ == '__main__':
    unittest.main()
