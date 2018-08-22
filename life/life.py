LIVE = '*'
DEAD = '.'
POTENTIAL_NEIGHBOURS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
]


def life(input):
    return Life(input).next()


class Life():
    def __init__(self, input):
        self.grid = input
        self.max_y = len(input)

    def next(self):
        self.grid = [self.row_next(y, row) for y, row in enumerate(self.grid)]
        return self.grid

    def row_next(self, y, row):
        return ''.join([self.cell_next(x, y) for x in range(len(row))])

    def cell_next(self, x, y):
        live_neighbours = 0
        for i, j in POTENTIAL_NEIGHBOURS:
            if self.is_live(x + i, y + j):
                live_neighbours += 1

        if self.is_live(x, y):
            if live_neighbours in (2, 3):
                return LIVE
            else:
                return DEAD
        else:
            if live_neighbours == 3:
                return LIVE
            else:
                return DEAD

    def is_live(self, x, y):
        return self.are_valid_coords(x, y) and self.grid[y][x] == LIVE

    def are_valid_coords(self, x, y):
        return 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid)


# Fourth pass. Back to the basics, following TDD. The end result is much
# better! No extraneous abstractions, no overengineering. Short, readable code.
