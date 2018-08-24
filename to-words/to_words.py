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

orders_of_magnitude = {
    10000: 'ten',
    1000: 'thousand',
    100: 'hundred',
    10: 'ten',
    1: '',
}


def to_words(n):
    words = ''
    for order in orders_of_magnitude:
        addition, n = order_of_magnitude_words(n, order)
        words += addition

    for incorrect, correct in exceptions.items():
        words = words.replace(incorrect, correct)
    words = words.strip()

    return words


def order_of_magnitude_words(n, order):
    words = ''
    if n >= order:
        words = digits[n // order] + ' ' + orders_of_magnitude[order] + ' '
        n %= order

    return words, n


# Second pass. I decided to make it a bit more fun this time, with the
# order_of_magnitude_words bit. Not sure it's a real improvement over the
# first pass in terms of comprehensibility though; it's an uncalled
# abstraction. Perhaps poorly named, also.
