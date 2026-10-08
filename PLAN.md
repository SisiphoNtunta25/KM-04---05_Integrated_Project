# Thabo's Corner Store — Sales Insights System

## 1. Project Overview

The purpose of this project is to clean, store, analyse and visualise sales data for Thabo's Corner Store. The system will use Python and SQLite to help Thabo understand his sales and make better business decisions.

## 2. Computational Thinking

### Decomposition

I will break the project into smaller tasks:

1. Inspect the products and sales CSV files.
2. Clean the product and sales data.
3. Store the cleaned data in a SQLite database.
4. Create SQL queries to retrieve useful business information.
5. Analyse the sales data using Python.
6. Create charts to show sales trends and product performance.
7. Add password security to protect the system.
8. Document the project and business findings.

### Pattern Recognition

While inspecting the data, I identified several repeated data quality problems.

The products data contains:

* Missing product names.
* Missing unit prices.
* Inconsistent category capitalisation.
* Duplicate product records.

The sales data contains:

* Missing quantities.
* Missing dates.
* Missing payment methods.
* Missing customer types.
* Dates written in different formats.
* Invalid product IDs such as P099.
* Duplicate sale IDs.

These patterns will be handled consistently during the data-cleaning stage.

### Abstraction

I will focus on the information needed for the store's sales system.

The main entities are:

* **Products** — product ID, product name, category, unit price and stock status.
* **Sales** — sale ID, product ID, quantity, sale date, payment method and customer type.

The product ID will connect the sales table to the products table.

## 3. Data Cleaning Approach

I will clean the data without changing the original CSV files.

For missing product names, I will use a suitable value such as "Unknown Product" where necessary.

For missing prices, I will use a reasonable value based on the available product information or clearly document the decision.

Categories will be standardised so that values such as `beverages` become `Beverages`.

Duplicate product records will be removed.

Sales dates will be converted into one standard date format.

Missing quantities will be handled using a documented rule.

Missing payment methods and customer types will be replaced with suitable values such as `Unknown` where necessary.

Invalid product IDs that do not exist in the products table will be identified and handled before inserting the sales data into the database.

Duplicate sales records will be identified and removed where appropriate.

All cleaning decisions will be documented in the project README.

## 4. Database Design

The cleaned data will be stored in a SQLite database.

There will be two main tables:

### Products Table

* product_id — Primary Key
* product_name
* category
* unit_price
* in_stock

### Sales Table

* sale_id — Primary Key
* product_id — Foreign Key
* quantity
* sale_date
* payment_method
* customer_type

The relationship between the tables will allow sales information to be connected to product information.

## 5. Analysis

Python will be used to analyse the cleaned data.

The analysis will include:

* Total sales revenue.
* Total quantity of products sold.
* Best-selling products.
* Sales by category.
* Sales by payment method.
* Monthly sales trends.
* Other useful business questions for Thabo's store.

I will use Python functions, loops, lists, dictionaries and conditional statements to demonstrate my understanding of programming.

## 6. Visualisation

I will create at least two charts:

1. A bar chart showing revenue by product or category.
2. A line chart showing sales trends over time.

The charts will be saved as PNG files and included in the final project.

## 7. Security

The system will include a password gate.

The password will not be stored as plain text. Instead, SHA-256 hashing will be used to protect the password.

The security design will consider the three parts of the CIA triad:

* Confidentiality
* Integrity
* Availability

## 8. Development Order

I will complete the project in the following order:

1. Inspect the original CSV data.
2. Plan the solution using computational thinking.
3. Complete the data cleaning module.
4. Create the SQLite database.
5. Add SQL queries.
6. Complete the Python analysis.
7. Create the visualisations.
8. Add password security.
9. Complete the README and documentation.
10. Test the complete system using `python main.py`.
11. Commit and push the completed work to GitHub.

## 9. Expected Outcome

The final system should allow Thabo to work with clean and organised sales data, store the information securely, analyse sales performance and view charts that make the results easier to understand.

The final project should run successfully from `main.py` without errors.

