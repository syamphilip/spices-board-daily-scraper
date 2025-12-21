
def format_cardamom_message_list(data_list: list) -> str:
    message = "🌿 *Small Cardamom Auction Report*\n\n"

    for item in data_list:
        message += (
            f"🏢 *{item['auctioneer']}*\n"
            f"📅 Date: {item['date']}\n"
            f"📦 Lots: {item['lots']}\n"
            f"⚖️ Arrived: {float(item['qty_arrived']):,.1f} kg\n"
            f"✅ Sold: {float(item['qty_sold']):,.1f} kg\n"
            f"💰 Max: ₹{float(item['max_price']):,.2f}\n"
            f"📊 Avg: ₹{float(item['avg_price']):,.2f}\n"
            "----------------------\n"
        )

    return message
