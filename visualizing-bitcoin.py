import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf

import datetime as dt

crypto = "BTC"
currency = "USD"

start = dt.datetime(2021,1,1)
end = dt.datetime.now()

btc = web.DataReader(f"{crypto}-{currency}","yahoo",start,end)
eth = web.DataReader(f"ETH-{currency}","yahoo",start,end)

plt.yscale("log")

plt.plot(btc['Close'], label="BTC")
plt.plot(eth['Close'], label="ETH")
plt.legend(loc="upper left")
plt.show()

# print(btc)

# plt.plot(btc['Close'])
# plt.show()
# mpf.plot(btc, type="candle", volume=True, style="yahoo")