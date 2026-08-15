"""技术指标计算"""
import numpy as np

def sma(data, period):
    """简单移动平均"""
    result = np.full_like(data, np.nan, dtype=float)
    if len(data) < period:
        return result
    cumsum = np.cumsum(data, dtype=float)
    result[period-1:] = (cumsum[period-1:] - np.concatenate([[0], cumsum[:-period]])) / period
    return result

def ema(data, period):
    """指数移动平均"""
    result = np.full_like(data, np.nan, dtype=float)
    if len(data) < period:
        return result
    alpha = 2 / (period + 1)
    result[period-1] = np.mean(data[:period])
    for i in range(period, len(data)):
        result[i] = alpha * data[i] + (1 - alpha) * result[i-1]
    return result

def atr(high, low, close, period=14):
    """平均真实波幅"""
    n = len(close)
    tr = np.zeros(n)
    tr[0] = high[0] - low[0]
    for i in range(1, n):
        tr[i] = max(
            high[i] - low[i],
            abs(high[i] - close[i-1]),
            abs(low[i] - close[i-1])
        )
    return sma(tr, period)

def rsi(close, period=14):
    """相对强弱指数"""
    n = len(close)
    result = np.full(n, np.nan)
    if n < period + 1:
        return result
    deltas = np.diff(close)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)
    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])
    result[period] = 100 - (100 / (1 + avg_gain / avg_loss)) if avg_loss > 0 else 100
    for i in range(period + 1, n):
        avg_gain = (avg_gain * (period - 1) + gains[i-1]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i-1]) / period
        result[i] = 100 - (100 / (1 + avg_gain / avg_loss)) if avg_loss > 0 else 100
    return result

def macd(close, fast=12, slow=26, signal=9):
    """MACD指标"""
    ema_fast = ema(close, fast)
    ema_slow = ema(close, slow)
    macd_line = ema_fast - ema_slow
    signal_line = ema(np.where(np.isnan(macd_line), 0, macd_line), signal)
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram

def bollinger_bands(close, period=20, std_dev=2):
    """布林带"""
    middle = sma(close, period)
    upper = np.full_like(close, np.nan)
    lower = np.full_like(close, np.nan)
    for i in range(period - 1, len(close)):
        std = np.std(close[i-period+1:i+1])
        upper[i] = middle[i] + std_dev * std
        lower[i] = middle[i] - std_dev * std
    return upper, middle, lower
