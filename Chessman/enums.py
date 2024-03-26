from enum import Enum


class EChessmanType(Enum):
    KING = "King"
    QUEEN = "Queen"
    ROOK = "Rook"
    BISHOP = "Bishop"
    KNIGHT = "Knight"
    PAWN = "Pawn"


class ESide(Enum):
    WHITE = "White"
    BLACK = "Black"
