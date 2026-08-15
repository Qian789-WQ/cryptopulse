"""风险管理"""
import threading

class RiskManager:
    """风险管理单例"""
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.consecutive_losses = {"long": 0, "short": 0}
        self.cooldown_until = {"long": 0, "short": 0}
        self.daily_pnl = 0
        self.daily_loss_limit = -100  # 单日亏损上限USDT

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def can_trade(self, direction, current_time=0):
        """检查是否可以交易"""
        if self.consecutive_losses.get(direction, 0) >= 3:
            return False, "连续亏损3次，暂停该方向"
        if current_time < self.cooldown_until.get(direction, 0):
            return False, "止损冷却中"
        if self.daily_pnl <= self.daily_loss_limit:
            return False, "已达单日亏损上限"
        return True, ""

    def record_trade(self, direction, pnl):
        """记录交易结果"""
        if pnl < 0:
            self.consecutive_losses[direction] = self.consecutive_losses.get(direction, 0) + 1
        else:
            self.consecutive_losses[direction] = 0
        self.daily_pnl += pnl

    def set_cooldown(self, direction, until_ts):
        """设置冷却时间"""
        self.cooldown_until[direction] = until_ts

    def reset_daily(self):
        """重置每日统计"""
        self.daily_pnl = 0
        self.consecutive_losses = {"long": 0, "short": 0}

def get_risk_manager():
    """获取风险管理单例"""
    return RiskManager.get_instance()
