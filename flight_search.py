import os
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.environ.get('TEQUILAKEY')


class FlightSearch:
    def find_codes(self, city):
        location_endpoint = f'{TEQUILA_ENDPOINT}/locations/query'
        headers = {'apikey': '9nfQXGdg4UY-0iYLM1DdIxq5UH6ja0Tc'}
        params = {
            'term': city,
            'location_types': 'city'
            }
        response = requests.get(
            url=location_endpoint,
            params=params,
            headers=headers
        )
        
        results = response.json()['locations']
        code = results[0]['code']
        return code

flight = FlightSearch()
print(flight.find_codes('Knoxville'))
