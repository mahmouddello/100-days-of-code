import os
import requests
import re
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("../../.env")  # .env path

# as per recommendation from @freylis, compile once only
CLEANER = re.compile('<.*?>')  # clear string from html tags

# ------------------------------- CONSTANTS -------------------------------
STOCK = "META"
COMPANY_NAME = "Meta Platforms Inc"
STOCK_API_KEY = os.getenv("ALPHA_VANTAGE_KEY")  # alphavantage api key
NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # newsapi api key
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = " https://newsapi.org/v2/everything"
TWILIO_ACC_SID = os.getenv("ACC_SID")
TWILIO_AUTH_TOKEN = os.getenv("AUTH_TOKEN")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "datatype": "json"
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]  # hold the dates in a list for easy access

yesterday_data = data_list[0]  # holds the yesterday data from the data_list
yesterday_closing_price = float(yesterday_data["4. close"])  # fetch yesterday's closing price

day_before_yesterday_data = data_list[1]  # holds the day before yesterday's data
day_before_yesterday_price = float(
    day_before_yesterday_data["4. close"])  # fetch the day before yesterday's closing price

up_down = None

difference = yesterday_closing_price - day_before_yesterday_price

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percentage = round((difference / yesterday_closing_price) * 100)  # calculate the difference in percentage

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if diff_percentage > -1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title,description,content",
        "pageSize": 5
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters).json()
    articles = news_response["articles"]
    three_articles = articles[:3]

    formatted_articles = [
        f"Headline: {article['title']} \nDescription: {re.sub(CLEANER, '', article['description'])} \nLink: {article['url']}"
        for article
        in three_articles]

    twilio_client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = twilio_client.messages.create(
            body=f"{STOCK}: {up_down}{diff_percentage}%\n {article}",
            from_=os.getenv("TWILIO_NUM"),
            to=os.getenv("MY_NUM")
        )
        print(message.status)
