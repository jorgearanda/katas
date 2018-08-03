from string import ascii_uppercase


def print_diamond(last_letter):
    diamond = [
        make_line(letter, last_letter)
        for letter in letters_up_to(last_letter)
    ]

    return diamond + lower_half_of(diamond)


def letters_up_to(last_letter):
    return ascii_uppercase[:index(last_letter) + 1]


def make_line(letter, last_letter):
    line = left_pad(letter, last_letter) + letter
    if letter != 'A':
        line += inner_pad(letter) + letter

    return line


def left_pad(letter, last_letter):
    return ' ' * (index(last_letter) - index(letter))


def inner_pad(letter):
    return ' ' * (index(letter) * 2 - 1)


def index(letter):
    return ascii_uppercase.index(letter)


def lower_half_of(upper_half):
    return upper_half[:-1][::-1]


# Third pass; fairly unchanged from the second other than minor naming changes.
