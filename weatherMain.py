import pandas as pd
from utils import overview, filter_data, analysis_data, data_visualization, clear_console

# This is the main function
def main():
    
    # input file for analysis
    csv_file = "data/weatherData2012.csv"

    try:
        df = pd.read_csv(csv_file)

        # Checking if file is empty or not
        if df.empty:
            print("Given file is empty.")
            return
        
        #convert date -> datetime & sort the data by date
        df['date'] = pd.to_datetime(df['date'],errors='coerce')
        df = df.sort_values(by='date') 
        
        # Handle missing temperature data
        df['max_temperature'] = df['max_temperature'].fillna(df['max_temperature'].mean())
        df['min_temperature'] = df['min_temperature'].fillna(df['min_temperature'].mean())

        # Handle missing humidity data
        df['max_humidity'] = df['max_humidity'].fillna(df['max_humidity'].mean())
        df['min_humidity'] = df['min_humidity'].fillna(df['min_humidity'].mean())

        # Handle missing precipitation data
        df['precipitation'] = df['precipitation'].fillna(df['precipitation'].mean())

        # Adding new columns in df for observation( mean_temperature, mean_humidity)
        df['mean_temperature'] = df[['max_temperature', 'min_temperature']].mean(axis=1)
        df['mean_humidity'] = df[['max_humidity', 'min_humidity']].mean(axis=1)
        
        while True:
            # Main menu
            print("\n===== WEATHER DATA ANALYZER =====")
            print("\n1. Overview of Data")
            print("2. Filter Data (Yearly / Monthly)")
            print("3. Data Analysis")
            print("4. Data Visualization")
            print("5. Exit")

            # Take user choice
            choice = input("Enter your choice (1-5): ")

            # Check if choice is digit or not
            if not choice.isdigit():
                print("Please enter number (1-5)")
                continue

            choice = int(choice)

            if choice == 1:
                clear_console()
                # run overview function
                overview(df)
            
            elif choice == 2:
                clear_console()
                # run filter_data function
                filter_data(df)

            elif choice == 3:
                clear_console()
                # run analysis_data function
                analysis_data(df)

            elif choice == 4:
                clear_console()
                #run data_visualization function
                data_visualization(df, features=['mean_temperature', 'mean_humidity'])

            elif choice == 5:
                break

            else:
                print("Invalid choice.")

    except FileNotFoundError:
        print("Error: File not found.")

    except KeyError as e:
        print(f"Error: Missing required column {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

# Calling main function
if __name__ == "__main__":
    main()