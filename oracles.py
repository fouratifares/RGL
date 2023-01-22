import numpy as np
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import warnings
from scipy.ndimage.filters import gaussian_filter
from matplotlib.pyplot import figure
from random import randint


# warnings.filterwarnings('ignore')

def oracle(arms):
    sigma = 0.1
    eps = np.random.normal(0, sigma, 1)
    if type(arms) == int:
        arms = list([arms])
#     arms = list(arms)
    input_set = set(arms)
    if input_set == set():
        return min(max(0.2 + eps,0),1)
    elif input_set == {1}:
        return min(max(0 + eps,0),1)
    elif input_set == {2}:
        return min(max(0.6 + eps,0),1)
    elif input_set == {1, 2}:
        return min(max(0.2 + eps,0),1)
    else:
        raise Exception(f"The input set was not expected: {input_set}")