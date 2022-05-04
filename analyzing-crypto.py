from cProfile import label
from distutils.command.build_scripts import first_line_re
from locale import currency
from tracemalloc import start
import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
import datetime as dt

from sklearn import metrics

currency = "USD"
metric = "Close"

start = dt.datetime(2021,1,1)
end = dt.datetime.now()

crypto = ['BTC','ETH','XRP','LTC']
colnames = []

first = True

for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

# plt.yscale('log')

# for ticker in crypto:
#     plt.plot(combined[ticker],label=ticker)

# plt.legend(loc="upper left")


combined = combined.pct_change().corr(method="pearson")
sns.heatmap(combined, annot=True, cmap="coolwarm")

plt.show()