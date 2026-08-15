"""CryptoPulse 配置"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# OKX API 配置
OKX_API_KEY = os.environ.get("OKX_API_KEY", "")
OKX_SECRET_KEY = os.environ.get("OKX_SECRET_KEY", "")
OKX_PASSPHRASE = os.environ.get("OKX_PASSPHRASE", "")
OKX_USE_DEMO = os.environ.get("OKX_USE_DEMO", "true").lower() == "true"

# 交易配置
DEFAULT_STYLE = os.environ.get("DEFAULT_STYLE", "short_term")
DEFAULT_SYMBOL = os.environ.get("DEFAULT_SYMBOL", "BTC-USDT-SWAP")
RISK_PER_TRADE = float(os.environ.get("RISK_PER_TRADE", "0.02"))
MAX_POSITION_PCT = float(os.environ.get("MAX_POSITION_PCT", "0.5"))

# 日志
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_FILE = os.environ.get("LOG_FILE", str(DATA_DIR / "cryptopulse.log"))
