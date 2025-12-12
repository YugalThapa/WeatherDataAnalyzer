import pandas as pd

#Define file to import
csv_file = "data/weatherData2012.csv"

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


    except FileNotFoundError:
        print("File doesn't exist.")

