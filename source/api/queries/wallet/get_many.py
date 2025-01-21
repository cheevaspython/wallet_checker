from dataclasses import dataclass

from source.api.dependency.wallet.output_data import WalletListPaginated
from source.api.dependency.wallet.reader import WalletReader
from source.filters.pagination import Pagination


@dataclass(slots=True, frozen=True)
class GetWallets:
    wallet_reader: WalletReader

    async def __call__(
        self,
        pagination: Pagination,
    ) -> WalletListPaginated:

        wallets = await self.wallet_reader.get_list(
            pagination=pagination,
        )
        return wallets
