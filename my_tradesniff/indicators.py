 
import pandas as pd
import ta  # `ta` library for indicators

def calculate_indicators(candles):
    """Calculates EMA, MACD, RSI, and ATR for historical data."""
    df = pd.DataFrame(candles)
    
    df["EMA9"] = ta.trend.ema_indicator(df["close"], window=9)
    df["EMA50"] = ta.trend.ema_indicator(df["close"], window=50)
    
    macd = ta.trend.MACD(df["close"])
    df["MACD"] = macd.macd()
    df["MACD_signal"] = macd.macd_signal()
    
    df["RSI"] = ta.momentum.rsi(df["close"], window=14)
    df["ATR"] = ta.volatility.average_true_range(df["high"], df["low"], df["close"], window=14)
    
    return df.iloc[-1]  # Return the latest row of indicators
