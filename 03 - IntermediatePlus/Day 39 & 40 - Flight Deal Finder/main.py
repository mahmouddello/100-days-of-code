from datetime import datetime, timedelta
from time import strftime
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

dataManager = DataManager()
flightSearch = FlightSearch()
notification_manager = NotificationManager()
sheet_data = dataManager.get_destination_data()  # sheet data returned from the sheety api

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        if row["iataCode"] == "":
            row["iataCode"] = flightSearch.get_destination_code(city=row["city"])
    dataManager.update_destination_data()

#     else:
#         temp = flightData.get_flights_data(row["iataCode"])
#         price_in_sheet = row["lowestPrice"] if row["city"] == temp["city"] else print("LOL")
#         if temp['price'] < price_in_sheet:
#             print(f"{temp['city']}: £{temp['price']}")
#         else:
#             print("Nan")

tomorrow = datetime.now() + timedelta(days=1)
tomorrow = tomorrow.strftime("%d/%m/%y")
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
six_month_from_today = six_month_from_today.strftime("%d/%m/%y")

for destination in sheet_data:
    flight = flightSearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
