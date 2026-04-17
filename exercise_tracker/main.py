import requests
import os
import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup current date and time for logging
now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

# API Endpoints
TRACKER_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_API_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

# Authentication Headers
headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY"),
}

sheets_headers = {
    "Authorization": os.environ.get("AUTHORIZATION")
}

# User Input
exercise_text = input("Tell me what exercise you did and for how long? ")

exercise_parameters = {
    "query": exercise_text,
}

# Step 1: Send natural language query to Nutritionix
response = requests.post(TRACKER_API_ENDPOINT, headers=headers, json=exercise_parameters)
result = response.json()

# Step 2: Extract data and post to Google Sheets via Sheety
if "exercises" in result:
    for exercise in result["exercises"]:
        sheet_data = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }

        sheet_response = requests.post(
            SHEET_API_ENDPOINT,
            json=sheet_data,
            headers=sheets_headers
        )

        # Feedback to console
        if sheet_response.status_code == 200:
            print(f"Success! Logged {exercise['name']} to your sheet.")
        else:
            print(f"Error logging data: {sheet_response.text}")
else:
    print("Could not retrieve exercises. Check your API keys and input.")