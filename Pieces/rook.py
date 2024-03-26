from Chessman.t_chessman import TChessman
from Chessman.enums import EChessmanType


class Rook(TChessman):
    def __init__(self, position, side):
        super().__init__(EChessmanType.ROOK, position, side)

    def available_moves(self, chessboard):
        available_positions = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            row, col = self.position.row, self.position.col
            for i in range(1, 8):
                new_row, new_col = row + i * dx, col + i * dy
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    available_positions.append((new_row, new_col))
                    if chessboard.get_field(new_row, new_col).is_busy:
                        break
                else:
                    break

        return available_positions
