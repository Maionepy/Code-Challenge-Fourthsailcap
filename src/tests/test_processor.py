import pytest
import sqlite3
import pandas as pd
from src.processor import process_currency_data

def test_processor():
    # Mock the currency data (replace this with actual test data if possible)
    currency_data = [
        {
            "ticker": "BRL/USD",
            "date": "2023-07-12",
            "open": 5.2,
            "high": 5.3,
            "low": 5.1,
            "close": 5.25,
        },
        # Add more test data as needed
    ]

    # Call the process_currency_data function
    process_currency_data(currency_data)

    # Check if the data is stored correctly in the database
    conn = sqlite3.connect(":memory:")  # Use an in-memory database for testing
    cursor = conn.cursor()

    # Retrieve the data from the table
    cursor.execute("SELECT * FROM currency_prices")
    results = cursor.fetchall()

    # Make sure the correct number of rows are inserted
    assert len(results) == len(currency_data)

    # Check if each row in the database matches the corresponding item in currency_data
    for i, data in enumerate(currency_data):
        assert results[i][0] == data["ticker"]
        assert results[i][1] == data["date"]
        assert results[i][2] == data["open"]
        assert results[i][3] == data["high"]
        assert results[i][4] == data["low"]
        assert results[i][5] == data["close"]

    # Close the connection
    conn.close()
