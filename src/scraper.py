import logging
import requests
from bs4 import BeautifulSoup
import datetime

logger = logging.getLogger(__name__)

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

def get_measurement(table_array, measurement):
    for table in table_array:
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if measurement.lower() in tds[0].get_text().lower():
                return(tds[1].get_text())

def scrape_currency_data():
    try:
        tickers = ["BRL/USD", "EUR/USD", "CHF/USD", "EUR/CHF"]
        gen_currency_data = []
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")

        for ticker in tickers:
            short_ticker = ticker.replace('/','')
            url = f"https://finance.yahoo.com/quote/{short_ticker}%3DX?p={short_ticker}%3DXs"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            currency_data = soup.find_all("table")
            # cur_data will contain multiple tables, next we examine each table one by one

            gen_currency_data.append({"ticker": ticker,
                                      "date": date,
                                      "open": float(get_measurement(currency_data, "open")),
                                      "high": float(get_measurement(currency_data, "day's range").split("-")[0]),
                                      "low": float(get_measurement(currency_data, "day's range").split("-")[-1]),
                                      "close": float(get_measurement(currency_data, "previous close")),
                                      })
        return gen_currency_data
    except Exception as e:
        logger.exception("An error occurred during web scraping")