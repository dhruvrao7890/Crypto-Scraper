import requests
from bs4 import BeautifulSoup

class CoinMarketCap:
    def __init__(self):
        self.base_url = "https://coinmarketcap.com/currencies/"

    def get_coin_data(self, coin):
        try:
            url = f"{self.base_url}{coin}/"
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Sample data extraction - update according to the required fields
            price = soup.find("div", {"class": "priceValue"}).text.strip()
            market_cap = soup.find("div", {"class": "statsValue"}).text.strip()

            return {
                "price": price,
                "market_cap": market_cap,
            }
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
