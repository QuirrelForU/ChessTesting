import unittest
from Pieces import Rook
from GameBoard import Chessboard
from Chessman import TChessman, EChessmanType, ESide


class TestRook(unittest.TestCase):

    def setUp(self):
        self.chessboard = Chessboard()

    def test_rook_initialization(self):
        rook = Rook((0, 0), ESide.WHITE)
        self.assertEqual(rook.chessman_type, EChessmanType.ROOK)
        self.assertEqual(rook.position, (0, 0))
        self.assertEqual(rook.side, ESide.WHITE)

    def test_get_position(self):
        rook = Rook((3, 3), ESide.WHITE)
        self.assertEqual(rook.get_position(), (3, 3))

    def test_go_to_position(self):
        rook = Rook((3, 3), ESide.WHITE)
        rook.go_to_position((4, 4))
        self.assertEqual(rook.get_position(), (4, 4))

    def test_available_moves_empty_board(self):
        test_cases = [
            (0, 0, {(0, i) for i in range(1, 8)} | {(i, 0) for i in range(1, 8)}),
            (7, 7, {(7, i) for i in range(7)} | {(i, 7) for i in range(7)}),
            (3, 3, {(3, i) for i in range(8) if i != 3} | {(i, 3) for i in range(8) if i != 3}),
        ]

        for start_row, start_col, expected_positions in test_cases:
            rook = Rook((start_row, start_col), ESide.WHITE)
            self.chessboard.get_field(start_row, start_col).occupied_by = rook
            available_positions = set(rook.available_moves(self.chessboard))
            self.assertEqual(available_positions, expected_positions, f"Failed for Rook at ({start_row}, {start_col})")

    def test_rook_surrounded_by_allies(self):
        rook = Rook((3, 3), ESide.WHITE)
        self.chessboard.get_field(3, 3).occupied_by = rook
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ally_piece = TChessman(EChessmanType.PAWN, (3 + dx, 3 + dy), ESide.WHITE)
            self.chessboard.get_field(3 + dx, 3 + dy).occupied_by = ally_piece
        expected_positions = set()
        available_positions = set(rook.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)

    def test_rook_with_mixed_blockage(self):
        rook = Rook((3, 3), ESide.WHITE)
        self.chessboard.get_field(3, 3).occupied_by = rook
        ally_piece = TChessman(EChessmanType.PAWN, (3, 4), ESide.WHITE)
        enemy_piece = TChessman(EChessmanType.PAWN, (2, 3), ESide.BLACK)
        self.chessboard.get_field(3, 4).occupied_by = ally_piece
        self.chessboard.get_field(2, 3).occupied_by = enemy_piece
        expected_positions = {(3, 2), (3, 1), (3, 0), (4, 3), (5, 3), (6, 3), (7, 3), (2, 3)}
        available_positions = set(rook.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)

    def test_rook_capturing_multiple_pieces(self):
        rook = Rook((3, 3), ESide.WHITE)
        self.chessboard.get_field(3, 3).occupied_by = rook
        enemy_piece_1 = TChessman(EChessmanType.PAWN, (3, 5), ESide.BLACK)
        enemy_piece_2 = TChessman(EChessmanType.PAWN, (5, 3), ESide.BLACK)
        self.chessboard.get_field(3, 5).occupied_by = enemy_piece_1
        self
