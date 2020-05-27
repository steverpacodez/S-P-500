import bs4 as bs
import datetime as dt 
import os  #creates new directories
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

def save_sp500_tickers():
    resp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = bs.BeautifulSoup(resp.text,"lxml")
    table = soup.find('table',{'id':'constituents'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.find('td').text.replace('\n',"")
        mapping = str.maketrans(".","-")
        ticker = ticker.translate(mapping)
        tickers.append(ticker)

    with open("sp500tickers.pick","wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers


def get_data_from_yahoo(reload_sp500=False): #reload is to connect it to the prior function when your running it
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pick", "rb") as f: #rb means read bytes
            tickers = pickle.load(f)    #our tickers list
    if not os.path.exists('stock_dfs'):   #makes directories to store the datas
        os.makedirs('stock_dfs')
    
    start = dt.datetime(2015, 1, 1)
    end = dt.datetime.now()
   
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):  #if the file dosent exsist:
            df = web.DataReader(ticker.replace('.','-'), 'yahoo', start, end)
            df.reset_index(inplace=True)
            df.set_index("Date", inplace=True)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()