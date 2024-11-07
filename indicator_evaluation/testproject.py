import datetime as dt
import os
import numpy as np
import pandas as pd
from util import get_data, plot_data
from marketsimcode import compute_portvals
import matplotlib.pyplot as plt
import TheoreticallyOptimalStrategy as tos
from indicators import plot_all_technical_indicators

def benchmark(df_trades, symbol):
    benchmark_trades = df_trades.copy()
    benchmark_trades[symbol] = 0
    benchmark_trades.iloc[0] = [1000]
    return benchmark_trades

def draw_plot(optimal, benchmark):
    plt.figure()
    plt.title('Optimal_portfolio vs Benchmark')
    plt.ylabel('Normalized Portfolio Value $')
    plt.xlabel('Time')
    plt.plot(optimal / optimal.iloc[0], color='red', label='optimal portfolio')
    plt.plot(benchmark / benchmark.iloc[0], color='purple', label='benchmark')
    plt.legend()


def author():
  return 'zfeng305'
def test_tos():
    sv = 100000
    # Process orders
    df_trades = tos.testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    portvals = compute_portvals(df_trades, start_val=100000, commission=0, impact=0)
    if isinstance(portvals, pd.DataFrame):
        portvals = portvals[portvals.columns[0]]  # just get the first column
    else:
        "warning, code did not return a DataFrame"

    # Get portfolio stats
    # Here we just fake the data. you should use your code from previous assignments.
    start_date, end_date = min(portvals.index), max(portvals.index)

    cum_ret = portvals.iloc[-1] / portvals.iloc[0] - 1
    daily_return = (portvals[1:] / portvals[:-1].values) - 1
    avg_daily_ret = daily_return.mean()
    std_daily_ret = daily_return.std()

    benchmark_trades = benchmark(df_trades, 'JPM')
    benchmark_portvals = compute_portvals(benchmark_trades, start_val=100000, commission=0, impact=0)
    benchmark_cum_ret = benchmark_portvals.iloc[-1] / benchmark_portvals.iloc[0] - 1
    benchmark_daily_return = (benchmark_portvals[1:] / benchmark_portvals[:-1].values) - 1
    benchmark_avg_daily_ret = benchmark_daily_return.mean()
    benchmark_std_daily_ret = benchmark_daily_return.std()



    # Compare portfolio against $SPX
    print(f"Date Range: {start_date} to {end_date}")
    print()
    print(f"Cumulative Return of Optimal Portfolio: {cum_ret}")
    print(f"Cumulative Return of Benchmark : {benchmark_cum_ret}")
    print()
    print(f"Standard Deviation of Optimal Portfolio: {std_daily_ret}")
    print(f"Standard Deviation of Benchmark : {benchmark_std_daily_ret}")
    print()
    print(f"Average Daily Return of Optimal Portfolio: {avg_daily_ret}")
    print(f"Average Daily Return of Benchmark : {benchmark_avg_daily_ret}")
    print()
    print(f"Final Optimal Portfolio Value: {portvals[-1]}")

    draw_plot(portvals, benchmark_portvals)
    plt.savefig('images/Theoratical_Optimal_Strategy.png')

if __name__ == "__main__":
    test_tos()
    plot_all_technical_indicators('JPM', dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31))