import os
import pandas as pd
def save_to_csv(data, filename='clean_covid_data.csv'):
    data.to_csv(filename, index=False)
    print(f'Saved cleaned data to {filename}')

def load_from_csv(filename='clean_covid_data.csv'):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    return pd.read_csv(filename)