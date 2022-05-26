import pandas as pd
tickers_list = ['AAPL']

# Fetch the data
import yfinance as yf
data = yf.download(tickers_list, start="2021-01-01")
intra_change = ((data["High"]-data["Low"])/data["Low"])*100
volume_next_date = data["Volume"][1:]
data = data[["High", "Low", "Volume"]]
data['Price_change'] = round(intra_change,2)
data["Volume_nextday"]  = data["Volume"].shift(-1)
data["Volume_change%"] = round(((data["Volume_nextday"]-data["Volume"])/data["Volume"])*100,2)

# Print first 5 rows of the data
print(data)



#volume_increase = ((data["High"]-data["Low"])/data["Low"])*100