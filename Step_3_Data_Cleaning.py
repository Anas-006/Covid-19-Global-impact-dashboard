import pandas as pd

# Load original dataset
df = pd.read_csv("owid-covid-data.csv")

print("Original Dataset Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Select required columns
required_columns = [
    "iso_code",
    "continent",
    "location",
    "date",
    "population",
    "total_cases",
    "new_cases",
    "total_deaths",
    "new_deaths",
    "total_vaccinations",
    "people_vaccinated",
    "people_fully_vaccinated",
    "new_vaccinations",
    "total_cases_per_million",
    "total_deaths_per_million",
    "people_vaccinated_per_hundred",
    "people_fully_vaccinated_per_hundred",
]

# Keep only columns available in the dataset
available_columns = [
    col for col in required_columns if col in df.columns
]

df = df[available_columns].copy()

print("\nSelected Dataset Shape:", df.shape)

# Check duplicate country-date records
duplicate_count = df.duplicated(
    subset=["location", "date"]
).sum()

print("\nDuplicate Country-Date Records:", duplicate_count)

# Remove exact duplicate rows only
df = df.drop_duplicates()

# Sort by country and date
df = df.sort_values(
    ["location", "date"]
).reset_index(drop=True)

# Save cleaned working dataset
df.to_csv(
    "covid_cleaned_working.csv",
    index=False
)

print("\nCleaned Dataset Shape:", df.shape)

print("\nMissing Values After Column Selection:")
print(df.isnull().sum())

print("\nCleaned Dataset Saved Successfully!")

# Check duplicate rows using country and date
print("Duplicate country-date rows:",
      df.duplicated(subset=["location", "date"]).sum())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check dataset shape
print("\nDataset shape:", df.shape)

# Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())