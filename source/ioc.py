from typing import AsyncIterable

from dishka import Provider, Scope, make_async_container, from_context, provide
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from source.api.dependency.wallet.gateway import WalletGateway
from source.api.dependency.wallet.gateway_impl import WalletGatewayImpl
from source.api.dependency.wallet.reader import WalletReader
from source.api.dependency.wallet.reader_impl import WalletReaderImpl
from source.api.interactors.wallet.create import CreateWalletInteractor
from source.api.interactors.wallet.get import GetWalletInteractor
from source.api.queries.wallet.get_many import GetWallets
from source.common.commiter import Commiter
from source.db.db_helper import db_helper
from source.db.sa_commiter import SACommiter
from source.config.settings import Settings, settings
from source.services.tron.common import TronService
from source.services.tron.tron_srv import TronServiceImpl


class AppProvider(Provider):
    config = from_context(provides=Settings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def provide_session_maker(self) -> async_sessionmaker[AsyncSession]:
        return db_helper.session_factory

    @provide(scope=Scope.REQUEST)
    async def provide_session(
        self,
        session_maker: async_sessionmaker[AsyncSession],
    ) -> AsyncIterable[AsyncSession,]:
        async with session_maker() as session:
            yield session

    wallet_gateway = provide(
        WalletGatewayImpl,
        scope=Scope.REQUEST,
        provides=WalletGateway,
    )
    wallet_reader = provide(
        WalletReaderImpl,
        scope=Scope.REQUEST,
        provides=WalletReader,
    )
    tron_service = provide(
        TronServiceImpl,
        scope=Scope.REQUEST,
        provides=TronService,
    )
    get_wallets_query = provide(
        GetWallets,
        scope=Scope.REQUEST,
    )
    get_wallets_interactor = provide(
        GetWalletInteractor,
        scope=Scope.REQUEST,
    )
    create_wallets_interactor = provide(
        CreateWalletInteractor,
        scope=Scope.REQUEST,
    )
    sa_commiter = provide(
        SACommiter,
        scope=Scope.REQUEST,
        provides=Commiter,
    )


def setup_fastapi_container():
    return make_async_container(
        AppProvider(),
        context={Settings: settings},
    )
