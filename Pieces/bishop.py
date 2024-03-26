from typing import Tuple, List

from Chessman.t_chessman import TChessman
from Chessman.enums import EChessmanType, ESide
from GameBoard import Chessboard


class Bishop(TChessman):
    """
    Represents a bishop chess piece, inheriting from TChessman.
    """

    def __init__(self, position: Tuple[int, int], side: ESide):
        super().__init__(EChessmanType.BISHOP, position, side)

    def available_moves(self, chessboard: Chessboard) -> List[Tuple[int, int]]:
        """
        Calculate the available moves for the bishop on the given chessboard.

        :param chessboard: The chessboard on which to calculate the moves.
        :return: A list of tuples representing the available move coordinates.
        """
        available_positions = []

        directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

        for dx, dy in directions:
            row, col = self.position[0], self.position[1]
            for i in range(1, 8):
                new_row, new_col = row + i * dx, col + i * dy
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if chessboard.get_field(new_row, new_col).is_busy:
                        if chessboard.get_field(new_row, new_col).occupied_by.side != self.side:
                            available_positions.append((new_row, new_col))
                        break
                    else:
                        available_positions.append((new_row, new_col))
                else:
                    break

        return available_positions
