from source.api.dependency.wallet.gateway import WalletGateway
from source.db.models.wallet import Wallet
from source.errors.does_not_exists import CustomDoesNotExist
from source.types.model_id import ModelIdType


class GetWalletInteractor:

    def __init__(
        self,
        wallet_gateway: WalletGateway,
    ):
        self._wallet_gateway = wallet_gateway

    async def by_id(
        self,
        wallet_id: ModelIdType,
    ) -> Wallet:
        wallet = await self._wallet_gateway.by_id(wallet_id=wallet_id)
        if not wallet:
            raise CustomDoesNotExist(
                model_id=wallet_id,
                class_name="Wallet",
            )
        return wallet
