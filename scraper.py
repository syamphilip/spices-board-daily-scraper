import requests
from bs4 import BeautifulSoup


def fetch_small_cardamom_prices(URL):
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # 1️⃣ Find the correct heading
    heading = soup.find("h2", string=lambda x: x and "Small Cardamom" in x)

    if not heading:
        raise Exception("Small Cardamom heading not found")

    # 2️⃣ Get the table right after this heading
    table = heading.find_next("table")

    rows = table.find_all("tr")[2:]  # skip title + header rows

    data = []

    for row in rows:
        cols = [td.text.strip() for td in row.find_all("td")]

        if len(cols) < 8:
            continue

        record = {
            "sno": cols[0],
            "date": cols[1],
            "auctioneer": cols[2],
            "lots": cols[3],
            "qty_arrived": cols[4],
            "qty_sold": cols[5],
            "max_price": cols[6],
            "avg_price": cols[7],
        }

        data.append(record)

    return data
