from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://g.agapito@localhost:5432/fintech_dw"

engine = create_engine(DATABASE_URL)

schema_sql = """
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    income DECIMAL,
    created_at TIMESTAMP
);

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(50),
    balance DECIMAL,
    created_at TIMESTAMP
);

CREATE TABLE merchants (
    merchant_id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(100),
    risk_level VARCHAR(50)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    customer_id INT,
    merchant_id INT,
    amount DECIMAL,
    transaction_type VARCHAR(20),
    timestamp TIMESTAMP,
    merchant_category VARCHAR(100),
    location VARCHAR(100)
);
"""

with engine.connect() as conn:
    conn.execute(text(schema_sql))
    conn.commit()

print("Warehouse tables created successfully.")