from tronpy import Tron

from source.errors.tron import BandwidthGetError, EnergyGetError
from source.schemas.other.tron import TronAccountData


class TronServiceImpl:

    async def get_account_data(
        self,
        address: str,
    ) -> TronAccountData:
        client = Tron()
        balance = client.get_account_balance(address)
        bandwidth, energy = await self._get_resources_data(
            address=address,
            client=client,
        )
        return TronAccountData(
            balance=balance,
            bandwidth=bandwidth,
            energy=energy,
        )

    async def _get_resources_data(
        self,
        address: str,
        client: Tron,
    ) -> tuple[int, int]:
        resources = client.get_account_resource(address)
        bandwidth = resources.get("free_bandwidth", None)
        energy = resources.get("energy", None)
        if not bandwidth:
            raise BandwidthGetError(address=address)
        if not energy:
            raise EnergyGetError(address=address)
        return bandwidth, energy
