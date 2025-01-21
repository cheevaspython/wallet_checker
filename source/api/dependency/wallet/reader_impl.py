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
        applications = []

        for row in rows:
            application = WalletResponseData(
                id=row.Wallet.id,
                address=row.Wallet.address,
                bandwidth=row.Wallet.bandwidth,
                energy=row.Wallet.energy,
                balance=row.Wallet.balance,
                created_date=row.Wallet.created_date,
            )
            applications.append(application)

        return WalletListPaginated(
            count=total_count,
            results=applications,
        )
