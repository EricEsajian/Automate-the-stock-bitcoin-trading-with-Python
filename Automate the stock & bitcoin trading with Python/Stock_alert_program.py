import openpyxl
import os
import pandas as pd
from alphaVantageAPI.alphavantage import AlphaVantage
#from openpyxl import workbook
import ezgmail

os.chdir('C:\\Automate the stock & bitcoin trading with Python\\Data')
workbook = openpyxl.load_workbook('SnP_100.xlsx')
sheet = workbook["SnP100"]

# alphavantage API key
ts = AlphaVantage(api_key='###########', datatype = 'pandas')

def Checking_cross():
    #calculation for today's difference
    TEMA_50 = EMA_50.iloc[-1].loc['EMA']
    TEMA_200 = EMA_200.iloc[-1].loc['EMA']
    TDiff = TEMA_50-TEMA_200
    #calculation for yesterday's difference
    YEMA_50 = EMA_50.iloc[-2].loc['EMA']
    YEMA_200 = EMA_200.iloc[-2].loc['EMA']
    YDiff = YEMA_50-YEMA_200

    if ( YDiff<0 and TDiff>0 ):
        print('We have a golden cross of 50 EMA and 200 EMA! Buy '+cell.value)

        # Send an email alert
        ezgmail.send('quantumprophetdeveloper@gmail.com',cell.value+' shows a golden cross today ', 'There was a golden cross of 50 and 200 EMAs for '+cell.value+' It is good time for buying it!')

    else:
        print('No signal')

for x in range (2, 103):
    try:
        cell = sheet['A'+str(x)]
        EMA_50 = ts.data(symbol = cell.value, function = 'EMA', interval = 'daily', time_period = 50, series_type = 'close')
        EMA_200 = ts.data(symbol = cell.value, function = 'EMA', interval = 'daily', time_period = 200, series_type = 'close')

        print('Checking '+cell.value)
        Checking_cross()
    except:
        print("A problem occurred while connecting to Alpha Vantage API")
