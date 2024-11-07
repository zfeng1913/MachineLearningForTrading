import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import indicators as ind
from util import get_data
from marketsimcode import compute_portvals

def author():
  return 'zfeng305'
class ManualStrategy(object):
    def __init__(self, verbose=False, impact=0.0, commission=0.0):
        """
        Constructor method
        """
        self.verbose = verbose
        self.impact = impact
        self.commission = commission

    def testPolicy(
        self,
        symbol="JPM",
        sd=dt.datetime(2008, 1, 1),
        ed=dt.datetime(2009, 12, 31),
        sv=100000):

        dates = pd.date_range(sd, ed)

        # pull price data
        prices = get_data([symbol], dates, addSPY=True).dropna(how='all')
        prices = prices.drop(columns='SPY').fillna(method='ffill').fillna(method='bfill')
        prices['nor_price'] = prices[symbol] / prices[symbol].iloc[0]
        mom = ind.get_mom(prices[symbol]).fillna(0)
        price_over_ema = ind.get_price_over_ema(prices['nor_price'], n=10).fillna(0)
        bbp = ind.get_bbp(prices[symbol]).fillna(0)
        prices['mom'] = 0
        prices['mom'][mom < -0.1] = 1
        prices['mom'][mom > 0.1] = -1
        prices['bbp'] = 0
        prices['bbp'][bbp < 0] = 1
        prices['bbp'][bbp > 1] = -1
        prices['p/ema'] = 0
        prices['p/ema'][price_over_ema < 0.95] = 1
        prices['p/ema'][price_over_ema < 1.05] = -1

        df_trades = pd.DataFrame(columns=[symbol], index=prices.index)

        prices['sum'] = prices['p/ema'] + prices['bbp'] + prices['mom']

        cum_pos = 0
        for d in prices.index:
            if prices.loc[d, 'sum'] > 0 and cum_pos < 1000:
                df_trades.loc[d, symbol] = 1000 - cum_pos
                cum_pos = 1000
            elif prices.loc[d, 'sum'] < 0 and cum_pos > -1000:
                df_trades.loc[d, symbol] = -1000 - cum_pos
                cum_pos = -1000
            else:
                df_trades.loc[d, symbol] = 0
        df_trades.index.name = 'Date'
        return df_trades





