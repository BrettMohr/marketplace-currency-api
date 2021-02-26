import app_config
from flask import request, jsonify, Blueprint
from api_helpers.api_helpers import check_required, get_data

get_rate = Blueprint('get_rate', __name__)


@get_rate.route(app_config.CURRENCY_RATE_ENDPOINT, methods=['GET'])
def currency_rate():
    """
    GET CURRENCY_RATE_ENDPOINT API ENDPOINT
    Request Body
        {
            "origin_currency":"USD",
            "destination_currency": "EUR"
        }
    :return: a payload with the value of 1 unit of origin_currency in destination_currency
    :rtype: dict
    """

    # Define json_data from API request
    json_data = request.json

    # Required list unique to CURRENCY_RATE_ENDPOINT
    required_keys = [app_config.ORIGIN_CURRENCY, app_config.DESTINATION_CURRENCY]

    # Check to see if any of the required values are missing
    # If required params are missing return 400
    missing_params = check_required(required_keys, json_data)
    if missing_params:
        return jsonify({
            'message': f'Required values {missing_params} are missing.',
            'error': 'required_values_not_provided'
        }), 400

    # Define parameters for conversion
    conversion_params = json_data[app_config.ORIGIN_CURRENCY], json_data[app_config.DESTINATION_CURRENCY]

    # Create response from conversion
    response = get_data().get_rate(conversion_params)

    return response
