import app_config
from flask import request, jsonify, Blueprint
from api_helpers.api_helpers import check_required, get_data

get_conversion = Blueprint('get_conversion', __name__)


@get_conversion.route(app_config.CURRENCY_CONVERT_ENDPOINT, methods=['GET'])
def currency_convert():
    """
    GET CURRENCY_CONVERT_ENDPOINT API ENDPOINT
    Request Body
        {
            "origin_currency":"USD",
            "destination_currency": "EUR",
            "origin_value": 12.23
        }
    :return: a payload with the amount in origin_currency, converted to an amount in the destination_currency
    :rtype: dict
    """

    # Define json_data from API request
    json_data = request.json

    # Required values unique to CURRENCY_CONVERT_ENDPOINT
    required_keys = [app_config.ORIGIN_CURRENCY, app_config.DESTINATION_CURRENCY, app_config.ORIGIN_VALUE]

    # Check to see if any of the required values are missing
    # If required params are missing return 400
    missing_params = check_required(required_keys, json_data)
    if missing_params:
        return jsonify({
            'message': f'Required values {missing_params} are missing.',
            'error': 'required_values_not_provided'
        }), 400

    # Define parameters for conversion
    conversion_params = json_data[app_config.ORIGIN_CURRENCY], json_data[app_config.DESTINATION_CURRENCY], json_data[
        app_config.ORIGIN_VALUE]

    # Create response from conversion
    response = get_data().convert(conversion_params)

    return response
