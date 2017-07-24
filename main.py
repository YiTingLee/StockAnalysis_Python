import datetime
from pandas_datareader import data

start = datetime.datetime(2017,3,1)
end = datetime.datetime(2017,3,10)

df = data.DataReader(name="GOOG", data_source="google", start=start, end=end)

print(df)