
-- Create Customers Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_fname VARCHAR(50),
    customer_lname VARCHAR(50),
    username VARCHAR(50),
    password VARCHAR(50),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    pincode VARCHAR(10)
);

-- Create Orders Table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    order_customer_id INT,
    order_status VARCHAR(50)
);

-- Create Products Table
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT
);

-- Copy data from CSV files
COPY customers FROM '/Users/kramkrishnaachary/Learning/Github/fastapi-orders-service/data/customers.csv' 
DELIMITER ',' CSV HEADER;

COPY orders FROM '/Users/kramkrishnaachary/Learning/Github/fastapi-orders-service/data/orders.csv' 
DELIMITER ',' CSV HEADER;

SELECT * FROM orders LIMIT 10;
SELECT * FROM customers LIMIT 10;
SELECT * FROM products;