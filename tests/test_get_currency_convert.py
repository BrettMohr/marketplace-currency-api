import json
import unittest
import app_config
from tests.base_case import BaseCase


class TestGetCurrencyConvert(BaseCase):

    def test_response_exists(self):
        user_payload = self.get_conversion_params
        response = self.app.get(app_config.CURRENCY_CONVERT_ENDPOINT, headers={'Content-Type': 'application/json'},
                                data=json.dumps(user_payload))
        data = json.loads(response.get_data())
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data[app_config.ORIGIN_CURRENCY], "USD")
        self.assertEqual(data[app_config.DESTINATION_CURRENCY], "GBP")
        self.assertEqual(data[app_config.DESTINATION_VALUE], 8.78)


if __name__ == "__main__":
    unittest.main()
