import numpy as np

from algorithms.bandits import OPT, ETCG, RGL, RND

import random

import config_parser as parser


def run_bandit():

    n = parser.args.n
    T = parser.args.T
    sol =parser.args.sol
    k =parser.args.k
    reps =parser.args.reps

    arms = list(np.arange(1, n + 1, 1))
    random.shuffle(arms)

    cumulative_rewardsOPT, rewardsOPT, best_arm_setOPT = OPT(T, sol)
    print('OPT: ', best_arm_setOPT)

    cumulative_rewardsETCG, rewardsETCG, Xi_ETCG = ETCG(n, T, k, arms)
    print('Xi_ETCG: ', Xi_ETCG)

    cumulative_rewardsRGL, rewardsRGL, Xi_RGL = RGL(n, T, arms)
    print('Xi_RGL: ', Xi_RGL)

    cumulative_rewardsRND, rewardsRND, Xi_RND = RND( T)
    print('Xi_RND: ', Xi_RND)

    array_cumulative_rewardsOPT = np.array(cumulative_rewardsOPT, dtype=float)
    array_rewardsOPT = np.array(rewardsOPT, dtype=float)

    array_cumulative_rewardsRGL = np.array(cumulative_rewardsRGL, dtype=float)
    array_rewardsRGL = np.array(rewardsRGL, dtype=float)

    array_cumulative_rewardsRND = np.array(cumulative_rewardsRND, dtype=float)
    array_rewardsRND = np.array(rewardsRND, dtype=float)

    array_cumulative_rewardsETCG = np.array(cumulative_rewardsETCG, dtype=float)
    array_rewardsETCG = np.array(rewardsETCG, dtype=float)


    for r in range(1, reps):

        random.shuffle(arms)

        cumulative_rewardsOPT, rewardsOPT, best_arm_setOPT = OPT(T, sol)
        print('OPT: ', best_arm_setOPT)

        cumulative_rewardsETCG, rewardsETCG, Xi_ETCG = ETCG(n, T, k, arms)
        print('Xi_ETCG: ', Xi_ETCG)

        cumulative_rewardsRGL, rewardsRGL, Xi_RGL = RGL(n, T, arms)
        print('Xi_RGL: ', Xi_RGL)

        cumulative_rewardsRND, rewardsRND, Xi_RND = RND(T)
        print('Xi_RND: ', Xi_RND)


        array_cumulative_rewardsOPT = np.vstack(
            [array_cumulative_rewardsOPT, np.array(cumulative_rewardsOPT, dtype=float)])
        array_rewardsOPT = np.vstack([array_rewardsOPT, np.array(rewardsOPT, dtype=float)])

        array_cumulative_rewardsETCG = np.vstack(
            [array_cumulative_rewardsETCG, np.array(cumulative_rewardsETCG, dtype=float)])
        array_rewardsETCG = np.vstack([array_rewardsETCG, np.array(rewardsETCG, dtype=float)])

        array_cumulative_rewardsRGL = np.vstack(
            [array_cumulative_rewardsRGL, np.array(cumulative_rewardsRGL, dtype=float)])
        array_rewardsRGL = np.vstack([array_rewardsRGL, np.array(rewardsRGL, dtype=float)])

        array_cumulative_rewardsRND = np.vstack(
            [array_cumulative_rewardsRND, np.array(cumulative_rewardsRND, dtype=float)])
        array_rewardsRND = np.vstack([array_rewardsRND, np.array(rewardsRND, dtype=float)])



if __name__ == '__main__':
    run_bandit()

