import os
from matplotlib import colors
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_excel('Coursework.xlsx', index_col=0)
data.columns = ['market_risk', 'smallMbig', 'highMlow', 'risk_free', 'returns', 'excess_returns']

x = data['market_risk']
y = data['excess_returns']
#x_sm = sm.add_constant(x)

model = smf.quantreg('excess_returns ~ market_risk', data)
result1 = model.fit(q=0.1)
result2 = model.fit(q=0.5)
result3 = model.fit(q=0.9)

print(result1.summary())
print(result2.summary())
print(result3.summary())

'''fig, ax = plt.subplots(figsize=(10,8))

get_y = lambda a, b: a +b * x
y = get_y(model.params['Intercept'], model.params['x'])

ax.plot(x, y, color='red')
ax.scatter(x, y_1, alpha=.3)'''

sb.quantregplot(x='market_risk', y='excess_returns', data=data)
plt.show()