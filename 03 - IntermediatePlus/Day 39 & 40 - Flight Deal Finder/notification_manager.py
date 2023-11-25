import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("../../.env")

account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, message):
        client = Client(account_sid, auth_token)
        msg = client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_NUM"),
            to=os.getenv("MY_NUM")
        )
        print(msg.status)
