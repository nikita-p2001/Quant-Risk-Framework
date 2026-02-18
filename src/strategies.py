import pandas as pd

class MomentumStrategy:
    def __init__(self, prices, window=50):
        self.prices = prices
        self.window = window

    def generate_signals(self):
        rolling_mean = self.prices.rolling(self.window).mean()
        signals = self.prices > rolling_mean
        return signals.astype(int)

    def strategy_returns(self):
        signals = self.generate_signals()
        returns = self.prices.pct_change().dropna()
        return (signals.shift(1) * returns).mean(axis=1)
