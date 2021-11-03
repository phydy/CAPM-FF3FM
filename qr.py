from matplotlib import colors
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sb
from lightgbm import LGBMRegressor


data = pd.read_excel('Coursework.xlsx', index_col=0)
data.columns = ['market_risk', 'smallMbig', 'highMlow', 'risk_free', 'returns', 'excess_returns']

X = data['market_risk']
Y = data['excess_returns']

#sb.scatterplot(data=data, x=X, y=Y, marker='+')
#plt.show()

classifiers = {}

for tau in [0.1, 0.5, 0.9]:
    clf = LGBMRegressor(objective='quantile', alpha=tau)
    clf.fit(X, Y)
    preds = pd.DataFrame(clf.predict(X), colunms = [str(tau)])
    classifiers[str(tau)] = {'clf': clf, 'predictions': preds}

df = pd.DataFrame({'market_risk': X.reset_index()['market_risk'],
            '0.1': classifiers['0.1']['predictions']['0.1'],
            '0.5': classifiers['0.5']['predictions']['0.5'],
            '0.9': classifiers['0.9']['predictions']['0.9'],
            'excess_returns': Y.reset_index()['excess_returns']
})
print(df.sample(2))
