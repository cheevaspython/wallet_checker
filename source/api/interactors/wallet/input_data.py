from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True, frozen=True)
class CreateWalletInputData:
    address: str
    free_bandwidth: str
    total_bandwidth: str
    total_energy: str
    balance: Decimal
