# 🕸️ SIAG Software — Web Scraper Sample

A clean, professional demo scraper showing how SIAG Software structures Python-based scraping tools using:

- Requests  
- BeautifulSoup  
- Environment-based configuration  
- Modular architecture  
- CSV export pipeline  

Useful as a template for production scrapers or as a learning example.

---

## 🚀 Features

- Configurable via `.env`
- Isolated parser + exporter modules
- Clear project structure
- Basic error handling
- CSV exporting
- Easy to extend or adapt

---

## 📁 Project Structure

```
scraper-sample/
│
├── scraper/
│ ├── config.py
│ ├── scraper.py
│ ├── parser.py
│ └── exporter.py
│
├── data/
│ └── output.csv
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Create .env
bash
Copiar código
cp .env.example .env
Edit it:

ini
Copiar código
TARGET_URL=https://example.com
OUTPUT_FILE=data/output.csv
USER_AGENT=SIAG-Scraper/1.0
▶️ Running the scraper
bash
Copiar código
python -m scraper.scraper
Output is saved to:

bash
Copiar código
data/output.csv
🧩 How it works
1. Fetch page
Using requests with custom headers.

2. Parse HTML
parser.py extracts all <h2> tags.

3. Export
Results saved into a clean CSV file.

📦 Tech Stack
Python 3.10+

Requests

BeautifulSoup

python-dotenv

🧠 About SIAG Software
SIAG Software builds AI automations, chatbots, scrapers, workflow systems and full-stack solutions for small and modern businesses.

Contact:
siag.software@protonmail.com

Website coming soon.
