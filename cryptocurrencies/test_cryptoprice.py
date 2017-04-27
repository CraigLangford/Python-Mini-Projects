from cryptoprice import (
    crypto_price_lambda, collect_crypto_price
)

EXAMPLE_INTENT_REQUEST = {
    "session": {
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


def test_collect_crypto_price_for_various_cryptocurrencies():
    title, response_message = collect_crypto_price(EXAMPLE_INTENT_REQUEST, {})
    assert title == "Bitcoin Price"
    assert response_message.startswith("Bitcoin is currently worth")

    EXAMPLE_INTENT_REQUEST['request'][
        'intent']['slots']['Cryptocurrency']['value'] = "ethereum"
    title, response_message = collect_crypto_price(EXAMPLE_INTENT_REQUEST, {})
    assert title == "Ethereum Price"
    assert response_message.startswith("Ethereum is currently worth")

    EXAMPLE_INTENT_REQUEST['request'][
        'intent']['slots']['Cryptocurrency']['value'] = "doge coin"
    title, response_message = collect_crypto_price(EXAMPLE_INTENT_REQUEST, {})
    assert title == "Dogecoin Price"
    assert response_message.startswith("Dogecoin is currently worth")

    EXAMPLE_INTENT_REQUEST['request'][
        'intent']['slots']['Cryptocurrency']['value'] = "XMR"
    title, response_message = collect_crypto_price(EXAMPLE_INTENT_REQUEST, {})
    assert title == "Monero Price"
    assert response_message.startswith("Monero is currently worth")


def test_collect_crypto_price_for_nearest_values():
    EXAMPLE_INTENT_REQUEST['request'][
        'intent']['slots']['Cryptocurrency']['value'] = "dog coin"
    title, response_message = collect_crypto_price(
        EXAMPLE_INTENT_REQUEST, {})
    assert title == "Dogecoin Price"
    assert response_message.startswith("Dogecoin is currently worth")

    EXAMPLE_INTENT_REQUEST['request'][
        'intent']['slots']['Cryptocurrency']['value'] = "XM are"
    title, response_message = collect_crypto_price(
        EXAMPLE_INTENT_REQUEST, {})
    assert title == "Monero Price"
    assert response_message.startswith("Monero is currently worth")


def test_crypto_price_lambda_returns_dictionary():
    assert type(crypto_price_lambda(EXAMPLE_INTENT_REQUEST, {})) == dict


def test_cryptocurrency_returns_correct_format():
    conversion_response = crypto_price_lambda(EXAMPLE_INTENT_REQUEST, {})
    assert 'version' in conversion_response
    assert 'response' in conversion_response
    assert 'card' in conversion_response['response']
    assert 'outputSpeech' in conversion_response['response']
