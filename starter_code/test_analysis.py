
from data_cleaning import load_raw_data, clean_products, clean_sales

from analysis import (
    total_sales_records,
    low_stock_alert,
    monthly_sales_trend,
    classify_transaction_size,
    average_basket_size,
)


def main():
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

    print(
        "Transaction examples:",
        classify_transaction_size(1),
        classify_transaction_size(3),
        classify_transaction_size(5),
        classify_transaction_size(0)
    )

    print("Average basket size:", average_basket_size(sales_rows))


if __name__ == "__main__":
    main()
