from typing import Protocol

from source.db.models.wallet import Wallet
from source.types.model_id import ModelIdType


class WalletGateway(Protocol):

    async def save(
        self,
        wallet: Wallet,
    ) -> Wallet:
        raise NotImplementedError

    async def by_id(
        self,
        wallet_id: ModelIdType,
    ) -> Wallet | None:
        raise NotImplementedError
