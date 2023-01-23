import numpy as np

from math import factorial

def combinations (k, n):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))