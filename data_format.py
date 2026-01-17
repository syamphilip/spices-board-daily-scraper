def format_cardamom_message_list(data_list: list) -> list:
    return [
        {
            "auctioneer": item["auctioneer"],
            "date": item["date"],
            "lots": int(item["lots"]),
            "qty_arrived": float(item["qty_arrived"]),
            "qty_sold": float(item["qty_sold"]),
            "max_price": float(item["max_price"]),
            "avg_price": float(item["avg_price"]),
        }
        for item in data_list
    ]
