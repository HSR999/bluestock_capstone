import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

txn = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

perf = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully")

print("NAV rows:", len(nav))
print("Transaction rows:", len(txn))
print("Performance rows:", len(perf))