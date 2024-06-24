import visualization
import dashboard
import file_handling
import Exception
import data_cleaning

def main():
    # Read the dataset
    df = file_handling.save_to_csv('C:\\Users\\Mahesh\\Desktop\\assign-8\\clean_covid_data.csv')

    try:
        # Clean the data
        df = data_cleaning.clean_data(df)
        
        # Write cleaned data to CSV
        file_handling.save_to_csv(df, 'C:\\Users\\Mahesh\\Desktop\\assign-8\\clean_covid_data.csv')
        
    except Exception.DataCleaningError as e:
        print(f"Data cleaning error: {e}")
        return

    # Plot visualizations
    visualization.plot_total_cases(df)
    visualization.plot_top_countries(df)


    # Create dashboard (assuming dashboard.py has a function named create_dashboard)
    dashboard.create_dashboard(df)

