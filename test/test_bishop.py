import unittest
from Pieces import Bishop
from GameBoard import Chessboard
from GameBoard import TChessField
from Chessman import TChessman, EChessmanType, ESide


class TestBishop(unittest.TestCase):

    def setUp(self):
        self.chessboard = Chessboard()

    def test_bishop_initialization(self):
        bishop = Bishop(TChessField(0, 2), ESide.WHITE)
        self.assertEqual(bishop.chessman_type, EChessmanType.BISHOP)
        self.assertEqual(bishop.position.row, 0)
        self.assertEqual(bishop.position.col, 2)
        self.assertEqual(bishop.side, ESide.WHITE)

    def test_get_position(self):
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        self.assertEqual(bishop.get_position().row, 3)
        self.assertEqual(bishop.get_position().col, 3)

    def test_go_to_position(self):
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        bishop.go_to_position(TChessField(4, 4))
        self.assertEqual(bishop.get_position().row, 4)
        self.assertEqual(bishop.get_position().col, 4)

    def test_available_moves_empty_board(self):
        test_cases = [
            # (start_row, start_col, expected_positions_set)
            (3, 3, {(2, 2), (1, 1), (0, 0), (4, 4), (5, 5), (6, 6), (7, 7),
                    (2, 4), (1, 5), (0, 6), (4, 2), (5, 1), (6, 0)}),
            (0, 0, {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)}),
            (0, 3, {(1, 2), (2, 1), (3, 0), (1, 4), (2, 5), (3, 6), (4, 7)}),
            (2, 4, {(1, 3), (0, 2), (3, 5), (4, 6), (5, 7),
                    (1, 5), (0, 6), (3, 3), (4, 2), (5, 1), (6, 0)})
        ]

        for start_row, start_col, expected_positions in test_cases:
            bishop = Bishop(TChessField(start_row, start_col), ESide.WHITE)
            available_positions = set(bishop.available_moves(self.chessboard))
            self.assertEqual(available_positions, expected_positions,
                             f"Failed for Bishop at ({start_row}, {start_col})")

    def test_available_moves_with_blockage(self):
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        blocking_piece = TChessman("Pawn", TChessField(4, 4), ESide.WHITE)
        self.chessboard.get_field(4, 4).occupied_by = blocking_piece
        expected_positions = {(2, 2), (1, 1), (0, 0), (2, 4), (1, 5), (0, 6), (4, 2), (5, 1), (6, 0)}
        available_positions = set(bishop.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)

    def test_available_moves_capturing(self):
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        enemy_piece = TChessman("Pawn", TChessField(4, 4), ESide.BLACK)
        self.chessboard.get_field(4, 4).occupied_by = enemy_piece
        expected_positions = {(2, 2), (1, 1), (0, 0), (4, 4), (2, 4), (1, 5), (0, 6), (4, 2), (5, 1), (6, 0)}
        available_positions = set(bishop.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)

    def test_bishop_surrounded_by_allies(self):
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            ally_piece = TChessman("Pawn", TChessField(3 + dx, 3 + dy), ESide.WHITE)
            self.chessboard.get_field(3 + dx, 3 + dy).occupied_by = ally_piece
        expected_positions = set()
        available_positions = set(bishop.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)

    def test_bishop_with_mixed_blockage(self):
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        ally_piece = TChessman("Pawn", TChessField(4, 4), ESide.WHITE)
        enemy_piece = TChessman("Pawn", TChessField(2, 4), ESide.BLACK)
        self.chessboard.get_field(4, 4).occupied_by = ally_piece
        self.chessboard.get_field(2, 4).occupied_by = enemy_piece
        expected_positions = {(2, 4), (2, 2), (1, 1), (0, 0), (4, 2), (5, 1), (6, 0)}
        available_positions = set(bishop.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)

    def test_bishop_capturing_multiple_pieces(self):
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        enemy_piece_1 = TChessman("Pawn", TChessField(5, 5), ESide.BLACK)
        enemy_piece_2 = TChessman("Pawn", TChessField(1, 5), ESide.BLACK)
        self.chessboard.get_field(5, 5).occupied_by = enemy_piece_1
        self.chessboard.get_field(1, 5).occupied_by = enemy_piece_2
        expected_positions = {(4, 4), (5, 5), (2, 4), (1, 5), (2, 2), (1, 1), (0, 0), (4, 2), (5, 1), (6, 0)}
        available_positions = set(bishop.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)


