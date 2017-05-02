import json
import logging
import requests
from difflib import get_close_matches

API_LINK = ("https://min-api.cryptocompare.com"
            "/data/price?fsym={from_symbol}&tsyms={to_symbols}")


def collect_crypto_price(event, session):
    """
    Extracts the cryptocurrency, finds the nearest match, and returns
    its price. If the financial currency is supplied the amount returned
    is in that currency. Otherwise the price is returned based on where
    the user is asking from.
    """

    slots = event['request']['intent']['slots']
    crypto_currency = slots['cryptocurrency']['value']
    currency = slots['Currency'].get('value')

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


def crypto_price_lambda(event, session):
    """
    Takes in a cryptocurrency as well as an optional currency and outputs
    the exchange rate.
    """
    logging.warn(str(event))
    logging.warn(str(session))

    if event['request'].get('type') == 'LaunchRequest':
        title = "Crypto Price Trends"
        response_message = ("Welcome to crypto price. You can ask a question "
                            "like: What is the price of cryptocurrency?")
        response = build_response(card_title=title,
                                  card_content=response_message,
                                  output_speech=response_message,
                                  should_end_sesion=False)
    else:
        title, response_message = collect_crypto_price(event, session)
        response = build_response(card_title=title,
                                  card_content=response_message,
                                  output_speech=response_message)

    return response


def build_response(
        card_title="Crypto Price",
        card_content="Returns price of a cryptocurrency"
        output_speech="Welcome to cryptoprice",
        should_end_sesion=True):
    """
    Builds a valid ASK response based on the incoming attributes.
    """
    return {
        "version": "1.0",
        "response": {
            "card": {
                "type": "Simple",
                "title": card_title,
                "content": card_content,
            },
            "outputSpeech": {
                "type": "PlainText",
                "text": output_speech
            }
        },
        "shouldEndSession": should_end_session
    }
