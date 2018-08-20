from enum import Enum


class State(Enum):
    DEAD = 0
    LIVE = 1


class Outlook(Enum):
    LONELY = 0
    STABLE = 1
    FERTILE = 2
    CROWDED = 3


def life(input):
    return Life(input).next()


class Life():
    def __init__(self, start_state):
        self.grid = []
        self.max_x = 0
        for y, row in enumerate(start_state):
            line = []
            for x, cell in enumerate(row):
                if cell == '*':
                    state = State.LIVE
                else:
                    state = State.DEAD
                line.append(Cell(x, y, state))
            self.grid.append(line)
            self.max_x = len(line) - 1
        self.max_y = len(self.grid) - 1
        self._link_cells()

    def _link_cells(self):
        candidates = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                neighbours = []
                for i, j in candidates:
                    if self._is_valid(x + i, y + j):
                        neighbours.append(self.grid[y + j][x + i])
                cell.link(neighbours)

    def _is_valid(self, x, y):
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def next(self):
        for row in self.grid:
            for cell in row:
                cell.prepare()

        for row in self.grid:
            for cell in row:
                cell.next()

        return self._present()

    def _present(self):
        grid_str = []
        for row in self.grid:
            grid_str.append(
                ''.join([self._state_str(cell.state) for cell in row]))

        return grid_str

    def _state_str(self, state):
        if state == State.DEAD:
            return '.'
        else:
            return '*'


class Cell():
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.outlook = None
        self.neighbours = []

    def link(self, neighbours):
        self.neighbours = neighbours

    def prepare(self):
        live_neighbours = 0
        for cell in self.neighbours:
            if cell.state == State.LIVE:
                live_neighbours += 1

        if live_neighbours < 2:
            self.outlook = Outlook.LONELY
        elif live_neighbours == 2:
            self.outlook = Outlook.STABLE
        elif live_neighbours == 3:
            self.outlook = Outlook.FERTILE
        else:
            self.outlook = Outlook.CROWDED

    def next(self):
        if self.outlook in [Outlook.LONELY, Outlook.CROWDED]:
            self.state = State.DEAD
        elif self.outlook == Outlook.FERTILE:
            self.state = State.LIVE
        self.outlook = None


# Third pass. What a lesson! This code is horrible.
# The abstractions are wrong and dirty, the workflow is clunky.
# Not pleasant to read.
# The reason is that I strayed from TDD, I think, as I wanted to try
# a different, Cell-based implementation.
# That was a disaster. I got lost in the weeds for a while, and ended
# up coding the whole solution mostly in the dark.
# Good learning on early/wrong abstractions.
