# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:34:49 2020

@author: esaeri-1122
"""

import openpyxl
import os
import pandas as pd
from alphaVantageAPI.alphavantage import AlphaVantage
import ezgmail

os.chdir('C:\\Automate the stock & bitcoin trading with Python\\Data')
workbook = openpyxl.load_workbook('SnP_100.xlsx')
sheet = workbook["SnP100"]

def Checking_MACD_cross():

    Hist_Y = Macd.iloc[-2].loc['MACD_Hist']
    Hist_T = Macd.iloc[-1].loc['MACD_Hist']
    print('Checking '+cell.value)
    if (Hist_Y<0 and Hist_T>0):
        print('We have a MACD golden cross in weekly time frame. Buy '+cell.value)
        # send an e-mail alert
        ezgmail.send('quantumprophetdeveloper@gmail.com',cell.value+' shows a MACD golden cross this week', 'There is a MACD golden cross for '+cell.value+' during this week!')

    else:
        print('No signal')

# alphavantage API key
ts = AlphaVantage(api_key='##############', datatype = 'pandas')

for x in range (2, 103):
    try:
        cell = sheet['A'+str(x)]
        Macd = ts.data(function = 'MACD', symbol = cell.value, interval = 'weekly', series_type = 'close', fastperiod = 12, slowperiod = 26, signalperiod = 9)

        Checking_MACD_cross()
    except:
        print("An error ocurred while trying to connect to Alphavantage API")
