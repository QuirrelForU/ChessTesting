from Chessman import EChessmanType
from GameBoard import TChessField


class TChessMove:
    def __init__(self, chessboard, piece, end_position):
        self.chessboard = chessboard
        self.piece = piece
        self.start_position = piece.get_position()
        self.end_position = end_position
        self.captured_piece = None if not chessboard.get_field(*end_position).is_busy else chessboard.get_field(
            *end_position).occupied_by

    def execute(self):
        # Check if the move is valid
        if self.end_position not in self.piece.available_moves(self.chessboard):
            raise ValueError("Invalid move")

        # Move the piece on the board
        self.chessboard.get_field(*self.start_position).occupied_by = None
        self.piece.go_to_position(TChessField(*self.end_position))
        self.chessboard.get_field(*self.end_position).occupied_by = self.piece

        # If there is a captured piece, remove it from the board
        if self.captured_piece:
            self.captured_piece.position = None  # Or any other way you denote a captured piece

    def __str__(self):
        move_notation = ''

        # Piece type notation
        if self.piece.chessman_type != EChessmanType.PAWN:
            move_notation += self.piece.chessman_type.value[0]

        # Starting position (optional in real notation, included here for clarity)
        move_notation += chr(self.start_position.col + ord('a'))
        move_notation += str(self.start_position.row + 1)

        # Capture notation
        if self.captured_piece:
            move_notation += 'x'

        # Ending position
        move_notation += chr(self.end_position.col + ord('a'))
        move_notation += str(self.end_position.row + 1)

        return move_notation
