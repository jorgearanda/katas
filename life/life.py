LIVE = '*'
DEAD = '.'


def life(input):
    game = GameOfLife(input)
    return game.next()


class GameOfLife():
    def __init__(self, input):
        self.grid = input
        self.min_x = 0
        self.max_x = 0
        if len(self.grid) > 0:
            self.max_x = len(self.grid[0]) - 1
        self.min_y = 0
        self.max_y = len(self.grid) - 1

    def next(self):
        self.grid = [
            ''.join([self._cell_status(x, y) for x in range(len(row))])
            for y, row in enumerate(self.grid)
        ]

        return self.grid

    def _cell_status(self, x, y):
        if self._is_live(x, y):
            if self._cell_survives(x, y):
                return LIVE
            else:
                return DEAD
        else:
            if self._is_ripe_for_life(x, y):
                return LIVE
            else:
                return DEAD

    def _cell_survives(self, x, y):
        return 2 <= self._neighbours(x, y) <= 3

    def _is_ripe_for_life(self, x, y):
        return self._neighbours(x, y) == 3

    def _neighbours(self, x, y):
        candidates = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        count = 0
        for i, j in candidates:
            if self._is_valid_cell(x + i, y + j) and \
                    self._is_live(x + i, y + j):
                count += 1

        return count

    def _is_valid_cell(self, x, y):
        return self.min_x <= x <= self.max_x and \
            self.min_y <= y <= self.max_y

    def _is_live(self, x, y):
        return self.grid[y][x] == LIVE

# Second pass. I think I went a little crazy with list comprehensions here;
# the result being maybe less readable than my first pass.
# I should have probably added another class for cells: so many of the
# methods above are for a single cell and it may make sense to
# isolate that next time.
