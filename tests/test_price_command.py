# tests/test_price_command.py

import pytest
from unittest.mock import AsyncMock, patch
from bot.commands.price import Price

@pytest.fixture
def mock_ctx():
    ctx = AsyncMock()
    ctx.send = AsyncMock()
    return ctx

@pytest.mark.asyncio
@patch('services.coingecko_service.CoinGeckoService.get_price')
async def test_price_valid_symbol(mock_get_price, mock_ctx):
    mock_get_price.return_value = 50000.0  # мокнемо ціну

    price_cog = Price(bot=None)  # передаємо None, бо в тесті нам бот не потрібен
    await price_cog.price(mock_ctx, "bitcoin")

    mock_ctx.send.assert_called_once()
    assert "50000" in mock_ctx.send.call_args[0][0]

@pytest.mark.asyncio
@patch('services.coingecko_service.CoinGeckoService.get_price')
async def test_price_invalid_symbol(mock_get_price, mock_ctx):
    mock_get_price.return_value = None  # якщо монета не знайдена

    price_cog = Price(bot=None)
    await price_cog.price(mock_ctx, "invalidcoin")

    mock_ctx.send.assert_called_once()
    assert "could not find" in mock_ctx.send.call_args[0][0].lower()
    