import os
from twilio.rest import Client
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_no = os.environ.get("TWILIO_NO")
        self.my_no = os.environ.get("MY_NO")
        self.client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ.get("EMAIL_ID")
        self.email_password = os.environ.get("EMAIL_PASS")

    def send_message(self, flight_data):
        message = self.client.messages.create(
            body=f"Low price alert! Only Rs{flight_data.price} to fly from {flight_data.origin} to {flight_data.destination}, on {flight_data.outbound_date} until {flight_data.return_date}",
            from_= self.twilio_no,
            to= self.my_no,
        )

        print(f"SMS Sent successfully! Message ID: {message.sid}")

    def send_email(self, email_list, flight_data):
        with smtplib.SMTP(self.smtp_address) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.email_password)
            for mail in email_list:
                email_body = f"Subject: New Low Flight Deal!\n\nLow price alert! Only Rs{flight_data.price} to fly from {flight_data.origin} to {flight_data.destination}, on {flight_data.outbound_date} until {flight_data.return_date}"
                connection.sendmail(from_addr=self.email, to_addrs=mail, msg= email_body.encode("utf-8"))