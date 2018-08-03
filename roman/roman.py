from collections import namedtuple

Expansion = namedtuple('Expansion', ['symbol', 'quantity'])
expansion_rules = [
    Expansion('M', 1000),
    Expansion('D', 500),
    Expansion('C', 100),
    Expansion('L', 50),
    Expansion('X', 10),
    Expansion('V', 5),
    Expansion('I', 1)
]

Shortening = namedtuple('Shortening', ['long', 'short'])
shortening_rules = [
    Shortening('DCCCC', 'CM'),
    Shortening('CCCC', 'CD'),
    Shortening('LXXXX', 'XC'),
    Shortening('XXXX', 'XL'),
    Shortening('VIIII', 'IX'),
    Shortening('IIII', 'IV')
]


def to_roman(arabic):
    return str(RomanNumeral(arabic))


class RomanNumeral():
    def __init__(self, arabic):
        self.roman = ''
        self._remainder = arabic
        self.convert()

    def __str__(self):
        return self.roman

    def convert(self):
        self.expand()
        self.shorten()

    def expand(self):
        for exp in expansion_rules:
            self.roman += exp.symbol * (self._remainder // exp.quantity)
            self._remainder %= exp.quantity

    def shorten(self):
        for sub in shortening_rules:
            self.roman = self.roman.replace(sub.long, sub.short)


# First pass. Except for some naming concerns, I like it!
