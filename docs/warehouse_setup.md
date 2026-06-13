# PostgreSQL Data Warehouse Setup

## Overview

The Fintech Data Engineering Platform uses PostgreSQL as its analytical data warehouse.

The warehouse stores:

- Customer data
- Account data
- Merchant data
- Transaction data

The warehouse acts as the central storage layer between the raw data generation process and the analytics layer.

## Why PostgreSQL?

PostgreSQL was selected because:

- Widely used in industry
- Strong SQL support
- Reliable ACID compliance
- Excellent compatibility with Python and SQLAlchemy
- Suitable for analytical workloads in small-to-medium data platforms

For enterprise-scale deployments, PostgreSQL can be replaced with:

- Snowflake
- Amazon Redshift
- Google BigQuery
- Databricks