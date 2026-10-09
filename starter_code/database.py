
"""
database.py
-----------
Create and manage the SQLite database for Thabo's Corner Store.
"""

import sqlite3
import pandas as pd


def create_database(db_path="store.db"):
    """Create the database tables and connect their product IDs."""
    connection = sqlite3.connect(db_path)

    cursor = connection.cursor()

    # Create the products table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            unit_price REAL NOT NULL,
            available INTEGER NOT NULL
        )
    """)

    # Create the sales table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id TEXT PRIMARY KEY,
            sale_date TEXT NOT NULL,
            product_id TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            payment_method TEXT NOT NULL,
            customer_type TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """)

    connection.commit()
    return connection


def insert_data(connection, products_df, sales_df):
    """Insert cleaned products and sales into the database."""
    cursor = connection.cursor()

    # Enable foreign key checking.
    cursor.execute("PRAGMA foreign_keys = ON")

    # Clear old records so repeated runs do not duplicate data.
    cursor.execute("DELETE FROM sales")
    cursor.execute("DELETE FROM products")

    # Insert cleaned product records.
    for _, row in products_df.iterrows():
        cursor.execute("""
            INSERT INTO products
            (product_id, product_name, category, unit_price, available)
            VALUES (?, ?, ?, ?, ?)
        """, (
            str(row["product_id"]),
            str(row["product_name"]),
            str(row["category"]),
            float(row["unit_price"]),
            int(bool(row["in_stock"]))
        ))

    # Insert cleaned sales records.
    for _, row in sales_df.iterrows():
        cursor.execute("""
            INSERT INTO sales
            (sale_id, sale_date, product_id, quantity,
             payment_method, customer_type)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            str(row["sale_id"]),
            str(row["sale_date"]),
            str(row["product_id"]),
            int(row["quantity"]),
            str(row["payment_method"]),
            str(row["customer_type"])
        ))

    connection.commit()


def run_query(connection, query, parameters=()):
    """Run an SQL query and return its results as a DataFrame."""
    return pd.read_sql_query(query, connection, params=parameters)