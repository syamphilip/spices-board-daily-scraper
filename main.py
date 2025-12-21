from data_format import format_cardamom_message_list
from scraper import fetch_small_cardamom_prices
from notifier import send_telegram
from dotenv import load_dotenv

PRODUCT_URL = "https://www.indianspices.com/marketing/price/domestic/daily-price.html"

def main():
    try:
        fetched_data = fetch_small_cardamom_prices(PRODUCT_URL)

        formatted_message = format_cardamom_message_list(fetched_data)
        send_telegram(formatted_message)
    except Exception as e:
        print("Error:", e)

load_dotenv()

if __name__ == "__main__":
    main()