from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from source.types.model_id import ModelIdType


class WalletBase(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance: Decimal


class WalletCreate(WalletBase):
    pass


class WalletScheme(WalletBase):
    model_config = ConfigDict(from_attributes=True)

    id: ModelIdType
