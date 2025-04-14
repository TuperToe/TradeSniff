import time
from trading_logic import check_trade_signal
from config import PAIRS, CHECK_INTERVAL

def monitor_market():
    """Runs the market monitoring loop."""
    while True:
        for pair in PAIRS:
            check_trade_signal(pair["symbol"], pair["timeframe"])
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("🚀 Market monitoring started...")
    monitor_market()
 
