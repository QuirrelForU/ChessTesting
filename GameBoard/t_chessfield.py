
class TChessField:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.occupied_by = None

    @property
    def is_busy(self):
        return self.occupied_by is not None
