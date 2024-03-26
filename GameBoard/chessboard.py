from GameBoard.t_chessfield import TChessField


class Chessboard:
    """
    Represents a chessboard, holding a grid of TChessField objects.
    """

    def __init__(self):
        self.board = [[TChessField(row, col) for col in range(8)] for row in range(8)]

    def get_field(self, row: int, col: int) -> TChessField:
        """
        Retrieve a specific field from the chessboard.
        :param row: The row index of the field.
        :param col: The column index of the field.
        :return: The TChessField object at the specified location.
        """
        return self.board[row][col]
