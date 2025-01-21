from typing import Protocol

from source.filters.pagination import Pagination


class WalletReader(Protocol):

    async def get_list(
        self,
        pagination: Pagination,
    ):
        raise NotImplementedError
