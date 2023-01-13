from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

STARTING_DESTINATION = 'NYC'
dm = DataManager()
flight_search = FlightSearch()
sheet_data = dm.get_destination_data()

if sheet_data[0]['iataCode'] == '':
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_flight_code(row['city'])
        print(f"sheet data: {sheet_data}")

    dm.destination_data = sheet_data
    dm.update_destination_codes() 

tomorrow = datetime.now() +timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        STARTING_DESTINATION,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_months_from_today
    )