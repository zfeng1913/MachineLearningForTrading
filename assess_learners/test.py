from DTLearner import DTLearner
# from DTLearner import DTLearner
from RTLearner import RTLearner
from BagLearner import BagLearner
import pandas as pd
import numpy as np

data = pd.read_csv('Data/Istanbul.csv').drop(columns='date')
print(data.dtypes)
data_y = np.array(data.iloc[:,-1])
data_x = np.array(data.iloc[:, :-1])
a = DTLearner(leaf_size=1)
model = a.add_evidence(data_x, data_y)

# print(model)
print(a.query(np.array([[2,5,5,3,6,5,4,3]])))
2qwq