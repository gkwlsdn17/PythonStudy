import requests
from bs4 import BeautifulSoup
from currency_converter import CurrencyConverter

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)



# cc = CurrencyConverter()
# print(cc.currencies)
'''
{'SEK', 'KRW', 'HRK', 'EUR', 'USD', 'CHF', 'BGN', 'ISK', 'THB', 'LVL', 'MTL', 'PLN', 'HUF', 'TRY', 'SIT', 'NZD', 
'CAD', 'LTL', 'SGD', 'CZK', 'MYR', 'JPY', 'INR', 'TRL', 'EEK', 'BRL', 'CNY', 'ZAR', 'RON', 'CYP', 'IDR', 'MXN', 'PHP', 
'GBP', 'AUD', 'DKK', 'ROL', 'ILS', 'NOK', 'HKD', 'RUB', 'SKK'}
'''

# cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
# print(cc.convert(1, 'USD', 'KRW'))

get_exchange_rate('usd', 'krw')