from source.api.dependency.wallet.gateway import WalletGateway
from source.common.commiter import Commiter
from source.common.error import ApplicationError
from source.db.models.wallet import Wallet
from source.services.tron.common import TronService


class CreateWalletInteractor:

    def __init__(
        self,
        wallet_gateway: WalletGateway,
        tron_service: TronService,
        commiter: Commiter,
    ):
        self._wallet_gateway = wallet_gateway
        self._tron_service = tron_service
        self._commiter = commiter

    async def __call__(
        self,
        address: str,
    ) -> Wallet:
        try:
            account_data = await self._tron_service.get_account_data(
                address=address,
            )
            wallet = await self._wallet_gateway.save(
                Wallet(
                    address=address,
                    bandwidth=account_data.bandwidth,
                    energy=account_data.energy,
                    balance=account_data.balance,
                ),
            )
            await self._commiter.commit()
            return wallet

        except ApplicationError as e:
            raise e
