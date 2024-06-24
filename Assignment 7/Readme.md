## COVID-19 Data Cleaning and Analysis ##
The dataset describes the Covid-19 Cases in various countries/states. 
It gives us the number of confirmed cases, recoverd cases, active cases, and many more details.

# How to run the Code
To run the program based of this project, follow these steps:

 ## 1. Setup the Environment:
    -> Ensure proper/required version of Python is installed on your system.
    -> Install required libraries using by pip:
          pip install pandas 

 ## 2. Download the Dataset
    -> Place the 'country_wise_latest.csv' dataset in the project directory.  

 ## 3. Execution
    -> Open command prompt or a terminal.
    -> Navigate to the project directory.     

# Data Cleaning (data_cleaning.py)
The data cleaning process involves loading the dataset, handling missing values, removing duplicates.

```import pandas as pd
import os
from Exception import DataCleaningError

# Data cleaning function
def clean_data(df):
    
    if df is None or df.empty:
        raise DataCleaningError("Data is not available")
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    numeric_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases',
                       'New deaths', 'New recovered', 'Deaths / 100 Cases',
                       'Recovered / 100 Cases', 'Deaths / 100 Recovered',
                       'Confirmed last week', '1 week change', '1 week % increase']
    
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = pd.read_csv('covid_19_data.csv')

        # Handle missing values
    df.fillna(0, inplace=True)

    df['Country/Region'] = df['Country/Region'].str.upper()

    return df
```
# File Handling (file_handling.py)
File handling functions are used open the file and write the data into Clean_Covid_Data.csv
File handling functions are used for saving cleaned data and loading data from files.

```import os
import pandas as pd
def save_to_csv(data, filename='Clean_Covid_Data.csv'):
    data.to_csv(filename, index=False)
    print(f'Saved cleaned data to {filename}')

def load_from_csv(filename='Clean_Covid_Data.csv'):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    return pd.read_csv(filename)
```
# Exception Handling (Exception.py)
Custom exceptions are defined in 'Exception.py 'and are handled throughout the project to manage errors effectively.

```
import pandas as pd 
class DataCleaningError(Exception):
    def __init__(self, message="Error during data cleaning"):
        self.message = message
        super().__init__(self.message)
```
# Analysis (analysis.py)
The code reads, cleans, and visualizes the COVID-19 data, by using 'pandas' for data manipulation and data cleaning.

```import pandas as pd
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
```


   