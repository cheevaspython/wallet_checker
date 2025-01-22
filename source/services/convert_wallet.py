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
        balance=wallet.balance,
        free_bandwidth=wallet.free_bandwidth,
        total_bandwidth=wallet.total_bandwidth,
        total_energy=wallet.total_energy,
        created_date=wallet.created_date,
    )
