import json
import logging
import requests
from difflib import get_close_matches

API_LINK = ("https://min-api.cryptocompare.com"
            "/data/price?fsym={from_symbol}&tsyms={to_symbols}")

def get_key_and_value_match(key_word, dictionary):
    """
    Takes a key word and finds the key or value inside the dictionary which
    matches it and returns the corresponding key and value pair. If there is
    no direct match, the nearest key or value is then found.
    Dictionary is expected to be with lower case keys and upper case values.
    """
    reverse_dictionary = {dictionary[k]: k for k in dictionary}
    if key_word.lower() in dictionary:
        key = key_word.title()
        value = dictionary[key_word.lower()]
    elif key_word.upper() in reverse_dictionary:
        key = reverse_dictionary[key_word.upper()].title()
        value = key_word.upper()
    else:
        all_names = ([k.lower() for k in dictionary.keys()]
                     + [v.lower() for v in dictionary.values()])
        closest_guesses = get_close_matches(key_word.lower(), all_names)
        closest_guess = closest_guesses[0]
        if closest_guess.lower() in dictionary.keys():
            key = closest_guess
            value = dictionary[closest_guess.lower()]
        else:
            key = reverse_dictionary[closest_guess.upper()]
            value = closest_guess.upper()

    return key.title(), value.upper()


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

    with open('cryptocurrencies.json') as cryptocurrency_file:
        SUPPORTED_COINS = json.load(cryptocurrency_file)
    from_currency, from_symbol = get_key_and_value_match(crypto_currency,
                                                         SUPPORTED_COINS)

    if currency:
        with open('currencies.json') as currency_file:
            SUPPORTED_CURRENCIES = json.load(currency_file)
        to_currency, to_symbol = get_key_and_value_match(currency,
                                                         SUPPORTED_CURRENCIES)
    else:
        to_currency = "US Dollars"
        to_symbol = "USD"

    api_link = API_LINK.format(from_symbol=from_symbol, to_symbols=to_symbol)
    api_response = requests.get(api_link)
    api_price = json.loads(api_response.content).get(to_symbol, 'USD')

    title = "{from_currency} Price in {to_currency}".format(
                from_currency=from_currency,
                to_currency=to_currency
            )
    response_message = ("{from_currency} is currently worth {value}"
                        " {to_currency}")
    response_message = response_message.format(
                           from_currency=from_currency,
                           value=api_price,
                           to_currency=to_currency
                       )

    return title, response_message


def crypto_price_lambda(event, session):
    """
    Takes in a cryptocurrency as well as an optional currency and outputs
    the exchange rate.
    """
    logging.warn(str(event))
    logging.warn(str(session))

    request_type = event['request'].get('type')

    if request_type == 'LaunchRequest':
        title = "Crypto Price Trends"
        response_message = ("Welcome to crypto price. Please ask a question "
                            "like: What is the price of bitcoin")
        return build_response(card_title=title,
                              card_content=response_message,
                              output_speech=response_message,
                              should_end_session=False)
    elif request_type == 'IntentRequest':
        request_intent = event['request']['intent']['name']
        if request_intent == 'GetCryptoPriceIntent':
            title, response_message = collect_crypto_price(event, session)
            return build_response(card_title=title,
                                  card_content=response_message,
                                  output_speech=response_message)
        elif request_intent == 'AMAZON.HelpIntent':
            title = "Crypto Price Help"
            response_message = ("Crypto price returns the price of the "
                                "leading cryptocurrencies. You can ask "
                                "questions like: What is the price of "
                                "bitcoin, tell me the current price of monero "
                                "in US dollars, and, what is the price of "
                                "litecoin in pounds. Please ask a question.")
            return build_response(card_title=title,
                                  card_content=response_message,
                                  output_speech=response_message,
                                  should_end_session=False)
        elif request_intent in ['AMAZON.StopIntent', 'AMAZON.CancelIntent']:
            title = "Crypto Price Cancel"
            response_message = ("Thanks for using crypto price. See you at "
                                "the moon.")
            return build_response(card_title=title,
                                  card_content=response_message,
                                  output_speech=response_message,
                                  should_end_session=True)



def build_response(
        card_title="Crypto Price",
        card_content="Returns price of a cryptocurrency",
        output_speech="Welcome to cryptoprice",
        should_end_session=True):
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
            },
            "shouldEndSession": should_end_session
        }
    }
