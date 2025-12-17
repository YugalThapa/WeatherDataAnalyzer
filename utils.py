import pandas as pd

#Define file to import
csv_file = "data/weatherData2012.csv"

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
def overview():
    try:
        df = pd.read_csv(csv_file)      #read csv file
        if df.empty:                    #check if file empty or not
            print("File is empty.")
            return
        
        #convert date -> datetime & sort the data by date
        df['date'] = pd.to_datetime(df['date'],errors='coerce')
        df = df.sort_values(by='date')  

        print("\n====== DATA OVERVIEW =======")

        # Display info
        summerize_info(df)

    except FileNotFoundError:
        print("File doesn't exist.")

# Filter function
def filter_data():
    try:
        df = pd.read_csv(csv_file)
        if df.empty:
            print("File is empty.")
            return

        #convert date -> datetime & sort the data by date
        df['date'] = pd.to_datetime(df['date'],errors='coerce')
        df = df.sort_values(by='date')  

        print("\n----- Filter Data -----")
        print("1. Yearly Data")
        print("2. Monthly Data")

        choice = input("Enter your choice (1 or 2): ")

        # yearly filter
        if choice == "1":
            year = input("Enter year (YYYY): ").strip()
            
            # validation
            if not ( year.isdigit() and len(year) == 4):
                print("Invalid year input.")
                return
            
            year = int(year)
            yearly_data = df[df['date'].dt.year == year]
            
            if yearly_data.empty:
                print(f"No data available for {year} year.")
                return
            
            # sample data
            print(f"\n===== Data of Year {year} =====")
            summerize_info(yearly_data)

        # Monthly filter
        elif choice == "2":
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
            monthly_data = df[(df['date'].dt.year == year) & (df['date'].dt.month == month)]
            
            if monthly_data.empty:
                print(f"No data available for {year}-{month:02d}.")
                return

            # sample data
            print(f"\n===== Data of Month {year}-{month:02d} =====")
            summerize_info(monthly_data)

    except FileNotFoundError:
        print("File doesn't exist.")

# Analysis function
def analysis_data():
    """
    Perform statistical analysis on weather data.
    Handles missing values and prints descriptive statistics.
    """

    try:
        df = pd.read_csv(csv_file)

        if df.empty:
            print("File is empty.")
            return

        print("\n===== STATISTICAL ANALYSIS =====")

        # ---------------- TEMPERATURE ----------------
        print("\n--- Temperature ---")

        # Handle missing temperature data
        df['max_temperature'] = df['max_temperature'].fillna(df['max_temperature'].mean())
        df['min_temperature'] = df['min_temperature'].fillna(df['min_temperature'].mean())

        # Mean temperature per observation
        df['mean_temperature'] = df[['max_temperature', 'min_temperature']].mean(axis=1)

        print(f"No. of observations: {len(df)}")
        print(f"Maximum Temperature: {df['max_temperature'].max():.2f} °C")
        print(f"Minimum Temperature: {df['min_temperature'].min():.2f} °C")
        print(f"Mean Temperature: {df['mean_temperature'].mean():.2f} °C")
        print(f"Median Temperature: {df['mean_temperature'].median():.2f} °C")
        print(f"Standard Deviation: {df['mean_temperature'].std():.2f} °C")

        # ---------------- HUMIDITY ----------------
        print("\n--- Humidity ---")

        df['max_humidity'] = df['max_humidity'].fillna(df['max_humidity'].mean())
        df['min_humidity'] = df['min_humidity'].fillna(df['min_humidity'].mean())

        df['mean_humidity'] = df[['max_humidity', 'min_humidity']].mean(axis=1)

        print(f"No. of observations: {len(df)}")
        print(f"Maximum Humidity: {df['max_humidity'].max():.2f}")
        print(f"Minimum Humidity: {df['min_humidity'].min():.2f}")
        print(f"Mean Humidity: {df['mean_humidity'].mean():.2f}")
        print(f"Median Humidity: {df['mean_humidity'].median():.2f}")
        print(f"Standard Deviation: {df['mean_humidity'].std():.2f}")

        # ---------------- PRECIPITATION ----------------
        print("\n--- Precipitation ---")

        df['precipitation'] = df['precipitation'].fillna(df['precipitation'].mean())

        print(f"No. of observations: {len(df)}")
        print(f"Maximum Precipitation: {df['precipitation'].max():.2f} mm")
        print(f"Minimum Precipitation: {df['precipitation'].min():.2f} mm")
        print(f"Mean Precipitation: {df['precipitation'].mean():.2f} mm")
        print(f"Median Precipitation: {df['precipitation'].median():.2f} mm")
        print(f"Standard Deviation: {df['precipitation'].std():.2f} mm")

    except FileNotFoundError:
        print("File does not exist.")
    except KeyError as e:
        print(f"Missing required column: {e}")
