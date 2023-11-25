import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("D:/Python Environment Variables/.env.txt")  # load .env

USERNAME = os.getenv("pixela_username")
TOKEN = os.getenv("pixela_token")
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

# 1) Create your user account
# Call /v1/users API by HTTP POST.
# Source: https://docs.pixe.la/entry/post-user

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

user_response = requests.post(url=pixela_endpoint, json=user_parameters)  # we send the data in json format

# 2) Create a graph definition
# Call /v1/users/<username>/graphs by HTTP POST.
# Source: https://docs.pixe.la/entry/post-graph


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Sport Graph",
    "unit": "Km",
    "color": "ajisai",  # purple but in japanese :)
    "type": "float",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Note: We should provide the auth token as an HTTP Header
graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# 3) Get the graph!
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph !
# This is also /v1/users/<username>/graphs/<graphID> API.

# 4) Post value to the graph
# Call /v1/users/<username>/graphs/<graphID> by HTTP POST.

post_pixel_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Autofill today's date using strftime method from the datetime module
# Source: https://www.w3schools.com/python/python_datetime.asp

today = datetime.today()

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "25"
}

post_pixel_response = requests.post(url=post_pixel_url, json=post_pixel_params, headers=headers)

update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
updated_graph_config = {
    "name": "Cycling Graph",
    "unit": "Mi",
    "color": "ichou",
    "date": today.strftime("%Y%m%d"),
    "quantity": "19"
}

# update_response = requests.put(url=update_graph_endpoint, json=updated_graph_config, headers=headers)
# print(update_response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
