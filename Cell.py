from pygame import Rect


class Cell:
    def __init__(self, x, y, cell_size):
        self.x = x
        self.y = y
        self.rect = Rect(x * cell_size, y * cell_size, cell_size, cell_size)
