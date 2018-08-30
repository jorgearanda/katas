digits = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

orders_of_magnitude = {
    1000000000: 'billion',
    100000000: 'hundred',
    10000000: 'ten',
    1000000: 'million',
    100000: 'hundred',
    10000: 'ten',
    1000: 'thousand',
    100: 'hundred',
    10: 'ten',
    1: '',
}

exceptions = {
    'one ten': 'ten',
    'two ten': 'twenty',
    'three ten': 'thirty',
    'four ten': 'forty',
    'five ten': 'fifty',
    'six ten': 'sixty',
    'seven ten': 'seventy',
    'eight ten': 'eighty',
    'nine ten': 'ninety',
    'ten one': 'eleven',
    'ten two': 'twelve',
    'ten three': 'thirteen',
    'ten four': 'fourteen',
    'ten five': 'fifteen',
    'ten six': 'sixteen',
    'ten seven': 'seventeen',
    'ten eight': 'eighteen',
    'ten nine': 'nineteen',
}


def to_words(n):
    long_form = _long_form_number_text(n)
    short_form = _eliminate_exceptions(long_form).strip()

    return short_form


def _long_form_number_text(n):
    words = ''
    for order, denomination in orders_of_magnitude.items():
        if n >= order:
            print(order);
            words += digits[n // order] + ' ' + denomination + ' '
            n %= order

    return words


def _eliminate_exceptions(words):
    for incorrect, correct in exceptions.items():
        words = words.replace(incorrect, correct)
    words = words.strip()

    return words


# Third pass. I think this is a slight improvement over the second.
# It would be hard to make the function cleaner than it is here,
# except perhaps in some of the naming choices.
#
# I decided to add a few more orders of magnitude, up to a billion,
# because it was very easy to do so.
