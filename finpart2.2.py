import datetime as dt# sets date and time for data
import matplotlib.pyplot as plt # create plots and graphs
from matplotlib import style # makes it visually appealing many styles to chose from
import pandas as pd # lets you create data structures
import pandas_datareader.data as web # grabs data from yahoo finance
style.use('ggplot')

df = pd.read_excel('SQ.xls',parse_dates=True, index_col=0)
# parse_dates makes the date coloumn as the index of the dataframe

df['Adj Close'].plot() # demostrates graph

plt.show # older version needs this to show graph