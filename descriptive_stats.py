import os
import pandas as pd
import numpy as np

data = pd.read_excel('Coursework.xlsx', index_col=0)

data.columns = ['market_risk', 'smallMbig', 'highMlow', 'risk_free', 'returns', 'excess_returns']
#print(data)
print(data.describe())
#print(data.mean())


market_risk = data['market_risk']
print(market_risk.mean())

def descptive_stats(x):
    print('sum: ')
    print(x.sum())
    print('median: ')
    print(x.median())
    print('variance: ')
    print(x.var())
    print('mode: ')
    print(x.mode())
   

descptive_stats(data)


