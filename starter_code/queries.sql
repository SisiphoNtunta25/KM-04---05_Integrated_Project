
-- Query 1: Display sales with product names (JOIN)
SELECT
    s.sale_id,
    s.sale_date,
    p.product_name,
    s.quantity,
    p.unit_price,
    s.quantity * p.unit_price AS total_revenue
FROM sales AS s
JOIN products AS p
    ON s.product_id = p.product_id
ORDER BY s.sale_date;


-- Query 2: Calculate total revenue for each product
SELECT
    p.product_name,
    SUM(s.quantity) AS total_quantity_sold,
    ROUND(SUM(s.quantity * p.unit_price), 2) AS total_revenue
FROM products AS p
JOIN sales AS s
    ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC;


-- Query 3: Calculate revenue by product category
SELECT
    p.category,
    ROUND(SUM(s.quantity * p.unit_price), 2) AS category_revenue
FROM products AS p
JOIN sales AS s
    ON p.product_id = s.product_id
GROUP BY p.category
ORDER BY category_revenue DESC;


-- Query 4: Show monthly sales and revenue
SELECT
    strftime('%Y-%m', s.sale_date) AS sales_month,
    SUM(s.quantity) AS total_quantity_sold,
    ROUND(SUM(s.quantity * p.unit_price), 2) AS monthly_revenue
FROM sales AS s
JOIN products AS p
    ON s.product_id = p.product_id
GROUP BY strftime('%Y-%m', s.sale_date)
ORDER BY sales_month;


-- Query 5: Compare sales by payment method
SELECT
    payment_method,
    COUNT(*) AS number_of_sales,
    SUM(quantity) AS total_quantity_sold
FROM sales
GROUP BY payment_method
ORDER BY number_of_sales DESC;


-- Business Question 1:
-- Which product sells the highest quantity?
SELECT
    p.product_name,
    SUM(s.quantity) AS total_quantity_sold
FROM products AS p
JOIN sales AS s
    ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 1;


-- Business Question 2:
-- Which customer type generates the most revenue?
SELECT
    s.customer_type,
    ROUND(SUM(s.quantity * p.unit_price), 2) AS total_revenue
FROM sales AS s
JOIN products AS p
    ON s.product_id = p.product_id
GROUP BY s.customer_type
ORDER BY total_revenue DESC;
