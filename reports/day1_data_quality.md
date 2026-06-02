# Day 1 Data Quality & Data Ingestion Report

## Project

Bluestock Mutual Fund Analytics Capstone

## Objective

The objective of Day 1 was to set up the project environment, ingest all provided datasets, perform an initial data quality assessment, understand the dataset structure, validate scheme identifiers, and fetch live mutual fund NAV data using the MFAPI service.

---

## Tasks Completed

### 1. Project Structure Creation

A standardized project structure was created to support the complete analytics pipeline.

```
bluestock_mf_capstone/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
├── scripts/
├── sql/
├── dashboard/
├── reports/
└── README.md
```

---

### 2. Environment Setup

The following libraries were installed and documented in requirements.txt:

* pandas
* numpy
* matplotlib
* seaborn
* plotly
* sqlalchemy
* requests
* scipy
* jupyter

A virtual environment was created to isolate project dependencies.

---

### 3. Dataset Ingestion

A total of 10 datasets were successfully loaded into Pandas DataFrames for inspection and profiling.

| Dataset                  | Rows   | Columns |
| ------------------------ | ------ | ------- |
| 01_fund_master           | 40     | 15      |
| 02_nav_history           | 46,000 | 3       |
| 03_aum_by_fund_house     | 180    | 5       |
| 04_monthly_sip_inflows   | 60     | 6       |
| 05_category_inflows      | 300    | 3       |
| 06_industry_folio_count  | 60     | 6       |
| 07_scheme_performance    | 40     | 19      |
| 08_investor_transactions | 40,000 | 13      |
| 09_portfolio_holdings    | 800    | 8       |
| 10_benchmark_indices     | 10,053 | 3       |

Total records analyzed: 97,493+

---

## Dataset Profiling

The following checks were performed on every dataset:

* Shape inspection
* Column inspection
* Data type inspection
* Missing value analysis
* Duplicate record detection
* Initial schema understanding

---

## Missing Value Analysis

Only one dataset contained missing values.

| Dataset                | Column         | Missing Values |
| ---------------------- | -------------- | -------------- |
| 04_monthly_sip_inflows | yoy_growth_pct | 12             |

Observation:

The missing values in yoy_growth_pct are likely expected because year-over-year growth cannot be calculated for the initial observation periods where prior-year data is unavailable.

No immediate corrective action is required.

---

## Duplicate Record Analysis

Duplicate row checks were performed across all datasets.

Result:

* No duplicate records were identified.
* Duplicate row count = 0 for all datasets.

This indicates strong source data consistency.

---

## Data Type Assessment

Most numerical columns were already stored using appropriate numeric data types.

Examples:

* NAV values → float64
* Expense ratios → float64
* AUM values → float64 / int64
* Transaction amounts → int64

However, all date-related columns are currently stored as strings and will require conversion during preprocessing.

Affected columns include:

* launch_date
* date (NAV history)
* date (AUM history)
* month (SIP inflows)
* month (Category inflows)
* month (Industry folio counts)
* transaction_date
* portfolio_date
* date (Benchmark indices)

These conversions will be performed during Day 2 data cleaning.

---

## Fund Master Exploration

The fund master dataset was explored to understand the overall mutual fund universe.

Key dimensions inspected:

* Fund Houses
* Categories
* Sub Categories
* Risk Categories
* Scheme Plans
* SEBI Category Codes

The dataset will serve as the primary reference table for future joins and analytics.

---

## AMFI Code Validation

AMFI scheme codes were validated between:

* 01_fund_master
* 02_nav_history

Validation Process:

1. Extract unique AMFI codes from fund master.
2. Extract unique AMFI codes from NAV history.
3. Compare both sets for unmatched values.

Result:

All AMFI scheme codes present in the fund master dataset were successfully found in the NAV history dataset.

Missing AMFI Codes: 0

This confirms referential consistency between the master and historical NAV datasets.

---

## Live NAV Data Collection

Historical NAV data was fetched from MFAPI.

Source:

https://api.mfapi.in

Schemes fetched:

* HDFC Top 100 Direct (125497)
* SBI Bluechip (119551)
* ICICI Bluechip (120503)
* Nippon Large Cap (118632)
* Axis Bluechip (119092)
* Kotak Bluechip (120841)

The retrieved data was successfully stored inside the data/raw directory for future analytics and benchmarking.

---

## Key Findings

1. Data quality is generally high across all datasets.
2. No duplicate records were detected.
3. Only one column contains missing values.
4. Date columns require datatype conversion.
5. AMFI code validation passed successfully.
6. Live NAV data ingestion was completed successfully.
7. The datasets are ready for preprocessing and database integration.

---

## Conclusion

Day 1 objectives were successfully completed.

All datasets were ingested, profiled, validated, and documented. Data quality issues were identified and logged for preprocessing in Day 2. Live NAV data was successfully fetched from MFAPI and stored for future performance analysis.

The project is now ready for the Data Cleaning and SQLite Database Integration phase.
