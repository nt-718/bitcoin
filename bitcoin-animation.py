import ccxt
import json
import requests
from time import sleep
from itertools import count
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')
mpl.use('TkAgg')

# GMOコイン 板情報
def gmo_table():
    ita_prep = requests.get('https://api.coin.z.com/public/v1/ticker?symbol=BTC')
    ita = ita_prep.json()['data'][0]
    return ita

# Coincheck 板情報
base = ccxt.coincheck()
def coin_table():
    ticker = base.fetch_ticker(symbol='BTC/JPY')
    return ticker

x      = []      # x軸
index  = count() # x軸(カウント)
y_gmo  = []      # gmo(ask)
y_coin = []      # coincheck(ask

# グラフ可視化関数
def animate(i):
    gmo_ask =  float(gmo_table()["ask"])       # GMOコイン(買値)
    coincheck_ask = float(coin_table()["ask"]) # Coin Check(買値)

    # リスト格納
    x.append(next(index))
    y_gmo.append(gmo_ask)
    y_coin.append(coincheck_ask)

    # グラフ設定
    plt.cla()
    plt.title("Compare Ask")
    plt.xlabel("Time")
    plt.ylabel("Bitcoin[BTC]")
    plt.plot(x,y_gmo ,label="GMO Coin")
    plt.plot(x,y_coin ,label="Coin Check")
    plt.legend(loc="upper left")
    plt.tight_layout()

# アニメーショングラフ適用(インターバル：2秒)
ani = FuncAnimation(plt.gcf(),animate,interval=1000)

# グラフ表示
plt.tight_layout()
plt.show()