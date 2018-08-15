from itertools import permutations

points = ['love', '15', '30', '40']


class Game():
    def __init__(self, first_player, second_player):
        self.first = Player(first_player)
        self.second = Player(second_player)
        self._score_str = 'love all'
        self._winner = None

    def point(self, player):
        if player == self.first.name:
            self.first.point()
        else:
            self.second.point()

        self.update_score()

    def score(self):
        return self._score_str

    def winner(self):
        return self._winner

    def update_score(self):
        for perm in permutations([self.first, self.second], 2):
            if victory_over(perm[0], perm[1]):
                self._score_str = perm[0].name + ' wins'
                self._winner = perm[0].name
                break
            elif advantage_over(perm[0], perm[1]):
                self._score_str = 'advantage ' + perm[0].name
                break
        else:
            if deuce(self.first, self.second):
                self._score_str = 'deuce'
            else:
                self._score_str = points[self.first.points] + '-' + \
                    points[self.second.points]


class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0

    def point(self):
        self.points += 1


def victory_over(a, b):
    return a.points >= 4 and a.points > b.points + 1


def advantage_over(a, b):
    return a.points >= 4 and a.points == b.points + 1


def deuce(a, b):
    return a.points >= 3 and a.points == b.points

# Third pass. Trying something different this time, with the
# permutations call that may be overkill and leads to a logic
# that is probably as hard to parse as what I had in the second pass.
# I still feel like there should be a simpler way, but I can't find it.
