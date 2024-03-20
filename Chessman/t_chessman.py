from Chessman.interface_chessman import IChessman
from Chessman.enums import EChessmanType, ESide


class TChessman(IChessman):
    def __init__(self, chessman_type, position, side):
        self.chessman_type = EChessmanType(chessman_type)
        self.position = position
        self.side = ESide(side)

    def get_position(self):
        return self.position

    def go_to_position(self, new_position):
        # Ваша логика для перемещения фигуры на новую позицию
        pass
