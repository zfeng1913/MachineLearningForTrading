""""""  		  	   		  		 			  		 			 	 	 		 		 	
"""Assess a betting strategy.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
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
GT User ID: zfeng305 (replace with your User ID)  		  	   		  		 			  		 			 	 	 		 		 	
GT ID: 903859012 (replace with your GT ID)  		  	   		  		 			  		 			 	 	 		 		 	
"""  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import numpy as np
import matplotlib.pyplot as plt
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def author():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The GT username of the student  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: str  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    return "zfeng305"  # replace tb34 with your Georgia Tech username.
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def gtid():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The GT ID of the student  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: int  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    return 903859012  # replace with your GT ID number
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def get_spin_result(win_prob):  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    :param win_prob: The probability of winning  		  	   		  		 			  		 			 	 	 		 		 	
    :type win_prob: float  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The result of the spin.  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: bool  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    result = False  		  	   		  		 			  		 			 	 	 		 		 	
    if np.random.random() <= win_prob:  		  	   		  		 			  		 			 	 	 		 		 	
        result = True  		  	   		  		 			  		 			 	 	 		 		 	
    return result  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	

def strategy():
    winning_series = np.empty(1001)

    episode_winnings = 0
    bet_time = 0
    winning_series[0] = 0
    while episode_winnings < 80 and bet_time < 1000:
        won = False
        bet_amount = 1
        while (not won) and (bet_time < 1000):
            won = get_spin_result(18/38)
            bet_time += 1
            if won:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2
            winning_series[bet_time] = episode_winnings
    winning_series[bet_time:] = winning_series[bet_time]
    return winning_series


def realistic_strategy():
    winning_series = np.empty(1001)
    episode_winnings = 0
    bet_time = 0
    winning_series[0] = 0
    while episode_winnings < 80 and bet_time < 1000 and episode_winnings > -256:
        won = False
        bet_amount = 1
        while (not won) and (bet_time < 1000):
            if episode_winnings - bet_amount < -256:
                bet_amount = episode_winnings + 256
            won = get_spin_result(18/38)
            bet_time += 1
            if won:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2
            winning_series[bet_time] = episode_winnings
    print(bet_time)
    winning_series[bet_time:] = winning_series[bet_time]

    return winning_series

def plot_start(title):
    plt.figure()
    plt.title(title)
    plt.ylim(ymax=100, ymin=-256)
    plt.xlim(xmax=300, xmin=0)
    plt.ylabel('Winnings amount in $')
    plt.xlabel('bets')

def test_code():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    Method to test your code  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    win_prob = 0.60  # set appropriately to the probability of a win  		  	   		  		 			  		 			 	 	 		 		 	
    np.random.seed(gtid())  # do this only once  		  	   		  		 			  		 			 	 	 		 		 	
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		  		 			  		 			 	 	 		 		 	
    # add your code here to implement the experiments
    plot_start('Experiment_1_Figure_1')
    for i in range(10):
        winning = strategy()
        plt.plot(winning)
    plt.savefig('images/figure_1.png')


    plot_start('Experiment_1_Figure_2')
    winnings = np.empty((1000, 1001))
    for i in range(1000):
        winnings[i] = strategy()
    winnings_mean = winnings.mean(axis=0)
    winnings_std = winnings.std(axis=0)
    plt.plot(winnings_mean, label='mean')
    plt.plot(winnings_mean + winnings_std, label='mean + std')
    plt.plot(winnings_mean - winnings_std, label='mean - std')

    plt.legend()
    plt.savefig('images/figure_2.png')

    plot_start('Experiment_1_Figure_3')
    winnings_median = np.median(winnings, axis=0)
    winnings_std = winnings.std(axis=0)
    plt.plot(winnings_median, label='median')
    plt.plot(winnings_median + winnings_std, label='median + std')
    plt.plot(winnings_median - winnings_std, label='median - std')
    plt.legend()
    plt.savefig('images/figure_3.png')

    plot_start('Experiment_2_Figure_1')
    winnings = np.empty((1000, 1001))
    for i in range(1000):
        winnings[i] = realistic_strategy()
    winnings_mean = winnings.mean(axis=0)
    winnings_std = winnings.std(axis=0)
    plt.plot(winnings_mean, label='mean')
    print(winnings_mean)
    plt.plot(winnings_mean + winnings_std, label='mean + std')
    plt.plot(winnings_mean - winnings_std, label='mean - std')
    plt.legend()
    plt.savefig('images/figure_4.png')

    plot_start('Experiment_2_Figure_2')
    winnings_median = np.median(winnings, axis=0)
    winnings_std = winnings.std(axis=0)
    plt.plot(winnings_median, label='median')
    plt.plot(winnings_median + winnings_std, label='median + std')
    plt.plot(winnings_median - winnings_std, label='median - std')
    plt.legend()
    plt.savefig('images/figure_5.png')

  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		  		 			  		 			 	 	 		 		 	
    test_code()  		  	   		  		 			  		 			 	 	 		 		 	
