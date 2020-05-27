from collections import Counter
import numpy as np 
import pandas as pd
import pickle

def proccess_data_for_labels(ticker): #ticker is an argument
    hm_days = 7 #In the next 7 days does the price go up or down 2%
    df = pd.read_csv('sp500_joined_closes.csv',index_col=0) #This is going to fail
    tickers = df. columns.values.tolist() # converts df into a python list
    df.fillna(0,inplace=True)

    for i in range(1,hm_days+1):  #range go up to a certain a point but ot actaully to that point ad wen want to start at 1 not 0
        df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i)- df[ticker]) /df[ticker]

    df.fillna(0,inplace=True)
    print(df['{}_{}d'.format(ticker,i)])
    return tickers,df,hm_days


def buy_sell_hold(*args):
    columns = [c for c in args]
    requirement = 0.02
    for column in columns:
        if column > requirement:
            return 1
        if column < -requirement:
            return -1
    return 0

def extract__featuresets(ticker):
    tickers, df,hm_days= proccess_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,*[df['{}_{}d'.format(ticker,i)]for i in range(1,hm_days+1)]))
    
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i)for i in vals]
    print('Data Spread:',Counter(str_vals))
    
    df.fillna(0,inplace=True)
    df = df.replace([np.inf, -np.inf],np.nan)
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf],0)
    df_vals.fillna (0, inplace = True)

    X = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return X, y, df

extract__featuresets('AAPL')