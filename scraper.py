import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        req = urllib.request.Request(
            self.site,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        
        with urllib.request.urlopen(req) as r:
            html = r.read()

        soup = BeautifulSoup(html, "html.parser")
        
        for card in soup.find_all("a", class_="offer-card"):
            title = card.find("h3")
            company = card.find("p", class_="offer-company")
            location = card.find("span", class_="offer-location")
            link = "https://justjoin.it" + card.get("href")
            
            print("Stanowisko:", title.text.strip() if title else "")
            print("Firma:", company.text.strip() if company else "")
            print("Miasto:", location.text.strip() if location else "")
            print("Link:", link)
            print("-" * 40)

url = "https://justjoin.it/"
Scraper(url).scrape()
