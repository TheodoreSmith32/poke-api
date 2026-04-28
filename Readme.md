# Data Pipeline Poke API 


## 📌 Overview
This project implements an end-to-end data pipeline that ingests data from an API, stores it in a staging layer, transforms it into an Operational Data Store (ODS) and finally loads it into a Data Warehouse for analytics.

## 🏗️ Architecture Flow
API (PokeAPI)
↓
FastAPI (Ingestion Layer)
↓
PostgreSQL (Staging - Raw Data)
↓
dbt Transformation
↓
PostgreSQL (ODS - Clean Data)
↓
Snowflake (Data Warehouse - Analytics)


## ⚙️ Tech Stack (exlucde Snowflake)

- FastAPI (Python) → API data ingestion  
- PostgreSQL → Staging & ODS layers  
- dbt  → Data transformation on Postgres
- Docker  → Containerization  

## dbt Run
You can run dbt using : 
- dbt run -s operational_data (on operational_data models)

## Poke Arc. PDF 
Poke Arc PDF is doc that explain the architecture of data pipeline pokemon API