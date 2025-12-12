import pandas as pd

df = pd.read_csv("data/Madrid Daily Weather 1997-2015.csv")

#clip only required column
clipped_data = df[["date","max_temperature","min_temperature","max_humidity","min_humidity","precipitation"]]

#converting string -> datetime object
clipped_data["date"] = pd.to_datetime(clipped_data["date"], format="%d-%m-%Y")

#converting datetime -> format (yyyy-mm-dd)
clipped_data["date"] = clipped_data["date"].dt.strftime("%Y-%m-%d")

#taking the data of 2012 only
data_2012 = clipped_data[ clipped_data["date"].str.startswith("2012")]
#reset the index
data_2012 = data_2012.reset_index(drop=True)
print(data_2012)
#check for null value
print(data_2012.isnull().sum())

#save the filtered data
data_2012.to_csv("data/weatherData2012.csv",index=False)