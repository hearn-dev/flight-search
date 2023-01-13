from data_manager import DataManager
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = DataManager()
sheet_data = dm.get_destination_data()
print(pprint(sheet_data))

if sheet_data[0]['iataCode'] == '':
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_flight_code(row['city'])
        print(f"sheet data: {sheet_data}")

    dm.destination_data = sheet_data
    dm.update_destination_codes() 