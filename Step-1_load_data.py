import pandas as pd

# Load the COVID-19 dataset
df = pd.read_csv("owid-covid-data.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display dataset information
print("\nDataset Information:")
df.info()

# Display missing values in important columns
print("\nMissing Values:")
print(
    df[
        [
            "location",
            "date",
            "total_cases",
            "new_cases",
            "total_deaths",
            "people_vaccinated",
            "population",
        ]
    ].isnull().sum()
)