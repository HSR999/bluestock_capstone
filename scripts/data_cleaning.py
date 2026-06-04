import pandas as pd

# NAV HISTORY

# nav = pd.read_csv("data/raw/02_nav_history.csv")

# nav["date"] = pd.to_datetime(nav["date"])

# nav = nav.sort_values(
#     ["amfi_code", "date"]
# )

# nav["nav"] = (
#     nav.groupby("amfi_code")["nav"]
#     .ffill()
# )

# nav = nav.drop_duplicates()

# nav = nav[nav["nav"] > 0]

# nav.to_csv(
#     "data/processed/02_nav_history_clean.csv",
#     index=False
# )

# print("NAV cleaned")


# INVESTOR TRANSACTIONS

# txn = pd.read_csv(
#     "data/raw/08_investor_transactions.csv"
# )


# txn["transaction_date"] = pd.to_datetime(
#     txn["transaction_date"]
# )

# txn["transaction_type"] = (
#     txn["transaction_type"]
#     .str.lower()
# )

# mapping = {
#     "sip": "SIP",
#     "lumpsum": "Lumpsum",
#     "redemption": "Redemption"
# }

# txn["transaction_type"] = (
#     txn["transaction_type"]
#     .map(mapping)
# )
# txn = txn[
#     txn["kyc_status"].isin(
#         ["Verified","Pending","Rejected"]
#     )
# ]
# txn = txn[txn["amount_inr"] > 0]

# txn.to_csv(
#     "data/processed/08_investor_transactions_clean.csv",
#     index=False
# )

# print("Transactions cleaned")


# PERFORMANCE

# PERFORMANCE

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Flag expense ratio anomalies

perf["expense_ratio_flag"] = (
    ~perf["expense_ratio_pct"].between(0.1, 2.5)
)

# Optional: print anomalous records

print(
    "Expense ratio anomalies:",
    perf["expense_ratio_flag"].sum()
)

perf.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")