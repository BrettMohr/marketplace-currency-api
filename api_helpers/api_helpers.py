# Create instance of CurrencyTranslation to connect to Fixer API
import app_config
from api_helpers.currency_converter import CurrencyConvertor
from resources.currency_translation import CurrencyTranslation

currency_api = CurrencyTranslation(access_key=app_config.FIXER_API_KEY, symbols=app_config.CURRENCY_SUPPORTED)


# Internal method to check validity of submitted parameters
def check_required(required_list, json_data):
    return [required_param for required_param in required_list if not json_data.get(required_param)]


# Internal method to retrieve conversion data from external API
def get_data():
    # Get data from conversion source
    data = currency_api.latest()

    # Create instance of CurrencyConvertor passing in data from conversion source
    converter = CurrencyConvertor(data)

    return converter
