import pandas as pd
df = pd.read_csv("owid-covid-data.csv")
print("Original Dataset Shape:", df.shape)
print(df.head())


# Sort data by country and date
df = df.sort_values(["location", "date"]).copy()

import pandas as pd
import numpy as np

# Sort data by country and date
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.sort_values(["location", "date"]).copy()

# 1. Seven-day rolling averages
df["new_cases_7day_avg"] = (
    df.groupby("location")["new_cases"]
    .transform(lambda x: x.rolling(7, min_periods=1).mean())
)

df["new_deaths_7day_avg"] = (
    df.groupby("location")["new_deaths"]
    .transform(lambda x: x.rolling(7, min_periods=1).mean())
)

# 2. Case Fatality Rate
df["case_fatality_rate"] = (
    df["total_deaths"]
    .div(df["total_cases"].where(df["total_cases"] > 0))
    .mul(100)
)

# 3. Cases and deaths per million
df["cases_per_million"] = (
    df["total_cases"]
    .div(df["population"].where(df["population"] > 0))
    .mul(1_000_000)
)

df["deaths_per_million"] = (
    df["total_deaths"]
    .div(df["population"].where(df["population"] > 0))
    .mul(1_000_000)
)

# 4. Check metrics
metrics = [
    "new_cases_7day_avg",
    "new_deaths_7day_avg",
    "case_fatality_rate",
    "cases_per_million",
    "deaths_per_million",
    "doubling_time_days"
]

print("METRIC AVAILABILITY CHECK")

for col in metrics:
    status = "Available" if col in df.columns else "Not available"
    print(f"{col}: {status}")

# 5. Save updated dataset
df.to_csv("covid19_final_dashboard_dataset.csv", index=False)

print("\nUpdated dataset saved successfully!")
print("Dataset shape:", df.shape)

# Calculate 7-day rolling average of new cases
df["new_cases_7day_avg"] = (
    df.groupby("location")["new_cases"]
    .transform(lambda x: x.rolling(7, min_periods=1).mean())
)

# Calculate 7-day rolling average of new deaths
df["new_deaths_7day_avg"] = (
    df.groupby("location")["new_deaths"]
    .transform(lambda x: x.rolling(7, min_periods=1).mean())
)

# Display results
print(df[[
    "location",
    "date",
    "new_cases",
    "new_cases_7day_avg",
    "new_deaths",
    "new_deaths_7day_avg"
]].head(10))

print("\n7-day rolling averages calculated successfully!")

# Calculate Case Fatality Rate (CFR)
df["case_fatality_rate"] = (
    df["total_deaths"] / df["total_cases"]
) * 100

# Replace infinite values with missing values
df["case_fatality_rate"] = df["case_fatality_rate"].replace(
    [float("inf"), -float("inf")], float("nan")
)

# Display results
print("Case Fatality Rate calculated successfully!")

print(df[[
    "location",
    "date",
    "total_cases",
    "total_deaths",
    "case_fatality_rate"
]].tail(10))

import pandas as pd
df = pd.read_csv("owid-covid-data.csv")
print("Original Dataset Shape:", df.shape)
print(df.head())

# Calculate COVID-19 cases and deaths per million people

df["cases_per_million"] = (
    df["total_cases"] / df["population"]
) * 1000000

df["deaths_per_million"] = (
    df["total_deaths"] / df["population"]
) * 1000000

# Handle missing or invalid values
df.loc[df["population"] <= 0, [
    "cases_per_million",
    "deaths_per_million"
]] = float("nan")