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
def get_ema(prices, n=10):
    return prices.ewm(span=n, min_periods=n-1).mean()

def get_bbp(price, n=10):
    upper_band = get_sma(price, n) + 2 *  price.rolling(n).std()
    lower_band = get_sma(price, n) - 2 *  price.rolling(n).std()
    bbp = (price - lower_band) / (upper_band - lower_band)
    return bbp
def get_price_over_sma(prices, n=10):
    sma = get_sma(prices, n)
    return prices/sma

def get_price_over_ema(prices, n=10):
    ema = get_ema(prices, n)
    return prices/ema
def get_sma(prices, n=10):
    return prices.rolling(n).mean()

def get_ppo(prices, n=4, m=14):
    return (get_ema(prices, m) - get_ema(prices, n)) / get_ema(prices, m)





