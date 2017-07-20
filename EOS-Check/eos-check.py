#!/usr/bin/env python

"""EOS Coin Profit Checker
Checks the current number of eos coins you would receive if you sent your
ethereum to the crowd sale in this 23 hours period. Exchange rates are based
on Kraken
"""

import requests

__author__ = "Craig Langford"
__credits__ = ["Craig Langford"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Craig Langford"
__email__ = "craigllangford@gmail.com"
__status__ = "Beta"


def create_exchange_url(exchange_types):
    """Returns the url to get the exchange data"""
    base_url = "https://api.kraken.com/0/public/Ticker"
    return "{}?pair={}".format(base_url, ','.join(exchange_types))


def extract_exchange_data(raw_exchange_data):
    """Returns a dictionary of the desired exchange data"""
    return {
        'EOSXBT': float(raw_exchange_data['result']['EOSXBT']['b'][0]),
        'XBTETH': 1 / float(raw_exchange_data['result']['XETHXXBT']['b'][0]),
    }


if __name__ == '__main__':
    exchange_url = create_exchange_url(['XETHXXBT', 'EOSXBT'])
    raw_exchange_data = requests.get(exchange_url).json()
    exchange_data = extract_exchange_data(raw_exchange_data)
    print(exchange_data)
