import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, departure_id, arrival_id, outbound_date, return_date, currency):

        self.params = {
            "engine": "google_flights",
            "departure_id": departure_id,
            "arrival_id": arrival_id,
            "currency": currency,
            "type": "1",
            "outbound_date": outbound_date,
            "return_date": return_date,
            "api_key": os.environ.get("SERP_API_KEY")
        }

    def check_flights(self, total_stops="1"):

        self.params["stops"] = total_stops

        response = requests.get(API_ENDPOINT, params=self.params)
        if response.status_code != 200:
            print(f"check_flight status code: {response.status_code}")
            return None
        data = response.json()
        return data