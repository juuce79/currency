import urllib.request  # Standard library module for working with URLs
import urllib.error  # Used for managing errors during web requests
import json  # Standard library module for working with JSON data


class CurrencyConverter:
    """
    A class for converting currencies using exchange rates fetched from the web.
    """

    def __init__(self):
        """
        Initializes the CurrencyConverter class.
        """

    @staticmethod
    def get_exchange_rate(from_currency, to_currency):
        """
        Fetches the exchange rate for the given "from" and "to" currencies

        :param from_currency: The currency to convert from
        :param to_currency: The currency to convert to
        """

        from_url = f"https://www.floatrates.com/daily/{from_currency}.json"  # Construct the API URL

        try:
            with urllib.request.urlopen(from_url) as response:  # Open the URL and store the response
                from_data = json.loads(response.read().decode('utf-8'))  # Load the JSON response

            if from_currency.upper() == to_currency.upper():  # Check for same currency conversion
                return 1  # Return 1 if currencies are the same
            else:
                from_to_rate = from_data[to_currency.lower()]['rate']  # Extract the exchange rate
                return from_to_rate  # Return the extracted rate

        except urllib.error.URLError as e:  # Exception handling for URL errors
            print(f"Error fetching data: {e}")  # Print the error message
            return None  # Return None on error

    def convert_currency(self, from_currency, to_currency, amount):
        """
        Converts the given amount from one currency to another currency

        :param from_currency: The currency to convert from
        :param to_currency: The currency to convert to
        :param amount: The amount to convert to
        :return: The converted amount of the given currency
        """
        rate = self.get_exchange_rate(from_currency, to_currency)  # Fetch the exchange rate
        if rate:  # Check if a valid exchange rate was retrieved
            converted_amount = rate * amount  # Calculate the converted amount
            return converted_amount  # Return the converted amount
        else:  # Handle the case where no exchange rate is available
            return None  # Indicate conversion failure
