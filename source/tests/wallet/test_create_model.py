from decimal import Decimal

import pytest
from unittest.mock import AsyncMock, MagicMock

from sqlalchemy.ext.asyncio import AsyncSession

from source.api.dependency.wallet.gateway import WalletGateway
from source.api.dependency.wallet.gateway_impl import WalletGatewayImpl
from source.api.interactors.wallet.get import GetWalletInteractor
from source.common.commiter import Commiter
from source.db.models.wallet import Wallet
from source.db.sa_commiter import SACommiter


@pytest.mark.asyncio
async def test_create_wallet_gateway():

    test_address = "LKJFf-2eifj2-eifjlahgalkgjldskgjag"
    test_balance = Decimal("111")
    test_free_bandwidth = "222"
    test_total_bandwidth = "333"
    test_total_energy = "444"

    mock_gateway = MagicMock(spec=WalletGateway)
    mock_commiter = MagicMock(spec=Commiter)

    fake_wallet = Wallet(
        address=test_address,
        balance=test_balance,
        free_bandwidth=test_free_bandwidth,
        total_bandwidth=test_total_bandwidth,
        total_energy=test_total_energy,
    )
    mock_gateway.save = AsyncMock(return_value=fake_wallet)

    result_wallet = await mock_gateway.save(
        Wallet(
            address=test_address,
            balance=test_balance,
            free_bandwidth=test_free_bandwidth,
            total_bandwidth=test_total_bandwidth,
            total_energy=test_total_energy,
        ),
    )

    await mock_commiter.commit()

    assert result_wallet.address == test_address
    assert result_wallet.balance == test_balance
    assert result_wallet.free_bandwidth == test_free_bandwidth
    assert result_wallet.total_bandwidth == test_total_bandwidth
    assert result_wallet.total_energy == test_total_energy


@pytest.mark.asyncio
async def test_get_wallet_interactor():

    test_address = "LKJFf-2eifj2-eifjlahgalkgjldskgjag"
    test_balance = Decimal("111")
    test_free_bandwidth = "222"
    test_total_bandwidth = "333"
    test_total_energy = "444"

    mock_gateway = MagicMock(spec=WalletGateway)

    fake_wallet = Wallet(
        address=test_address,
        balance=test_balance,
        free_bandwidth=test_free_bandwidth,
        total_bandwidth=test_total_bandwidth,
        total_energy=test_total_energy,
    )
    mock_gateway.by_id = AsyncMock(return_value=fake_wallet)

    assert fake_wallet.address == test_address
    assert fake_wallet.balance == test_balance
    assert fake_wallet.free_bandwidth == test_free_bandwidth
    assert fake_wallet.total_bandwidth == test_total_bandwidth
    assert fake_wallet.total_energy == test_total_energy

    mock_gateway.save = AsyncMock()

    interactor = GetWalletInteractor(
        wallet_gateway=mock_gateway,
    )
    geted_wallet = await interactor.by_id(wallet_id=fake_wallet.id)
    mock_gateway.by_id.assert_awaited_once_with(wallet_id=fake_wallet.id)

    assert geted_wallet.id == fake_wallet.id
    assert geted_wallet.address == fake_wallet.address
    assert geted_wallet.balance == fake_wallet.balance
    assert geted_wallet.free_bandwidth == fake_wallet.free_bandwidth
    assert geted_wallet.total_bandwidth == fake_wallet.total_bandwidth
    assert geted_wallet.total_energy == fake_wallet.total_energy
