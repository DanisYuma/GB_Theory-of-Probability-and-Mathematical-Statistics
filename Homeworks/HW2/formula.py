import numpy as np

from math import factorial

def combinations (k, n):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

def bernoulli (k, n, p, q):
    return (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) * p ** k * q ** (n - k)

def poison_m (n, p, m):
    lamb = n * p
    e = 2.72
    return (lamb ** m / factorial(m)) * (e ** -m)