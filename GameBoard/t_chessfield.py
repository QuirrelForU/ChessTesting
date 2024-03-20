class TChessField:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.occupied_by = None

    # def get_row(self):
    #     return self.row
    #
    # def get_col(self):
    #     return self.col

    @property
    def is_busy(self):
        return self.occupied_by is not None
