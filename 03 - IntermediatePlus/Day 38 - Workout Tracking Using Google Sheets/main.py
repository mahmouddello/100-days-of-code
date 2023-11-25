import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("../../.env")

# ---------------------- CONSTANTS ---------------------- #

# Nutritionix API Credentials
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
APP_KEY = os.getenv("NUTRITIONIX_API_KEY")

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

# exercise
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
today = datetime.today()
today_date = today.strftime("%Y/%m/%d")
current_hour = today.strftime("%H:%M:%S")

params = {
    "query": input("Tell me what you did today? "),
}

response = requests.post(url=endpoint, json=params, headers=HEADERS)

data = response.json()
for i in range(len(data["exercises"])):
    workout = str.title(data["exercises"][i]["name"])
    duration = data["exercises"][i]["duration_min"]
    calories = data["exercises"][i]["nf_calories"]
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": current_hour,
            "exercise": workout,
            "duration": duration,
            "calories": calories
        }
    }
    sheety_post_endpoint = os.getenv("SHEETY_POST_EP")
    sheety_post_response = requests.post(url=sheety_post_endpoint, json=sheety_params, headers=HEADERS)
    print(sheety_post_response.json())
