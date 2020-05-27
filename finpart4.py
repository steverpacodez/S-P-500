import datetime as dt# sets date and time for data
import matplotlib.pyplot as plt # create plots and graphs
from matplotlib import style # makes it visually appealing many styles to chose fromfrom mpl-finance import candlestick_ohlc
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates 
import pandas as pd # lets you create data structures
import pandas_datareader.data as web # grabs data from yahoo finance

style.use('ggplot')

df = pd.read_excel('SQ.xls',parse_dates=True, index_col=0)
# parse_dates makes the date coloumn as the index of the dataframe

df_ohlc = df ['Adj Close'].resample ('10D').ohlc()
df_volume = df ['Volume'].resample ('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date() # converts matplotlib dates into visible dates in chart

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values,0)
  #botttom chart  #         x value                          y value
plt.show()