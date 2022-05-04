from tracemalloc import start
from turtle import color
import pandas_datareader.data as reader
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

end = dt.datetime.now()
start = dt.date(end.year - 4, end.month, end.day)
cryptolist = ['BTC-USD','ETH-USD','XRP-USD','LTC-USD']

df = reader.get_data_yahoo(cryptolist, start, end)['Close']
# print(df)

# df.plot()
# plt.show()

daily_returns = df.pct_change().dropna(axis=0)
daily_cum_returns = (daily_returns +1).cumprod() -1

colors = ['r', 'k', 'b', 'g']
daily_cum_returns.plot(color=colors, figsize=(11,6))
plt.title('Cumulative returns of the largest cryptocurrencies')
# plt.show()

fig, axs= plt.subplots(2, 2, figsize=(14,8), gridspec_kw={'hspace': 0.2, 'wspace':0.1})
axs[0,0].plot(df['BTC-USD'], c='r')
axs[0,0].set_title('BTC')
axs[0,1].plot(df['ETH-USD'], c='k')
axs[0,1].set_title('ETH')
axs[1,0].plot(df['XRP-USD'], c='b')
axs[1,0].set_title('XRP')
axs[1,1].plot(df['LTC-USD'], c='g')
axs[1,1].set_title('LTC')


fig, axs= plt.subplots(2, 2, figsize=(14,8), gridspec_kw={'hspace': 0.2, 'wspace':0.1})
axs[0,0].plot(daily_returns['BTC-USD'], c='r')
axs[0,0].set_title('BTC')
axs[0,0].set_ylim([-0.6,0.6])
axs[0,1].plot(daily_returns['ETH-USD'], c='k')
axs[0,1].set_title('ETH')
axs[0,1].set_ylim([-0.6,0.6])
axs[1,0].plot(daily_returns['XRP-USD'], c='b')
axs[1,0].set_title('XRP')
axs[1,0].set_ylim([-0.6,0.6])
axs[1,1].plot(daily_returns['LTC-USD'], c='g')
axs[1,1].set_title('LTC')
axs[1,1].set_ylim([-0.6,0.6])

fig, axs= plt.subplots(2, 2, figsize=(14,8), gridspec_kw={'hspace': 0.2, 'wspace':0.1})
axs[0,0].set_title('BTC')
axs[0,0].hist(daily_returns['BTC-USD'], bins=100, color='r', range=(-0.2, 0.2))

axs[0,1].hist(daily_returns['ETH-USD'], bins=100, color='k', range=(-0.2, 0.2))
axs[0,1].set_title('ETH')

axs[1,0].hist(daily_returns['XRP-USD'], bins=100, color='b', range=(-0.2, 0.2))
axs[1,0].set_title('XRP')

axs[1,1].hist(daily_returns['LTC-USD'], bins=100, color='g', range=(-0.2, 0.2))
axs[1,1].set_title('LTC')
plt.show()

daily_returns.boxplot(showfliers=False)
plt.title('Boxplot of daily returns without outliers')

plt.show()

daily_returns.corr()
sns.heatmap(daily_returns.corr())
plt.show()

