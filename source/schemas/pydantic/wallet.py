from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from source.types.model_id import ModelIdType


class WalletBase(BaseModel):
    address: str
    free_bandwidth: str
    total_bandwidth: str
    total_energy: str
    balance: Decimal


class WalletCreate(WalletBase):
    pass


class WalletScheme(WalletBase):
    model_config = ConfigDict(from_attributes=True)

    id: ModelIdType
