import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# --- CONFIGURATION FROM .ENV ---
U_NAME = os.environ.get("USERNAME")
U_TOKEN = os.environ.get("TOKEN")
GRAPH_ID = os.environ.get("GRAPH_ID") # Now pulled from .env

# --- API ENDPOINTS ---
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{U_NAME}/graphs"
# This endpoint points directly to your specific graph
SPECIFIC_GRAPH_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

# Security Headers
headers = {
    "X-USER-TOKEN": U_TOKEN
}

# --- 1. POST DATA (ADD PIXEL) ---
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

print(f"--- Logging for {today.strftime('%B %d, %Y')} ---")
workout_duration = input(f"How many hours of {GRAPH_ID} did you complete? ")

pixel_parameters = {
    "date": formatted_date,
    "quantity": workout_duration,
}

# Add the pixel to the graph
response = requests.post(url=SPECIFIC_GRAPH_ENDPOINT, json=pixel_parameters, headers=headers)

# Use raise_for_status to catch connection errors early
response.raise_for_status()
print(f"Server Response: {response.text}")

# --- VIEW RESULTS ---
# Open this URL in your browser to see your progress:
print(f"View your graph here: https://pixe.la/v1/users/{U_NAME}/graphs/{GRAPH_ID}.html")