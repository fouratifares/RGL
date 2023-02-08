import numpy as np


def average_signal(y, window = 5):
    average_y = []
    for ind in range(len(y) - window + 1):
        average_y.append(np.mean(y[ind:ind+window]))
    return average_y


def cumulative_regret(cumulative_rewardsRGL, cumulative_rewards):
    return np.array(cumulative_rewards) - np.array(cumulative_rewardsRGL)


def f(T):
    return int((T*np.sqrt((25/32)*np.log(T)))**(2/3)) + 1


def g(T, n, k):
    num = T*np.sqrt(2*np.log(T))
    den = n + 2*n*k*np.sqrt(2*np.log(T))
    v = num/den
    return int(v**(2/3))+1