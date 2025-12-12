import pandas as pd

#Define file to import
csv_file = "data/weatherData2012.csv"

# Display summerize info
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

filter_data()