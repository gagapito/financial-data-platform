# Data Model Design

## Overview
This project uses a star schema optimized for fintech analytics.

## Relationship Map
            customers
                |
             accounts
                |
            transactions  ← FACT TABLE
           /     |     \
      merchants  date   (analytics queries)

## Fact Table
- transactions: central event table storing all banking activity

## Dimension Tables
- customers: user demographic data
- accounts: banking account metadata
- merchants: merchant categories and risk levels
- date_dim: time-based analytics support

## Design Choice
A star schema was chosen to optimize query performance for:
- fraud detection
- customer analytics
- financial reporting