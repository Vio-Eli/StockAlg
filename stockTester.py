import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import csv
from AV import incoming_data as datastock

stockList = ["INTC", "GOOGL", "AAPL"]
principal = 100


start = dt.datetime(2015, 1, 1)
end = dt.date.today()
datelist = pd.date_range(start, end).tolist()
myList = [["date", "Adj Close"]]
data_type = 'adj close'

for i in datelist:
    myList.append([mdates.date2num(i.strftime("%Y-%m-%d")), 100])

with open('stockTesting.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(myList)
    csvFile.close()

"""#FIXME ARCHIVED
for i in stockList:
    stockData = yf.download(i,'1970-01-01','2050-08-01')
    #print(stockData) #FIXME Debug
    stockData['Adj Close'].plot() 
"""

myData = pd.read_csv('stockTesting.csv', index_col = 'date')
#print(myData) #FIXME Debug
myData['Adj Close'].plot()

for i in stockList:
    #data = AlphaVantage.GetStockData(i, interval)
    #data['4. close'].plot() #FIXME Broken way of getting data from api. OLD

    df = datastock(i, data_type)
    print(df)
    df[data_type].plot()

    

#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')

plt.show()