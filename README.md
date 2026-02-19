# Project Name: Real-Time Stock Market Analysis

The project implements a **real-time data pipeline** that:
- Extracts stock data from Alpha Vantage API
- Streams it through Apache Kafka
- Processes it with Apache Spark
- Loads the results into a PostgreSQL database

All components are containerized with **Docker** for easy deployment and reproducibility.

## Data Pipeline Architecture
![Architecture Diagram](./img/real_time_pipline.png)  

#### Project Tech Stack & Flow

- **Kafka UI** → inspect topics and messages[](http://localhost:8085)
- **API Producer** → fetches data from Alpha Vantage and produces JSON events into Kafka
- **Spark Streaming** → consumes from Kafka, processes the data, writes results to PostgreSQL
- **PostgreSQL** → stores processed results for analytics and querying
- **pgAdmin** → visual management of the PostgreSQL database
- **Power BI** (external) → connects to PostgreSQL for dashboards and reporting

