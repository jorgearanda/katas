from diamond import print_diamond


def test_A():
    expected = 'A\n'
    assert print_diamond('A') == expected


def test_B():
    expected = ' A\nB B\n A\n'
    assert print_diamond('B') == expected


def test_C():
    expected = '  A\n B B\nC   C\n B B\n  A\n'
    assert print_diamond('C') == expected


def test_D():
    expected = '   A\n  B B\n C   C\nD     D\n C   C\n  B B\n   A\n'
    assert print_diamond('D') == expected
