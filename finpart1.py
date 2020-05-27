import datetime as dt# sets date and time for data
import matplotlib.pyplot as plt # create plots and graphs
from matplotlib import style # makes it visually appealing many styles to chose from
import pandas as pd # lets you create data structures
import pandas_datareader.data as web # grabs data from yahoo finance

style.use('ggplot')

start = dt.datetime (2017,1,1) #parameters for dataframe df
end = dt.datetime.now()

df = web.DataReader ('SQ', 'yahoo', start ,end)# dataframe is a spreadsheet like excel( feature in panda)
print(df.tail()) # by default it prints 5
df.to_excel('SQ.xls') # converts the file to a specific file format(excel example)