import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import MarketDataLoader
from src.portfolio import Portfolio
from src.risk_metrics import RiskMetrics
from src.strategies import MomentumStrategy

st.title("Quantitative Strategy & Risk Analytics Framework")

tickers = st.text_input("Enter Tickers (comma separated)", "AAPL,MSFT,SPY")
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2024-01-01"))

if st.button("Run Analysis"):

    tickers_list = [t.strip() for t in tickers.split(",")]

    loader = MarketDataLoader(tickers_list, str(start_date), str(end_date))
    prices = loader.fetch_data()

    portfolio = Portfolio(prices)
    returns = portfolio.portfolio_returns()

    risk = RiskMetrics(returns)

    st.subheader("Risk Metrics")
    st.write("Volatility:", risk.volatility())
    st.write("Sharpe Ratio:", risk.sharpe_ratio())
    st.write("Max Drawdown:", risk.max_drawdown())
    st.write("Historical VaR:", risk.historical_var())
    st.write("Parametric VaR:", risk.parametric_var())

    strategy = MomentumStrategy(prices)
    strategy_returns = strategy.strategy_returns()

    fig, ax = plt.subplots()
    portfolio.cumulative_returns().plot(ax=ax, label="Portfolio")
    ((1 + strategy_returns).cumprod()).plot(ax=ax, label="Momentum Strategy")
    plt.legend()

    st.pyplot(fig)
