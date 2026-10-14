
"""
visualize.py
-------------
Create and save charts for Thabo's Corner Store.
"""

import matplotlib.pyplot as plt


def bar_chart_revenue_per_product(
    product_names: list,
    revenues: list,
    save_path: str = "revenue_per_product.png"
):
    """Create and save a bar chart of revenue per product."""

    plt.figure(figsize=(10, 6))
    plt.bar(product_names, revenues)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Revenue (R)")
    plt.xlabel("Product")
    plt.title("Total Revenue per Product — Thabo's Corner Store")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

    print(f"Bar chart saved to {save_path}")


def line_chart_monthly_trend(
    monthly_trend: dict,
    save_path: str = "monthly_trend.png"
):
    """Create and save a line chart of monthly sales quantities."""

    months = list(monthly_trend.keys())
    totals = list(monthly_trend.values())

    plt.figure(figsize=(8, 5))
    plt.plot(months, totals, marker="o")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.title("Monthly Sales Trend — Thabo's Corner Store")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

    print(f"Line chart saved to {save_path}")
