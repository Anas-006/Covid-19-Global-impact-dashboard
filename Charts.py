import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("owid-covid-data.csv")
print("Original Dataset Shape:", df.shape)
print(df.head())

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Select India data for visualization
india_df = df[df["location"] == "India"].copy()

# Group daily cases
india_trend = (
    india_df.groupby("date", as_index=False)["new_cases"]
    .sum()
    .sort_values("date")
)

# Calculate 7-day rolling average
india_trend["new_cases_7day_avg"] = (
    india_trend["new_cases"]
    .rolling(7, min_periods=1)
    .mean()
)

# Plot the trend
plt.figure(figsize=(14, 6))

plt.plot(
    india_trend["date"],
    india_trend["new_cases"],
    label="Daily New Cases",
    alpha=0.5
)

plt.plot(
    india_trend["date"],
    india_trend["new_cases_7day_avg"],
    label="7-Day Average"
)

plt.title("COVID-19 Daily Cases Trend - India")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Select India data
india_df = df[df["location"] == "India"].copy()

# Convert date column
india_df["date"] = pd.to_datetime(
    india_df["date"], errors="coerce"
)

# Group daily deaths by date
india_deaths = (
    india_df.groupby("date", as_index=False)["new_deaths"]
    .sum()
    .sort_values("date")
)

# Calculate 7-day rolling average
india_deaths["deaths_7day_avg"] = (
    india_deaths["new_deaths"]
    .rolling(window=7, min_periods=1)
    .mean()
)

# Create chart
plt.figure(figsize=(14, 6))

plt.plot(
    india_deaths["date"],
    india_deaths["new_deaths"],
    label="Daily New Deaths",
    alpha=0.5
)

plt.plot(
    india_deaths["date"],
    india_deaths["deaths_7day_avg"],
    label="7-Day Average Deaths"
)

plt.title("COVID-19 Daily Deaths Trend - India")
plt.xlabel("Date")
plt.ylabel("New Deaths")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("covid19_india_deaths_trend.png", dpi=300)

plt.show()

print("Deaths trend chart created successfully!")

# Get the latest available record for each country
latest_date = df.groupby("location")["date"].transform("max")

latest_df = df[df["date"] == latest_date].copy()

# Exclude aggregate regions and income groups
if "iso_code" in latest_df.columns:
    latest_df = latest_df[
        ~latest_df["iso_code"].astype(str).str.startswith("OWID_")
    ]

# Select top 10 countries by total cases
top_countries = (
    latest_df[["location", "total_cases"]]
    .dropna(subset=["total_cases"])
    .sort_values("total_cases", ascending=False)
    .head(10)
)

# Create chart
plt.figure(figsize=(12, 6))

plt.bar(
    top_countries["location"],
    top_countries["total_cases"]
)

plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save chart
plt.savefig("covid19_top10_countries.png", dpi=300)

plt.show()

print("Top 10 country comparison chart created successfully!")
print(top_countries.to_string(index=False))

# Check vaccination columns
if "people_fully_vaccinated_per_hundred" in df.columns:

    vaccine_col = "people_fully_vaccinated_per_hundred"

elif "people_fully_vaccinated" in df.columns:

    vaccine_col = "people_fully_vaccinated"

else:
    vaccine_col = None

if vaccine_col is None:

    print("Vaccination data is not available in the cleaned dataset.")
    print("Available columns:")
    print(df.columns.tolist())

else:

    # Get the latest vaccination record for each country
    vaccine_df = df[
        ["location", "date", vaccine_col]
    ].copy()

    vaccine_df["date"] = pd.to_datetime(
        vaccine_df["date"], errors="coerce"
    )

    vaccine_df = vaccine_df.dropna(
        subset=["date", vaccine_col]
    )

    vaccine_df = vaccine_df.sort_values("date")

    latest_vaccine = vaccine_df.groupby(
        "location", as_index=False
    ).tail(1)

    # Exclude aggregate regions
    if "iso_code" in df.columns:
        valid_locations = df[
            ~df["iso_code"].astype(str).str.startswith("OWID_")
        ]["location"].unique()

        latest_vaccine = latest_vaccine[
            latest_vaccine["location"].isin(valid_locations)
        ]

    # Select top 10 countries
    top_vaccinated = latest_vaccine.sort_values(
        vaccine_col, ascending=False
    ).head(10)

    # Create chart
    plt.figure(figsize=(12, 6))

    plt.bar(
        top_vaccinated["location"],
        top_vaccinated[vaccine_col]
    )

    plt.title("Top 10 Countries by Full Vaccination Coverage")
    plt.xlabel("Country")
    plt.ylabel(vaccine_col)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(
        "covid19_vaccination_progress.png",
        dpi=300
    )

    plt.show()

    print("Vaccination chart created successfully!")
    print(top_vaccinated[[
        "location", vaccine_col
    ]].to_string(index=False))