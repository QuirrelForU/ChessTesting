import unittest
from Pieces import Bishop, Rook
from GameBoard import Chessboard, TChessField
from Chessman import TChessman, EChessmanType, ESide, TChessMove


class TestTChessMove(unittest.TestCase):

    def setUp(self):
        self.chessboard = Chessboard()

    def test_valid_move(self):
        rook = Rook(TChessField(0, 0), ESide.WHITE)
        self.chessboard.get_field(0, 0).occupied_by = rook
        move = TChessMove(self.chessboard, rook, (0, 4))
        move.execute()
        self.assertIsNone(self.chessboard.get_field(0, 0).occupied_by)
        self.assertEqual(self.chessboard.get_field(0, 4).occupied_by, rook)
        self.assertEqual(str(move), 'Ra1a5')

    def test_invalid_move(self):
        bishop = Bishop(TChessField(0, 2), ESide.WHITE)
        self.chessboard.get_field(0, 2).occupied_by = bishop
        move = TChessMove(self.chessboard, bishop, (0, 4))
        with self.assertRaises(ValueError):
            move.execute()

    def test_capture_move(self):
        pawn = Pawn(TChessField(1, 1), ESide.WHITE)
        rook = Rook(TChessField(1, 3), ESide.BLACK)
        self.chessboard.get_field(1, 1).occupied_by = pawn
        self.chessboard.get_field(1, 3).occupied_by = rook
        move = TChessMove(self.chessboard, pawn, (1, 3))
        move.execute()
        self.assertIsNone(self.chessboard.get_field(1, 1).occupied_by)
        self.assertEqual(self.chessboard.get_field(1, 3).occupied_by, pawn)
        self.assertIsNone(rook.position)  # Assuming this is how we mark captured pieces
        self.assertEqual(str(move), 'b2xb4')


if __name__ == '__main__':
    unittest.main()
