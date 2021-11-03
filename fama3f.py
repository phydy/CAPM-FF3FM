import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_excel('Coursework.xlsx', index_col=0)
data.columns = ['market_risk', 'smallMbig', 'highMlow', 'risk_free', 'returns', 'excess_returns']

x = data[['market_risk', 'smallMbig', 'highMlow']]
y = data['excess_returns']

#creates a constant
x_sm = sm.add_constant(x)

model = sm.OLS(y, x_sm)
result = model.fit()

print(result.summary())

sb.regplot(x='market_risk', y='excess_returns', data=data)
sb.regplot(x='smallMbig', y='excess_returns', data=data)
sb.regplot(x='highMlow', y='excess_returns', data=data)
plt.show()