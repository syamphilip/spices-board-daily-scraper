from flask import Flask
import os
from data_format import format_cardamom_message_list
from scraper import fetch_small_cardamom_prices
from notifier import send_telegram
from dotenv import load_dotenv

load_dotenv()

PRODUCT_URL = "https://www.indianspices.com/marketing/price/domestic/daily-price.html"

app = Flask(__name__)

def run_scraper():
    fetched_data = fetch_small_cardamom_prices(PRODUCT_URL)
    formatted_message = format_cardamom_message_list(fetched_data)
    send_telegram(formatted_message)

@app.route("/")
def health():
    return "Spices Board Scraper is running"

@app.route("/run")
def run():
    try:
        run_scraper()
        return "Scraping completed successfully"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
