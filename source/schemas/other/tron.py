from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True, frozen=True)
class TronResourceData:
    free_bandwidth: str
    total_bandwidth: str
    total_energy: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass(slots=True)
class TronAccountData:
    balance: str | Decimal
    resources_data: TronResourceData

    def __post_init__(self):
        if isinstance(self.balance, str):
            self.balance = Decimal(self.balance)
