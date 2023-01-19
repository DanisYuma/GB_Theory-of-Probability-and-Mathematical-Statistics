# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import numpy as np

from math import factorial

def combinations (n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

m = (combinations(48, 4))
n = (combinations(52, 4))
q = m / n                   # Обратная ситуация, когда тузов нету
p = 1 - q

print('{:.3f}'.format(p))