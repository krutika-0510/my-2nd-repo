import pandas as pd
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