import yfinance as yf
import pandas as pd
import datetime
import requests
import matplotlib.pyplot as plt

# Cryptoのティッカー取得
url = 'https://finance.yahoo.com/cryptocurrencies?offset=0&count=24'
# 取引高の多い株
# url = 'https://finance.yahoo.com/most-active'
# 世界のインデックス
# url = 'https://finance.yahoo.com/world-indices'

ua = "Gozilla/5.0" # Mozilla
r = requests.get(url, headers={'User-Agent': ua})
tables = pd.read_html(r.text)
df = tables[0]
list=df["Symbol"].tolist()
start = datetime.date.today() - datetime.timedelta(days=300)
end = datetime.date.today()
data = yf.download(list, start=start, end=end)["Adj Close"]
df_all300=(1+data.pct_change()).cumprod()
df_all300_2=df_all300.iloc[:,:24].copy()
df_all300_2.sort_values(by=df_all300_2.index[-1], axis=1, ascending=False, inplace=True)
df_all300_2.iloc[:,:24].plot(figsize=(10,20),linewidth=2,alpha=0.5, subplots=True,layout=(8,3),grid=False)

plt.legend(fontsize=50)  
plt.legend(loc = 'best')
plt.show()

print(url)