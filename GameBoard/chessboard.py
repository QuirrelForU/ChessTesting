from t_chessfield import TChessField


class Chessboard:
    def __init__(self):
        self.board = [[TChessField(row, col) for col in range(8)] for row in range(8)]

    def get_field(self, row, col):
        return self.board[row][col]
