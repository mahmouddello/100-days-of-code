import requests

# parameters to pass in the request
parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # Raise Errors if needed

data = response.json()  # fetch json data, Dictionary

question_data = data["results"]  # fetch the results (questions)
