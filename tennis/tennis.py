points = ['love', '15', '30', '40']


class Game():
    def __init__(self, first_player, second_player):
        self.first = Player(first_player)
        self.second = Player(second_player)
        self._score_str = 'love all'
        self._winner = None

    def point(self, player_name):
        if player_name == self.first.name:
            self.first.point()
        else:
            self.second.point()

        self.update_score()

    def score(self):
        return self._score_str

    def winner(self):
        return self._winner

    def update_score(self):
        if victory_over(self.first, self.second):
            self._score_str = self.first.name + ' wins'
            self._winner = self.first.name
        elif victory_over(self.second, self.first):
            self._score_str = self.second.name + ' wins'
            self._winner = self.second.name
        elif advantage_over(self.first, self.second):
            self._score_str = 'advantage ' + self.first.name
        elif advantage_over(self.second, self.first):
            self._score_str = 'advantage ' + self.second.name
        elif deuce(self.first, self.second):
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

# Second pass. Cleaner than the first, but the big if/elif/else
# method on update_score still rubs me the wrong way.
