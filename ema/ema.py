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


# Second pass. Separating the input processing and the calculation
# makes for a cleaner structure.
#
# It also allows for an alternative approach: `put` could keep a list of
# values so far, and _calc could use a subset for them for the calculation.
#
# This would allow, for instance, an EMA of only the last ten values.
