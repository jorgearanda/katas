tens = {
    0: '',
    1: 'ten ',
    2: 'twenty ',
    3: 'thirty ',
    4: 'forty ',
    5: 'fifty ',
    6: 'sixty ',
    7: 'seventy ',
    8: 'eighty ',
    9: 'ninety ',
}

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
    words = ''
    if n >= 10000:
        words += tens [n // 10000]
        n = n % 10000
    if n >= 1000:
        words += digits[n // 1000] + ' thousand '
        n = n % 1000
    if n >= 100:
        words += digits[n // 100] + ' hundred '
        n = n % 100
    if n >= 10:
        words += tens[n // 10]
        n = n % 10
    words += digits[n]
    for key, value in exceptions.items():
        words = words.replace(key, value)
    words = words.strip()

    return words


# First pass. Less exciting than I had hoped.
