from dataclasses import dataclass


@dataclass
class Numeral:
    symbol: str
    value: int


numerals = [
    Numeral("M", 1000),
    Numeral("CM", 900),
    Numeral("D", 500),
    Numeral("CD", 400),
    Numeral("C", 100),
    Numeral("XC", 90),
    Numeral("L", 50),
    Numeral("XL", 40),
    Numeral("X", 10),
    Numeral("IX", 9),
    Numeral("V", 5),
    Numeral("IV", 4),
    Numeral("I", 1),
]


def to_roman(arabic):
    if arabic == 0:
        return ""
    for numeral in numerals:
        if arabic >= numeral.value:
            return numeral.symbol + to_roman(arabic - numeral.value)


# Fourth pass, a recursive solution (not my original idea) that feels more
# elegant than the previous string substitution.
