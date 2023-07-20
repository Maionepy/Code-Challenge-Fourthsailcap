import pytest
from src.scraper import scrape_currency_data


def test_scraper():
    currency_data = scrape_currency_data()
    assert isinstance(currency_data, list)
    assert len(currency_data) > 0
