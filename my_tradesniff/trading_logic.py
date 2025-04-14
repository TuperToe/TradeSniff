from okx_api import get_live_price, get_historical_data
from indicators import calculate_indicators
from discord_notifier import send_discord_notification

last_signals = {}

def check_trade_signal(symbol, timeframe):
    """Analyzes market conditions and determines whether to buy or sell."""
    trade_price = get_live_price(symbol)
    candles = get_historical_data(symbol, timeframe, 50)
    
    if not trade_price or len(candles) < 50:
        return
    
    indicators = calculate_indicators(candles)
    
    if indicators["EMA9"] > indicators["EMA50"] and indicators["MACD"] > indicators["MACD_signal"] and indicators["RSI"] > 50:
        signal = "BUY"
        emoji = "🚀"
    elif indicators["EMA9"] < indicators["EMA50"] and indicators["MACD"] < indicators["MACD_signal"] and indicators["RSI"] < 50:
        signal = "SELL"
        emoji = "📉"
    else:
        return

    if last_signals.get(symbol) != signal:
        tp = trade_price + indicators["ATR"] * 2 if signal == "BUY" else trade_price - indicators["ATR"] * 2
        sl = trade_price - indicators["ATR"] * 1.5 if signal == "BUY" else trade_price + indicators["ATR"] * 1.5
        
        send_discord_notification(f"📢 **{signal} ALERT** {emoji}\nPair: {symbol}\nPrice: ${trade_price:.2f}\nTP: ${tp:.2f}\nSL: ${sl:.2f}")
        last_signals[symbol] = signal

