# Data Generation

## Overview

This project uses synthetic fintech data to simulate a banking environment.

The generator creates realistic relationships between:

- Customers
- Accounts
- Merchants
- Transactions

## Dataset Sizes

- Customers: 5,000
- Accounts: 7,000
- Merchants: 200
- Transactions: 100,000

## Generated Fields

### Customers
- customer_id
- name
- age
- income
- created_at

### Accounts
- account_id
- customer_id
- account_type
- balance
- created_at

### Merchants
- merchant_id
- name
- category
- risk_level

### Transactions
- transaction_id
- account_id
- customer_id
- merchant_id
- amount
- transaction_type
- timestamp
- merchant_category
- location

## Purpose

The generated data serves as the source layer for:

- ETL pipelines
- Data warehouse ingestion
- Fraud detection
- Risk scoring analytics