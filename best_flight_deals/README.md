# Flight Deals Tracker

A professional Python backend service part of a larger backend engineering portfolio.

## 🚀 Technical Stack
- **Language:** Python 3
- **Libraries:** requests, twilio, python-dotenv, requests-cache, smtplib

## 🏗️ Architecture & Data Flow
Object-Oriented backend service automating flight price tracking. It queries a Google Sheet for target destinations, searches live flight data with tiered fallback logic (Direct -> 1-stop -> Multi-stop), updates the database if a cheaper flight is found, and dispatches multi-channel alerts (SMS & Email) to subscribed users.

## 📡 External APIs & Databases
- SerpAPI (Google Flights Engine)
- Sheety API (Google Sheets Database)
- Twilio API (SMS Notifications)
- SMTP Server (Email Notifications)

## 🛠️ Challenges Overcome
- Engineered a robust tiered fallback search logic to prevent application crashes when airlines omit pricing data or direct flights are unavailable.
- Managed complex secure credential handling using environment variables and `.gitignore`.
- Handled safe SMTP context management to prevent connection drops during batch email sending.

## 💻 Installation (WSL/Linux)
1. Ensure Python 3 is installed.
2. Install dependencies: `pip install requests twilio python-dotenv requests-cache`
3. Set up environment variables: 
   - Rename `.env.example` to `.env` and fill in your Twilio, SerpAPI, Sheety, and Email credentials.
4. Run the application:
   ```bash
   python3 main.py
