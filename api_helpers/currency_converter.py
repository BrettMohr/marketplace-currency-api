import app_config


class CurrencyConvertor:
    # Empty dict to store conversion rates
    rates = {}

    def __init__(self, data):
        # Get rates from the data
        self.rates = data["rates"]

    # Convert amount based upon two currencies
    # Cross multiplication between the amount and conversion rate
    def convert(self, params):
        from_currency, to_currency, amount = params
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # Limit float precision to 2 decimals
        amount = round(amount * self.rates[to_currency], 2)
        response = {app_config.ORIGIN_CURRENCY: from_currency, app_config.ORIGIN_VALUE: initial_amount,
                    app_config.DESTINATION_VALUE: amount,
                    app_config.DESTINATION_CURRENCY: to_currency}
        return response

    def get_rate(self, params):
        from_currency, to_currency = params

        # Calculate currency ratio and limit float precision to 2 decimals
        ratio = self.rates[to_currency] / self.rates[from_currency]

        response = {app_config.ORIGIN_CURRENCY: from_currency, app_config.DESTINATION_CURRENCY: to_currency, app_config.CONVERSION_RATIO: ratio}

        return response
