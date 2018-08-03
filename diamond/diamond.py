from string import ascii_uppercase


def print_diamond(last):
    diamond = [
        make_line(letter, last)
        for letter in letters_until(last)
    ]
    diamond += lower_half_of(diamond)

    return diamond


def make_line(letter, last):
    line = outer_pad(letter, last) + letter
    if letter != 'A':
        line += inner_pad(letter) + letter

    return line


def letters_until(last):
    return ascii_uppercase[:index(last) + 1]


def index(letter):
    return ascii_uppercase.index(letter)


def outer_pad(letter, last):
    return ' ' * (index(last) - index(letter))


def inner_pad(letter):
    return ' ' * (index(letter) * 2 - 1)


def lower_half_of(upper_half):
    lower = []
    for line in reverse(upper_half)[1:]:
        lower.append(line)

    return lower


def reverse(items):
    return items[::-1]
