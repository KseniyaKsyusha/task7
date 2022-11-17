import turtle as t

from Figure import Figure


class Square(Figure):
    def __init__(self, side):
        super().__init__(side, 4, 90)

