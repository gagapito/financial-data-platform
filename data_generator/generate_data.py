import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# ----------------------------
# CONFIG
# ----------------------------
NUM_CUSTOMERS = 5000
NUM_ACCOUNTS = 7000
NUM_MERCHANTS = 200
NUM_TRANSACTIONS = 100000

# ----------------------------
# MERCHANT CATEGORIES
# ----------------------------
MERCHANT_CATEGORIES = [
    "grocery", "restaurant", "travel", "entertainment",
    "utilities", "retail", "health", "subscription"
]

TRANSACTION_TYPES = ["debit", "credit"]

# ----------------------------
# 1. CUSTOMERS
# ----------------------------
def generate_customers(n):
    customers = []
    for i in range (1, n + 1):
        customers.append({
            "customer_id": i,
            "name": fake.name(),
            "age": random.randint(18,75),
            "income": round(random.uniform(30000,200000), 2),
            "created_at": fake.date_time_between(start_date="-3y", end_date="now")
        })
    return pd.DataFrame(customers)

# ----------------------------
# 2. ACCOUNTS
# ----------------------------
def generate_accounts(n, customer_ids):
    accounts = []
    for i in range(1, n + 1):
        accounts.append({
            "account_id": i,
            "customer_id": random.choice(customer_ids),
            "account_type": random.choice(["checking", "savings"]),
            "balance": round(random.uniform(0, 50000), 2),
            "created_at": fake.date_time_between(start_date="-3y", end_date="now")
        })
    return pd.DataFrame(accounts)

# ----------------------------
# 3. MERCHANTS
# ----------------------------
def generate_merchants(n):
    merchants = []
    for i in range(1, n + 1):
        merchants.append({
            "merchant_id": i,
            "name": fake.company(),
            "category": random.choice(MERCHANT_CATEGORIES),
            "risk_level": random.choice(["low", "medium", "high"])
        })
    return pd.DataFrame(merchants)

# ----------------------------
# 4. TRANSACTIONS (CORE TABLE)
# ----------------------------
def generate_transactions(n, accounts, customers, merchants):
    transactions = []

    start_date = datetime.now() - timedelta(days=365)

    for i in range(1, n + 1):
        
        account = accounts.sample(1).iloc[0]
        customer_id = account["customer_id"]

        merchant = merchants.sample(1).iloc[0]

        timestamp = start_date + timedelta(
            seconds=random.randint(0, 365 * 24 * 60 * 60)
        )

        amount = round(random.uniform(5, 2000), 2)

        # introduce real-world behavior patterns
        if merchant["category"] == "travel":
            amount *= random.uniform(1.5, 3)

        if merchant["category"] == "entertainment":
            amount *= random.uniform(1, 2)

        transactions.append({
            "transaction_id": i,
            "account_id": account["account_id"],
            "customer_id": customer_id,
            "merchant_id": merchant["merchant_id"],
            "amount": round(amount, 2),
            "transaction_type": random.choice(TRANSACTION_TYPES),
            "timestamp": timestamp,
            "merchant_category": merchant["category"],
            "location": fake.city()
        })
    
    return pd.DataFrame(transactions)

# ----------------------------
# MAIN EXECUTION
# ----------------------------
def main():
    print("Generating fintech datasets...")

    customers = generate_customers(NUM_CUSTOMERS)
    accounts = generate_accounts(NUM_ACCOUNTS, customers["customer_id"].tolist())
    merchants = generate_merchants(NUM_MERCHANTS)
    transactions = generate_transactions(NUM_TRANSACTIONS, accounts, customers, merchants)

    # Save outputs
    customers.to_csv("data/raw/customers.csv", index=False)
    accounts.to_csv("data/raw/accounts.csv", index=False)
    merchants.to_csv("data/raw/merchants.csv", index=False)
    transactions.to_csv("data/raw/transactions.csv", index=False)

    print("Data generation complete!")
    print(f"Customers: {len(customers)}")
    print(f"Accounts: {len(accounts)}")
    print(f"Merchants: {len(merchants)}")
    print(f"Transactions: {len(transactions)}")

if __name__ == "__main__":
    main()