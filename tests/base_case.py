import app_config
from app import app
from unittest import TestCase
from resources.currency_translation import CurrencyTranslation


class BaseCase(TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.currency_api = CurrencyTranslation(access_key=app_config.FIXER_API_KEY, symbols=app_config.CURRENCY_SUPPORTED)
        self.get_rate_params = {
            "origin_currency": "USD",
            "destination_currency": "GBP"
        }
        self.get_conversion_params = {
            "origin_currency": "USD",
            "destination_currency": "GBP",
            "origin_value": 12.23
        }
