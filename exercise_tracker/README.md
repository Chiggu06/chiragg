# Workout & Nutrition Tracker

A professional Python application part of a larger full-stack portfolio, leveraging NLP to automate health data logging.

## 🚀 Technical Stack
- **Language:** Python 3.13+
- **Libraries:** requests, python-dotenv, os, datetime

## 🏗️ Architecture & Data Flow
Processes natural language user input via the Nutritionix NLP engine to extract exercise metrics, then synchronizes that data to a remote Google Sheet using RESTful API calls via Sheety.

## 📡 External APIs & Setup

### 1. Google Sheets Configuration
- Create a new Google Sheet.
- Rename the bottom tab (sheet name) to `workouts`.
- Add these exact headers to the first row: `Date`, `Time`, `Exercise`, `Duration`, `Calories`.

### 2. Nutritionix API (NLP Logic)
- Register at [Nutritionix Developers](https://developer.nutritionix.com/).
- Retrieve your `APP_ID` and `APP_KEY` from the dashboard.

### 3. Sheety API (REST Integration)
- Connect your Google Sheet at [Sheety.co](https://sheety.co/).
- Enable **POST** requests in the project settings.
- Enable **Bearer Token** authentication and define your secret token.

## 🛠️ Challenges Overcome
- Successfully implemented **Bearer Token Authorization** for secure API communication and handled **JSONDecodeErrors** by implementing response status checks to ensure data integrity.

## 💻 Installation (WSL/Linux)
1. Ensure Python 3 is installed.
2. Install dependencies: 
   ```bash
   pip install requests python-dotenv
