from source.api.interactors.wallet.input_data import CreateWalletInputData
from source.api.dependency.wallet.gateway import WalletGateway
from source.common.commiter import Commiter
from source.common.error import ApplicationError
from source.db.models.wallet import Wallet


class CreateWalletInteractor:

    def __init__(
        self,
        wallet_gateway: WalletGateway,
        commiter: Commiter,
    ):
        self._wallet_gateway = wallet_gateway
        self._commiter = commiter

    async def __call__(
        self,
        create_data: CreateWalletInputData,
    ) -> Wallet:
        try:
            wallet = await self._wallet_gateway.save(
                Wallet(
                    address=create_data.address,
                    bandwidth=create_data.bandwidth,
                    energy=create_data.energy,
                    balance=create_data.balance,
                ),
            )
            await self._commiter.commit()
            return wallet

        except ApplicationError as e:
            raise e
