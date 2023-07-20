import sqlite3


def create_connection(database_file="data/my_currency.db"):
    """Create a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(database_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


def create_table(cursor):
    """Create the currency_prices table if it doesn't exist."""
    try:
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
    except sqlite3.Error as e:
        print(e)


if __name__ == "__main__":
    # This block of code runs when the database.py file is executed as a script
    # It creates the currency_prices table in the database
    conn = create_connection()
    cursor = conn.cursor()
    create_table(cursor)
    conn.commit()
    conn.close()
