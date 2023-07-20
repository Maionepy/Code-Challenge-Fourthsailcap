import sqlite3
import pytest
import os
from src.database import create_connection, create_table


def test_create_connection():
    # Test if the connection to the database can be established
    conn = create_connection()
    assert isinstance(conn, sqlite3.Connection)
    conn.close()


def test_create_table():
    # Test if the table is created successfully
    conn = create_connection(":memory:")
    cursor = conn.cursor()

    # Create the table
    create_table(cursor)

    # Check if the table exists in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='currency_prices'")
    result = cursor.fetchone()
    assert result is not None
    assert result[0] == "currency_prices"

    conn.close()