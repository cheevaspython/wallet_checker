from dataclasses import dataclass

from source.common.error import ApplicationError
from source.services.logging import logger


@dataclass(eq=False)
class CannotSaveWalletError(ApplicationError):

    @property
    def message(self):
        text = "Cannot save wallet"
        logger.warning(text)
        return text
