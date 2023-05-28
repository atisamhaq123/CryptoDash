from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'put your key here'

def get_cryptocurrency_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    }
    params = {
        'start': '1',
        'limit': '7',
        'convert': 'USD'
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    return data['data']

def extract_currency_names(data):
    currency_names = []
    for currency in data:
        currency_names.append(currency['name'])
    return currency_names

def extract_currency_prices(data):
    currency_prices = []
    for currency in data:
        currency_prices.append(currency['quote']['USD']['price'])
    return currency_prices

@app.route('/')
def home():
    crypto_data = get_cryptocurrency_data()
    currency_names = extract_currency_names(crypto_data)
    currency_prices = extract_currency_prices(crypto_data)
    return render_template('dashboard.html', crypto_data=crypto_data, currency_names=currency_names, currency_prices=currency_prices)

if __name__ == '__main__':
    app.run(debug=True, port=3500)
