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

# Display results
print("Cases and Deaths Per Million calculated successfully!")

print(df[[
    "location",
    "date",
    "population",
    "total_cases",
    "total_deaths",
    "cases_per_million",
    "deaths_per_million"
]].tail(10))