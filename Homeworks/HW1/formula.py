import numpy as np

from math import factorial

def combinations (n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))