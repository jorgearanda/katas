from collections import namedtuple

RomanDigit = namedtuple('RomanDigit', 'symbol quantity')
roman_digits = [
    RomanDigit('M', 1000),
    RomanDigit('D', 500),
    RomanDigit('C', 100),
    RomanDigit('L', 50),
    RomanDigit('X', 10),
    RomanDigit('V', 5),
    RomanDigit('I', 1)
]

Abbreviation = namedtuple('Abbreviation', 'long short')
abbreviations = [
    Abbreviation('DCCCC', 'CM'),
    Abbreviation('CCCC', 'CD'),
    Abbreviation('LXXXX', 'XC'),
    Abbreviation('XXXX', 'XL'),
    Abbreviation('VIIII', 'IX'),
    Abbreviation('IIII', 'IV')
]


def to_roman(arabic):
    long_roman = to_long_form_roman(arabic)
    roman = abbreviate(long_roman)

    return roman


def to_long_form_roman(arabic):
    roman = ''
    while arabic > 0:
        for digit in roman_digits:
            if arabic >= digit.quantity:
                roman += digit.symbol
                arabic -= digit.quantity
                break

    return roman


def abbreviate(roman):
    for abbr in abbreviations:
        roman = roman.replace(abbr.long, abbr.short)

    return roman


# Second pass. The move away from // and % operations is a big improvement.
# I'm not sure if a RomanNumeral class (as in the first pass) is warranted;
# as the above is quite readable and serves its purpose.
