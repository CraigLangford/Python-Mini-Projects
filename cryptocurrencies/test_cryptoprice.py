from cryptoprice import (
    get_crypto_price, collect_price_for_crypto_currency
)

EXAMPLE_REQUEST = {"session": {
        "sessionId": "SessionId.6beee92e-e49fakjdsh73-b514-3c03b7eec660",
        "application": {
            "applicationId": "amzn1.ask.skill.fasjdofsad998fasdj"
        },
        "attributes": {},
        "user": {"userId": "21376468928"},
        "new": True
    },
    "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.768c7cd1-b270-47ab-810e-80208e7e16ed",
        "locale": "en-US",
        "timestamp": "2017-04-26T00:41:00Z",
        "intent": {
            "name": "GetCryptoPriceIntent",
            "slots": {
                "Currency": {"name": "Currency"},
                "Cryptocurrency": {
                    "name": "Cryptocurrency",
                    "value": "Bitcoin"
                }
            }
        }
    },
    "version": "1.0"
}


def test_cryptocurrency_returns_dictionary():
    assert type(get_crypto_price(EXAMPLE_REQUEST, {})) == dict


def test_get_crypto_price_takes_crypto_currency():
    assert type(get_crypto_price(EXAMPLE_REQUEST, {})) == dict


def test_cryptocurrency_returns_correct_format():
    conversion_response = get_crypto_price(EXAMPLE_REQUEST, {})
    assert 'version' in conversion_response
    assert 'response' in conversion_response
    assert 'card' in conversion_response['response']
    assert 'outputSpeech' in conversion_response['response']


def test_collect_price_for_various_crypto_currencies():
    crypto_type, crypto_price = collect_price_for_crypto_currency()
    assert crypto_type == "Bitcoin"
    assert type(crypto_price) in [float, int]
    crypto_type, crypto_price = collect_price_for_crypto_currency(
        crypto_currency="Ethereum")
    assert crypto_type == "Ethereum"
    assert type(crypto_price) in [float, int]
    crypto_type, crypto_price = collect_price_for_crypto_currency(
        crypto_currency="DOGE")
    assert crypto_type == "Dogecoin"
    assert type(crypto_price) in [float, int]
    crypto_type, crypto_price = collect_price_for_crypto_currency(
        crypto_currency="monero")
    assert crypto_type == "Monero"
    assert type(crypto_price) in [float, int]


def test_collect_price_for_nearest_values():
    crypto_type, crypto_price = collect_price_for_crypto_currency(
        crypto_currency="doge coin")
    assert crypto_type == "Dogecoin"
    assert type(crypto_price) in [float, int]
    crypto_type, crypto_price = collect_price_for_crypto_currency(
        crypto_currency="lite coin")
    assert crypto_type == "Litecoin"
    assert type(crypto_price) in [float, int]
