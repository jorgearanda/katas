score_map = {
    0: 'love',
    1: '15',
    2: '30',
    3: '40'
}


class Game():
    def __init__(self, first_player, second_player):
        self.first = Player(first_player)
        self.second = Player(second_player)
        self._score_str = 'love all'
        self._winner = None

    def point(self, player):
        if self._is_over():
            return
        if player == self.first.name:
            self.first.points += 1
        else:
            self.second.points += 1

        self._update_score()

    def score(self):
        return self._score_str

    def winner(self):
        return self._winner

    def _update_score(self):
        if self._is_over():
            if self._is_first_player_winner():
                self._winner = self.first.name
            else:
                self._winner = self.second.name
            self._score_str = self._winner + ' wins'
        elif self.first.points >= 3 and \
                self.first.points == self.second.points:
            self._score_str = 'deuce'
        elif self.first.points > 3 and \
                self.first.points > self.second.points:
            self._score_str = 'advantage ' + self.first.name
        elif self.second.points > 3 and self.second.points > self.first.points:
            self._score_str = 'advantage ' + self.second.name
        else:
            self._score_str = score_map[self.first.points] + '-' + \
                score_map[self.second.points]

    def _is_over(self):
        return self._is_first_player_winner() or \
            self._is_second_player_winner()

    def _is_first_player_winner(self):
        return self.first.points >= 4 and \
            self.first.points - self.second.points > 1

    def _is_second_player_winner(self):
        return self.second.points >= 4 and \
            self.second.points - self.first.points > 1


class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0

# First full pass. I'm not happy with this code!
# I think part of the problem is that I had to come up with the Kata
# definition as I went along. I'm hopeful the next iterations
# will simplify things.
