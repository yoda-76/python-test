from flask import Flask, jsonify
from delta_rest_client import DeltaRestClient

app = Flask(__name__)

class Portfolio:
    def __init__(self, api_key: str, api_secret: str, base_url: str = 'https://api.delta.exchange'):
        self.delta_client = DeltaRestClient(base_url=base_url, api_key=api_key, api_secret=api_secret)
        self.initial_balance = 10000 #change initial wallet accordingly

    def get_wallet_balance(self) -> int:
        balance_data = self.delta_client.get_balances(5)
        wallet_balance = int(float(balance_data['balance']))
        return wallet_balance

    def calculate_nav(self) -> float:
        wallet_balance = self.get_wallet_balance()
        nav = (wallet_balance / self.initial_balance) * 100
        return nav

@app.route('/nav', methods=['GET'])
def get_nav():
    api_key = 'k6yPWzNpaYnxOt6TjhgVnrRQB9qubc'
    api_secret = 'J7gy4yTEoIDxoZPekyyoYF4MS7bDYC2JuN0PNMiXmo59g7sut4hwSw1qDrrS'

    portfolio = Portfolio(api_key, api_secret)
    nav = portfolio.calculate_nav()

    response = nav#{'nav': nav}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
