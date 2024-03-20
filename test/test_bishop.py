import unittest

from Pieces.bishop import Bishop
from GameBoard.chessboard import Chessboard


class TestBishop(unittest.TestCase):
    def test_available_moves(self):
        board = Chessboard()
        bishop = Bishop(board.get_field(3, 3), "White")

        available_positions = bishop.available_moves(board)

        self.assertIn((0, 0), available_positions)
        self.assertIn((1, 1), available_positions)
        self.assertIn((2, 2), available_positions)
        self.assertIn((4, 4), available_positions)
        self.assertIn((5, 5), available_positions)
        self.assertIn((6, 6), available_positions)
        self.assertIn((7, 7), available_positions)
        self.assertIn((0, 6), available_positions)
        self.assertIn((1, 5), available_positions)
        self.assertIn((2, 4), available_positions)
        self.assertIn((4, 2), available_positions)
        self.assertIn((5, 1), available_positions)
        self.assertIn((6, 0), available_positions)
