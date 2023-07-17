# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

data_manager = DataManager()
flight_search =FlightSearch()

data = data_manager.take_data()

for city in data:
   if city['iataCode'] == '':
       city['iataCode'] = flight_search.iatacode(city['city'])

data_manager.update(data)


