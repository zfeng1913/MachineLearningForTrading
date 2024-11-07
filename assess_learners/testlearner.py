""""""  		  	   		  		 			  		 			 	 	 		 		 	
"""  		  	   		  		 			  		 			 	 	 		 		 	
Test a learner.  (c) 2015 Tucker Balch  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
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
  		  	   		  		 			  		 			 	 	 		 		 	
import math  		  	   		  		 			  		 			 	 	 		 		 	
import sys  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
  		  	   		  		 			  		 			 	 	 		 		 	
import LinRegLearner as lrl
import BagLearner as bgl
import RTLearner as rtl
import DTLearner as dtl


def plot_start(title):
    plt.figure()
    plt.title(title)

    plt.xlabel('Leaf Size')

if __name__ == "__main__":  		  	   		  		 			  		 			 	 	 		 		 	
    if len(sys.argv) != 2:  		  	   		  		 			  		 			 	 	 		 		 	
        print("Usage: python testlearner.py <filename>")  		  	   		  		 			  		 			 	 	 		 		 	
        sys.exit(1)  		  	   		  		 			  		 			 	 	 		 		 	
    inf = open(sys.argv[1])
    data = np.array([s.strip().split(',')[1:] for s in inf.readlines()])
    if sys.argv[1] == "Data/Istanbul.csv":
        data = data[1:]
    data = data.astype('float')
  		  	   		  		 			  		 			 	 	 		 		 	
    # compute how much of the data is training and testing  		  	   		  		 			  		 			 	 	 		 		 	
    train_rows = int(0.6 * data.shape[0])  		  	   		  		 			  		 			 	 	 		 		 	
    test_rows = data.shape[0] - train_rows  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    # separate out training and testing data  		  	   		  		 			  		 			 	 	 		 		 	
    train_x = data[:train_rows, 0:-1]  		  	   		  		 			  		 			 	 	 		 		 	
    train_y = data[:train_rows, -1]  		  	   		  		 			  		 			 	 	 		 		 	
    test_x = data[train_rows:, 0:-1]  		  	   		  		 			  		 			 	 	 		 		 	
    test_y = data[train_rows:, -1]
  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"{test_x.shape}")  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"{test_y.shape}")  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    # create a learner and train it  		  	   		  		 			  		 			 	 	 		 		 	
    learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner  		  	   		  		 			  		 			 	 	 		 		 	
    learner.add_evidence(train_x, train_y)  # train it  		  	   		  		 			  		 			 	 	 		 		 	
    print(learner.author())  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    # evaluate in sample  		  	   		  		 			  		 			 	 	 		 		 	
    pred_y = learner.query(train_x)  # get the predictions  		  	   		  		 			  		 			 	 	 		 		 	
    rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  		  	   		  		 			  		 			 	 	 		 		 	
    print()  		  	   		  		 			  		 			 	 	 		 		 	
    print("In sample results")  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"RMSE: {rmse}")  		  	   		  		 			  		 			 	 	 		 		 	
    c = np.corrcoef(pred_y, y=train_y)  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"corr: {c[0,1]}")  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    # evaluate out of sample  		  	   		  		 			  		 			 	 	 		 		 	
    pred_y = learner.query(test_x)  # get the predictions  		  	   		  		 			  		 			 	 	 		 		 	
    rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		  		 			  		 			 	 	 		 		 	
    print()  		  	   		  		 			  		 			 	 	 		 		 	
    print("Out of sample results")  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"RMSE: {rmse}")  		  	   		  		 			  		 			 	 	 		 		 	
    c = np.corrcoef(pred_y, y=test_y)  		  	   		  		 			  		 			 	 	 		 		 	
    print(f"corr: {c[0,1]}")


    #experiment 1 test various dt models with different leaf size
    print('Experiment I ')
    plot_start("Experiment 1: Overfitting effect with leaf size")
    plt.ylabel('RMSE')
    leaves = range(1,51)
    in_sample_rmse = []
    out_of_sample_rmse = []

    for i in leaves:
        learner = dtl.DTLearner(leaf_size=i, verbose=True)  # create a LinRegLearner
        learner.add_evidence(train_x, train_y)  # train it
        # evaluate in sample
        pred_y = learner.query(train_x)  # get the predictions
        in_sample_rmse.append(math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0]))
        # evaluate out of sample
        pred_y = learner.query(test_x)  # get the predictions
        out_of_sample_rmse.append(math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0]))

    plt.plot(leaves, in_sample_rmse, label='in_sample_rmse')
    plt.plot(leaves, out_of_sample_rmse, label='out_of_sample_rmse')
    plt.legend()
    plt.savefig('images/Experiment1.png')

    # Experiment 2 Research and discuss the use of bagging and its effect on overfitting.
    plot_start("Experiment 2: Examine overfitting with bagging effect")
    plt.ylabel('RMSE')

    in_sample_rmse_bag = []
    out_of_sample_rmse_bag = []

    for i in leaves:
        learner = bgl.BagLearner(
            learner=dtl.DTLearner, kwargs={"leaf_size": i},
            bags=20, boost=False, verbose=False)
        learner.add_evidence(train_x, train_y)  # train it
        # evaluate in sample
        pred_y = learner.query(train_x)  # get the predictions
        in_sample_rmse_bag.append(math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0]))
        # evaluate out of sample
        pred_y = learner.query(test_x)  # get the predictions
        out_of_sample_rmse_bag.append(math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0]))

    plt.plot(leaves, in_sample_rmse, label='in_sample_rmse_dt')
    plt.plot(leaves, out_of_sample_rmse, label='out_of_sample_rmse_dt')
    plt.plot(leaves, in_sample_rmse_bag, label='in_sample_rmse_bag')
    plt.plot(leaves, out_of_sample_rmse_bag, label='out_of_sample_rmse_bag')
    plt.legend()
    plt.savefig('images/Experiment2.png')

    #Experiment 3

    #mean absolute error
    #time to train



    train_time_dt = []
    in_sample_mae_dt = []
    out_of_sample_mae_dt = []
    train_time_rt = []
    in_sample_mae_rt = []
    out_of_sample_mae_rt = []

    for i in leaves:
        learner = dtl.DTLearner(leaf_size=i, verbose=False)
        start = time.time()
        learner.add_evidence(train_x, train_y)  # train
        end = time.time()
        train_time_dt.append(end - start)
        # evaluate in sample
        pred_y = learner.query(train_x)  # get the predictions
        in_sample_mae_dt.append(np.mean(abs(train_y - pred_y)))
        # evaluate out of sample
        pred_y = learner.query(test_x)  # get the predictions
        out_of_sample_mae_dt.append(np.mean(abs(test_y - pred_y)))

    for i in leaves:
        learner = rtl.RTLearner(leaf_size=i, verbose=False)
        start = time.time()
        learner.add_evidence(train_x, train_y)  # train
        end = time.time()
        train_time_rt.append(end - start)
        # evaluate in sample
        pred_y = learner.query(train_x)  # get the predictions
        in_sample_mae_rt.append(np.mean(abs(train_y - pred_y)))
        # evaluate out of sample
        pred_y = learner.query(test_x)  # get the predictions
        out_of_sample_mae_rt.append(np.mean(abs(test_y - pred_y)))

    plot_start("Experiment 3: Comparison of mean absolute error")
    plt.ylabel('Mean Absolute Error')
    plt.plot(leaves, in_sample_mae_dt, label='in_sample_dt')
    plt.plot(leaves, out_of_sample_mae_dt, label='out_of_sample_dt')
    plt.plot(leaves, in_sample_mae_rt, label='in_sample_rt')
    plt.plot(leaves, out_of_sample_mae_rt, label='out_of_sample_rt')
    plt.legend()
    plt.savefig('images/Experiment3_mae.png')

    plot_start("Experiment 3: Comparison of train time")
    plt.ylabel('Time to train')
    plt.plot(leaves, train_time_dt, label='DT')
    plt.plot(leaves, train_time_rt, label='RT')
    # plt.plot(leaves, out_of_sample_mae_dt, label='out_of_sample_mae_dt')
    plt.legend()
    plt.savefig('images/Experiment3_train_time.png')





