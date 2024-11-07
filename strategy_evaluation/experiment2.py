import datetime as dt
import matplotlib.pyplot as plt
from marketsimcode import compute_portvals
from StrategyLearner import StrategyLearner

def experiment2(symbol='JPM', sv=100000):
    res = {}
    for impact in [0.005, 0.01, 0.05, 0.1, 0.2]:
        sl = StrategyLearner(impact=impact)
        sl.add_evidence(symbol=symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31))
        bag_trades = sl.testPolicy(symbol=symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31))
        portvals = compute_portvals(bag_trades, start_val=sv, commission=9.95, impact=impact)
        cum_ret = portvals.iloc[-1] / portvals.iloc[0] - 1
        daily_return = (portvals[1:] / portvals[:-1].values) - 1
        avg_daily_ret = daily_return.mean()
        std_daily_ret = daily_return.std()
        res[str(impact)] = portvals
        print("impact_value: ", impact)
        print('cum_return: ', cum_ret)
        print('avg_daily_ret: ', avg_daily_ret)
        print('std_daily_ret: ', std_daily_ret)



    plt.figure()
    plt.title('experiment2_StrategyLearner Portfolio vs different impact values')
    plt.ylabel('Normalized Portfolio Value $')
    plt.xlabel('Time')
    for impact, ts in res.items():
        plt.plot(ts / ts.iloc[0], label=impact)

    plt.legend()
    plt.savefig('images/experiment2.png')
