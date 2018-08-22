from life import life


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
