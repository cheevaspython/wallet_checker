import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_wallet(async_client: AsyncClient):
    wallet_address = "TVjsyZ7fYF3qLF6BQgPmTEZy1xrNNyVAAA"

    response = await async_client.post(
        "/api/v1/wallet/",
        data={"value": wallet_address},
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )

    assert response.status_code == 201
    response_data = response.json()
    assert "address" in response_data
    assert response_data["address"] == wallet_address


@pytest.mark.asyncio
async def test_get_wallets(async_client: AsyncClient):
    offset = 0
    limit = 10

    response = await async_client.get(
        "/api/v1/wallet/",
        params={"offset": offset, "limit": limit},
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )

    assert response.status_code == 200
    response_data = response.json()

    assert "count" in response_data
    assert "results" in response_data

    assert isinstance(response_data["count"], int)
    assert isinstance(response_data["results"], list)

    assert len(response_data["results"]) <= limit

    for wallet in response_data["results"]:
        assert "id" in wallet
        assert "address" in wallet
        assert "free_bandwidth" in wallet
        assert "total_bandwidth" in wallet
        assert "total_energy" in wallet
        assert "balance" in wallet
        assert "created_date" in wallet
