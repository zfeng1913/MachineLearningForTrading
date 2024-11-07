""""""
"""  		  	   		  		 			  		 			 	 	 		 		 	
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		  	   		  		 			  		 			 	 	 		 		 	

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
"""

import numpy as np


class RTLearner(object):
    """
    This is a Linear Regression Learner. It is implemented correctly.

    :param verbose: If “verbose” is True, your code can print out information for debugging.
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.
    :type verbose: bool
    """

    def __init__(self, leaf_size=1, verbose=False):
        """
        Constructor method
        """
        self.leaf_size = leaf_size
        self.verbose = verbose

    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "zfeng305"  # replace tb34 with your Georgia Tech username

    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """
        self.tree = self.build_tree(data_x, data_y)

    def build_tree(self, data_x, data_y):
        if data_x.shape[0] <= self.leaf_size:
            return np.array([[-1, np.mean(data_y), np.nan, np.nan]])
        if len(np.unique(data_y)) == 1:
            return np.array([[-1, np.mean(data_y), np.nan, np.nan]])

        i = np.random.randint(data_x.shape[1])

        SplitVal = np.median(data_x[:, i])
        if len(data_x[data_x[:, i] > SplitVal]) == 0:
            return np.array([[-1, np.mean(data_y), np.nan, np.nan]])

        left_tree = self.build_tree(data_x[data_x[:, i] <= SplitVal], data_y[data_x[:, i] <= SplitVal])
        right_tree = self.build_tree(data_x[data_x[:, i] > SplitVal], data_y[data_x[:, i] > SplitVal])
        root = np.array([[i, SplitVal, 1, len(left_tree) + 1]])
        return np.concatenate((root, left_tree, right_tree))

    def query(self, points):
        if self.verbose:
            pass
        return np.array([self.predict(point, 0) for point in points])

    def predict(self, point, row):
        row = int(float(row))
        current_feature, SplitVal, left_row, right_row = self.tree[row, :]
        current_feature = int(float(current_feature))
        if current_feature == -1:
            return SplitVal
        if point[current_feature] <= SplitVal:
            return self.predict(point, row + left_row)
        else:
            return self.predict(point, row + right_row)


if __name__ == "__main__":
    print("the secret clue is 'zzyzx'")
