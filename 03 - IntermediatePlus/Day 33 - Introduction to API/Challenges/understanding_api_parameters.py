import requests
import pytz
import datetime

# Some Parameters are Required, others maybe optional; and some APIs don't have parameters
LOCAL_UTC_OFFSET = 3
MY_LAT = 36.812103
MY_LONG = 34.641479


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
# latitude, longitude for Mersin, Turkey

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # Raise Exceptions if something went wrong.

data = response.json()
print(data)
print("-" * 50)
print("- Solution for local time -")
print(data["results"]["sunrise"].split("T"))
print(data["results"]["sunrise"].split("T")[1].split(":")[0])

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

lt_sunrise = utc_to_local(sunrise)
lt_sunset = utc_to_local(sunset)

print(f"Local Sunrise hour: {lt_sunrise}")
print(f"Local Sunset hour: {lt_sunset}")
