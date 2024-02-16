from unittest import TestCase, mock  # Import for mocking
from unittest.mock import patch  # Import for mocking
from currency_converter import CurrencyConverter  # Import the class to test


class TestCurrencyConverter(TestCase):

    @patch('currency_converter.urllib.request.urlopen')  # Mock the method
    def test_get_exchange_rate(self, mock_urlopen):  # Pass the mock as an argument
        converter = CurrencyConverter()  # Create an instance of the class

        # Configure the mock response
        mock_response = mock.MagicMock()  # Create a mock object
        mock_response.read.return_value = b'{"usd": {"rate": 0.9}}'  # Set the return value for the 'read' method
        mock_response.__enter__.return_value = mock_response  # Set the return value for the context manager
        mock_urlopen.return_value = mock_response  # Set the mock response

        # Test same currency
        result = converter.get_exchange_rate('USD', 'USD')  # Call the method
        self.assertEqual(result, 1)  # Check the result

        # Test fetching a rate
        result = converter.get_exchange_rate('USD', 'EUR')  # Call the method
        self.assertEqual(result, 0.9)  # Check the result

    @patch('currency_converter.CurrencyConverter.get_exchange_rate')  # Mock the method
    def test_convert_currency(self, mock_get_exchange_rate):
        converter = CurrencyConverter()
        mock_get_exchange_rate.return_value = 0.9  # Set a mock return value for the rate

        result = converter.convert_currency('USD', 'EUR', 100)
        self.assertEqual(result, 90)
