#Compiling all s&p500 adj close to one dataframe
import bs4 as bs
import datetime as dt 
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

def compile_data():
    with open ("sp500tickers.pick","rb") as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()  #this is a empty dataframe

    for count, ticker in enumerate(tickers):  #enumerate numbers the rows so you can count them
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date',inplace=True)

        df.rename(columns = {'Adj Close': ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'], 1, inplace=True)   # the number 1th is what axis to drop on

        if main_df.empty:  # we have to do this b/c in the beggining the DF is empty so it wont joined  correctly
            main_df =df
        else:
            main_df = main_df.join(df, how= 'outer') #outer keeps both data if it messes up when it can't join

        print(count)

    print(main_df.tail())
    main_df.to_csv('sp500_joined_closes.csv') #This saves the updated file to csv

compile_data()

