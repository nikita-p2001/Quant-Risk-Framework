# Quantitative Strategy & Risk Analytics Framework

An interactive Python-based framework for portfolio construction, risk measurement, and systematic strategy evaluation.

This project explores how systematic trading systems evaluate performance and manage risk using time-series financial data.

Live Demo: https://quant-risk-framework.streamlit.app  
Source Code: https://github.com/nikita-p2001/Quant-Risk-Framework  


## Overview

This framework provides:

- Market data ingestion via Yahoo Finance
- Portfolio return aggregation
- Rolling risk metrics computation
- Strategy backtesting (momentum-based)
- Scenario simulation
- Interactive dashboard deployment using Streamlit

The system is structured with modular separation between data, strategy, and risk layers.


## Implemented Risk Metrics

- Annualized Volatility  
- Sharpe Ratio  
- Maximum Drawdown  
- Historical Value-at-Risk (VaR)  
- Parametric Value-at-Risk (Normal distribution assumption)  


## Strategy Module

- Rolling-window momentum strategy  
- Lookahead bias prevention using signal shifting  
- Cumulative performance comparison vs baseline portfolio  




## Design principles:

- Vectorized computation using NumPy and Pandas  
- Modular class-based design  
- Defensive handling of missing data  
- Production-style execution entry points  


## Tech Stack

- Python  
- Pandas  
- NumPy  
- SciPy  
- Matplotlib  
- Streamlit  
- yfinance  


## How to Run Locally

1. Clone repository  
2. Create virtual environment  
3. Install dependencies:

pip install -r requirements.txt

4. Run Streamlit app:

streamlit run app.py


## Future Enhancements

- Transaction cost modeling  
- Rolling beta estimation  
- Multi-asset risk attribution  
- Portfolio rebalancing logic  
- Extension to fixed income instruments  
