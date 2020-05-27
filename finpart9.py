#Making a machine that recognizes corellation relationship between the stocks
#convert pricing to percentage change and it would be our features. Take into account all other companies feature and the company we are considering as well to analyze
#buy,sell,hold are our labels
#if it went up more than %2 its a buy etc.
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
    return tickers,df


proccess_data_for_labels('AAPL')





