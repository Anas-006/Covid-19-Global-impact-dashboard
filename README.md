COVID-19 Global Impact Dashboard

Project Overview

The COVID-19 Global Impact Dashboard analyzes publicly available COVID-19 data to understand the global impact of the pandemic through reported cases, deaths, and country-level comparisons.

The project uses data cleaning, exploratory data analysis, and Tableau visualizations to identify trends over time and compare reported COVID-19 statistics across countries.

Objectives

- Analyze daily COVID-19 cases and deaths.
- Identify periods with increased reported cases and deaths.
- Compare total reported cases across countries.
- Explore cases and deaths per million population where the required fields are available.
- Present key findings through an interactive Tableau dashboard.

Dataset

Source: Our World in Data — COVID-19 Dataset

The original dataset contained approximately 429,435 rows and 67 columns.

The data includes country names, dates, reported cases, reported deaths, and other pandemic-related indicators.

Tools Used

- Tableau — Data visualization and dashboard development
- Python and Pandas — Data cleaning and preparation
- Microsoft Excel — Data inspection and validation
- GitHub — Project documentation and version control

Data Cleaning

The following preparation steps were performed:

- Inspected dataset dimensions and column names.
- Reviewed date and numeric fields.
- Prepared a cleaned CSV file for analysis.
- Checked the availability of required analytical fields.
- Used the available fields to create visualizations.

Output file: "COVID-19 Cleaned Analysis.csv"

Dashboard Visualizations

The Tableau dashboard includes the following charts, where the required fields were available:

1. COVID-19 Daily Cases Trend
2. COVID-19 Daily Deaths Trend
3. Top 10 Countries by Total COVID-19 Cases
4. COVID-19 Cases per Million by Country
5. COVID-19 Deaths per Million by Country

Key Insights

1. The World aggregate represents the combined reported COVID-19 case burden across countries.
2. The daily cases trend showed a prominent peak around 2022 in the chart reviewed.
3. The daily deaths trend showed a prominent peak around 2021 in the chart reviewed.

These observations describe the trends seen in the current visualizations. Exact peak values and dates have not been independently verified.

Important Assumptions and Limitations

- Reported COVID-19 statistics can differ due to testing coverage and reporting practices.
- Missing or unavailable metrics were not treated as verified values.
- Per-million comparisons depend on the availability and quality of population-related data.
- The dashboard presents reported statistics and should not be interpreted as a complete measure of all infections or deaths.
- Country-level comparisons should be interpreted carefully because reporting methods may vary.

Conclusion

This project demonstrates data preparation, exploratory analysis, visualization, and insight communication using publicly available COVID-19 data.

The dashboard provides a visual overview of reported COVID-19 trends and country-level comparisons.
