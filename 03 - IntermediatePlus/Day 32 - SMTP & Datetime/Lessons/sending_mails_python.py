import os
import smtplib
from dotenv import load_dotenv

load_dotenv("../../../.env")

my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASS")

# SMTP: Simple Mail Transfer Protocol
connection = smtplib.SMTP("smtp.gmail.com")  # SMTP Object
connection.starttls()  # TLS: Transfer Layer Security; way to secure our connection to our email service
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="mail@example.com",
    msg=f"Subject:Python Email\n\n Hello This an email sent by a python script")
# We add subject to make our sent mail doesn't get counted as a Spam
connection.close()

# with keyword: closes automatically after we sent the email

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # TLS: Transfer Layer Security; way to secure our connection to our email service
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="mail@example.com",
#         msg=f"Subject:Python Email\n\n Hello This an email sent by a python script")
