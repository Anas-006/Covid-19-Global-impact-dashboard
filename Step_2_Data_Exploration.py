import pandas as pd

# Load dataset
df = pd.read_csv("owid-covid-data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

print("=" * 50)
print("COVID-19 DATA EXPLORATION")
print("=" * 50)

# 1. Dataset size
print("\n1. Dataset Size")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Date range
print("\n2. Date Range")
print("Start Date:", df["date"].min())
print("End Date:", df["date"].max())

# 3. Total locations
print("\n3. Number of Locations")
print(df["location"].nunique())

# 4. Sample locations
print("\n4. Sample Locations")
print(df["location"].drop_duplicates().head(15).to_list())

# 5. Important columns available
important_columns = [
    "location",
    "date",
    "continent",
    "population",
    "total_cases",
    "new_cases",
    "total_deaths",
    "new_deaths",
    "people_vaccinated",
    "people_fully_vaccinated",
    "total_vaccinations",
    "positive_rate",
    "icu_patients",
    "hosp_patients",
]

print("\n5. Available Important Columns")

for col in important_columns:
    if col in df.columns:
        print(col, "-> Available")
    else:
        print(col, "-> Not Available")

# 6. Missing values in important columns
print("\n6. Missing Values")

available_columns = [
    col for col in important_columns if col in df.columns
]

missing_values = df[available_columns].isnull().sum()

print(missing_values)

# 7. India data preview
print("\n7. India COVID-19 Data Preview")

india = df[df["location"] == "India"]

print(
    india[
        [
            "location",
            "date",
            "new_cases",
            "total_cases",
            "new_deaths",
            "total_deaths",
        ]
    ].tail(10).to_string(index=False)
)

print("\nExploration Completed Successfully!")