-- =========================
-- CUSTOMERS TABLE
-- =========================
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    income DECIMAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- ACCOUNTS TABLE
-- =========================
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    account_type VARCHAR(50),
    balance DECIMAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- MERCHANTS TABLE
-- =========================
CREATE TABLE merchants (
    merchant_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(100),
    risk_level VARCHAR(50)
);

-- =========================
-- DATE DIMENSION TABLE
-- =========================
CREATE TABLE date_dim (
    date_id SERIAL PRIMARY KEY,
    full_date DATE,
    day INT,
    month INT,
    year INT,
    day_of_week VARCHAR(20),
    is_weekend BOOLEAN
);

-- =========================
-- TRANSACTIONS FACT TABLE
-- =========================
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT REFERENCES accounts(account_id),
    customer_id INT REFERENCES customers(customer_id),
    merchant_id INT REFERENCES merchants(merchant_id),
    amount DECIMAL,
    transaction_type VARCHAR(20),
    timestamp TIMESTAMP,
    merchant_category VARCHAR(100),
    location VARCHAR(100)
);