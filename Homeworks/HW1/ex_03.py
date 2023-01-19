# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

import numpy as np

from math import factorial

def combinations (n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

m = (combinations(9, 3))
n = (combinations(15, 3))
p = m / n

print('{:.4f}'.format(p))