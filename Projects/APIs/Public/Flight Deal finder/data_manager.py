import requests
from pprint import pprint

class DataManager:
    def __init__(self):
        self.sheetify_url = 'https://api.sheety.co/2b0abfaa449748150f97e506773072dc/flightDeals/prices'

    def take_data(self):
        sent_sheet = requests.get(url=self.sheetify_url)
        data = sent_sheet.json()
        destinations = data['prices']
        return destinations

    def update(self, data):

        for city in data:
            data_new = {
                'price': {
                    'iataCode':city['iataCode']
                }
            }
            request = requests.put(url=f"{self.sheetify_url}/{city['id']}", json=data_new)
            print(request.text)
