import json
import requests
from difflib import get_close_matches

API_LINK = ("https://min-api.cryptocompare.com"
            "/data/price?fsym={from_symbol}&tsyms={to_symbols}")


def collect_crypto_price(request, session):
    """
    Extracts the cryptocurrency, finds the nearest match, and returns
    its price. If the financial currency is supplied the amount returned
    is in that currency. Otherwise the price is returned based on where
    the user is asking from.
    """

    data = request['request']['intent']['slots']
    crypto_currency = data['Cryptocurrency']['value']
    currency = data['Currency'].get('value')

    with open('currencies.json') as currency_file:
        SUPPORTED_COINS = json.load(currency_file)
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
            crypto_currency = crypto_currency.title()

    currency_symbol = 'GBP'

    api_link = API_LINK.format(from_symbol=from_symbol,
                               to_symbols=currency_symbol)
    api_response = requests.get(api_link)
    api_price = json.loads(api_response.content)[currency_symbol]

    title = "{crypto_currency} Price".format(crypto_currency=crypto_currency)

    response_message = ("{crypto_currency} is currently worth {value}"
                        " {currency}.")
    response_message = response_message.format(
        crypto_currency=crypto_currency, value=api_price, currency="pounds")
    if currency:
        response_message += " Different currencies aren't yet supported."

    return title, response_message


def crypto_price_lambda(request, session):
    """
    Takes in a cryptocurrency as well as an optional currency and outputs
    the exchange rate.
    """
    if request.get('type') == 'LaunchRequest':
        title = "Welcome to Crypto Price"
        response_message = "Hello from crypto price"
    else:
        title, response_message = collect_crypto_price(request, session)

    response = {"version": "1.0"}
    response['response'] = {
        "card": {
            "type": "Simple",
            "title": title,
            "content": response_message
        },
        "outputSpeech": {
            "type": "PlainText",
            "text": response_message
        }
    }
    return response
