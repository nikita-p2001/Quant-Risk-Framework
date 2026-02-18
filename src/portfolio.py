import numpy as np

class Portfolio:
    def __init__(self, prices, weights=None):
        self.prices = prices
        self.returns = prices.pct_change().dropna()

        if weights is None:
            self.weights = np.ones(len(prices.columns)) / len(prices.columns)
        else:
            self.weights = np.array(weights)

    def portfolio_returns(self):
        return (self.returns * self.weights).sum(axis=1)

    def cumulative_returns(self):
        return (1 + self.portfolio_returns()).cumprod()
