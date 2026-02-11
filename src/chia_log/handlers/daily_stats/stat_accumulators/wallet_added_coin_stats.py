# std
from datetime import datetime

# project
from .. import WalletAddedCoinMessage, WalletAddedCoinConsumer, StatAccumulator


class WalletAddedCoinStats(WalletAddedCoinConsumer, StatAccumulator):
    def __init__(self):
        self._last_reset_time = datetime.now()
        self._total_added_mojos = 0
        self._total_spent_mojos = 0

    def reset(self):
        self._last_reset_time = datetime.now()
        self._total_added_mojos = 0
        self._total_spent_mojos = 0

    def consume(self, obj: WalletAddedCoinMessage):
        if obj.is_spent:
            self._total_spent_mojos += obj.amount_mojos
        else:
            self._total_added_mojos += obj.amount_mojos

    def get_summary(self) -> str:
        received_xch = self._total_added_mojos / 1e12
        received_str = f"{received_xch:.12f}".rstrip("0").rstrip(".")
        spent_xch = self._total_spent_mojos / 1e12
        spent_str = f"{spent_xch:.12f}".rstrip("0").rstrip(".")
        return f"Received ☘️: {received_str} XCH\nSpent: {spent_str} XCH"
