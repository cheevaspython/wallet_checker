from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class CreateWalletInputData:
    address: str
    bandwidth: int
    energy: int
    balance: Decimal
