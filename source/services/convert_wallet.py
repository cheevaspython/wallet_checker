from source.api.dependency.wallet.output_data import (
    WalletResponseData,
)
from source.db.models.wallet import Wallet


def convert_wallet_to_output(
    wallet: Wallet,
) -> WalletResponseData:
    return WalletResponseData(
        id=wallet.id,
        address=wallet.address,
        bandwidth=wallet.bandwidth,
        energy=wallet.energy,
        balance=wallet.balance,
        created_date=wallet.created_date,
    )
