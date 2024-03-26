from Chessman.interface_chessman import IChessman
from Chessman.enums import EChessmanType, ESide
from typing import Tuple


class TChessman(IChessman):
    """
    Represents a generic chess piece, providing basic functionalities such as
    getting and setting the piece's position.
    """

    def __init__(self, chessman_type: EChessmanType, position: Tuple[int, int], side: ESide):
        """
         Initialize a chess piece with its type, position, and side.

         :param chessman_type: The type of the chess piece (e.g., Pawn, Rook).
         :param position: The position of the chess piece on the board as a (row, col) tuple.
         :param side: The side the chess piece belongs to (White or Black).
         """
        self.chessman_type = EChessmanType(chessman_type)
        self.position = position
        self.side = ESide(side)

    def get_position(self) -> Tuple[int, int]:
        return self.position

    def go_to_position(self, new_position: Tuple[int, int]):
        self.position = new_position
