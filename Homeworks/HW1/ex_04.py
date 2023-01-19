# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

import numpy as np

from math import factorial

def combinations (n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

m = (combinations(2, 2))
n = (combinations(100, 2))
p = m / n

print('{:.8f}'.format(p))