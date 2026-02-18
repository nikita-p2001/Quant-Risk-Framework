import numpy as np
from scipy.stats import norm

class RiskMetrics:
    def __init__(self, returns):
        self.returns = returns

    def volatility(self):
        return self.returns.std() * np.sqrt(252)

    def sharpe_ratio(self, risk_free_rate=0.02):
        excess_returns = self.returns - risk_free_rate/252
        return np.sqrt(252) * excess_returns.mean() / excess_returns.std()

    def max_drawdown(self):
        cumulative = (1 + self.returns).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        return drawdown.min()

    def historical_var(self, confidence=0.95):
       if len(self.returns) == 0:
         return None
       return np.percentile(self.returns, (1 - confidence) * 100)


    def parametric_var(self, confidence=0.95):
        mean = self.returns.mean()
        std = self.returns.std()
        return norm.ppf(1 - confidence, mean, std)
