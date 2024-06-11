from celery import shared_task
from .coinmarketcap import scrape_coinmarketcap

@shared_task
def run_scraping():
    return scrape_coinmarketcap()
