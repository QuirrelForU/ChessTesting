from typing import Tuple
from Chessman import EChessmanType, TChessman
from GameBoard import Chessboard, TChessField


class TChessMove:
    """
    Represents a chess move, encapsulating the logic to execute the move,
    check its validity, and represent it as a string.
    """

    def __init__(self, chessboard: Chessboard, piece: TChessman, end_position: Tuple[int, int]):
        """
        Initialize a chess move with the game board, the piece to move, and the destination.

        param chessboard: The game board on which the move is made.
        param piece: The chess piece to move.
        param end_position: The destination position of the move as a (row, col) tuple.
        """
        self.chessboard = chessboard
        self.piece = piece
        self.start_position = piece.get_position()
        self.end_position = end_position
        self.captured_piece = None if not chessboard.get_field(*end_position).is_busy else chessboard.get_field(
            *end_position).occupied_by

    def execute(self):
        """
        Executes the chess move, updating the board and piece positions.
        Raises an error if the move is invalid.
        """
        if self.end_position not in self.piece.available_moves(self.chessboard):
            raise ValueError("Invalid move")

        self.chessboard.get_field(*self.start_position).occupied_by = None
        self.piece.go_to_position(TChessField(*self.end_position))
        self.chessboard.get_field(*self.end_position).occupied_by = self.piece

        if self.captured_piece:
            self.captured_piece.position = None

    def __str__(self) -> str:
        """
        Returns the string representation of the chess move in standard algebraic notation.

        :return: The string notation of the chess move.
        """
        move_notation = ''

        if self.piece.chessman_type != EChessmanType.PAWN:
            move_notation += self.piece.chessman_type.value[0]

        move_notation += chr(self.start_position[0] + ord('a'))
        move_notation += str(self.start_position[1] + 1)

        if self.captured_piece:
            move_notation += 'x'

        move_notation += chr(self.end_position[0] + ord('a'))
        move_notation += str(self.end_position[1] + 1)

        return move_notation
