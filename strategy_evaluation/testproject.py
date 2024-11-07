import datetime as dt
import matplotlib.pyplot as plt
from marketsimcode import compute_portvals
from ManualStrategy import ManualStrategy
from StrategyLearner import StrategyLearner
from experiment1 import experiment1
from experiment2 import experiment2

def benchmark(df_trades, symbol):
    benchmark_trades = df_trades.copy()
    benchmark_trades[symbol] = 0
    benchmark_trades.iloc[0] = [1000]
    return benchmark_trades
def draw_plot_manual_strategy(
        symbol="JPM",
        sv=100000):
    ms = ManualStrategy(impact=0.005, commission=9.95)
    df_trades = ms.testPolicy(symbol=symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=sv)
    draw_helper(df_trades, "In-Sample-ManualLearner VS Benchmark", sv, commission=9.95, impact=0.005,
                symbol=symbol)

    df_trades = ms.testPolicy(symbol=symbol, sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=sv)
    draw_helper(df_trades, "Out-of-Sample-ManualLearner VS Benchmark", sv, commission=9.95, impact=0.005,
                symbol=symbol)

def draw_helper(df_trades, plot_name, sv, commission, impact, symbol):
    portvals = compute_portvals(df_trades, start_val=sv, commission=commission, impact=impact)
    start_date, end_date = min(portvals.index), max(portvals.index)
    cum_ret = portvals.iloc[-1] / portvals.iloc[0] - 1
    daily_return = (portvals[1:] / portvals[:-1].values) - 1
    avg_daily_ret = daily_return.mean()
    std_daily_ret = daily_return.std()

    benchmark_trades = benchmark(df_trades, symbol)
    benchmark_portvals = compute_portvals(benchmark_trades, start_val=sv, commission=commission, impact=impact)
    benchmark_cum_ret = benchmark_portvals.iloc[-1] / benchmark_portvals.iloc[0] - 1
    benchmark_daily_return = (benchmark_portvals[1:] / benchmark_portvals[:-1].values) - 1
    benchmark_avg_daily_ret = benchmark_daily_return.mean()
    benchmark_std_daily_ret = benchmark_daily_return.std()
    # Compare portfolio against $SPX
    print(f"Date Range: {start_date} to {end_date}")
    print()
    print(f"Cumulative Return of Strategy Portfolio: {cum_ret}")
    print(f"Cumulative Return of Benchmark : {benchmark_cum_ret}")
    print()
    print(f"Standard Deviation of Strategy Portfolio: {std_daily_ret}")
    print(f"Standard Deviation of Benchmark : {benchmark_std_daily_ret}")
    print()
    print(f"Average Daily Return of Strategy Portfolio: {avg_daily_ret}")
    print(f"Average Daily Return of Benchmark : {benchmark_avg_daily_ret}")
    print()
    print(f"Final Strategy Portfolio Value: {portvals[-1]}")

    plt.figure()
    plt.title(plot_name)
    plt.ylabel('Normalized Portfolio Value $')
    plt.xlabel('Time')
    for day in df_trades.index:
        if df_trades.loc[day, symbol] > 0:
            plt.axvline(x=day, color="blue", linestyle="--", linewidth=0.5)
        elif df_trades.loc[day, symbol] < 0:
            plt.axvline(x=day, color="black", linestyle="--", linewidth=0.5)

    plt.plot(portvals / portvals.iloc[0], color='red', label='Manual Learner')
    plt.plot(benchmark_portvals / benchmark_portvals.iloc[0], color='purple', label='benchmark')
    plt.legend()
    plt.savefig('images/' + plot_name + '.png')

def author():
  return 'zfeng305'

def draw_plot_strategy_learner(
        symbol="JPM",
        sv=100000):
    sl = StrategyLearner(impact=0.005, commission=9.95)
    sl.add_evidence(symbol=symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31))
    bag_trades = sl.testPolicy(symbol=symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31))
    draw_helper(bag_trades, "In-Sample-StrategyLearner VS Benchmark", sv, commission=9.95, impact=0.005,
                symbol=symbol)
    bag_trades = sl.testPolicy(symbol=symbol, sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31))
    draw_helper(bag_trades, "Out-of-Sample-StrategyLearner VS Benchmark", sv, commission=9.95, impact=0.005,
                symbol=symbol)

if __name__ == "__main__":

    draw_plot_manual_strategy()
    draw_plot_strategy_learner()
    experiment1()
    experiment2()
