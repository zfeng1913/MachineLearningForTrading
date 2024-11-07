import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from util import get_data, plot_data

def author():
  return 'zfeng305'

def get_mom(price, n=10):
    momentum = (price / price.shift(n)) - 1
    return momentum

def get_bbp_upper(price, n=10):
    return get_sma(price, n) + 2 * price.rolling(n).std()

def get_bbp_lower(price, n=10):
    return get_sma(price, n) - 2 * price.rolling(n).std()

def get_bbp(price, n=10):
    upper_band = get_bbp_upper(price, n)
    lower_band = get_bbp_lower(price, n)
    return (price - lower_band) / (upper_band - lower_band)

def get_price_over_sma(prices, n=10):
    sma = get_sma(prices, n)
    return prices/sma

def get_ema(prices, n=10):
    return prices.ewm(span=n, min_periods=n-1).mean()

def get_price_over_ema(prices, n=10):
    ema = get_ema(prices, n)
    return prices/ema

def get_sma(prices, n=10):
    return prices.rolling(n).mean()

def get_ppo(prices, n=4, m=10):
    return (get_ema(prices, m) - get_ema(prices, n)) / get_ema(prices, m)

def plot_all_technical_indicators(
    symbol="AAPL",
    sd=dt.datetime(2010, 1, 1),
    ed=dt.datetime(2010, 6, 30)):
    dates = pd.date_range(sd, ed)
    prices = get_data([symbol], dates).dropna(how='all')
    prices = prices[symbol].fillna(method='ffill').fillna(method='bfill')
    nor_prices = prices/prices[0]

    mom = get_mom(prices)
    plt.figure()
    plt.title('MOM and Price')
    plt.ylabel('Price or MOM $')
    plt.xlabel('Time')
    plt.plot(nor_prices, color='purple', label='Normalized_Price')
    plt.axhline(0, linestyle='--', linewidth=1.5, color='green')
    plt.axhline(-0.1, linestyle='--', linewidth=1.5, color='green')
    plt.axhline(0.1, linestyle='--', linewidth=1.5, color='green')
    plt.plot(mom, color='red', label='MOM_10')
    plt.legend()
    plt.savefig('images/MOM_and_Price.png')

    plt.figure()
    price_over_ema = get_price_over_ema(nor_prices)
    ema = get_ema(nor_prices)
    plt.title('Price/EMA_10 and Normalized Price')
    plt.ylabel('Normalized_Price or  Normalized_Price/EMA $')
    plt.xlabel('Time')
    plt.axhline(1, linestyle='--', linewidth=1.5, color='green')
    plt.axhline(0.9, linestyle='--', linewidth=1.5, color='green')
    plt.axhline(1.1, linestyle='--', linewidth=1.5, color='green')
    plt.plot(nor_prices, color='purple', label='Normalized_Price')
    plt.plot(price_over_ema, color='red', label='Price/EMA_10')
    plt.plot(ema, color='blue', label='EMA_10')
    plt.legend()
    plt.savefig('images/Normalized_Price_Price_over_EMA_10.png')

    price_over_sma = get_price_over_sma(nor_prices)
    sma = get_sma(nor_prices)
    plt.figure()
    plt.title('Price/SMA_10 and Normalized Price')
    plt.ylabel('Normalized_Price or Nor_Price/SMA_10 $')
    plt.xlabel('Time')
    plt.plot(nor_prices, color='purple', label='Normalized_Price')
    plt.plot(sma, color='blue', label='SMA_10')
    plt.plot(price_over_sma, color='red', label='Price/SMA_10')
    plt.axhline(1, linestyle='--', linewidth=1.5, color='green')
    plt.axhline(0.9, linestyle='--', linewidth=1.5, color='green')
    plt.axhline(1.1, linestyle='--', linewidth=1.5, color='green')
    plt.legend()
    plt.savefig('images/Normalized_Price_Price_over_SMA.png')

    ppo = get_ppo(nor_prices)
    ema_4 = get_ema(nor_prices, 4)
    ema_10 = get_ema(nor_prices, 10)
    plt.figure()
    plt.title('PPO and Normalized Price')
    plt.ylabel('Normalized Price or PPO $')
    plt.xlabel('Time')
    plt.plot(nor_prices, color='purple', label='Normalized Price')
    plt.axhline(0, linestyle='--', linewidth=1.5, color='green')
    plt.plot(ppo, color='red', label='ppo_4_10')
    plt.plot(ema_4, color='green', label='ema_4')
    plt.plot(ema_10, color='blue', label='ema_10')
    plt.legend()
    plt.savefig('images/Normalized_Price_PPO_4_10.png')

    bbp = get_bbp(prices)
    plt.figure()
    plt.title('BBP_10 and Price')
    plt.ylabel('Price or BBP_10 $')
    plt.xlabel('Time')
    plt.plot(nor_prices, color='purple', label='Nor_Price')
    plt.plot(bbp, color='red', label='BBP_10')
    plt.axhline(0, linestyle='--', linewidth=1.5, color='green')
    plt.axhline(1, linestyle='--', linewidth=1.5, color='red')
    plt.legend()
    plt.savefig('images/Price_BBP_10.png')

    plt.figure()
    plt.title('BBP_10 and Price')
    plt.ylabel('Price or BBP_10 $')
    plt.xlabel('Time')
    sma = get_sma(prices)
    bbp_upper = get_bbp_upper(prices)
    bbp_lower = get_bbp_lower(prices)
    plt.plot(prices, color='purple', label='Price')
    plt.plot(sma, color='red', label='SMA_10')
    plt.plot(bbp_upper, color='yellow', label='BBP_10_upper')
    plt.plot(bbp_lower, color='blue', label='BBP_10_lower')
    plt.legend()
    plt.savefig('images/Price_BBP_explain.png')
    return prices





