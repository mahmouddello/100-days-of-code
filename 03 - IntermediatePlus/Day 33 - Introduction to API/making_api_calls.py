import requests

# The HTTP 200K success status response code indicates that the request has succeeded
response = requests.get(url="http://api.open-notify.org/iss-now.json")  # response code
# print(response.status_code)  # 200: Success

# Below is not a good approach to check for requestes status code errors:

# if response.status_code == 404:
#     raise Exception("That resource doesn't exist :(")
# elif response.status_code == 401:
#     raise Exception("You're not authorized to access this data :|")

response.raise_for_status()

# Hold The Data

data = response.json()  # dictionary

latitude = data["iss_position"]["latitude"]  # خطوط العرض
longitude = data["iss_position"]["longitude"]  # خطوط الطول
iss_position = (longitude, latitude)
print(iss_position)
