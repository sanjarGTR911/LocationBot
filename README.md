# 📍 Telegram Location Bot

A professional Telegram bot that converts user-inputted addresses into geolocation coordinates (latitude & longitude), displays the location on the map, and offers integration with Yandex Taxi and map view functionality.

---

## 🚀 Features

- Accepts user-inputted addresses
- Converts addresses to accurate locations
- Sends Telegram location message to users
- Integrates with Yandex for:
  - 🗺 Viewing the location on map
  - 🚕 Ordering a Yandex Taxi
- Clean and user-friendly design
- Built using Python & Telegram Bot API

---

## 🛠 Tech Stack

- Python 3.10+
- python-telegram-bot
- PostgreSQL
- Geocoding API (Yandex or others)
- PyCharm IDE
- Hosting (Heroku / Railway / VPS)

---

## 🧰 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sanjarGTR911/telegram_location_bot.git
   cd telegram_location_bot
   
## Install dependencies:

pip install -r requirements.txt

## Set up environment variables: Create a .env file and add your tokens and keys:

BOT_TOKEN=your_telegram_bot_token
YANDEX_API_KEY=your_yandex_api_key

## Run the bot:

python bot.py
