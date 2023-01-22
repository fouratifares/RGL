import numpy as np
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import warnings
from scipy.ndimage.filters import gaussian_filter
from matplotlib.pyplot import figure
from random import randint


def RND(n, T):
    cumulative_rewards = [0]
    rewards = [0]

    for _ in tqdm(range(1, T+1)):

        best_arm_set = [arm for arm in [1,2,] if random.random() < 1/2]
        reward = oracle(best_arm_set)
        rewards.append(reward)
        cumulative_rewards.append(cumulative_rewards[-1]+reward)
    return cumulative_rewards, rewards, best_arm_set


def ETCG(n, T, k, m, arms):

    cumulative_rewards = [0]
    rewards = [0]

    Xi_ = []

    t = 0
    # decide for each arm
    for _ in tqdm(range(0, k)):
        i_max = 0
        r_max = 0
        for i in tqdm(range(0, n)):
            exist = arms[i] in Xi_
            mean = 0
            if not exist:

                # estimate the probability
                for j in range(1, m + 1):
                    s = set(Xi_)
                    s.add(arms[i])
                    r = oracle(list(s))
                    mean += r / m
                    t += 1
                    if t == T + 1:
                        return cumulative_rewards, rewards, Xi_
                    cumulative_rewards.append(cumulative_rewards[-1] + r)
                    rewards.append(float(r))

                if mean >= r_max:
                    r_max = mean
                    i_max = i
        Xi_.append(arms[i_max])

    # exploit until T
    time_ = t + 1

    for _ in range(time_, T + 1):
        cumulative_rewards.append(cumulative_rewards[-1] + oracle(Xi_))
        rewards.append(float(oracle(Xi_)))
        t += 1
        if t == T:
            return cumulative_rewards, rewards, Xi_

    return cumulative_rewards, rewards, Xi_


def RGL(n, T, arms):
    print('RGL')
    cumulative_rewards = [0]
    rewards = [0]
    m = f(T)
    Xi_ = []
    Yi_ = arms.copy()
    t = 0

    # decide for each arm
    for i in tqdm(range(0, n)):
        ai = 0
        bi = 0

        # estimate the probability
        for j in range(1, m + 1):
            r1 = oracle(Xi_)
            t += 1
            if t == T + 1:
                return cumulative_rewards, rewards, Xi_
            s = set(Xi_)
            s.add(arms[i])
            r2 = oracle(list(s))
            t += 1
            if t == T + 1:
                return cumulative_rewards, rewards, Xi_
            cumulative_rewards.append(cumulative_rewards[-1] + r1)
            rewards.append(float(r1))
            cumulative_rewards.append(cumulative_rewards[-1] + r2)
            rewards.append(float(r2))
            ai += (r2 - r1)

            r1 = oracle(Yi_)
            t += 1
            if t == T + 1:
                return cumulative_rewards, rewards, Xi_
            s = set(Yi_)
            s = s - set([arms[i]])
            r2 = oracle(list(s))
            t += 1
            if t == T + 1:
                return cumulative_rewards, rewards, Xi_
            cumulative_rewards.append(cumulative_rewards[-1] + r1)
            rewards.append(float(r1))
            cumulative_rewards.append(cumulative_rewards[-1] + r2)
            rewards.append(float(r2))
            bi += (r2 - r1)

        ai_prime = max(ai / m, 0)
        bi_prime = max(bi / m, 0)

        # decide probabilistically
        if ai_prime == bi_prime:
            if ai_prime == 0:
                p = 1
        else:
            p = ai_prime / (ai_prime + bi_prime)

        if np.random.uniform(0, 1) < p:
            Xi_.append(arms[i])
        else:
            Yi_.remove(arms[i])

    # exploit until T
    time_ = int(4 * n * m + 1)
    for _ in range(time_, T + 1):
        cumulative_rewards.append(cumulative_rewards[-1] + oracle(Xi_))
        rewards.append(float(oracle(Xi_)))
        t += 1
        if t == T:
            return cumulative_rewards, rewards, Xi_

    return cumulative_rewards, rewards, Xi_