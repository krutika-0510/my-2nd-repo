## Covid-19 Data Visualization ##

## Description of Dataset
This project is a Python-based data visualization dashboard for COVID-19 data. 
It includes modules for data cleaning, file handling, exception handling, analysis of data, visualization, and dashboard creation.

## Columns used for Data Visualization:
- Country/Region : Name of the country or region.
- Confirmed : Total confirmed COVID-19 cases.
- Deaths : Total deaths due to COVID-19.
- Recovered : Total recovered COVID-19 cases.
- New cases : Total New Cases of COVID-19 cases.

# How to run the Code
To run the program based on this project, follow these steps:

## 1. Setup the Environment:
    -> Ensure proper/required version of Python is installed on your system.
    -> Install required libraries using by pip:
        pip install pandas
        pip install matplotlib
        pip install streamlit
        
## 2. Use the Dataset
    - Use the 'clean_covid_data.csv' dataset for the project.  

## 3. Run the Application
    - Open a terminal or command prompt.
    - Navigate to the project directory.
    - Execute the following command:
        streamlit run dashboard.py
    - This command will start a local server and open the application in your default web browser.   

# Data Cleaning (data_cleaning.py)
The data cleaning process involves loading the dataset, handling missing values, removing duplicates.

```import pandas as pd
import os
from Exception import DataCleaningError

#Data cleaning function
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

# Exception (Exception.py)
Custom exceptions are defined in 'Exception.py 'and are handled throughout the project to manage errors effectively.

#Custom exception class
import os
import pandas as pd 
class DataCleaningError(Exception):
    def __init__(self, message="Error during data cleaning"):
        self.message = message
        super().__init__(self.message)

# File Handling (file_handling.py)
File handling functions are used open the file and write the data into clean_covid_data.csv
File handling functions are used for saving cleaned data and loading data from files.

```import os
import pandas as pd
def save_to_csv(data, filename='clean_covid_data.csv'):
    data.to_csv(filename, index=False)
    print(f'Saved cleaned data to {filename}')

def load_from_csv(filename='clean_covid_data.csv'):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    return pd.read_csv(filename)
```
# Dashboard (dashboard.py)
Creates a Streamlit dashboard for user interactive data visualization.

```import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_dashboard():

#Load the cleaned dataset
    try:
        df = pd.read_csv('clean_covid_data.csv')
    except FileNotFoundError:
        st.error("File 'clean_covid_data.csv' not found.")
        st.stop()

#User inputs
    countries = st.multiselect('Select Country/Region', df['Country/Region'].unique())
    case_type = st.selectbox('Select Case Type', ['Confirmed', 'Deaths', 'Recovered'])
    filtered_data = df[df['Country/Region'].isin(countries)]

#Function to plot bar chart
    def plot_bar_chart(data, case_type):
        plt.figure(figsize=(10, 6))
        data.groupby('Country/Region').sum()[case_type].plot(kind='bar', color='skyblue')
        plt.xlabel('Country/Region')
        plt.ylabel(f'Number of {case_type} Cases')
        plt.title(f'Total {case_type} Cases by Country/Region')
        plt.xticks(rotation=45)
        st.pyplot(plt)

#Display the bar chart based on user selections
    if st.button('Generate Bar Chart'):
        if filtered_data.empty:
            st.warning("No data available for the selected filters.")
        else:
            plot_bar_chart(filtered_data, case_type)
```

# Visualization (visualization.py)
Generates plots for total Confirmed, Deaths, and Recovered cases of each country.
Also generates a plot for total cases in top 10 countries.

```import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    return pd.read_csv(filename)

def plot_total_cases(df):
    df_country = df.groupby('Country/Region').sum()
    countries = df_country.index.tolist()

    i = 0
    while i < len(countries):
        country = countries[i]
        df_total = df_country.loc[country, ['Confirmed', 'Deaths', 'Recovered']].to_frame().reset_index()
        df_total.columns = ['CaseType', 'Count']

        colors = {'Confirmed': 'blue', 'Deaths': 'red', 'Recovered': 'green'}

        ax = df_total.plot(kind='bar', x='CaseType', y='Count', legend=False, color=[colors[case] for case in df_total['CaseType']], figsize=(5, 5))

        plt.xlabel('Case Type')
        plt.ylabel('Count')
        plt.title(f'Total Confirmed, Deaths, and Recovered Cases in {country}')

        # Adding data labels
        for idx, row in df_total.iterrows():
            plt.text(idx, row['Count'], str(row['Count']), ha='center', va='bottom', color=colors[row['CaseType']])

        plt.tight_layout()
        plt.show()

        # input(f'Press Enter to continue to the next country...')
        plt.close()

        i += 1

def plot_top_countries(df):
    df_country = df.groupby('Country/Region').sum()
    df_top_countries = df_country.nlargest(10, 'Confirmed')[['Confirmed', 'Deaths', 'Recovered']]

    colors = ['blue', 'red', 'green']

    ax = df_top_countries.plot(kind='bar', stacked=True, figsize=(12, 8), color=colors)

    plt.xlabel('Country/Region')
    plt.ylabel('Count')
    plt.title('Top 10 Countries with Highest Number of Cases')
    plt.legend(['Confirmed', 'Deaths', 'Recovered'])

    # Adding data labels
    for bar in ax.patches:
        if bar.get_height() > 0:  # To avoid placing text on bars with height 0
            plt.text(bar.get_x() + bar.get_width() / 2,
                     bar.get_y() + bar.get_height() / 2,
                     f'{int(bar.get_height())}',
                     ha='center',
                     va='center',
                     color='white' if bar.get_height() > 20000 else 'black')  # White text for better contrast on large bars

    plt.tight_layout()
    plt.show()
    plt.close()

if __name__ == "__main__":
    filename = '/content/clean_covid_data.csv'
    df = load_data(filename)

    print("Displaying individual country charts:")
    plot_total_cases(df)

    print("Displaying top 10 countries with highest number of cases:")
    plot_top_countries(df)
```

# Analysis (analysis.py) 
Organize/Arrange data cleaning, visualization, and dashboard creation.

```import visualization
import dashboard
import file_handling
import Exception
import data_cleaning

def main():
    # Read the dataset
    df = file_handling.save_to_csv('C:\\Users\\Lenovo\\Desktop\\Python\\clean_covid_data.csv')

    try:
        # Clean the data
        df = data_cleaning.clean_data(df)
        
        # Write cleaned data to CSV
        file_handling.save_to_csv(df, 'C:\\Users\\Lenovo\\Desktop\\Python\\clean_covid_data.csv')
        
    except Exception.DataCleaningError as e:
        print(f"Data cleaning error: {e}")
        return

    # Plot visualizations
    visualization.plot_total_cases(df)
    visualization.plot_top_countries(df)


    # Create dashboard (assuming dashboard.py has a function named create_dashboard)
    dashboard.create_dashboard(df)
```