import string


def print_diamond(last):
    diamond = ''
    for letter in letters_until(last):
        diamond += outer_pad(letter, last) + letter
        if letter != 'A':
            diamond += inner_pad(letter) + letter
        diamond += '\n'
    diamond += lower_half(diamond)

    return diamond


def idx(letter):
    return string.ascii_uppercase.index(letter)


def letters_until(letter):
    return string.ascii_uppercase[:idx(letter) + 1]


def outer_pad(letter, last):
    return ' ' * (idx(last) - idx(letter))


def inner_pad(letter):
    return ' ' * (idx(letter) * 2 - 1)


def lower_half(diamond):
    lower = ''
    for line in diamond.split('\n')[-3::-1]:
        lower += line + '\n'

    return lower
