from typing import Protocol

from source.schemas.other.tron import TronAccountData


class TronService(Protocol):

    async def get_account_data(
        self,
        address: str,
    ) -> TronAccountData:
        raise NotImplementedError
