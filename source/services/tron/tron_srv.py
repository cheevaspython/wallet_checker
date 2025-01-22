from tronpy import Tron

from source.config.settings import settings
from source.errors.tron import TronBalanceParseError, TronResourcesParseError
from source.schemas.other.tron import TronAccountData, TronResourceData


class TronServiceImpl:

    async def get_account_data(
        self,
        address: str,
    ) -> TronAccountData:
        client = Tron(network=settings.tron.network)
        try:
            balance = client.get_account_balance(address)
        except Exception as e:
            raise TronBalanceParseError(
                address=address,
                error=str(e),
            )
        return TronAccountData(
            balance=balance,
            resources_data=await self._get_resources_data(
                address=address,
                client=client,
            ),
        )

    async def _get_resources_data(
        self,
        address: str,
        client: Tron,
    ) -> TronResourceData:
        try:
            resources = client.get_account_resource(address)
            free_bandwidth = resources.get("freeNetLimit", 0)
            total_bandwidth = resources.get("TotalNetLimit", 0)
            total_energy = resources.get("TotalEnergyLimit", 0)
            return TronResourceData(
                free_bandwidth=str(free_bandwidth),
                total_bandwidth=str(total_bandwidth),
                total_energy=str(total_energy),
            )
        except Exception as e:
            raise TronResourcesParseError(
                address=address,
                error=str(e),
            )
