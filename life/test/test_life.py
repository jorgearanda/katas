from life import life, Cell, State, Outlook


def test_empty():
    input = []
    expected = []

    assert life(input) == expected


def test_a_single_live_cell_dies():
    input = ['*']
    expected = ['.']

    assert life(input) == expected


def test_a_single_dead_cell_stays_dead():
    input = ['.']
    expected = ['.']

    assert life(input) == expected


def test_a_row_of_live_cells_shrinks():
    input = ['*****']
    expected = ['.***.']

    assert life(input) == expected


def test_a_row_with_live_groups_has_them_shrinking():
    input = ['***..***']
    expected = ['.*....*.']

    assert life(input) == expected


def test_a_column_of_live_cells_shrinks():
    input = ['*', '*', '*', '*', '*']
    expected = ['.', '*', '*', '*', '.']

    assert life(input) == expected


def test_two_dimensions():
    input = [
        '....',
        '..*.',
        '.**.',
        '....'
    ]
    expected = [
        '....',
        '.**.',
        '.**.',
        '....'
    ]

    assert life(input) == expected


def test_donut():
    input = [
        '.....',
        '.***.',
        '.*.*.',
        '.***.',
        '.....'
    ]
    expected = [
        '..*..',
        '.*.*.',
        '*...*',
        '.*.*.',
        '..*..'
    ]

    assert life(input) == expected


class TestCell():
    def test_smoke(self):
        c = Cell(0, 0, State.LIVE)

        assert True

    def test_link(self):
        c1 = Cell(0, 0, State.LIVE)
        c2 = Cell(0, 1, State.DEAD)
        c1.link([c2])

        assert c1.neighbours == [c2]

    def test_prepare(self):
        c1 = Cell(0, 0, State.LIVE)
        c2 = Cell(0, 1, State.LIVE)
        c3 = Cell(0, 2, State.LIVE)
        c2.link([c1, c3])
        c2.prepare()

        assert c2.outlook == Outlook.STABLE

    def test_next(self):
        c1 = Cell(0, 0, State.LIVE)
        c2 = Cell(0, 1, State.LIVE)
        c3 = Cell(0, 2, State.DEAD)
        c2.link([c1, c3])
        c2.prepare()
        c2.next()

        assert c2.state == State.DEAD
