import unittest
import app_config
from api_helpers.currency_converter import CurrencyConvertor


class CurrencyConvertorTestCase(unittest.TestCase):

    def setUp(self):
        self.data = data = {
            "success": True,
            "timestamp": 1519296206,
            "base": "EUR",
            "date": "2021-02-26",
            "rates": {
                "AUD": 1.566015,
                "CAD": 1.560132,
                "CHF": 1.154727,
                "CNY": 7.827874,
                "GBP": 0.882047,
                "JPY": 132.360679,
                "USD": 1.23396,
            }
        }
        self.rates = data['rates']
        self.converter = CurrencyConvertor(data)

    def test_convert(self):
        from_currency = 'USD'
        to_currency = 'GBP'
        amount = 12.23
        params = from_currency, to_currency, amount
        res = self.converter.convert(params)
        self.assertEqual(8.74, res[app_config.DESTINATION_VALUE])

    def test_get_rate(self):
        from_currency = 'USD'
        to_currency = 'GBP'
        params = from_currency, to_currency
        res = self.converter.get_rate(params)
        self.assertEqual(0.7148100424649098, res[app_config.CONVERSION_RATIO])


if __name__ == "__main__":
    unittest.main()
