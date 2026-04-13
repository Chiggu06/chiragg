Stock News Alert
An automated financial monitoring system that correlates stock market volatility with global news headlines and delivers real-time SMS notifications.

🚀 Technical Stack
Language: Python 3.10+

Libraries: requests, python-dotenv, twilio

APIs: Alpha Vantage (Market Data), NewsAPI (Global News), Twilio (SMS Gateway)

🏗️ Architecture & Data Flow
The application monitors specific ticker symbols (e.g., TSLA, IBM) using a daily time-series feed. When the percentage variance between the last two closing prices exceeds a defined threshold (e.g., 1%), the system triggers a contextual search for related news, formats the top headline, and dispatches an SMS alert via the Twilio API.

📡 External APIs & Databases
Alpha Vantage: Time-series stock data fetching.

NewsAPI: Search and extraction of trending financial articles.

Twilio: Cloud communications for mobile SMS delivery.

Environment Variables (.env): Secure storage for API credentials and private keys.

🛠️ Challenges Overcome
API Rate Limit Management: Implemented defensive checks to handle provider-side request limits without script failure.

Payload Optimization: Managed SMS character constraints by truncating headlines and formatting multi-line content for mobile readability.

Security Protocols: Migrated hardcoded credentials to a robust .env structure to ensure secure version control practices.

💻 Installation (macOS/Linux)
Ensure Python 3 is installed.

Clone the repository and navigate to the project folder.

Install dependencies:

Bash
pip install requests python-dotenv twilio
Configure your environment:

Rename .env.example to .env.

Add your API keys and phone numbers to the .env file.

Run the application:

Bash
python3 main.py