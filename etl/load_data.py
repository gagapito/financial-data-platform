import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://g.agapito@localhost:5432/fintech_dw"

engine = create_engine(DATABASE_URL)

print("Loading CSV files...")

customers = pd.read_csv("data/raw/customers.csv")
accounts = pd.read_csv("data/raw/accounts.csv")
merchants = pd.read_csv("data/raw/merchants.csv")
transactions = pd.read_csv("data/raw/transactions.csv")

print("Loading customers...")
customers.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False
)

print("Loading accounts...")
accounts.to_sql(
    "accounts",
    engine,
    if_exists="append",
    index=False
)

print("Loading merchants...")
merchants.to_sql(
    "merchants",
    engine,
    if_exists="append",
    index=False
)

print("Loading transactions...")
transactions.to_sql(
    "transactions",
    engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

print("Data loaded successfully.")