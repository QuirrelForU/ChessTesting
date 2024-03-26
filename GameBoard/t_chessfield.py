class TChessField:
    """
    Represents a single field on a chessboard, holding information about its position and occupancy.
    """

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.occupied_by = None

    @property
    def is_busy(self) -> bool:
        """
        Checks if the field is occupied by a chess piece.

        :return: True if the field is occupied, False otherwise.
        """
        return self.occupied_by is not None
