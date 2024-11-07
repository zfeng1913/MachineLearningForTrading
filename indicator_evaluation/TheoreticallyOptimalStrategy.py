import datetime as dt
import os
import numpy as np

import pandas as pd
from util import get_data, plot_data

def author():
  return 'zfeng305'
def testPolicy(
    symbol="AAPL",
    sd=dt.datetime(2010, 1, 1),
    ed=dt.datetime(2011, 12, 31),
    sv = 100000):
    dates = pd.date_range(sd, ed)
    prices = get_data([symbol], dates, addSPY=True).dropna(how='all').drop(columns='SPY')
    prices = prices.fillna(method='ffill').fillna(method='bfill')
    df_trades = pd.DataFrame(columns=[symbol], index=prices.index)
    prices['change'] = prices.diff().shift(-1).fillna(0)
    cum_pos = 0
    for d in prices.index:
        if prices.loc[d, 'change'] > 0 and cum_pos < 1000:
            df_trades.loc[d, symbol] = 1000 - cum_pos
            cum_pos = 1000
        elif prices.loc[d, 'change'] < 0 and cum_pos > -1000:
            df_trades.loc[d, symbol] = -1000 - cum_pos
            cum_pos = -1000
        else:
            df_trades.loc[d, symbol] = 0
    df_trades.index.name = 'Date'
    return df_trades