# ⚙️ Tri Engine Data Processing Project

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PySpark](https://img.shields.io/badge/PySpark-Spark-orange)
![Databricks](https://img.shields.io/badge/Databricks-Cloud-red)
![Snowflake](https://img.shields.io/badge/Snowflake-Warehouse-blue)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 🚀 Overview

The **Tri Engine Data Processing Project** demonstrates how a single retail dataset can be processed and analyzed across three different data engineering environments:

- Local PySpark  
- Databricks  
- Snowflake  

The project highlights how data pipelines can be implemented across different platforms while maintaining consistent results.

---

## 🎯 Problem Statement

Retail datasets are often stored in raw formats like CSV and require preprocessing before analysis.

However:

- Different tools are used across organizations  
- Pipelines vary across environments  
- Maintaining consistency across systems is difficult  

---

## ✅ Solution

This project solves the problem by:

- Implementing **same logic across 3 engines**
- Processing a shared dataset (`orders.csv`)
- Ensuring consistent outputs across:
  - PySpark
  - Databricks
  - Snowflake

---

## 🏗️ Architecture

orders.csv → PySpark → Databricks → Snowflake → Analytics


---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|--------|
| Python | Core programming |
| PySpark | Local data processing |
| Databricks | Cloud Spark processing |
| Snowflake | Data warehouse |
| SQL | Analytics queries |
| Pandas | Data handling |
| GitHub | Version control |

---

## 📊 Dataset

### Key Fields

- OrderID  
- CustomerID  
- ItemName  
- Quantity  
- Price  
- Date  
- Status  

---

## 🔄 Data Pipeline

### 1️⃣ Local PySpark

- Load CSV  
- Apply schema  
- Clean data  
- Convert types  
- Calculate metrics  

---

### 2️⃣ Databricks

- Upload dataset  
- Process with Spark  
- Run queries  
- Display results  

---

### 3️⃣ Snowflake

- Create warehouse & tables  
- Load data  
- Run SQL analytics  

---

## 🧹 Data Cleaning

- Type conversions  
- Missing value handling  
- Date formatting  
- Column standardization  
- Trim spaces  

---

## 🧪 Data Validation

```sql
SELECT COUNT(*) FROM STAGING_ORDERS_SF;

SELECT SUM(Price * Quantity) AS total_revenue
FROM STAGING_ORDERS_SF;

SELECT AVG(Price * Quantity) AS avg_order_value
FROM STAGING_ORDERS_SF;
```

---

## ⚙️ Environment Setup

### Requirements
* Python 3.10+
* Java JDK
* PySpark
* Databricks account
* Snowflake account

---

## 🐍 Setup

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python local_pyspark_app.py
```
### Databricks
- Import notebook
- Upload dataset
- Run all cells
### Snowflake
- Open SQL script
- Run queries
- Validate results

---

## 📈 Outputs
* Clean dataset
* Revenue metrics
* Customer analysis
* Databricks results
* Snowflake outputs

---

## 📌 Conclusion

The Tri Engine Data Processing Project shows how a single dataset can be processed across multiple data platforms while maintaining consistent results.
It provides practical exposure to:
* PySpark
* Databricks
* Snowflake
* Data pipelines

---

## 🌐 Author

[![GitHub](https://img.shields.io/badge/GitHub-rimsha7-181717?logo=github&logoColor=white)](https://github.com/rimsha7)

---
