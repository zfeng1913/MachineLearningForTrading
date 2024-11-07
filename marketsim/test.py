from marketsim import compute_portvals
import pandas as pd

orders = pd.DataFrame({
    'Date' : ['2011-01-05', '2011-01-20'],
    'Symbol': ['AAPL'] * 2,
    'Order': ['BUY', 'SELL'],
    'Shares': [1500, 1500]
}
)
orders['Date'] = pd.to_datetime(orders['Date'])
print(compute_portvals(orders, 1000000))