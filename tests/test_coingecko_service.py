# tests/test_coingecko_service.py

import pytest
from services.coingecko_service import CoinGeckoService

@pytest.mark.parametrize("symbol,expected_currency", [
    ("bitcoin", "usd"),
    ("ethereum", "usd"),
    ("dogecoin", "usd"),
])
def test_get_price_success(symbol, expected_currency):
    price = CoinGeckoService.get_price(symbol)
    assert price is not None, f"Price for {symbol} should not be None"
    assert isinstance(price, (int, float)), f"Price for {symbol} should be a number"

def test_get_price_invalid_symbol():
    price = CoinGeckoService.get_price("thisisnotacoin")
    assert price is None, "Price for invalid symbol should be None"
