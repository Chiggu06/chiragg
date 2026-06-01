import os
import requests
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.api_key = os.environ.get("SHEETY_API_TOKEN")
        self.api_flight_endpoint = os.environ.get("SHEETY_FLIGHT_API")
        self.api_user_endpoint = os.environ.get("SHEETY_USER_API")
        self.header = {"Authorization": f"Bearer {self.api_key}"}

    def get_flight_data(self):
        response = requests.get(self.api_flight_endpoint, headers=self.header)
        response.raise_for_status()
        data = response.json()
        sheet_data = data["flight"]
        return sheet_data

    def put_flight_data(self, row_id, new_price):
        new_data = {
            "flight":
                {
                    "lowestPrice": new_price
                }
        }
        requests.put(f"{self.api_flight_endpoint}/{row_id}", json=new_data, headers=self.header)

    def get_user_data(self):
        response = requests.get(self.api_user_endpoint, headers=self.header)
        data = response.json()
        user_data = data["user"]
        return user_data