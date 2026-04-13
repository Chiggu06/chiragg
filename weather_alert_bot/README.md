# Weather Alert Bot

A professional automation tool designed to monitor weather patterns and deliver proactive SMS alerts, integrated into a backend development portfolio.

## 🚀 Technical Stack
- **Language:** Python 3.10+
- **APIs:** OpenWeatherMap (JSON Data Parsing), Twilio (SMS Gateway)
- **Libraries:** requests, schedule, python-dotenv

## 🏗️ Architecture & Data Flow
1. **Scheduler:** A background daemon triggers the application daily at a specified time (8:00 AM).
2. **Data Acquisition:** Fetching a 5-day/3-hour forecast via OpenWeatherMap API using custom coordinates.
3. **Logic Engine:** Parsing nested JSON to identify precipitation condition codes (< 700) within a 12-hour window.
4. **Notification:** Initializing a Twilio REST client to dispatch an SMS alert if rain is detected.

## 🔑 API & Credential Setup
To run this project, you will need to obtain credentials from the following services:

### **1. OpenWeatherMap**
- **Where to find:** [OpenWeatherMap API Keys Page](https://home.openweathermap.org/api_keys)
- **Key needed:** `OWM_API_KEY` (Generated after creating a free account).

### **2. Twilio**
- **Where to find:** [Twilio Console Dashboard](https://www.twilio.com/console)
- **Keys needed:** - `TWILIO_ACCOUNT_SID`: Found on the main Account Info pane.
    - `TWILIO_AUTH_TOKEN`: Found right below the SID (click "View" to reveal).
    - `TWILIO_NUMBER`: Found in the "Phone Numbers" section after purchasing a trial number.

## 📡 External APIs & Databases
- **OpenWeatherMap API:** Used for real-time meteorological forecasting.
- **Twilio API:** Leveraged for automated telecommunications and SMS delivery.

## 🛠️ Challenges Overcome
- **Environment Security:** Successfully implemented `.env` masking to ensure API credentials are never exposed in version control.
- **Data Extraction:** Navigated complex JSON responses to isolate specific weather condition IDs from time-series data.
- **Automation:** Implemented a persistent event loop using the `schedule` library for time-accurate execution.

## 💻 Installation (macOS/Linux)
1. Ensure Python 3 is installed.
2. Clone the repository and navigate to the project folder.
3. Install dependencies:
   ```bash
   pip install requests twilio schedule python-dotenv
