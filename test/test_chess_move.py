import unittest
from Pieces import Bishop, Rook
from GameBoard import Chessboard, TChessField
from Chessman import TChessman, EChessmanType, ESide, TChessMove, TChessman


class TestTChessMove(unittest.TestCase):

    def setUp(self):
        self.chessboard = Chessboard()

    def test_valid_move(self):
        rook = Rook((0, 0), ESide.WHITE)
        self.chessboard.get_field(0, 0).occupied_by = rook
        move = TChessMove(self.chessboard, rook, (0, 4))
        move.execute()
        self.assertIsNone(self.chessboard.get_field(0, 0).occupied_by)
        self.assertEqual(self.chessboard.get_field(0, 4).occupied_by, rook)
        self.assertEqual(str(move), 'Ra1a5')

    def test_invalid_move(self):
        bishop = Bishop((0, 2), ESide.WHITE)
        self.chessboard.get_field(0, 2).occupied_by = bishop
        move = TChessMove(self.chessboard, bishop, (0, 4))
        with self.assertRaises(ValueError):
            move.execute()

    def test_capture_move(self):
        bishop = Bishop((1, 1), ESide.WHITE)
        enemy_piece = TChessman(EChessmanType.PAWN, (2, 2), ESide.BLACK)
        self.chessboard.get_field(1, 1).occupied_by = bishop
        self.chessboard.get_field(2, 2).occupied_by = enemy_piece
        move = TChessMove(self.chessboard, bishop, (2, 2))
        move.execute()
        self.assertIsNone(self.chessboard.get_field(1, 1).occupied_by)
        self.assertEqual(self.chessboard.get_field(2, 2).occupied_by, bishop)
        self.assertIsNone(enemy_piece.position)
        self.assertEqual(str(move), 'Bb2xc3')

    def test_rook_capture_move(self):
        rook = Rook((1, 0), ESide.WHITE)
        enemy_piece = TChessman(EChessmanType.PAWN, (1, 5), ESide.BLACK)
        self.chessboard.get_field(1, 0).occupied_by = rook
        self.chessboard.get_field(1, 5).occupied_by = enemy_piece
        move = TChessMove(self.chessboard, rook, (1, 5))
        move.execute()
        self.assertIsNone(self.chessboard.get_field(1, 0).occupied_by)
        self.assertEqual(self.chessboard.get_field(1, 5).occupied_by, rook)
        self.assertIsNone(enemy_piece.position)
        self.assertEqual(str(move), 'Rb1xb6')

    def test_rook_move_to_empty_square(self):
        rook = Rook((7, 7), ESide.WHITE)
        self.chessboard.get_field(7, 7).occupied_by = rook
        move = TChessMove(self.chessboard, rook, (7, 4))
        move.execute()
        self.assertIsNone(self.chessboard.get_field(7, 7).occupied_by)
        self.assertEqual(self.chessboard.get_field(7, 4).occupied_by, rook)
        self.assertEqual(str(move), 'Rh8h5')

    def test_bishop_diagonal_capture(self):
        bishop = Bishop((2, 0), ESide.WHITE)
        enemy_piece = TChessman(EChessmanType.PAWN, (4, 2), ESide.BLACK)
        self.chessboard.get_field(2, 0).occupied_by = bishop
        self.chessboard.get_field(4, 2).occupied_by = enemy_piece
        move = TChessMove(self.chessboard, bishop, (4, 2))
        move.execute()
        self.assertIsNone(self.chessboard.get_field(2, 0).occupied_by)
        self.assertEqual(self.chessboard.get_field(4, 2).occupied_by, bishop)
        self.assertIsNone(enemy_piece.position)
        self.assertEqual(str(move), 'Bc1xe3')