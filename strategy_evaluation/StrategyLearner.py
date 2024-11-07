""""""  		  	   		  		 			  		 			 	 	 		 		 	
"""  		  	   		  		 			  		 			 	 	 		 		 	
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		  		 			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		  		 			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		  		 			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		  		 			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 			  		 			 	 	 		 		 	
or edited.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		  		 			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		  		 			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Student Name: Tucker Balch (replace with your name)  		  	   		  		 			  		 			 	 	 		 		 	
GT User ID: tb34 (replace with your User ID)  		  	   		  		 			  		 			 	 	 		 		 	
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 			  		 			 	 	 		 		 	
"""  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import datetime as dt  		  	   		  		 			  		 			 	 	 		 		 	
import random
import matplotlib.pyplot as plt
from marketsimcode import compute_portvals
  		  	   		  		 			  		 			 	 	 		 		 	
import pandas as pd  		  	   		  		 			  		 			 	 	 		 		 	
import util as ut
import indicators as ind
import BagLearner as bl
import RTLearner as rt
  		  	   		  		 			  		 			 	 	 		 		 	

def author():
  return 'zfeng305'

class StrategyLearner(object):  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  		 			  		 			 	 	 		 		 	
        If verbose = False your code should not generate ANY output.  		  	   		  		 			  		 			 	 	 		 		 	
    :type verbose: bool  		  	   		  		 			  		 			 	 	 		 		 	
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		  		 			  		 			 	 	 		 		 	
    :type impact: float  		  	   		  		 			  		 			 	 	 		 		 	
    :param commission: The commission amount charged, defaults to 0.0  		  	   		  		 			  		 			 	 	 		 		 	
    :type commission: float  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    # constructor  		  	   		  		 			  		 			 	 	 		 		 	
    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		  		 			  		 			 	 	 		 		 	
        """  		  	   		  		 			  		 			 	 	 		 		 	
        Constructor method  		  	   		  		 			  		 			 	 	 		 		 	
        """  		  	   		  		 			  		 			 	 	 		 		 	
        self.verbose = verbose  		  	   		  		 			  		 			 	 	 		 		 	
        self.impact = impact  		  	   		  		 			  		 			 	 	 		 		 	
        self.commission = commission
        self.y = 0.02
        self.learner = bl.BagLearner(learner=rt.RTLearner, kwargs={"leaf_size": 5}, bags=20, boost=False,
                                     verbose=False)
        self.n = 10
  		  	   		  		 			  		 			 	 	 		 		 	
    # this method should create a QLearner, and train it for trading

    def add_evidence(
        self,  		  	   		  		 			  		 			 	 	 		 		 	
        symbol="IBM",  		  	   		  		 			  		 			 	 	 		 		 	
        sd=dt.datetime(2008, 1, 1),  		  	   		  		 			  		 			 	 	 		 		 	
        ed=dt.datetime(2009, 1, 1),  		  	   		  		 			  		 			 	 	 		 		 	
        sv=10000,  		  	   		  		 			  		 			 	 	 		 		 	
    ):  		  	   		  		 			  		 			 	 	 		 		 	
        """  		  	   		  		 			  		 			 	 	 		 		 	
        Trains your strategy learner over a given time frame.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
        :param symbol: The stock symbol to train on  		  	   		  		 			  		 			 	 	 		 		 	
        :type symbol: str  		  	   		  		 			  		 			 	 	 		 		 	
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  		 			  		 			 	 	 		 		 	
        :type sd: datetime  		  	   		  		 			  		 			 	 	 		 		 	
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  		 			  		 			 	 	 		 		 	
        :type ed: datetime  		  	   		  		 			  		 			 	 	 		 		 	
        :param sv: The starting value of the portfolio  		  	   		  		 			  		 			 	 	 		 		 	
        :type sv: int  		  	   		  		 			  		 			 	 	 		 		 	
        """  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
        # add your code to do learning here  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
        # example usage of the old backward compatible util function  		  	   		  		 			  		 			 	 	 		 		 	
        dates = pd.date_range(sd, ed)
        # pull price data
        prices = ut.get_data([symbol], dates, addSPY=True).dropna(how='all')
        prices = prices.drop(columns='SPY').fillna(method='ffill').fillna(method='bfill')
        prices['nreturn'] = prices[symbol].shift(-self.n)/prices[symbol] - 1
        prices['signal'] = 0
        prices['signal'][prices['nreturn'] > self.y + self.impact] = 1
        prices['signal'][prices['nreturn'] < - self.y - self.impact] = -1

        prices['mom'] = ind.get_mom(prices[symbol], n=10).fillna(0)
        prices['bbp'] = ind.get_bbp(prices[symbol], n=10).fillna(0)
        prices['p/ema'] = ind.get_price_over_ema(prices[symbol], n=10).fillna(0)

        self.learner.add_evidence(prices[['mom', 'p/ema', 'bbp']].values, prices['signal'].values)

  		  	   		  		 			  		 			 	 	 		 		 	
    # this method should use the existing policy and test it against new data  		  	   		  		 			  		 			 	 	 		 		 	
    def testPolicy(  		  	   		  		 			  		 			 	 	 		 		 	
        self,  		  	   		  		 			  		 			 	 	 		 		 	
        symbol="IBM",  		  	   		  		 			  		 			 	 	 		 		 	
        sd=dt.datetime(2009, 1, 1),  		  	   		  		 			  		 			 	 	 		 		 	
        ed=dt.datetime(2010, 1, 1),  		  	   		  		 			  		 			 	 	 		 		 	
        sv=10000,  		  	   		  		 			  		 			 	 	 		 		 	
    ):  		  	   		  		 			  		 			 	 	 		 		 	
        """  		  	   		  		 			  		 			 	 	 		 		 	
        Tests your learner using data outside of the training data  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
        :param symbol: The stock symbol that you trained on on  		  	   		  		 			  		 			 	 	 		 		 	
        :type symbol: str  		  	   		  		 			  		 			 	 	 		 		 	
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  		 			  		 			 	 	 		 		 	
        :type sd: datetime  		  	   		  		 			  		 			 	 	 		 		 	
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  		 			  		 			 	 	 		 		 	
        :type ed: datetime  		  	   		  		 			  		 			 	 	 		 		 	
        :param sv: The starting value of the portfolio  		  	   		  		 			  		 			 	 	 		 		 	
        :type sv: int  		  	   		  		 			  		 			 	 	 		 		 	
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		  		 			  		 			 	 	 		 		 	
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		  		 			  		 			 	 	 		 		 	
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		  		 			  		 			 	 	 		 		 	
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		  		 			  		 			 	 	 		 		 	
        :rtype: pandas.DataFrame  		  	   		  		 			  		 			 	 	 		 		 	
        """  		  	   		  		 			  		 			 	 	 		 		 	

        dates = pd.date_range(sd, ed)
        # pull price data
        prices_all = ut.get_data([symbol], dates, addSPY=True).dropna(how='all')
        prices = prices_all.drop(columns='SPY').fillna(method='ffill').fillna(method='bfill')
        trades = pd.DataFrame(columns=[symbol], index=prices.index)
        prices['nreturn'] = prices[symbol].shift(-self.n)/prices[symbol] - 1
        prices['signal'] = 0
        prices['signal'][prices['nreturn'] > self.y + self.impact] = 1
        prices['signal'][prices['nreturn'] < -self.y - self.impact] = -1

        prices['mom'] = ind.get_mom(prices[symbol], n=self.n).fillna(0)
        prices['bbp'] = ind.get_bbp(prices[symbol], n=self.n).fillna(0)
        prices['p/ema'] = ind.get_price_over_ema(prices[symbol], n=self.n).fillna(0)
        trades_signal = self.learner.query(prices[['mom', 'p/ema', 'bbp']].values)
        cum_pos = 0
        for i in range(len(trades.index)):
            d = trades.index[i]
            signal = trades_signal[i]
            if signal > 0 and cum_pos < 1000:
                trades.loc[d, symbol] = 1000 - cum_pos
                cum_pos = 1000
            elif signal < 0 and cum_pos > -1000:
                trades.loc[d, symbol] = -1000 - cum_pos
                cum_pos = -1000
            else:
                trades.loc[d, symbol] = 0

        if self.verbose:  		  	   		  		 			  		 			 	 	 		 		 	
            print(type(trades))  # it better be a DataFrame!  		  	   		  		 			  		 			 	 	 		 		 	
        if self.verbose:  		  	   		  		 			  		 			 	 	 		 		 	
            print(trades)  		  	   		  		 			  		 			 	 	 		 		 	
        if self.verbose:  		  	   		  		 			  		 			 	 	 		 		 	
            print(prices_all)  		  	   		  		 			  		 			 	 	 		 		 	
        return trades

  		  	   		  		 			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		  		 			  		 			 	 	 		 		 	
    print("One does not simply think up a strategy")




