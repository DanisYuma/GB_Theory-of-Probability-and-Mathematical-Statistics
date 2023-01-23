# Вероятность события А в каждом независимом испытании 0.0015. 
# Какова вероятность того, что при 2000 испытаниях событие А появится 3 раза.

import numpy as np
from math import factorial

n = 2000
p = 0.0015
m = 3
e = 2.72

lamb = n * p
poisson_m = (lamb ** m / factorial(m)) * (e ** -m)
print('{:.3f}'.format(poisson_m))