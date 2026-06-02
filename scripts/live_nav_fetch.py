from pathlib import Path
import requests
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

# Create raw directory if it doesn't exist
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Required schemes
funds = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("=" * 60)
print("Fetching NAV Data")
print("=" * 60)

for fund_name, scheme_code in funds.items():

    try:
        url = f"https://api.mfapi.in/mf/{scheme_code}"

        print(f"\nFetching {fund_name} ({scheme_code})...")

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        if "data" not in data:
            print(f"❌ No NAV data found for {fund_name}")
            continue

        nav_df = pd.DataFrame(data["data"])

        output_file = RAW_DIR / f"{fund_name}.csv"

        nav_df.to_csv(output_file, index=False)

        print(
            f"✅ Saved {fund_name}.csv "
            f"({len(nav_df)} records)"
        )

    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error for {fund_name}: {e}")

    except Exception as e:
        print(f"❌ Error processing {fund_name}: {e}")

print("\n" + "=" * 60)
print("NAV Fetch Complete")
print("=" * 60)