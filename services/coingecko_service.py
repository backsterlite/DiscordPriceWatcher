# services/coingecko_service.py

import requests

class CoinGeckoService:
    """
    CoinGeckoService provides methods to fetch cryptocurrency prices from the CoinGecko public API.
    """
    BASE_URL = "https://api.coingecko.com/api/v3"

    @staticmethod
    def get_price(symbol: str, currency: str = "usd") -> float | None:
        try:
            response = requests.get(
                f"{CoinGeckoService.BASE_URL}/simple/price",
                params={
                    "ids": symbol.lower(),
                    "vs_currencies": currency
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            if symbol.lower() in data:
                return data[symbol.lower()][currency]
            return None
        except Exception as e:
            print(f"[ERROR] CoinGeckoService.get_price: {e}")
            return None
