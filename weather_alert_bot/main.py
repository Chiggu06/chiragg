import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import time

load_dotenv()


def check_weather_and_send_sms():
    # twilio
    account_sid = os.environ.get("ACCOUNT_ID")
    auth_token = os.environ.get("AUTH_TOKEN")
    twilio_no = "+16064986146"
    my_no = os.environ.get("MY_NO")

    # OpenWeather
    api_key = os.environ.get("OW_API_KEY")

    parameters = {
        "lat": 29.288420,
        "lon": 117.200142,
        "cnt": 4,
        "appid": api_key
    }

    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
        response.raise_for_status()
        data = response.json()

        is_raining = False
        for weather_check in data["list"]:
            weather_id = weather_check["weather"][0]["id"]
            if weather_id < 700:
                is_raining = True

        if is_raining:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body="It might rain today. Don't forget an umbrella! ☔",
                from_=twilio_no,
                to=my_no,
            )
            print(f"SMS Sent! Status: {message.status}")
        else:
            print("No rain forecast. No SMS sent.")

    except Exception as e:
        print(f"An error occurred: {e}")

print("Rain Alert Daemon started...")
while True:
    local_time = time.localtime()
    if local_time.tm_hour == 8 and local_time.tm_min == 0:
        print("It's 8 AM! Running weather check...")
        check_weather_and_send_sms()
        time.sleep(61)

    time.sleep(30)