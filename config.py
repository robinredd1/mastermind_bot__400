
# ====== config.py ======
# Alpaca PAPER trading credentials (provided by user)
API_KEY = "PKXB8N50RX1YLX2N39AE"
API_SECRET = "3IGZrOtdWnuOCNGOVAYfGTCaccZh7h0tPDmNvFHq"

# Trade + scan settings
SCAN_INTERVAL_SECONDS = 5            # how often to scan
SCAN_BATCH_SIZE = 400                # scan 400 tickers per batch
UNIVERSE_FILE = "symbols_400.txt"    # list of symbols to rotate through

# Signal thresholds (loosened to catch more)
MIN_PCT_UP_FROM_PREV_CLOSE = 0.2     # % up vs previous close
MIN_MINUTE_VOLUME = 0                # no volume restriction
MIN_PRICE = 0.1                       # min price (basically none)
MAX_PRICE = 100000.0                  # max price (none)

# Risk / position sizing
DOLLARS_PER_TRADE = 75               # fixed dollars per entry
MAX_OPEN_POSITIONS = 5               # allow multiple positions

# Order params
USE_EXTENDED_HOURS = True            # allow pre/after market for limit orders
LIMIT_SLIPPAGE_BPS = 15               # limit buy at last trade * (1 + 0.0015) for momentum entries

# Exit: trailing stop once filled
TRAIL_PERCENT = 3.0                   # trailing stop %
BROKER_BASE_URL = "https://paper-api.alpaca.markets"
DATA_BASE_URL = "https://data.alpaca.markets"
