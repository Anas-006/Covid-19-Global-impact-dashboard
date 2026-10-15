import pandas as pd
df = pd.read_csv("owid-covid-data.csv")
print("Original Dataset Shape:", df.shape)
print(df.head())

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