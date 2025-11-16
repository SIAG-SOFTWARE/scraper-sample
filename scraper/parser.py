from bs4 import BeautifulSoup

def parse_titles(html: str):
    soup = BeautifulSoup(html, "html.parser")
    return [tag.get_text(strip=True) for tag in soup.find_all("h2")]
