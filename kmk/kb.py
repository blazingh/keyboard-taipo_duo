import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

class ChouChou(KMKKeyboard):

    def __init__(self):
        self.col_pins = (board.IO18,board.IO33,board.IO35,board.IO37)
        self.row_pins = (board.IO9,board.IO7,board.IO5)
        self.diode_orientation = DiodeOrientation.COL2ROW

