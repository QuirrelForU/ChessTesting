class TChessMove:
    def __init__(self, piece, start_position, end_position, captured_piece=None):
        self.piece = piece
        self.start_position = start_position
        self.end_position = end_position
        self.captured_piece = captured_piece

    def as_string(self):
        move_notation = ''
        move_notation += self.piece.chessman_type.value[0]
        move_notation += chr(self.start_position.col + ord('a'))
        move_notation += str(self.start_position.row + 1)
        move_notation += 'x' if self.captured_piece else '-'
        move_notation += chr(self.end_position.col + ord('a'))
        move_notation += str(self.end_position.row + 1)
        return move_notation
