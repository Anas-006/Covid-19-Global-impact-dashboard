import pandas as pd
import numpy as np
df = pd.read_csv("owid-covid-data.csv")
print("Original Dataset Shape:", df.shape)
print(df.head())

# Sort data by country and date
df = df.sort_values(["location", "date"]).copy()

# Calculate cases doubling time
def calculate_doubling_time(series):
    previous_cases = series.shift(7)

    ratio = series / previous_cases

    doubling_time = np.where(
        (series > previous_cases) &
        (previous_cases > 0) &
        (ratio > 1),
        7 * np.log(2) / np.log(ratio),
        np.nan
    )

    return doubling_time

df["doubling_time_days"] = (
    df.groupby("location")["total_cases"]
    .transform(calculate_doubling_time)
)

# Display results
print("Doubling time calculated successfully!")

print(df[[
    "location",
    "date",
    "total_cases",
    "doubling_time_days"
]].tail(10))

# Check vaccination-related columns
vaccination_columns = [
    col for col in df.columns
    if "vaccination" in col.lower()
    or "vaccinated" in col.lower()
    or "people_vaccinated" in col.lower()
    or "people_fully_vaccinated" in col.lower()
]

print("Vaccination columns available:")
print(vaccination_columns)

# Check required columns
required_columns = [
    "location",
    "date",
    "population",
    "people_vaccinated",
    "people_fully_vaccinated"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    print("Missing columns:", missing_columns)
    print("Available columns:")
    print(df.columns.tolist())

else:
    # Calculate vaccination percentages
    df["vaccination_percentage"] = (
        df["people_vaccinated"] / df["population"]
    ) * 100

    df["fully_vaccinated_percentage"] = (
        df["people_fully_vaccinated"] / df["population"]
    ) * 100

    print("Vaccination percentages calculated successfully!")

    print(df[[
        "location",
        "date",
        "population",
        "vaccination_percentage",
        "fully_vaccinated_percentage"
    ]].tail(10))

    # Save the processed dataset

output_file = "covid19_cleaned_analysis.csv"

df.to_csv(output_file, index=False)

print("Dataset saved successfully!")
print("File name:", output_file)
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

   