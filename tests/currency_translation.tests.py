import json
import responses
import unittest
from http.client import responses
from urllib.parse import urlencode
from resources.currency_translation import LATEST_PATH
from resources.currency_translation import BASE_URL, CurrencyTranslation, CurrencyTranslationException


class CurrencyTranslationTestCase(unittest.TestCase):

    def setUp(self):
        self.access_key = 'test-access-key'
        query = urlencode({'access_key': self.access_key})
        self.url = BASE_URL + LATEST_PATH + '?' + query

    def test_raises_if_access_key_is_not_passed(self):
        with self.assertRaises(TypeError):
            CurrencyTranslation()

    def test_sets_access_key(self):
        client = CurrencyTranslation(self.access_key, symbols=None)
        self.assertEqual(client.access_key, self.access_key)

    def test_sets_none_symbols_attribute_if_it_is_not_passed(self):
        client = CurrencyTranslation(self.access_key, symbols=None)
        self.assertIsNone(client.symbols)

    def test_sets_symbols_attribute(self):
        symbols = ['USD', 'GBP']
        client = CurrencyTranslation(self.access_key, symbols=symbols)
        self.assertEqual(client.symbols, symbols)

    @responses.activate
    def test_returns_latest_rates(self):
        expected_response = {'base': 'EUR', 'date': '2016-04-29',
                             'rates': {'GBP': 0.78025}}
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')

        c = CurrencyTranslation(self.access_key, symbols=None)
        response = c.latest()

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.url, self.url)
        self.assertIsNone(request.body)

    @responses.activate
    def test_raises_exception_if_bad_request(self):
        responses.add(responses.GET,
                      self.url,
                      body="{'success': false}",
                      status=400,
                      content_type='text/json')

        with self.assertRaises(CurrencyTranslationException)as ex:
            client = CurrencyTranslation(self.access_key, None)
            client.latest()

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
