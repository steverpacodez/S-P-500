#Getting Data of all S&P500
import bs4 as bs        # beautifulsoup4
import datetime as dt 
import os
import pandas as pd
import pandas_datareader.data as web
import pickle #serializes any python object (saves any object)
import requests

def save_sp500_tickers():
    resp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = bs.BeautifulSoup(resp.text,"lxml") #text gets the text of the source code, use lxml because it needs it as a parser
    table = soup.find('table',{'id':'constituents'}) # what you want from site: table, what specidic thing you want: id consitutes
    tickers = []
    for row in table.findAll('tr')[1:]:  #tr means table row , [1:] means start from second row onward since the first row is just headers we dont need 
        ticker = row.find_all('td') [0].text.replace('\n','')
        tickers.append(ticker)

    with open("sp500tickers.pick","wb") as f:   #wb means write bytes
        pickle.dump(tickers, f)   #dumping tickers to the file called f

    print(tickers)

    return tickers

save_sp500_tickers()