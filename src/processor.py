import sqlite3


def process_currency_data(currency_data):
    # Process the currency data as per your requirements
    # and store it into the SQLite database

    conn = sqlite3.connect("data/my_currency.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS currency_prices (
            ticker TEXT,
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            PRIMARY KEY (ticker, date)
        )
        """
    )

    # Insert the processed data into the table
    for data in currency_data:
        ticker = data["ticker"]
        date = data["date"]
        open_price = data["open"]
        high_price = data["high"]
        low_price = data["low"]
        close_price = data["close"]

        cursor.execute(
            """
            INSERT OR REPLACE INTO currency_prices
            (ticker, date, open, high, low, close)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (ticker, date, open_price, high_price, low_price, close_price),
        )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()