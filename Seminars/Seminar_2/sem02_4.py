# Подбрасывают 4 одинаковые монеты. Какова вероятность, что решка выпадет не более 1 раза

import numpy as np
from math import factorial

p = 0.5
q = 1 - p
def combinations (k, n):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

bernoulli = (combinations(0, 4) * p ** 0 * q ** (4 - 0)) + (combinations(1, 4) * p ** 1 * q ** (4 - 1))
print(bernoulli)