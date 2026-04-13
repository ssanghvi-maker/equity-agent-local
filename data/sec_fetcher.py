import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Local Agent your@email.com"}


def get_latest_10k(cik: str):
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    data = requests.get(url, headers=HEADERS).json()

    filings = data["filings"]["recent"]

    for i, form in enumerate(filings["form"]):
        if form == "10-K":
            accession = filings["accessionNumber"][i].replace("-", "")
            doc = filings["primaryDocument"][i]

            filing_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession}/{doc}"
            html = requests.get(filing_url, headers=HEADERS).text

            soup = BeautifulSoup(html, "html.parser")
            return soup.get_text()

    return None
