import urllib.request  # Standard library module for working with URLs
import json  # Standard library module for working with JSON data

from exchange_rate_parser import ExchangeRateParser  # Import the ExchangeRateParser class


class CurrencyConverter:
    """
    Class for converting currency using exchange rates from the web

    Attributes:
        parser (ExchangeRateParser): An instance of the ExchangeRateParser class

    Methods:
        get_exchange_rate: Fetches the exchange rate from the web
        convert_currency: Converts an amount from one currency to another
    """

    def __init__(self):
        """
        Initializes the CurrencyConverter class
        """
        self.parser = ExchangeRateParser()

    def get_exchange_rate(self, from_currency, to_currency):
        """
        Fetches the exchange rate from the web

        Args:
            from_currency (str): The currency to convert from
            to_currency (str): The currency to convert to

        Returns:
            float: The exchange rate
        """

        from_url = f"https://www.floatrates.com/daily/{from_currency}.json"

        try:
            with urllib.request.urlopen(from_url) as response:
                from_data = json.loads(response.read().decode('utf-8'))

            # Extract rates - Access from_data directly
            if from_currency.upper() == to_currency.upper():
                return 1
            else:
                print(f"Rate: {from_data}")
                from_to_rate = from_data[to_currency.lower()]['rate']
                return from_to_rate

        except urllib.error.URLError as e:
            print(f"Error fetching data: {e}")
            return None

    def convert_currency(self, from_currency, to_currency, amount):
        rate = self.get_exchange_rate(from_currency, to_currency)
        if rate:
            converted_amount = rate * amount
            return converted_amount
        else:
            return None