#There are video lessons on mapping functions and args
import numpy as numpy
import pandas as pd 
import pickle

def buy_sell_hold(*args):   #Lets  us pass any # of paramaters,arguments and becomes an iriteable
    cols = [c for c in args] #List comperhension
    #The way this work, when mapping to pandas, you have function and it goes by rows and you can pass columns (passing tommorows price, the next day, following day)
    requirement= 0.02 #if the stock prices goes up by 2% within 7 days we buy, if it falls 2% we sell
for col in cols:
    if col > requirement:
        return 1  #buy
    if col < -requirement:
        return -1  #sell
return 0  #hold