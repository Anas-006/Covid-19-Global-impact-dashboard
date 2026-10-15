import pandas as pd
import numpy as np

df = pd.read_csv("owid-covid-data.csv")
print("Original Dataset Shape:", df.shape)
print(df.head())

# Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove aggregate regions if iso_code is available
analysis_df = df.copy()

if "iso_code" in analysis_df.columns:
    analysis_df = analysis_df[
        ~analysis_df["iso_code"].astype(str).str.startswith("OWID_")
    ]

# Get latest record for each country
latest_df = (
    analysis_df.sort_values("date")
    .groupby("location", as_index=False)
    .tail(1)
    .copy()
)

# Insight 1: Top 5 countries by total cases
top_cases = (
    latest_df[["location", "total_cases"]]
    .dropna()
    .sort_values("total_cases", ascending=False)
    .head(5)
)

print("INSIGHT 1: Top 5 Countries by Total Cases")
print(top_cases.to_string(index=False))

# Insight 2: Top 5 countries by deaths per million
if "deaths_per_million" in latest_df.columns:
    top_deaths = (
        latest_df[["location", "deaths_per_million"]]
        .dropna()
        .sort_values("deaths_per_million", ascending=False)
        .head(5)
    )

    print("\nINSIGHT 2: Top 5 Countries by Deaths per Million")
    print(top_deaths.to_string(index=False))

# Insight 3: Highest daily case peak in India
india_df = analysis_df[
    analysis_df["location"] == "India"
].copy()

if not india_df.empty and "new_cases" in india_df.columns:
    india_peak = india_df.loc[
        india_df["new_cases"].idxmax()
    ]

    print("\nINSIGHT 3: India's Highest Daily Case Count")
    print("Date:", india_peak["date"])
    print("New cases:", india_peak["new_cases"])

# Insight 4: Highest daily death count in India
if not india_df.empty and "new_deaths" in india_df.columns:
    india_death_peak = india_df.loc[
        india_df["new_deaths"].idxmax()
    ]

    print("\nINSIGHT 4: India's Highest Daily Death Count")
    print("Date:", india_death_peak["date"])
    print("New deaths:", india_death_peak["new_deaths"])

# Insight 5: Vaccination coverage, if available
if "people_fully_vaccinated_per_hundred" in latest_df.columns:
    top_vax = (
        latest_df[["location", "people_fully_vaccinated_per_hundred"]]
        .dropna()
        .sort_values(
            "people_fully_vaccinated_per_hundred",
            ascending=False
        )
        .head(5)
    )

    print("\nINSIGHT 5: Top 5 Countries by Full Vaccination Coverage")
    print(top_vax.to_string(index=False))
else:
    print("\nINSIGHT 5: Full vaccination percentage is not available.")