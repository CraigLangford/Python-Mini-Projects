import json
import requests
from difflib import get_close_matches

with open('currencies.json') as currency_file:
    SUPPORTED_COINS = json.load(currency_file)

API_LINK = ("https://min-api.cryptocompare.com"
            "/data/price?fsym={from_symbol}&tsyms={tsyms}")


def collect_price_for_crypto_currency(
        crypto_currency="Bitcoin", currency="GBP"):
    """
    Takes a crypto currency, finds the nearest match, and hits the API
    searching for the conversion rate.
    """
    REVERSE_SUPPORTED_COINS = {SUPPORTED_COINS[k]: k for k in SUPPORTED_COINS}
    if crypto_currency.lower() in SUPPORTED_COINS:
        from_symbol = SUPPORTED_COINS[crypto_currency.lower()]
        crypto_currency = crypto_currency.title()
    elif crypto_currency.upper() in REVERSE_SUPPORTED_COINS:
        from_symbol = crypto_currency.upper()
        crypto_currency = REVERSE_SUPPORTED_COINS[
            crypto_currency.upper()].title()
    else:
        all_names = ([w.lower() for w in SUPPORTED_COINS.keys()]
                     + [w.lower() for w in SUPPORTED_COINS.values()])
        closest_guesses = get_close_matches(crypto_currency.lower(), all_names)
        closest_guess = closest_guesses[0]
        if closest_guess.lower() in SUPPORTED_COINS.keys():
            from_symbol = SUPPORTED_COINS[closest_guess.lower()]
            crypto_currency = closest_guess.title()
        else:
            from_symbol = closest_guess.upper()
            crypto_currency = REVERSE_SUPPORTED_COINS[closest_guess.upper()]
    api_link = API_LINK.format(from_symbol=from_symbol, tsyms='GBP')
    api_response = requests.get(api_link)
    api_prices = json.loads(api_response.content)
    return crypto_currency, api_prices['GBP']


def get_crypto_price(request, context):
    """
    Takes in a cryptocurrency as well as an optional currency and outputs
    the exchange rate.
    """
    data = request['request']['intent']['slots']
    crypto_currency = data['Cryptocurrency']['value']
    currency = data['Currency'].get('value')
    crypto_currency, crypto_value = collect_price_for_crypto_currency(
        crypto_currency=crypto_currency)
    response_message = "{crypto_currency} is currently worth {value} pounds."
    response_message = response_message.format(
        crypto_currency=crypto_currency, value=crypto_value)
    if currency:
        response_message += " Different currencies aren't yet supported."
    response = {"version": "1.0"}
    response['response'] = {
        "card": {
            "type": "Simple",
            "title": "{crypto_currency} Price".format(
                crypto_currency=crypto_currency),
            "content": response_message
        },
        "outputSpeech": {
            "type": "PlainText",
            "text": response_message
        }
    }
    return response
