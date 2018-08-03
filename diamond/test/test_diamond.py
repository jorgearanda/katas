from diamond import print_diamond


def test_A():
    expected = [
        'A'
    ]

    assert print_diamond('A') == expected


def test_B_has_right_characters():
    expected = ['A', 'BB', 'A']
    assert strip_spaces_from(print_diamond('B')) == expected


def test_B():
    expected = [
        ' A',
        'B B',
        ' A'
    ]

    assert print_diamond('B') == expected


def test_C_has_right_characters():
    expected = ['A', 'BB', 'CC', 'BB', 'A']
    assert strip_spaces_from(print_diamond('C')) == expected


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
        '    A'
    ]

    assert print_diamond('E') == expected


def strip_spaces_from(d):
    return [line.replace(' ', '') for line in d]
