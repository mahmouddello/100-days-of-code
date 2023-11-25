import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("../../../.env")

# -------------------------------- Constants -------------------------------- #

LAT = 32.060253  # latitude
LONG = 118.796875  # longitude
OMW_API_KEY = "cc68d4e2f4fd989c49ad1a9d0040b8c0"  # API key for authentication.
OMW_endpoint = "https://api.openweathermap.org/data/2.8/onecall"  # openweathermap API endpoint.

ACC_SID = os.getenv("ACC_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

# -------------------------------- Script -------------------------------- #

# Openweathermap API parameters
weather_parameters = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily",
    "appid": OMW_API_KEY
}

response = requests.get(url=OMW_endpoint, params=weather_parameters)  # response from the openweathermap API
response.raise_for_status()

weather_data = response.json()

weather_sliced = weather_data["hourly"][:12]  # holding the weather data of the next 12 hours

will_rain = False  # weather boolean flag
for hour_data in weather_sliced:
    condition_code = hour_data["weather"][0]["id"]  # access each hour's condition id (Read Documentation)
    if int(condition_code) < 700:
        will_rain = True  # Check condition id documentations

if will_rain:
    client = Client(ACC_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella with you ☔.",
        from_=os.getenv("TWILIO_NUM"),
        to=os.getenv("MY_NUM")
    )
    print(message.sid)
    print("SMS Sent Successfully")
