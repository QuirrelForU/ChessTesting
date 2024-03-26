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
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        expected_positions = {(2, 2), (1, 1), (0, 0), (4, 4), (5, 5), (6, 6), (7, 7),
                              (2, 4), (1, 5), (0, 6), (4, 2), (5, 1), (6, 0), (4, 4), }
        available_positions = set(bishop.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)

    def test_available_moves_with_blockage(self):
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        # Placing a piece at (4, 4) to block the bishop
        blocking_piece = TChessman("Pawn", TChessField(4, 4), ESide.WHITE)
        self.chessboard.get_field(4, 4).occupied_by = blocking_piece
        expected_positions = {(2, 2), (1, 1), (0, 0), (2, 4), (1, 5), (0, 6), (4, 2), (5, 1), (6, 0)}
        available_positions = set(bishop.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)

    def test_available_moves_capturing(self):
        bishop = Bishop(TChessField(3, 3), ESide.WHITE)
        # Placing an enemy piece at (4, 4)
        enemy_piece = TChessman("Pawn", TChessField(4, 4), ESide.BLACK)
        self.chessboard.get_field(4, 4).occupied_by = enemy_piece
        # Bishop should be able to move to (4, 4) but not beyond
        expected_positions = {(2, 2), (1, 1), (0, 0), (4, 4), (2, 4), (1, 5), (0, 6), (4, 2), (5, 1), (6, 0)}
        available_positions = set(bishop.available_moves(self.chessboard))
        self.assertEqual(expected_positions, available_positions)


if __name__ == '__main__':
    unittest.main()
