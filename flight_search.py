import requests
import os

TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'
TEQUILA_KEY = os.environ.get('TEQUILAKEY')

class FlightSearch:
    def get_flight_code(self, city_name):
        params = {
            'term': city_name
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/locations/query",
            headers = {"apikey": TEQUILA_KEY},
            params = params)
        code = response.json()['locations'][0]['code']
        return code