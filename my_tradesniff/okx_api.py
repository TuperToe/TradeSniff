import requests
BASE_URL = "https://www.okx.com/api/v5/market"

def get_live_price(symbol):
    """Fetches the latest price for a given trading pair."""
    try:
        response = requests.get(f"{BASE_URL}/ticker?instId={symbol}")
        return float(response.json()["data"][0]["last"])
    except Exception as e:
        print(f"Error fetching price for {symbol}: {e}")
        return None

def get_historical_data(symbol, timeframe, limit=50):
    """Fetches historical OHLCV data."""
    try:
        response = requests.get(f"{BASE_URL}/candles?instId={symbol}&bar={timeframe}&limit={limit}")
        data = response.json()["data"]
        return [{
            "timestamp": int(candle[0]), "open": float(candle[1]), "high": float(candle[2]),
            "low": float(candle[3]), "close": float(candle[4]), "volume": float(candle[5])
        } for candle in data]
    except Exception as e:
        print(f"Error fetching historical data for {symbol}: {e}")
        return [] 
