from sqlalchemy import Result, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from source.api.dependency.wallet.output_data import (
    WalletListPaginated,
    WalletResponseData,
)
from source.db.models.wallet import Wallet
from source.filters.pagination import Pagination


class WalletReaderImpl:

    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def get_list(
        self,
        pagination: Pagination,
    ) -> WalletListPaginated:

        query = select(
            Wallet,
            func.count().over().label("total_count"),
        ).order_by(desc(Wallet.id))

        if pagination.offset is not None:
            query = query.offset(pagination.offset)

        if pagination.limit is not None:
            query = query.limit(pagination.limit)

        result = await self._session.execute(query)
        return self._load_model_data(result=result)

    def _load_model_data(self, result: Result) -> WalletListPaginated:
        rows = result.all()
        total_count = rows[0].total_count if rows else 0
        wallets = []

        for row in rows:
            wallet = WalletResponseData(
                id=row.Wallet.id,
                address=row.Wallet.address,
                balance=row.Wallet.balance,
                free_bandwidth=row.Wallet.free_bandwidth,
                total_bandwidth=row.Wallet.total_bandwidth,
                total_energy=row.Wallet.total_energy,
                created_date=row.Wallet.created_date,
            )
            wallets.append(wallet)

        return WalletListPaginated(
            count=total_count,
            results=wallets,
        )
