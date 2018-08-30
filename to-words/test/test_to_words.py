from to_words import to_words


def test_1():
    assert to_words(1) == 'one'


def test_2():
    assert to_words(2) == 'two'


def test_3():
    assert to_words(3) == 'three'


def test_4():
    assert to_words(4) == 'four'


def test_5():
    assert to_words(5) == 'five'


def test_10():
    assert to_words(10) == 'ten'


def test_11():
    assert to_words(11) == 'eleven'


def test_12():
    assert to_words(12) == 'twelve'


def test_13():
    assert to_words(13) == 'thirteen'


def test_19():
    assert to_words(19) == 'nineteen'


def test_20():
    assert to_words(20) == 'twenty'


def test_27():
    assert to_words(27) == 'twenty seven'


def test_35():
    assert to_words(35) == 'thirty five'


def test_78():
    assert to_words(78) == 'seventy eight'


def test_103():
    assert to_words(103) == 'one hundred three'


def test_741():
    assert to_words(741) == 'seven hundred forty one'


def test_999():
    assert to_words(999) == 'nine hundred ninety nine'


def test_1015():
    assert to_words(1015) == 'one thousand fifteen'


def test_8765():
    assert to_words(8765) == 'eight thousand seven hundred sixty five'


def test_12345():
    assert to_words(12345) == 'twelve thousand three hundred forty five'


def test_99999():
    assert to_words(99999) == 'ninety nine thousand nine hundred ninety nine'


def test_9999999999():
    assert to_words(9999999999) == \
        'nine billion nine hundred ninety nine million ' + \
        'nine hundred ninety nine thousand nine hundred ninety nine'
