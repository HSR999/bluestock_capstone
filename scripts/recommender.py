import pandas as pd

perf = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

risk = input(
    "Risk Appetite: "
)

risk_map = {

    "Low":"Low",

    "Moderate":"Moderate",

    "High":"High"
}

res = perf[
    perf["risk_grade"]
    ==
    risk_map[risk]
]

res = res.sort_values(
    "sharpe_ratio",
    ascending=False
)

print(
    res[
        [
            "scheme_name",
            "sharpe_ratio"
        ]
    ].head(3)
)