import requests
from bs4 import BeautifulSoup
import csv
import time

URL = "https://example.com"
HEADERS = {"User-Agent": "SIAG-Scraper/1.0 (+https://github.com/SIAG-Software)"}
OUTPUT_FILE = "data.csv"

def scrape():
    print(f"Scraping {URL} ...")
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to fetch page:", response.status_code)
        return

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("h2")

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title"])
        for item in items:
            writer.writerow([item.get_text(strip=True)])
            time.sleep(0.5)

    print(f"✅ Saved {len(items)} items to {OUTPUT_FILE}")

if __name__ == "__main__":
    scrape()
