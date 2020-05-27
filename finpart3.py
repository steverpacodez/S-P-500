import datetime as dt# sets date and time for data
import matplotlib.pyplot as plt # create plots and graphs
from matplotlib import style # makes it visually appealing many styles to chose from
import pandas as pd # lets you create data structures
import pandas_datareader.data as web # grabs data from yahoo finance
style.use('ggplot')

df = pd.read_excel('SQ.xls',parse_dates=True, index_col=0)
# parse_dates makes the date coloumn as the index of the dataframe

df['100ma'] = df ['Adj Close'].rolling(window=100 , min_periods=0).mean() #data frame takes todays price and 99 of the prior day's prices amd creates an avg
#df.dropna(inplace=True) NOTE:to demostrate (df.head()) if needed
print (df.tail())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df ['Adj Close'])  #axis
ax1.plot(df.index, df ['100ma'])
ax2.bar(df.index, df ['Volume'])

plt.show()