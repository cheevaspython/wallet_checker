from typing import Protocol

from source.api.dependency.wallet.output_data import WalletListPaginated
from source.filters.pagination import Pagination


class WalletReader(Protocol):

    async def get_list(
        self,
        pagination: Pagination,
    ) -> WalletListPaginated:
        raise NotImplementedError
