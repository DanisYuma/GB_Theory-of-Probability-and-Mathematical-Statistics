# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from formula import bernoulli as b

p = 0.5
n = 144
q = 1 - p
k = 70

print('{:.4f}'.format(b(k, n, p, q)))