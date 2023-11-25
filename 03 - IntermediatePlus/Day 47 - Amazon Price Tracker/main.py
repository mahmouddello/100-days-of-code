import requests
import os
import lxml
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv("D:/Python Environment Variables/.env.txt")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASS = os.getenv("MY_PASS")

PRODUCT_URL = "https://www.amazon.com.tr/Samsung-Galaxy-Kablosuz-Kulakl%C4%B1k-Ye%C5%9Fil/dp/B09GS74RX7?th=1"

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7,tr;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url=PRODUCT_URL, headers=headers).text

soup = BeautifulSoup(response, "lxml")
print(soup.prettify())

product_price = soup.find(name="span", class_="a-offscreen").text
print(product_price)

# target_price = 1250.0
#
# if product_price >= target_price:
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=MY_PASS)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="",
#             msg=f"The Product You have interest in is on sale now!".encode("utf-8")
#         )
