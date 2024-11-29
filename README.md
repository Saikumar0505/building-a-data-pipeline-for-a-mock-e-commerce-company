# building-a-data-pipeline-for-a-mock-e-commerce-company
Build a scalable and automated data pipeline to ingest, process, and store sales data for analytics
# E-Commerce Data Pipeline

## Overview
This project demonstrates an end-to-end data pipeline for an e-commerce company. The pipeline ingests raw sales data, transforms it, and loads it into a database for analytics.

## Data used
- Here is dataset used: https://github.com/Saikumar0505/building-a-data-pipeline-for-a-mock-e-commerce-company/blob/main/sales_data_1.csv
- 
## Features
- Ingest sales data from multiple CSV files.
- Transform and clean data (e.g., calculate total price, handle missing values).
- Load data into a relational database.
- Perform SQL-based analytics.

## Project Structure
```plaintext
ecommerce-data-pipeline/
├── config/config.yaml
├── data/sales_data_1.csv
├── src/data_ingestion.py
├── src/data_transformation.py
├── src/data_loading.py
├── src/analytics_query.py
├── tests/test_data_ingestion.py
├── tests/test_data_transformation.py
├── Dockerfile
├── requirements.txt
├── README.md
