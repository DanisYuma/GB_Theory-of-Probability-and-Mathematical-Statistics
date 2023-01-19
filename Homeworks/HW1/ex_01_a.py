# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# Найти вероятность того, что все карты – крести

import numpy as np

from math import factorial

def combinations (n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

m = (combinations(13, 4))
n = (combinations(52, 4))
p = m / n

print('{:.6f}'.format(p))