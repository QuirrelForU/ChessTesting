from interface_chessman import IChessman


class TChessman(IChessman):
    def __init__(self, chessman_type, position, side):
        self.chessman_type = chessman_type
        self.position = position
        self.side = side

    def get_position(self):
        return self.position

    def go_to_position(self, new_position):
        # Ваша логика для перемещения фигуры на новую позицию
        pass
