import requests
import time

from .config import TARGET_URL, USER_AGENT, OUTPUT_FILE
from .parser import parse_titles
from .exporter import export_to_csv


def scrape():
    print(f"🔍 Fetching: {TARGET_URL}")

    try:
        response = requests.get(TARGET_URL, headers={"User-Agent": USER_AGENT})
        response.raise_for_status()
    except Exception as e:
        print("❌ Request failed:", e)
        return

    print("📦 Parsing HTML...")
    titles = parse_titles(response.text)

    print(f"💾 Exporting {len(titles)} items → {OUTPUT_FILE}")
    export_to_csv(OUTPUT_FILE, titles)

    time.sleep(0.5)
    print("✅ Done!")


if __name__ == "__main__":
    scrape()
