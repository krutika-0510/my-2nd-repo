import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



# Load the cleaned dataset
try:
    df = pd.read_csv('clean_covid_data.csv')
except FileNotFoundError:
    st.error("File 'clean_covid_data.csv' not found.")
    st.stop()

# User inputs
countries = st.multiselect('Select Country/Region', df['Country/Region'].unique())
case_type = st.selectbox('Select Case Type', ['Confirmed', 'Deaths', 'Recovered'])
filtered_data = df[df['Country/Region'].isin(countries)]

# Function to plot bar chart
def plot_bar_chart(data, case_type):
    plt.figure(figsize=(10, 6))
    data.groupby('Country/Region').sum()[case_type].plot(kind='bar', color='skyblue')
    plt.xlabel('Country/Region')
    plt.ylabel(f'Number of {case_type} Cases')
    plt.title(f'Total {case_type} Cases by Country/Region')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Display the bar chart based on user selections
if st.button('Generate Bar Chart'):
    if filtered_data.empty:
        st.warning("No data available for the selected filters.")
    else:
        plot_bar_chart(filtered_data, case_type)
