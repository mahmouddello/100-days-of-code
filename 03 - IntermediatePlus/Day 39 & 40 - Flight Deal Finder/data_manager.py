import os
import requests
from dotenv import load_dotenv

load_dotenv("../../.env")

SHEETY_GET = os.getenv("SHEETY_GET_EP")
SHEETY_UPDATE = os.getenv("SHEETY_UPDATE_EP")


class DataManager:
    def __init__(self):
        self.destination_data = {}  # empty dictionary to store the api response (json)

    def get_destination_data(self):
        # Using Sheety API to get data
        data = requests.get(url=SHEETY_GET).json()
        self.destination_data = data["prices"]  # "prices" : sheet name
        return self.destination_data

    def update_destination_data(self):
        # Updating the data in the Google sheet
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                    # TESTING returned from get_destination_code (flight_search.py)
                    # which means it's already saved to the iataCode in the variable "sheet_data"
                    # then we update the Google sheet with the sheety api

                    # Replaced TESTING with the correct city code later on.
                }
            }
            response = requests.put(url=f"{SHEETY_UPDATE}/{city['id']}", json=new_data)
