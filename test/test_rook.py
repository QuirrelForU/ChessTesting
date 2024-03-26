import unittest
from Pieces import Rook
from GameBoard import Chessboard, TChessField
from Chessman import TChessman, EChessmanType, ESide


class TestRook(unittest.TestCase):

    def setUp(self):
        self.chessboard = Chessboard()

    def test_rook_movement_empty_board(self):
        test_cases = [
            # (start_row, start_col, expected_positions_set)
            (0, 0, {(0, i) for i in range(1, 8)} | {(i, 0) for i in range(1, 8)}),
            (7, 7, {(7, i) for i in range(7)} | {(i, 7) for i in range(7)}),
            (3, 3, {(3, i) for i in range(8) if i != 3} | {(i, 3) for i in range(8) if i != 3}),
        ]

        for start_row, start_col, expected_positions in test_cases:
            rook = Rook(TChessField(start_row, start_col), ESide.WHITE)
            available_positions = set(rook.available_moves(self.chessboard))
            self.assertEqual(available_positions, expected_positions, f"Failed for Rook at ({start_row}, {start_col})")
