from src.data_loader import MarketDataLoader
from src.portfolio import Portfolio
from src.risk_metrics import RiskMetrics
from src.strategies import MomentumStrategy
from src.scenario import apply_shock
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "SPY"]
loader = MarketDataLoader(tickers, "2020-01-01", "2024-01-01")
prices = loader.fetch_data()

portfolio = Portfolio(prices)
returns = portfolio.portfolio_returns()

risk = RiskMetrics(returns)

print("Volatility:", risk.volatility())
print("Sharpe Ratio:", risk.sharpe_ratio())
print("Max Drawdown:", risk.max_drawdown())
print("Historical VaR:", risk.historical_var())
print("Parametric VaR:", risk.parametric_var())

# Momentum Strategy
strategy = MomentumStrategy(prices)
strategy_returns = strategy.strategy_returns()

# Plot
plt.figure()
portfolio.cumulative_returns().plot(label="Portfolio")
((1 + strategy_returns).cumprod()).plot(label="Momentum Strategy")
plt.legend()
plt.show()
