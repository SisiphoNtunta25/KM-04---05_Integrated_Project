"""
analysis.py
------------
Task 4: Programming logic — functions, loops, conditionals and arrays.

This module covers KM-05 topics: Programming Basics (data types,
conditionals, loops, arrays/lists, functions) and Introduction to
Algorithms.

IMPORTANT: For this file, use plain Python (for-loops, if/else,
lists and dictionaries) even where pandas could do it in one line.
The point of this section is to demonstrate the programming
fundamentals from KM-05, not just pandas shortcuts.
"""


def total_sales_records(sales_rows: list) -> int:
    """
    Count the number of sales records using a loop.
    """
    count = 0
    for row in sales_rows:
        count += 1
    return count

def low_stock_alert(products_rows: list, threshold: int = 5) -> list:
    """
    Return a list of product names where in_stock is False, OR where
    you decide a product should be flagged (use a conditional / if
    statement here — this is the KM-05 "conditionals" checkpoint).

    Args:
        products_rows: list of dictionaries, one per product
        threshold: (optional) use this if you extend the dataset with
            a stock-count column later

    Returns:
        a list of product_name strings that need re-ordering.
    """
    
    alerts = []

    for product in products_rows:
        if product["in_stock"] == False:
            alerts.append(product["product_name"])

    return alerts


def monthly_sales_trend(sales_rows: list) -> dict:
    """
    Build a dictionary that maps each month (e.g. "2026-01") to the
    total quantity sold that month, using a loop.

    Args:
        sales_rows: list of dictionaries, one per sale, each with a
            "sale_date" key already cleaned to "YYYY-MM-DD" format
            and a "quantity" key (as an int)

    Returns:
        a dict like {"2026-01": 143, "2026-02": 97}

    TODO:
        trend = {}
        for row in sales_rows:
            month = row["sale_date"][:7]        # "YYYY-MM"
            if month in trend:
                trend[month] += row["quantity"]
            else:
                trend[month] = row["quantity"]
        return trend
    """
    
    trend = {}

    for row in sales_rows:
        month = row["sale_date"][:7]

        if month in trend:
            trend[month] += row["quantity"]
        else:
            trend[month] = row["quantity"]

    return trend


def classify_transaction_size(quantity: int) -> str:
    """
    A small function that demonstrates if / elif / else.

    Rules:
        quantity >= 5   -> "Bulk"
        quantity >= 2   -> "Multiple"
        quantity == 1   -> "Single"
        anything else   -> "Invalid"

    TODO: implement the if / elif / else chain above.
    """
    
    if quantity >= 5:
        return "Bulk"
    elif quantity >= 2:
        return "Multiple"
    elif quantity == 1:
        return "Single"
    else:
        return "Invalid"



def average_basket_size(sales_rows: list) -> float:
    """
    Calculate the average quantity per sale across all sales.
    Return the result rounded to two decimal places.
    """
    if not sales_rows:
        return 0.0

    total = 0

    for row in sales_rows:
        total += row["quantity"]

    return round(total / len(sales_rows), 2)
from data_cleaning import load_raw_data, clean_products, clean_sales
from analysis import (
    total_sales_records,
    low_stock_alert,
    monthly_sales_trend,
    classify_transaction_size,
    average_basket_size,
)

products, sales = load_raw_data(
    "data/products.csv",
    "data/sales.csv"
)

clean_products_df = clean_products(products)
clean_sales_df = clean_sales(
    sales,
    clean_products_df["product_id"]
)
product_rows = clean_products_df.to_dict("records")
sales_rows = clean_sales_df.to_dict("records")

print("Sales records:", total_sales_records(sales_rows))
print("Low-stock alerts:", low_stock_alert(product_rows))
print("Monthly trend:", monthly_sales_trend(sales_rows))
print("Transaction examples:",
      classify_transaction_size(1),
      classify_transaction_size(3),
      classify_transaction_size(5),
      classify_transaction_size(0))
print("Average basket size:", average_basket_size(sales_rows))