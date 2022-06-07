import unittest
import random
from Connect4Game.src.board import Board
from copy import deepcopy


class TestBoard(unittest.TestCase):

    test_num_row = random.randint(2, 20)
    test_num_col = random.randint(2, 20)
    test_blank_char = random.choice(["*", "^", "!", "#"])

    def test_property_getters(self):
        # set test board
        test_board = Board(self.test_num_row,
                           self.test_num_col, self.test_blank_char)
        correct_msg = "Should be {yes}."
        print(test_board)
        # num rows
        self.assertEqual(self.test_num_row, test_board.num_rows,
                         correct_msg.format(yes={self.test_num_row}))
        # num cols
        self.assertEqual(self.test_num_col, test_board.num_cols,
                         correct_msg.format(yes={self.test_num_col}))
        # is_full
        random_chars = ["$", "&"]
        copy_board = deepcopy(test_board)
        for row_pos, row in enumerate(test_board):
            for col_pos, col in enumerate(row):
                pick_rand_char = random.choice(random_chars)
                copy_board[row_pos][col_pos] = pick_rand_char
        self.assertEqual(True, copy_board.is_full,
                         correct_msg.format(yes={True}))
        print("copyboard", copy_board)
        self.assertEqual(False, test_board.is_full,
                         correct_msg.format(yes={False}))
        print("testBOard", test_board)

    def test_is_column_in_bounds(self):
        # set test board
        test_board = Board(self.test_num_row,
                           self.test_num_col, self.test_blank_char)
        # is_column_in_bound
        column_lower_over_bound = -1
        column_in_bound = random.randint(0, test_board.num_cols - 1)
        column_upper_over_bound = test_board.num_cols
        self.assertEqual(False, test_board.is_column_in_bounds(
            column_lower_over_bound))
        self.assertEqual(True, test_board.is_column_in_bounds(column_in_bound))
        self.assertEqual(False, test_board.is_column_in_bounds(
            column_upper_over_bound))

    def test_contains_blank_character(self):
        # set test board
        test_board = Board(self.test_num_row,
                           self.test_num_col, self.test_blank_char)
        rand_row = random.randint(0, test_board.num_rows - 1)
        rand_col = random.randint(0, test_board.num_cols - 1)
        test_board[rand_row][rand_col] = "$"
        self.assertEqual(
            False, test_board.contains_blank_character(rand_row, rand_col))

    def test_remove_piece_from_position(self):
        # set test board
        test_board = Board(self.test_num_row,
                           self.test_num_col, self.test_blank_char)
        rand_row = random.randint(0, test_board.num_rows - 1)
        rand_col = random.randint(0, test_board.num_cols - 1)
        test_board[rand_row][rand_col] = "$"
        test_board.remove_piece_from_position(rand_row, rand_col)
        test_board.remove_piece_from_position(rand_row, rand_col)
        self.assertEqual(test_board.blank_char, test_board[rand_row][rand_col])

    # def test_add_piece_to_column(self):
    #     # set test board
    #     test_board = Board(self.test_num_row,
    #                        self.test_num_col, self.test_blank_char)

    #     rand_col = random.randint(0, test_board.num_cols)

    def test_get_piece_at(self):
        # set test board
        test_board = Board(self.test_num_row,
                           self.test_num_col, self.test_blank_char)
        rand_row = random.randint(0, test_board.num_rows - 1)
        rand_col = random.randint(0, test_board.num_cols - 1)
        test_board[rand_row][rand_col] = "$"
        self.assertEqual("$", test_board.get_piece_at(rand_row, rand_col))