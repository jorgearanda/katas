from diamond import print_diamond


def test_A():
    expected = ['A']

    assert print_diamond('A') == expected


def test_B():
    expected = [
        ' A',
        'B B',
        ' A'
    ]

    assert print_diamond('B') == expected


def test_C_has_correct_sequences():
    expected = 'ABBCCBBA'

    assert ''.join(print_diamond('C')).replace(' ', '') == expected


def test_C():
    expected = [
        '  A',
        ' B B',
        'C   C',
        ' B B',
        '  A'
    ]

    assert print_diamond('C') == expected


def test_E():
    expected = [
        '    A',
        '   B B',
        '  C   C',
        ' D     D',
        'E       E',
        ' D     D',
        '  C   C',
        '   B B',
        '    A',
    ]

    assert print_diamond('E') == expected
