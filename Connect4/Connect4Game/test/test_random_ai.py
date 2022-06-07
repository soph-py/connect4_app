import unittest
from unittest.mock import patch
from Connect4Game.src import move, board
from Connect4Game.src.players import random_ai

class TestRandomAiPlayer(unittest.TestCase):

    def test_name(self):
        random_test1 = random_ai.RandomAi('Random1', 'o')
        random_test2 = random_ai.RandomAi('Random2', '!')
        self.assertEqual(random_test1.name, 'Random1')
        self.assertEqual(random_test2.name, 'Random2')

    def test_opponent(self):
        random_test1 = random_ai.RandomAi('Random1', 'o')
        random_test2 = random_ai.RandomAi('Random2', '!', random_test1)
        self.assertEqual(random_test1, random_test2.opponent)
        random_test1.opponent = random_test2
        self.assertEqual(random_test2, random_test1.opponent)

    def test_piece(self):
        random_test1 = random_ai.RandomAi('Random1', 'o')
        random_test2 = random_ai.RandomAi('Random2', '!')
        self.assertEqual(random_test1.piece, 'o')
        self.assertEqual(random_test2.piece, '!')

if __name__ == '__main__':
    unittest.main()