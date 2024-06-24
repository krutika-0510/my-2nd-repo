import pandas as pd
from Exception import DataCleaningError
from file_handling import load_from_csv,save_to_csv

try:
    cleaned_data = load_from_csv('Clean_Covid_Data.csv')

    # Ensure cleaned_data is a DataFrame
    if not isinstance(cleaned_data, pd.DataFrame):
        raise DataCleaningError("Loaded data is not a DataFrame")

    # Perform basic analysis
    total_confirmed = cleaned_data['Confirmed'].sum()
    total_deaths = cleaned_data['Deaths'].sum()
    total_recovered = cleaned_data['Recovered'].sum()

    # Identify countries/states with highest and lowest cases
    country_with_highest_cases = cleaned_data.loc[cleaned_data['Confirmed'].idxmax(), 'Country/Region']
    country_with_lowest_cases = cleaned_data.loc[cleaned_data['Confirmed'].idxmin(), 'Country/Region']

    print(f"Total confirmed cases: {total_confirmed}")
    print(f"Total deaths: {total_deaths}")
    print(f"Total recovered cases: {total_recovered}")
    print(f"Highest cases in: {country_with_highest_cases}")
    print(f"Lowest cases in: {country_with_lowest_cases}")

except FileNotFoundError as e:
    print(e)
except KeyError as e:
    print(f"Error: Missing key {e} in the dataset.")
except DataCleaningError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")