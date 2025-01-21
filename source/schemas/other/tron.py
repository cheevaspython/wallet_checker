from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True)
class TronAccountData:
    bandwidth: int
    energy: int
    balance: str | Decimal

    def __post_init__(self):
        if isinstance(self.balance, str):
            self.balance = Decimal(self.balance)
