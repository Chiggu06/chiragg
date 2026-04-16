# Habit Tracker (Pixela API)

A habit-tracking automation tool that visualizes daily consistency using a customized intensity map. The system implements full CRUD functionality to manage habit data via encrypted endpoints.

## 🚀 Technical Stack
- **Language:** Python 3.10+
- **Libraries:** `requests`, `python-dotenv`, `datetime`
- **APIs:** Pixela (Graphing & Habit Data Visualization)

## 🏗️ Architecture & Data Flow
The application acts as a command-line interface (CLI) for the Pixela graphing service. It establishes a secure connection to the Pixela server via custom HTTP headers. When a user inputs their daily activity metric (e.g., hours of workout), the system processes the current date and dispatches a JSON payload to the specific graph endpoint. The server then updates the user's heatmap, reflecting the habit's intensity through color-coded levels.

## 📡 External APIs & Databases
- **Pixela API:** Management of graph creation, pixel plotting, and data visualization.
- **RESTful Methods:** Implements POST (add data), PUT (update data), and DELETE (remove data) requests.
- **Environment Variables (.env):** Secure storage for the `USERNAME`, `TOKEN`, and `GRAPH_ID` to maintain account privacy.

## 🛠️ Challenges Overcome
- **HTTP Header Authentication:** Implemented the `X-USER-TOKEN` header protocol to ensure secure authentication without exposing credentials in the URL parameters.
- **Data Formatting:** Utilized the `strftime` method to convert Python datetime objects into the specific `YYYYMMDD` string format required by the Pixela API.
- **Dynamic Endpoint Configuration:** Developed a modular URL construction system that allows the script to remain functional even if the `GRAPH_ID` or `USERNAME` is modified in the environment settings.
