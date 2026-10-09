
"""
data_cleaning.py
-----------------
Task 2: Load and clean the raw products and sales CSV files.
"""

import pandas as pd


def load_raw_data(products_path: str, sales_path: str):
    """Load both raw CSV files and return them as DataFrames."""
    products_df = pd.read_csv(products_path)
    sales_df = pd.read_csv(sales_path)

    return products_df, sales_df


def clean_products(products_df: "pd.DataFrame") -> "pd.DataFrame":
    """Clean products without changing the original DataFrame."""
    products = products_df.copy()

    # Remove exact duplicate rows.
    products = products.drop_duplicates()

    # Remove products that have no name because they cannot be
    # reliably identified by the store.
    products = products.dropna(subset=["product_name"])

    # Remove extra spaces from text values.
    products["product_name"] = products["product_name"].astype(str).str.strip()
    products["category"] = products["category"].astype(str).str.strip()

    # Standardise category capitalisation.
    products["category"] = products["category"].str.title()

    # Convert prices to numeric values.
    products["unit_price"] = pd.to_numeric(
        products["unit_price"], errors="coerce"
    )

    # Fill missing prices with the median price in the same category.
    # If the category has no available price, use the overall median.
    overall_median = products["unit_price"].median()

    for category in products["category"].unique():
        category_mask = products["category"] == category
        category_median = products.loc[
            category_mask, "unit_price"
        ].median()

        if pd.isna(category_median):
            category_median = overall_median

        products.loc[
            category_mask & products["unit_price"].isna(),
            "unit_price"
        ] = category_median

    # Remove rows if a valid price still cannot be obtained.
    products = products.dropna(subset=["unit_price"])

    # Ensure product IDs are consistently formatted.
    products["product_id"] = products["product_id"].astype(str).str.strip()

    return products.reset_index(drop=True)


def clean_sales(sales_df: "pd.DataFrame", valid_product_ids) -> "pd.DataFrame":
    """Clean sales and standardise their dates."""
    sales = sales_df.copy()

    # Remove exact duplicate rows.
    sales = sales.drop_duplicates()

    # Remove extra spaces from IDs and text columns.
    sales["product_id"] = sales["product_id"].astype(str).str.strip()

    # Convert quantities to numeric values.
    sales["quantity"] = pd.to_numeric(
        sales["quantity"], errors="coerce"
    )

    # Drop sales with missing or invalid quantities.
    sales = sales.dropna(subset=["quantity"])

    # Keep only positive whole-number quantities.
    sales = sales[
        (sales["quantity"] > 0)
        & (sales["quantity"] % 1 == 0)
    ].copy()
    sales["quantity"] = sales["quantity"].astype(int)

    # Parse dates in the formats used by the source CSV.
    # Day-first parsing is appropriate for dates such as 02/01/2026
    # in this dataset, which represents 2 January 2026.
    date_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%Y/%m/%d",
        "%d-%m-%Y",
    ]

    parsed_dates = pd.Series(
        pd.NaT, index=sales.index, dtype="datetime64[ns]"
    )

    for date_format in date_formats:
        missing_dates = parsed_dates.isna()
        parsed_dates.loc[missing_dates] = pd.to_datetime(
            sales.loc[missing_dates, "sale_date"],
            format=date_format,
            errors="coerce",
        )

    sales["sale_date"] = parsed_dates

    # Drop sales without a usable date because they cannot be placed
    # reliably in the sales trend.
    sales = sales.dropna(subset=["sale_date"]).copy()

    # Standardise dates to YYYY-MM-DD.
    sales["sale_date"] = sales["sale_date"].dt.strftime("%Y-%m-%d")

    # Use Unknown rather than guessing a missing payment method.
    sales["payment_method"] = (
        sales["payment_method"].fillna("Unknown").astype(str).str.strip()
    )
    sales.loc[
        sales["payment_method"] == "", "payment_method"
    ] = "Unknown"

    # Fill missing customer types honestly.
    sales["customer_type"] = (
        sales["customer_type"].fillna("Unknown").astype(str).str.strip()
    )
    sales.loc[
        sales["customer_type"] == "", "customer_type"
    ] = "Unknown"

    # Remove sales that refer to products not in the cleaned products table.
    valid_ids = set(valid_product_ids)
    sales = sales[sales["product_id"].isin(valid_ids)].copy()

    return sales.reset_index(drop=True)


def cleaning_summary(
    raw_df: "pd.DataFrame",
    clean_df: "pd.DataFrame",
    name: str
) -> str:
    """Summarise the number of rows before and after cleaning."""
    removed = len(raw_df) - len(clean_df)

    return (
        f"{name}: {len(raw_df)} raw rows -> "
        f"{len(clean_df)} clean rows ({removed} removed)"
    )