from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from source.db.models.wallet import Wallet
from source.errors.wallet import CannotSaveWalletError
from source.types.model_id import ModelIdType


class WalletGatewayImpl:

    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def save(
        self,
        wallet: Wallet,
    ) -> Wallet:
        try:
            self._session.add(wallet)
            await self._session.flush()
            return wallet
        except IntegrityError:
            raise CannotSaveWalletError()

    async def by_id(
        self,
        wallet_id: ModelIdType,
    ) -> Wallet | None:
        query = select(Wallet).where(
            Wallet.id == wallet_id,
        )
        result = await self._session.execute(query)
        return result.scalar_one_or_none()
