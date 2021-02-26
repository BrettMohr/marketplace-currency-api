import requests

BASE_URL = 'http://data.fixer.io/api/'
LATEST_PATH = 'latest'


class CurrencyTranslationException(BaseException):
    """ Common base class for all CurrencyTranslation exceptions. """
    pass


class CurrencyTranslation(object):
    """ A client for Fixer.io. """

    def __init__(self, access_key, symbols):
        """
        :param access_key: your API Key.
        :type access_key: str or unicode
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple or None
        """
        self.access_key = access_key
        self.symbols = symbols

    def _create_payload(self, symbols):
        """ Creates a payload with no none values.
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        :return: a payload.
        :rtype: dict
        """
        payload = {'access_key': self.access_key}
        if symbols is not None:
            payload['symbols'] = ','.join(symbols)

        return payload

    def latest(self, symbols=None):
        """ Get the latest foreign exchange reference rates.
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        :return: the latest foreign exchange reference rates.
        :rtype: dict
        :raises CurrencyTranslationException: if any error making a request.
        """
        try:
            symbols = symbols or self.symbols
            payload = self._create_payload(symbols)

            url = BASE_URL + LATEST_PATH

            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise CurrencyTranslationException(str(ex))
