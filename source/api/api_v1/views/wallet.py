from typing import Annotated
from fastapi import APIRouter, Form, HTTPException, status

from dishka.integrations.fastapi import DishkaRoute, inject, FromDishka

from source.api.dependency.wallet.output_data import (
    WalletListPaginated,
    WalletResponseData,
)
from source.api.interactors.wallet.create import CreateWalletInteractor
from source.api.interactors.wallet.get import GetWalletInteractor
from source.api.queries.wallet.get_many import GetWallets
from source.common.error import ApplicationError
from source.filters.pagination import Pagination
from source.schemas.pydantic.wallet import WalletAddress
from source.services.convert_wallet import convert_wallet_to_output
from source.types.model_id import ModelIdType

router = APIRouter(
    tags=["Wallet"],
    prefix="/wallet",
    route_class=DishkaRoute,
)


@router.get(
    "/{wallet_id}/",
    response_model=WalletResponseData,
)
@inject
async def get_wallet(
    wallet_id: ModelIdType,
    interactor: FromDishka[GetWalletInteractor],
):
    try:
        wallet = await interactor.by_id(wallet_id=wallet_id)
        return convert_wallet_to_output(wallet)

    except ApplicationError as e:
        raise HTTPException(
            status_code=404,
            detail={"message": e.message},
        )


@router.get(
    "/",
    response_model=WalletListPaginated,
)
@inject
async def get_wallets(
    query: FromDishka[GetWallets],
    offset: int | None = None,
    limit: int | None = None,
):
    try:
        pagination = Pagination(offset=offset, limit=limit)
        wallets = await query(
            pagination=pagination,
        )
        return wallets
    except ApplicationError as e:
        raise HTTPException(
            status_code=400,
            detail={"message": e.message},
        )


@router.post(
    "/",
    response_model=WalletResponseData,
    status_code=status.HTTP_201_CREATED,
)
@inject
async def create_wallet(
    wallet_address: Annotated[WalletAddress, Form()],
    interactor: FromDishka[CreateWalletInteractor],
):
    try:
        application = await interactor(
            address=wallet_address.value,
        )
        return convert_wallet_to_output(application)

    except ApplicationError as e:
        raise HTTPException(
            status_code=400,
            detail={"message": e.message},
        )
