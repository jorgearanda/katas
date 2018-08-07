class ExponentialMovingAverage():
    def __init__(self, alpha=0.5):
        self.ema = None
        self.alpha = alpha

    def put(self, input):
        if type(input) == int:
            input = [input]

        for i in input:
            if self.ema is None:
                self.ema = i

            self.ema = (i * self.alpha) + (self.ema * (1 - self.alpha))

    def get(self):
        return self.ema
