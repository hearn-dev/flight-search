import requests
from pprint import pprint

SHEETY_ENDPOINT = 'https://api.sheety.co/559ac6fe5eab6a429dd19fd710cbf24c/flightDeals/prices'

class DataManager:
    def __init__(self) -> None:
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        self.destination_data = response.json()['prices']
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

