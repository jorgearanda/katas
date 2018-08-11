score_map = {
    0: 'love',
    1: '15',
    2: '30',
    3: '40',
    4: 'game'
}


class Game():
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player
        self.points = [0, 0]

    def point(self, player):
        if player == self.first_player:
            self.points[0] += 1
        else:
            self.points[1] += 1

    def score(self):
        _score = score_map[self.points[0]] + '-' + score_map[self.points[1]]
        if _score == 'love-love':
            _score = 'love all'
        elif _score == '40-40':
            _score = 'deuce'
        elif self.points[0] == 4:
            _score = self.first_player + ' wins'
        elif self.points[1] == 4:
            _score = self.second_player + ' wins'

        return _score
