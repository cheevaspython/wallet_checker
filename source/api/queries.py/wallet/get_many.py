from dataclasses import dataclass

from source.api.dependency.wallet.output_data import WalletListPaginated
from source.api.dependency.wallet.reader import WalletReader
from source.filters.pagination import Pagination


@dataclass(slots=True, frozen=True)
class GetApplications:
    application_reader: WalletReader

    async def __call__(
        self,
        pagination: Pagination,
    ) -> WalletListPaginated:

        wallets = await self.application_reader.get_list(
            pagination=pagination,
        )
        return wallets
