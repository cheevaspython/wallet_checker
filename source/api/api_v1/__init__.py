from fastapi import APIRouter

from source.config.settings import settings
from source.api.api_v1.views.wallet import router as wallet_router


public_router = APIRouter(
    prefix=settings.api.v1.prefix,
)
public_router.include_router(router=wallet_router)
