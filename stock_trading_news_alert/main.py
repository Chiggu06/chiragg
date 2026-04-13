import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("STOCK_API_KEY")
}

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

stock_response = requests.get("https://www.alphavantage.co/query?", params=stock_parameters)
stock_response.raise_for_status()
stocks_data = stock_response.json()

if "Time Series (Daily)" not in stocks_data:
    print("API Error or Rate Limit reached:", stocks_data.get("Note", "Unknown Error"))
else:
    close_price = stocks_data["Time Series (Daily)"]

    dates = [date for date in close_price.keys()]
    yesterday_date = dates[0]
    day_before_date = dates[1]

    required_data = [value for (key, value) in close_price.items()]
    yesterday_close = required_data[0]["4. close"]
    day_before_close = required_data[1]["4. close"]

    close_difference = float(yesterday_close) - float(day_before_close)
    close_per = (close_difference / float(day_before_close)) * 100

    if close_difference > 0:
        emoji = "🔺"
    else:
        emoji = "🔻"

    if abs(close_per) > 0.5:
        news_parameters = {
            "q": COMPANY_NAME,
            "from": yesterday_date,
            "sortBy": "popularity",
            "apiKey": os.environ.get("NEWS_API_KEY"),
        }

        news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
        news_response.raise_for_status()
        news_data = news_response.json()

        if news_data["articles"]:
            articles = news_data["articles"][1]
            content = f"Headline: {articles['title']}\n"
            message_body = f"{STOCK}: {emoji}{close_per:.2f}%\n{content}"
            message = client.messages.create(
                body=message_body,
                from_=os.environ.get("TWILIO_NO"),
                to=os.environ.get("MY_NO"),
            )
        else:
            message = client.messages.create(
                body=f"The difference was {close_difference:.2f} which is {close_per:.2f}%\nNo news articles found for this date.",
                from_=os.environ.get("TWILIO_NO"),
                to=os.environ.get("MY_NO"),
            )



