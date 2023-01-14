from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/559ac6fe5eab6a429dd19fd710cbf24c/flightDeals/prices'


class DataManager:
    
    def __init__(self):
        self.destination_data = {}
    
    def update_codes(self):
        for city in self.destination_data:
            new_code = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_code
            )
            print(response.text)
    
    def pull_data(self):
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT
            )
        self.destination_data = response.json()
        return self.destination_data