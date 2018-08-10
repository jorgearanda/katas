class ExponentialMovingAverage():
    def __init__(self, alpha=0.5):
        self.alpha = alpha
        self.ema = None

    def get(self):
        return self.ema

    def put(self, input):
        if type(input) is int:
            input = [input]

        for value in input:
            self._calc(value)

    def _calc(self, value):
        if self.ema is None:
            self.ema = value
        else:
            self.ema = value * self.alpha + self.ema * (1.0 - self.alpha)


# Third pass. The result was identical to the second.
