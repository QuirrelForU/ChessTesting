from Chessman.t_chessman import TChessman
from Chessman.enums import EChessmanType


class Bishop(TChessman):
    def __init__(self, position, side):
        super().__init__(EChessmanType.BISHOP, position, side)
