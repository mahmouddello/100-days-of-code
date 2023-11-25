import os
import datetime as dt
import smtplib
import pandas as pd
import random
from dotenv import load_dotenv

load_dotenv("../../.env")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASS = os.getenv("MY_PASS")

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()

month = now.month
today = now.day

for index, row in df.iterrows():
    if row.month == month and row.day == today:
        with open(f"birthday letters/letter_{random.randint(1, 3)}.txt") as letter:
            mail = letter.read()
            mail = mail.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=row.email,
                                msg=f"Subject: Happy Birthday 🎂\n\n{mail}".encode("utf8"))
