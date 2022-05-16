import requests
import json


class Rates:

    def __init__(self):
        url = 'https://v6.exchangerate-api.com/v6/a84240ee51dc634c8c3eceb5/latest/USD'
        self.url = url
        self.data = requests.get(url).json()
        self.rates = self.data['conversion_rates']

    """
    def get_rates(self):
        url = 'https://v6.exchangerate-api.com/v6/a84240ee51dc634c8c3eceb5/latest/USD'

        response = requests.get(url)
        data = response.json()

        rates_dict = data['conversion_rates']

        return rates_dict


rates = get_rates()

   """
    def dollar_to_other(self, amount, cur_to):
        cur_from = self.rates['USD']
        ans = amount * cur_from * self.rates[cur_to]
        return ans

    def other_to_dollar(self, amount, cur_from):
        cur_to = self.rates['USD']
        ans = (amount * cur_to) / self.rates[cur_from]
        return ans

    def exchange(self, amount, cur_from, cur_to):
        if cur_from == 'USD':
            return self.dollar_to_other(amount, cur_to)
        if cur_from != 'USD':
            dollar_c_from = self.other_to_dollar(amount, cur_from)
            return self.dollar_to_other(dollar_c_from, cur_to)


