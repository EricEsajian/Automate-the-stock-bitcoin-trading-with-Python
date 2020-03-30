# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:49:13 2020

@author: esaeri-1122
"""

import openpyxl
import os
import pandas as pd
from alphaVantageAPI.alphavantage import AlphaVantage
import ezgmail

# Alphavantage API key
ts = AlphaVantage(api_key='##############', datatype = 'pandas')
Bit = ts.digital(symbol='BTC', market='USD')

def calculate_ma(start, end):
    sum = 0
    for x in range (start, end):
        temp = Bit.iloc[x].loc['4a. close (USD)']
        sum = sum + temp
    average = sum / abs((start-end))
    return(average)

MA200_T = calculate_ma(-200, 0)
MA50_T = calculate_ma(-50, 0)
MA200_Y = calculate_ma(-201, -1)
MA50_Y = calculate_ma(-51, -1)

Diff_Y = MA50_Y - MA200_Y
Diff_T = MA50_T - MA200_T
print('Moving average difference was '+str(Diff_Y)+' yesterday')
print('Moving average difference is '+str(Diff_T)+' today')
if (Diff_Y<0 and Diff_T>0 ):
    print('There is a 50 and 200 day MA golden cross!! You need to buy Bitcoin today.')
    ezgmail.send('quantumprophetdeveloper@gmail.com', 'Buy Bitcoin today!', 'There is a golden cross signal for Bitcoin today. you need to buy it')
else:
    print('There is no signal')
