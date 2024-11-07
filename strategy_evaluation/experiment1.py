import datetime as dt
import matplotlib.pyplot as plt
from marketsimcode import compute_portvals
from ManualStrategy import ManualStrategy
from StrategyLearner import StrategyLearner

def benchmark(df_trades, symbol):
    benchmark_trades = df_trades.copy()
    benchmark_trades[symbol] = 0
    benchmark_trades.iloc[0] = [1000]
    return benchmark_trades

def experiment1(impact=0.005, commission=9.95, symbol='JPM', sv=100000):
    #in_sample

    sl = StrategyLearner(impact=0, commission=0)
    sl.add_evidence(symbol=symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31))
    bag_trades = sl.testPolicy(symbol=symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31))

    ms = ManualStrategy(impact=impact, commission=commission)
    df_trades = ms.testPolicy(symbol=symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=sv)
    portvals = compute_portvals(df_trades, start_val=sv, commission=commission, impact=impact)
    start_date, end_date = min(portvals.index), max(portvals.index)
    cum_ret = portvals.iloc[-1] / portvals.iloc[0] - 1
    daily_return = (portvals[1:] / portvals[:-1].values) - 1
    avg_daily_ret = daily_return.mean()
    std_daily_ret = daily_return.std()

    bag_portvals = compute_portvals(bag_trades, start_val=sv, commission=commission, impact=impact)
    start_date, end_date = min(bag_portvals.index), max(bag_portvals.index)
    bag_cum_ret = bag_portvals.iloc[-1] / bag_portvals.iloc[0] - 1
    bag_daily_return = (bag_portvals[1:] / bag_portvals[:-1].values) - 1
    bag_avg_daily_ret = bag_daily_return.mean()
    bag_std_daily_ret = bag_daily_return.std()

    benchmark_trades = benchmark(df_trades, symbol)
    benchmark_portvals = compute_portvals(benchmark_trades, start_val=sv, commission=commission,
                                          impact=impact)
    benchmark_cum_ret = benchmark_portvals.iloc[-1] / benchmark_portvals.iloc[0] - 1
    benchmark_daily_return = (benchmark_portvals[1:] / benchmark_portvals[:-1].values) - 1
    benchmark_avg_daily_ret = benchmark_daily_return.mean()
    benchmark_std_daily_ret = benchmark_daily_return.std()

    # Compare portfolio against $SPX
    print(f"Date Range: {start_date} to {end_date}")
    print()
    print(f"Cumulative Return of Manual Strategy Portfolio: {cum_ret}")
    print(f"Cumulative Return of StrategyLearner Portfolio: {bag_cum_ret}")
    print(f"Cumulative Return of Benchmark : {benchmark_cum_ret}")
    print()
    print(f"Standard Deviation of Manual Strategy Portfolio: {std_daily_ret}")
    print(f"Standard Deviation of StrategyLearner Portfolio: {bag_std_daily_ret}")
    print(f"Standard Deviation of Benchmark : {benchmark_std_daily_ret}")
    print()
    print(f"Average Daily Return of Manual Strategy Portfolio: {avg_daily_ret}")
    print(f"Average Daily Return of StrategyLearner Portfolio: {bag_avg_daily_ret}")
    print(f"Average Daily Return of Benchmark : {benchmark_avg_daily_ret}")
    print()
    print(f"Final Manual Strategy Portfolio Value: {portvals[-1]}")
    print(f"Final StrategyLearner Portfolio Value: {bag_portvals[-1]}")

    plt.figure()
    plt.title('In-Sample Manual Strategy Portfolio vs StrategyLearner Portfolio vs Benchmark')
    plt.ylabel('Normalized Portfolio Value $')
    plt.xlabel('Time')

    plt.plot(portvals / portvals.iloc[0], color='red', label='Manual Strategy')
    plt.plot(bag_portvals / bag_portvals.iloc[0], color='blue', label='StrategyLearner')
    plt.plot(benchmark_portvals / benchmark_portvals.iloc[0], color='purple', label='benchmark')
    plt.legend()
    plt.savefig('images/experiment1_in-sample-compare.png')

    bag_trades = sl.testPolicy(symbol=symbol, sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31))
    df_trades = ms.testPolicy(symbol=symbol, sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=sv)
    portvals = compute_portvals(df_trades, start_val=sv, commission=commission, impact=impact)
    start_date, end_date = min(portvals.index), max(portvals.index)
    cum_ret = portvals.iloc[-1] / portvals.iloc[0] - 1
    daily_return = (portvals[1:] / portvals[:-1].values) - 1
    avg_daily_ret = daily_return.mean()
    std_daily_ret = daily_return.std()

    bag_portvals = compute_portvals(bag_trades, start_val=sv, commission=commission, impact=impact)
    start_date, end_date = min(bag_portvals.index), max(bag_portvals.index)
    bag_cum_ret = bag_portvals.iloc[-1] / bag_portvals.iloc[0] - 1
    bag_daily_return = (bag_portvals[1:] / bag_portvals[:-1].values) - 1
    bag_avg_daily_ret = bag_daily_return.mean()
    bag_std_daily_ret = bag_daily_return.std()

    benchmark_trades = benchmark(df_trades, symbol)
    benchmark_portvals = compute_portvals(benchmark_trades, start_val=sv, commission=commission,
                                          impact=impact)
    benchmark_cum_ret = benchmark_portvals.iloc[-1] / benchmark_portvals.iloc[0] - 1
    benchmark_daily_return = (benchmark_portvals[1:] / benchmark_portvals[:-1].values) - 1
    benchmark_avg_daily_ret = benchmark_daily_return.mean()
    benchmark_std_daily_ret = benchmark_daily_return.std()

    # Compare portfolio against $SPX
    print(f"Date Range: {start_date} to {end_date}")
    print()
    print(f"Cumulative Return of Manual Strategy Portfolio: {cum_ret}")
    print(f"Cumulative Return of StrategyLearner Portfolio: {bag_cum_ret}")
    print(f"Cumulative Return of Benchmark : {benchmark_cum_ret}")
    print()
    print(f"Standard Deviation of Manual Strategy Portfolio: {std_daily_ret}")
    print(f"Standard Deviation of StrategyLearner Portfolio: {bag_std_daily_ret}")
    print(f"Standard Deviation of Benchmark : {benchmark_std_daily_ret}")
    print()
    print(f"Average Daily Return of Manual Strategy Portfolio: {avg_daily_ret}")
    print(f"Average Daily Return of StrategyLearner Portfolio: {bag_avg_daily_ret}")
    print(f"Average Daily Return of Benchmark : {benchmark_avg_daily_ret}")
    print()
    print(f"Final Manual Strategy Portfolio Value: {portvals[-1]}")
    print(f"Final StrategyLearner Portfolio Value: {bag_portvals[-1]}")

    plt.figure()
    plt.title('experiment1_out-of-Sample Manual Strategy Portfolio vs StrategyLearner Portfolio vs Benchmark')
    plt.ylabel('Normalized Portfolio Value $')
    plt.xlabel('Time')

    plt.plot(portvals / portvals.iloc[0], color='red', label='Manual Strategy')
    plt.plot(bag_portvals / bag_portvals.iloc[0], color='blue', label='StrategyLearner')
    plt.plot(benchmark_portvals / benchmark_portvals.iloc[0], color='purple', label='benchmark')
    plt.legend()
    plt.savefig('images/experiment1_out-of-sample-compare.png')


def author():
  return 'zfeng305'