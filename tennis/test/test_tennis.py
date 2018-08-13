from tennis import Game


class TestGame():
    def setup(self):
        self.g = Game('Player A', 'Player B')

    def many_points(self, player, points):
        for point in range(points):
            self.g.point(player)

    def deuce(self):
        for point in range(3):
            self.g.point('Player A')
            self.g.point('Player B')

    def test_starting_score(self):
        assert self.g.score() == 'love all'
        assert self.g.winner() is None

    def test_point_for_first(self):
        self.g.point('Player A')

        assert self.g.score() == '15-love'
        assert self.g.winner() is None

    def test_two_points_for_first(self):
        self.many_points('Player A', 2)

        assert self.g.score() == '30-love'
        assert self.g.winner() is None

    def test_three_points_for_first(self):
        self.many_points('Player A', 3)

        assert self.g.score() == '40-love'
        assert self.g.winner() is None

    def test_four_points_for_first(self):
        self.many_points('Player A', 4)

        assert self.g.score() == 'Player A wins'
        assert self.g.winner() == 'Player A'

    def test_point_for_second(self):
        self.g.point('Player B')

        assert self.g.score() == 'love-15'
        assert self.g.winner() is None

    def test_both_players_have_points(self):
        self.many_points('Player B', 2)
        self.g.point('Player A')

        assert self.g.score() == '15-30'
        assert self.g.winner() is None

    def test_second_player_wins(self):
        self.many_points('Player A', 2)
        self.many_points('Player B', 4)

        assert self.g.score() == 'Player B wins'
        assert self.g.winner() == 'Player B'

    def test_extra_points_do_not_break_game(self):
        self.many_points('Player A', 2)
        self.many_points('Player B', 6)

        assert self.g.score() == 'Player B wins'
        assert self.g.winner() == 'Player B'

    def test_deuce(self):
        self.deuce()

        assert self.g.score() == 'deuce'
        assert self.g.winner() is None

    def test_advantage_first(self):
        self.deuce()
        self.g.point('Player A')

        assert self.g.score() == 'advantage Player A'
        assert self.g.winner() is None

    def test_advantage_second(self):
        self.deuce()
        self.g.point('Player B')

        assert self.g.score() == 'advantage Player B'
        assert self.g.winner() is None

    def test_deuce_after_advantage(self):
        self.deuce()
        self.g.point('Player B')
        self.g.point('Player A')

        assert self.g.score() == 'deuce'
        assert self.g.winner() is None

    def test_advantage_sequence(self):
        self.deuce()
        self.g.point('Player B')
        self.g.point('Player A')
        self.g.point('Player A')

        assert self.g.score() == 'advantage Player A'
        assert self.g.winner() is None

    def test_victory_after_advantage(self):
        self.deuce()
        self.g.point('Player B')
        self.g.point('Player A')
        self.g.point('Player B')
        self.g.point('Player B')

        assert self.g.score() == 'Player B wins'
        assert self.g.winner() == 'Player B'
