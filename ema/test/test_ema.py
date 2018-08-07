from pytest import approx

from ema import ExponentialMovingAverage


class TestEMADefaultAlpha():
    def setup(self):
        self.ema = ExponentialMovingAverage()

    def test_no_input(self):
        assert self.ema.get() is None

    def test_one_zero(self):
        self.ema.put(0)

        assert self.ema.get() == 0

    def test_one_one(self):
        self.ema.put(1)

        assert self.ema.get() == 1

    def test_three_values(self):
        self.ema.put(1)
        self.ema.put(2)
        self.ema.put(3)

        assert self.ema.get() == 2.25

    def test_three_values_list(self):
        self.ema.put([1, 2, 3])

        assert self.ema.get() == 2.25

    def test_ten_values_list(self):
        self.ema.put([-1, -1, -1, -1, -1, -1, -1, -1, -1, 1])

        assert self.ema.get() == 0.0

    def test_get_halfway(self):
        self.ema.put([-1, -1, -1, -1, -1])
        assert self.ema.get() == -1.0

        self.ema.put([-1, -1, -1, -1, 1])
        assert self.ema.get() == 0.0


class TestEMALowAlpha():
    def setup(self):
        self.ema = ExponentialMovingAverage(alpha=0.2)

    def test_no_input(self):
        assert self.ema.get() is None

    def test_one_zero(self):
        self.ema.put(0)

        assert self.ema.get() == 0

    def test_one_one(self):
        self.ema.put(1)

        assert self.ema.get() == 1

    def test_three_values(self):
        self.ema.put(1)
        self.ema.put(2)
        self.ema.put(3)

        assert self.ema.get() == approx(1.56)

    def test_ten_values(self):
        self.ema.put([-1, -1, -1, -1, -1, -1, -1, -1, -1, 1])

        assert self.ema.get() == approx(-0.6)
