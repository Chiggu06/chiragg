import requests_cache
from datetime import datetime, timedelta
from data_manager import  DataManager
from flight_search import FlightSearch
from flight_data import check_cheap_flight
from notification_manager import NotificationManager

origin_code = "BLR"

data_manager = DataManager()
user_data = data_manager.get_user_data()
notification_manager = NotificationManager()

requests_cache.install_cache("flight_cache.sqlite", urls_expire_after = {"*.sheety.co*": requests_cache.DO_NOT_CACHE, "*": 3600})

user_email_list = [row["enterYourEmailId"] for row in user_data]

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_months_from_now =  (datetime.now() + timedelta(days=30*6)).strftime("%Y-%m-%d")

sheet_data = data_manager.get_flight_data()

for row in sheet_data:
    destination_code = row["iataCode"]
    city_name = row["city"]

    print(f"\nChecking flights for {city_name}: {destination_code}")

    search = FlightSearch(origin_code, destination_code, tomorrow, six_months_from_now, "INR")

    flight_data = search.check_flights()
    cheapest_flight = check_cheap_flight(flight_data, six_months_from_now)

    if cheapest_flight.price == "N/A":
        print("Direct flight not found. Searching for flights with 1-stop")
        flight_data = search.check_flights(total_stops="2")
        cheapest_flight = check_cheap_flight(flight_data, six_months_from_now)

    if cheapest_flight.price == "N/A":
        print("1-stop flight not found. Searching for flights with more than 1-stop as last resort")
        flight_data = search.check_flights(total_stops="0")
        cheapest_flight = check_cheap_flight(flight_data, six_months_from_now)

    if cheapest_flight.price != "N/A":
        print(f"Best flight to {city_name}: Rs. {cheapest_flight.price}")

        if cheapest_flight.price < row["lowestPrice"]:
            print("Cheaper price found! Updating spreadsheet and sending SMS")
            data_manager.put_flight_data(row["id"], cheapest_flight.price)
            notification_manager.send_message(cheapest_flight)
            notification_manager.send_email(user_email_list, cheapest_flight)
        else:
            print("Not cheaper than the sheet. No update sent.")
    else:
        print(f"Sorry, there are no flights found to {city_name}")