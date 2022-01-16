import random
from Cell import Cell


class Field:
    def __init__(self, cols, rows, cell_size):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size

        self.field = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.fill_randomly()

    def fill_randomly(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if random.choice([0, 1]):
                    self.field[i][j] = Cell(j, i, self.cell_size)

    def update_field(self):
        new_field = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                count = self.count_near(i, j)
                if not self.field[i][j] and count == 3:
                    new_field[i][j] = Cell(j, i, self.cell_size)
                elif self.field[i][j] and (count == 2 or count == 3):  # check: equation count == 3 is redundant
                    new_field[i][j] = self.field[i][j]
                else:
                    new_field[i][j] = None
        self.field = new_field

    def count_near(self, i, j):
        count = 0
        neighbours = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        for neighb in neighbours:
            if self.field[(i + neighb[0]) % self.rows][(j + neighb[1]) % self.cols]:
                count += 1
        return count

    def print_field(self):
        print('Current generation')
        for row in self.field:
            row_str = ''
            for el in row:
                if el:
                    row_str += '1 '
                else:
                    row_str += '0 '
            print(row_str[:-1])
        print()
