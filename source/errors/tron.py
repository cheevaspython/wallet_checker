from dataclasses import dataclass

from source.common.error import ApplicationError
from source.services.logging import logger


@dataclass(eq=False)
class BandwidthGetError(ApplicationError):
    address: str

    @property
    def message(self):
        text = f"Cannot get bandwidth from address: {self.address}."
        logger.warning(text)
        return text


@dataclass(eq=False)
class EnergyGetError(ApplicationError):
    address: str

    @property
    def message(self):
        text = f"Cannot get energy from address: {self.address}."
        logger.warning(text)
        return text
