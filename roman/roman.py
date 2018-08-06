from collections import namedtuple

Abbreviation = namedtuple('Abbreviation', 'long short')
abbreviations = [
    Abbreviation('I' * 1000, 'M'),
    Abbreviation('I' * 500, 'D'),
    Abbreviation('I' * 100, 'C'),
    Abbreviation('I' * 50, 'L'),
    Abbreviation('I' * 10, 'X'),
    Abbreviation('I' * 5, 'V'),
    Abbreviation('DCCCC', 'CM'),
    Abbreviation('CCCC', 'CD'),
    Abbreviation('LXXXX', 'XC'),
    Abbreviation('XXXX', 'XL'),
    Abbreviation('VIIII', 'IX'),
    Abbreviation('IIII', 'IV')
]


def to_roman(arabic):
    roman = 'I' * arabic
    for abbr in abbreviations:
        roman = roman.replace(abbr.long, abbr.short)

    return roman

# Third pass. This is so much cleaner than the previous ones!
# Simple, a single for loop, and a clear path to convert back
# to arabic. <3
