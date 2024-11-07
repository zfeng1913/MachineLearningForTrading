import numpy as np
from LinRegLearner import LinRegLearner
from BagLearner import BagLearner
class InsaneLearner(object):
    def __init__(self, verbose=False):
        self.learners = [BagLearner(learner=LinRegLearner, kwargs={}, bags=20, boost=False, verbose=False) for _ in range(20)]
    def author(self):
        return "zfeng305"  # replace tb34 with your Georgia Tech username
    def add_evidence(self, data_x, data_y):
        for i in range(20):
            self.learners[i].add_evidence(data_x, data_y)
    def query(self, points):
        ans = [self.learners[i].query(points) for i in range(20)]
        return np.mean(ans, axis=0)

if __name__ == "__main__":
    print("the secret clue is 'zzyzx'")
