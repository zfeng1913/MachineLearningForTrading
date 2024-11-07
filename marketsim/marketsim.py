""""""  		  	   		  		 			  		 			 	 	 		 		 	
"""MC2-P1: Market simulator.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
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

import os  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import numpy as np  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import pandas as pd  		  	   		  		 			  		 			 	 	 		 		 	
from util import get_data, plot_data

def compute_portvals(
    orders_file="./orders/orders.csv",
    start_val=1000000,
    commission=9.95,
    impact=0.005,
):
    """
    Computes the portfolio values.

    :param orders_file: Path of the order file or the file object
    :type orders_file: str or file object
    :param start_val: The starting value of the portfolio
    :type start_val: int
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)
    :type commission: float
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction
    :type impact: float
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.
    :rtype: pandas.DataFrame
    """
    # this is the function the autograder will call to test your code
    # NOTE: orders_file may be a string, or it may be a file object. Your
    # code should work correctly with either input

    orders = pd.read_csv(orders_file, parse_dates=['Date'], na_values=['nan']).sort_values(by=['Date'])
    # orders = orders_file
    start_date, end_date = min(orders['Date']), max(orders['Date'])
    dates = pd.date_range(start_date, end_date)

    # pull price data
    prices = get_data(orders['Symbol'].unique(), dates).dropna(how='all').drop(columns='SPY')
    prices = prices.fillna(method='ffill').fillna(method='bfill')
    change_in_position = pd.DataFrame(
        columns=orders['Symbol'].unique(), index=prices.index).fillna(0)
    change_in_position['cash'] = start_val
    change_in_position['commission'] = 0

    #translate orders into change_in_positions
    for i in range(len(orders)):
        date, symbol, order, shares = orders.iloc[i]
        sign = -1
        if order == 'SELL':
            sign = 1
        change_in_position.loc[date:, symbol] -= sign * shares
        change_in_position.loc[date:, 'commission'] -= commission + impact * shares * prices.loc[date, symbol]
        change_in_position.loc[date:, 'cash'] += sign * shares * prices.loc[date, symbol]

    for i in orders['Symbol'].unique():
        change_in_position[i] = change_in_position[i].multiply(prices[i])
    change_in_position['sum'] = change_in_position.sum(axis=1)
    return change_in_position['sum']

def author():
  return 'zfeng305'

def test_code():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    Helper function to test code  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    # this is a helper function you can use to test your code  		  	   		  		 			  		 			 	 	 		 		 	
    # note that during autograding his function will not be called.  		  	   		  		 			  		 			 	 	 		 		 	
    # Define input parameters  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    of = "./orders/orders.csv"
    sv = 1000000  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    # Process orders  		  	   		  		 			  		 			 	 	 		 		 	
    portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		  		 			  		 			 	 	 		 		 	
    if isinstance(portvals, pd.DataFrame):  		  	   		  		 			  		 			 	 	 		 		 	
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		  		 			  		 			 	 	 		 		 	
    else:  		  	   		  		 			  		 			 	 	 		 		 	
        "warning, code did not return a DataFrame"  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    # Get portfolio stats  		  	   		  		 			  		 			 	 	 		 		 	
    # Here we just fake the data. you should use your code from previous assignments.
    start_date, end_date = min(portvals.index), max(portvals.index)
    dates = pd.date_range(start_date, end_date)
    cum_ret = portvals.iloc[-1] / portvals.iloc[0] - 1
    daily_return = (portvals[1:] / portvals[:-1].values) - 1
    avg_daily_ret = daily_return.mean()
    std_daily_ret = daily_return.std()
    sharpe_ratio = avg_daily_ret / std_daily_ret
    prices_SPY = get_data(['SPY'], dates).dropna(how='all')
    cum_ret_SPY = (prices_SPY[1:] / prices_SPY[:-1].values) - 1
    daily_return = prices_SPY.shift(1)/ prices_SPY - 1
    avg_daily_ret_SPY = daily_return.mean()
    std_daily_ret_SPY = daily_return.std()
    sharpe_ratio_SPY = avg_daily_ret_SPY / std_daily_ret_SPY
  		  	   		  		 			  		 			 	 	 		 		 	
    # Compare portfolio against $SPX  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Date Range: {start_date} to {end_date}")  		  	   		  		 			  		 			 	 	 		 		 	
    print()  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")  		  	   		  		 			  		 			 	 	 		 		 	
    print()  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Cumulative Return of SPY : {cum_ret_SPY}")  		  	   		  		 			  		 			 	 	 		 		 	
    print()  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")  		  	   		  		 			  		 			 	 	 		 		 	
    print()  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")  		  	   		  		 			  		 			 	 	 		 		 	
    print()  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"Final Portfolio Value: {portvals[-1]}")  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		  		 			  		 			 	 	 		 		 	
    test_code()
