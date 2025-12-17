import pandas as pd
import matplotlib.pyplot as plt
import os

#clear console 
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Display summerize info. Helper function for Overview function
def summerize_info(df):
    #Basic shape
    print(f"Total rows: {df.shape[0]}")
    print(f"Total column: {df.shape[1]}")

    #column name and type
    print("\n----- Cloumn Info -----")
    print(df.dtypes)

    #sample data
    print("\n----- First 5 rows -----")
    print(df.head(5).to_string(index=False))
    print("\n----- Last 5 rows -----")
    print(df.tail(5).to_string(index=False))

    # date range
    print("\nDate range:")
    print(f"From : {df['date'].min()} To: {df['date'].max()}")

    #check is any value is null
    print("\n----- Missing values -----")
    print(df.isnull().sum())

#Overview of data
def overview(df):
    #convert date -> datetime & sort the data by date
    df['date'] = pd.to_datetime(df['date'],errors='coerce')
    df = df.sort_values(by='date')  

    print("\n====== DATA OVERVIEW =======")

    # Display info
    summerize_info(df)


# Filter function
def filter_data(df): 

    print("\n----- Filter Data -----")
    print("1. Yearly Data")
    print("2. Monthly Data")

    choice = int(input("Enter your choice (1 or 2): "))

    # yearly filter
    if choice == 1:
        year = input("Enter year (YYYY): ").strip()
            
        # validation
        if not ( year.isdigit() and len(year) == 4):
            print("Invalid year input.")
            return
            
        year = int(year)
        yearly_data_df = df[df['date'].dt.year == year]
            
        if yearly_data_df.empty:
            print(f"No data available for {year} year.")
            return
            
        # sample data
        print(f"\n===== Data of Year {year} =====")
        summerize_info(yearly_data_df)

    # Monthly filter
    elif choice == 2:
        month_input = input("Enter month (YYYY-MM): ").strip()

        if "-" not in month_input:
            print("Invalid format. Use YYYY-MM.")
            return
            
        year, month = [x.strip() for x in month_input.split("-")]
            
        # VALIDATION
        if not (year.isdigit() and month.isdigit()):
            print("Year and month must be numeric.")
            return
            
        if len(year) != 4 or not (1 <= int(month) <= 12):
            print("Invalid year or month.")
            return
            
        year, month = int(year), int(month)
        monthly_data_df = df[(df['date'].dt.year == year) & (df['date'].dt.month == month)]
            
        if monthly_data_df.empty:
            print(f"No data available for {year}-{month:02d}.")
            return

        # sample data
        print(f"\n===== Data of Month {year}-{month:02d} =====")
        summerize_info(monthly_data_df)

    else:
        print("Invalid choice.")
        return


# Analysis function
def analysis_data(df):
    """
    Perform statistical analysis on weather data.
    Handles missing values and prints descriptive statistics.
    """

    print("\n===== STATISTICAL ANALYSIS =====")
    print(f"\nTotal observations: {len(df)}")

    # ---------------- TEMPERATURE ----------------
    print("\n--- Temperature ---")
    print(f"Maximum Temperature: {df['max_temperature'].max():.2f} °C")
    print(f"Minimum Temperature: {df['min_temperature'].min():.2f} °C")
    print(f"Mean Temperature: {df['mean_temperature'].mean():.2f} °C")
    print(f"Median Temperature: {df['mean_temperature'].median():.2f} °C")
    print(f"Standard Deviation: {df['mean_temperature'].std():.2f} °C")

    # ---------------- HUMIDITY ----------------
    print("\n--- Humidity ---")
    print(f"Maximum Humidity: {df['max_humidity'].max():.2f}")
    print(f"Minimum Humidity: {df['min_humidity'].min():.2f}")
    print(f"Mean Humidity: {df['mean_humidity'].mean():.2f}")
    print(f"Median Humidity: {df['mean_humidity'].median():.2f}")
    print(f"Standard Deviation: {df['mean_humidity'].std():.2f}")

    # ---------------- PRECIPITATION ----------------
    print("\n--- Precipitation ---")
    print(f"Maximum Precipitation: {df['precipitation'].max():.2f} mm")
    print(f"Minimum Precipitation: {df['precipitation'].min():.2f} mm")
    print(f"Mean Precipitation: {df['precipitation'].mean():.2f} mm")
    print(f"Median Precipitation: {df['precipitation'].median():.2f} mm")
    print(f"Standard Deviation: {df['precipitation'].std():.2f} mm")


# Data visualization for better analysis
def data_visualization(df, features=None):
    """
    Visualize numeric features in the DataFrame.

    Parameters:
        df (pd.DataFrame): Cleaned dataset
        features (list): List of column names to visualize; 
                         if None, all numeric columns are visualized
    """

    # Determine columns to plot
    if features is None:
        features = df.select_dtypes(include='number').columns.tolist()

    # Loop through each feature
    for col in features:
        if col not in df.columns:
            print(f"Warning: Column '{col}' not found, skipping.")
            continue

        # Skip empty columns
        if df[col].dropna().empty:
            print(f"Column '{col}' has no data, skipping.")
            continue

        # Line plot (trend)
        plt.figure(figsize=(6, 4))
        plt.plot(df[col], linestyle='-', color='blue')
        plt.title(f"{col} Trend")
        plt.xlabel("Observation Index")
        plt.ylabel(col)
        plt.grid(True)
        plt.show()

        # Histogram (distribution)
        plt.figure(figsize=(6, 4))
        plt.hist(df[col].dropna(), bins=20, color='orange', edgecolor='black')
        plt.title(f"{col} Distribution")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()

        # Boxplot (outliers)
        plt.figure(figsize=(4, 4))
        plt.boxplot(df[col].dropna())
        plt.title(f"{col} Boxplot")
        plt.ylabel(col)
        plt.show()
