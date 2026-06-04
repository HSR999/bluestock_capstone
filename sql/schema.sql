CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    amfi_code TEXT UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    date DATE
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_transactions (
    txn_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    investor_id TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    payment_mode TEXT,
    kyc_status TEXT,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance (
    perf_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    sharpe_ratio REAL,
    alpha REAL,
    beta REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    aum_crore REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);