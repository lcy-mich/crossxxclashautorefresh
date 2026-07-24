from flask import Flask
from scrape import CrossXXScraper

app = Flask(__name__)
scraper = CrossXXScraper()

@app.route("/freeclash/<protocol>")
def main(protocol):
    return scraper.get(protocol)