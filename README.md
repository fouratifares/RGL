# RGL: Randomized Greedy Learning for Non-monotone Stochastic Submodular Maximization Under Full-bandit Feedback

We investigate the problem of unconstrained combinatorial multi-armed bandits with full-bandit feedback and stochastic rewards for submodular maximization. Previous works investigate the same problem assuming a submodular and monotone reward function. In this work, we study a more general problem, i.e., when the reward function is not necessarily monotone, and the submodularity is assumed only in expectation. We propose Randomized Greedy Learning (RGL) algorithm and theoretically prove that it achieves a -regret upper bound of  for horizon  and number of arms . We also show in experiments that RGL empirically outperforms other full-bandit variants in submodular and non-submodular settings.

Paper Link: https://proceedings.mlr.press/v206/fourati23a/fourati23a.pdf .

![alt text](https://github.com/fouratifares/RGL/blob/main/submodular_sum.png)

## Citing the Project

To cite this repository in publications:

```bibtex
@inproceedings{fourati2023randomized,
  title={Randomized greedy learning for non-monotone stochastic submodular maximization under full-bandit feedback},
  author={Fourati, Fares and Aggarwal, Vaneet and Quinn, Christopher and Alouini, Mohamed-Slim},
  booktitle={International Conference on Artificial Intelligence and Statistics},
  pages={7455--7471},
  year={2023},
  organization={PMLR}
}
```
