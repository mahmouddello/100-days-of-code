import os
import datetime as dt
import smtplib
import random
from dotenv import load_dotenv

load_dotenv("../../../.env")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASS = os.getenv("MY_PASS")

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 5:  # if day of the week is Monday
    with open("../Lessons/quotes.txt", mode="r") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # TLS: Transfer Layer Security; a way to secure our connection to our email service
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="mail@example.com",
            msg=f"Subject: Monday Motivation :D\n\n{quote}"
        )
