def apply_shock(returns, shock_percent):
    shocked = returns.copy()
    shocked.iloc[-1] += shock_percent
    return shocked
