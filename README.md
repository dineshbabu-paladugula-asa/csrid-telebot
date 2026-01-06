# Telegram Survey Bot

A simple Python-based Telegram bot to collect user feedback.

## Features
- Collects product rating (1-5)
- Collects text feedback
- Collects recommendation (Yes/No)
- Stores data in-memory

## Prerequisites
- Python 3.8+
- Telegram Bot Token

## Installation

1. Clone the repository (or extract the zip):
   ```bash
   cd csrid-telegram-bot
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory (if not already present) and add your bot token:
   ```env
   TELEGRAM_BOT_TOKEN=your_token_here
   ```
   *(Note: A `.env` file with the provided token has been created for you)*

## Usage

1. Run the bot:
   ```bash
   python app/main.py
   ```

2. Open Telegram and search for your bot.
3. Send `/start` to begin the survey.

## Project Structure
```
csrid-telegram-bot/
 ├── app/
 │   ├── main.py       # Entry point
 │   ├── bot.py        # Logic and handlers
 │   ├── states.py     # Conversation states
 │   ├── storage.py    # In-memory storage
 │   └── settings.py   # Configuration
 ├── requirements.txt
 ├── .env
 └── README.md
```
