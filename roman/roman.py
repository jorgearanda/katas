from dataclasses import dataclass


@dataclass
class RomanNumeral:
    symbol: str
    value: int


roman_numerals = [
    RomanNumeral("M", 1000),
    RomanNumeral("CM", 900),
    RomanNumeral("D", 500),
    RomanNumeral("CD", 400),
    RomanNumeral("C", 100),
    RomanNumeral("XC", 90),
    RomanNumeral("L", 50),
    RomanNumeral("XL", 40),
    RomanNumeral("X", 10),
    RomanNumeral("IX", 9),
    RomanNumeral("V", 5),
    RomanNumeral("IV", 4),
    RomanNumeral("I", 1),
]


def to_roman(arabic: int) -> str:
    for numeral in roman_numerals:
        if numeral.value <= arabic:
            return numeral.symbol + to_roman(arabic - numeral.value)
    return ""


def to_arabic(roman: str) -> int:
    for numeral in roman_numerals:
        if roman.startswith(numeral.symbol):
            return numeral.value + to_arabic(roman[len(numeral.symbol) :])
    return 0


# Seventh pass. Minimal naming changes only; clean progression.
