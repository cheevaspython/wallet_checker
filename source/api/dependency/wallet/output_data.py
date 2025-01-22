from collections.abc import Sequence
from datetime import datetime
from dataclasses import dataclass
from decimal import Decimal

from source.types.model_id import ModelIdType


@dataclass(slots=True)
class WalletResponseData:
    id: ModelIdType
    address: str
    free_bandwidth: str
    total_bandwidth: str
    total_energy: str
    balance: Decimal
    created_date: datetime | str

    def __post_init__(self):
        if isinstance(self.created_date, datetime):
            self.created_date = self.created_date.strftime("%m/%d/%Y, %H:%M:%S")


@dataclass(slots=True, frozen=True)
class WalletListPaginated:
    count: int
    results: Sequence[WalletResponseData]
