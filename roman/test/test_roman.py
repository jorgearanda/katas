from roman import to_roman


def test_1():
    assert "I" == to_roman(1)


def test_2():
    assert "II" == to_roman(2)


def test_3():
    assert "III" == to_roman(3)


def test_4():
    assert "IV" == to_roman(4)


def test_5():
    assert "V" == to_roman(5)


def test_6():
    assert "VI" == to_roman(6)


def test_9():
    assert "IX" == to_roman(9)


def test_27():
    assert "XXVII" == to_roman(27)


def test_48():
    assert "XLVIII" == to_roman(48)


def test_59():
    assert "LIX" == to_roman(59)


def test_93():
    assert "XCIII" == to_roman(93)


def test_141():
    assert "CXLI" == to_roman(141)


def test_163():
    assert "CLXIII" == to_roman(163)


def test_402():
    assert "CDII" == to_roman(402)


def test_575():
    assert "DLXXV" == to_roman(575)


def test_911():
    assert "CMXI" == to_roman(911)


def test_1024():
    assert "MXXIV" == to_roman(1024)


def test_3000():
    assert "MMM" == to_roman(3000)
