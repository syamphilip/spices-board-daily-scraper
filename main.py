from flask import Flask,jsonify
import os
from data_format import format_cardamom_message_list
from scraper import fetch_small_cardamom_prices
from dotenv import load_dotenv

load_dotenv()

PRODUCT_URL = "https://www.indianspices.com/marketing/price/domestic/daily-price.html"

app = Flask(__name__)

def run_scraper():
    try:
        fetched_data = fetch_small_cardamom_prices(PRODUCT_URL)
        response = format_cardamom_message_list(fetched_data)
        return jsonify({
            "success": True,
            "count": len(response),
            "data": response
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
    
@app.route("/")
def health():
    return "Spices Board Scraper is running"

@app.route("/run")
def run():
    try:
       return run_scraper()
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
