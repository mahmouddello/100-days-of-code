import os
import requests
from flight_data import FlightData
from dotenv import load_dotenv

load_dotenv("../../.env")

tequila_api_key = os.getenv("TEQUILA_API_KEY")
tequila_api_location_endpoint = os.getenv("TEQUILA_API_LOC_ENDPOINT")
tequila_api_search_endpoint = os.getenv("TEQUILA_API_SER_ENDPOINT")

HEADERS = {
    "apikey": tequila_api_key
}


class FlightSearch:

    def get_destination_code(self, city):
        # Using Tequila API, search for the city name and get the code then saving the city code to a google sheet
        params = {
            "term": city
        }
        data = requests.get(url=tequila_api_location_endpoint, params=params, headers=HEADERS).json()
        code = data["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": "21/06/2023",
            "date_to": "17/12/2023",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=tequila_api_search_endpoint, params=query, headers=HEADERS).json()
        try:
            data = response["data"][0]
        except IndexError:
            print("No flights found for the destination city")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
