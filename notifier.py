import requests
import os

def send_telegram(msg: str):
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    print(BOT_TOKEN, CHAT_ID)

    url="https://api.telegram.org/bot{}/sendMessage".format(BOT_TOKEN)

    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Failed to send message:", response.text)
    else:
        print("Message sent successfully")