from tennis import Game


class TestGame():
    def setup(self):
        self.g = Game('Player A', 'Player B')

    def many_points(self, player, points):
        for point in range(points):
            self.g.point(player)

    def test_starting_score(self):
        assert self.g.score() == 'love all'

    def test_point_for_first(self):
        self.g.point('Player A')

        assert self.g.score() == '15-love'

    def test_two_points_for_first(self):
        self.many_points('Player A', 2)

        assert self.g.score() == '30-love'

    def test_three_points_for_first(self):
        self.many_points('Player A', 3)

        assert self.g.score() == '40-love'

    def test_four_points_for_first(self):
        self.many_points('Player A', 4)

        assert self.g.score() == 'Player A wins'

    def test_point_for_second(self):
        self.g.point('Player B')

        assert self.g.score() == 'love-15'

    def test_both_players_have_points(self):
        self.many_points('Player B', 2)
        self.g.point('Player A')

        assert self.g.score() == '15-30'

    def test_second_player_wins(self):
        self.many_points('Player A', 2)
        self.many_points('Player B', 4)

        assert self.g.score() == 'Player B wins'

    def test_deuce(self):
        self.many_points('Player A', 3)
        self.many_points('Player B', 3)

        assert self.g.score() == 'deuce'
