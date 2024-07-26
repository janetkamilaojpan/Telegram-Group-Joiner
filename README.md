# Telegram Group Joiner

This Python script automates the process of joining multiple Telegram groups using invite links. It leverages the Telethon library to interact with the Telegram API and handles various exceptions that might occur during the joining process, such as rate limiting and user privacy restrictions.

## Features

- Reads configuration from a JSON file.
- Initializes a Telegram client session.
- Joins multiple Telegram groups using invite links.
- Handles common errors such as rate limits and privacy restrictions.
- Uses color-coded output for easy readability.

## Requirements

- Python 3.9+

## Installation

1. Clone the repository or download the script.

2. Prepare a `config.json` file in the same directory as `joiner.py` with the following structure:

   ```json
   {
       "api_id": "YOUR_API_ID",
       "api_hash": "YOUR_API_HASH",
       "phone_number": "YOUR_PHONE_NUMBER",
       "invite_links": [
           "https://t.me/joinchat/AAAAAE1KXl2G1b4Z8zL3PQ",
           "https://t.me/joinchat/BBBBBF2KXl2G2c4Z8zL3PQ"
       ]
   }
   ```

## Usage

1. Ensure your `config.json` file is correctly set up.

2. Run `start.bat`

## Notes

- Ensure that the `config.json` file is correctly formatted and contains valid data.
- Make sure to replace the placeholder values in the `config.json` file with your actual Telegram API credentials and invite links.
