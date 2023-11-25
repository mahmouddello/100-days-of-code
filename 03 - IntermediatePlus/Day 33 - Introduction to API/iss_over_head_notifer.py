import os
import requests
import smtplib
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("../../.env")

# ISS: International Space Station

# ----------------------------- CONSTANTS -----------------------------
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASS = os.getenv("MY_PASS")
LOCAL_UTC_OFFSET = 3  # your local utc offset goes here.
MY_LAT = 36.812103
MY_LONG = 34.641479


def is_iss_overhead() -> bool:
    """
    The system confirms whether the International Space Station has crossed over the user's location,
    using their latitude and longitude coordinates.
    """
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data_iss = response_iss.json()

    # ISS's latitude and longitude information
    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude or iss_latitude <= MY_LAT + 5 \
            and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def utc_to_local(utc_hour: int) -> int:
    """
    Transforms the Coordinated Universal Time (UTC) retrieved from the sunset-sunrise API into
    the local time zone of the user.

    Parameters
    ----------
    utc_hour: int
              The hour in Coordinated Universal Time (UTC) that has been returned by the sunset-sunrise API.

    Returns
    -------
    local_time : int
                 The local time hour in the user time zone.
    """
    local_time = utc_hour + LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if local_time > 23:
            local_time -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if local_time < 0:
            local_time += 24
    return local_time


def is_night() -> bool:
    """
    Verifies whether it is presently nighttime in your specific area, based on the current local time.
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Raise Exceptions if something went wrong.

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # local time sunrise-sunset hours
    lt_sunrise = utc_to_local(sunrise)
    lt_sunset = utc_to_local(sunset)

    time_now = datetime.now()  # The current time in the user's time zone.
    return time_now.hour >= lt_sunset or time_now.hour <= lt_sunrise


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="smjnnhm57@gmail.com",
                            msg=f"Subject:Look Up 👆\n\nThe ISS is above you in the sky 🌠")
