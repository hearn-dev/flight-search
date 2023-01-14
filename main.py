from data_manager import DataManager
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()

sheet_data = data_manager.pull_data()['prices']

if sheet_data[0]['iataCode'] =='':
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.find_codes(row['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_codes()