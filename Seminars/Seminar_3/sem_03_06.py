# Задача 4.Известно, что в принятой для сборки партии из 1000 деталей имеются 4 дефектных. 
# Найдите вероятность, что среди 50 случайно взятых деталей нет дефектных.

from formula import poison_m
from formula import bernoulli as ber
from math import factorial

n = 50
p = 4 / 1000
q = 1 - p
m = 0

a = poison_m(n, p, m)
b = ber(m, n, p, q)

print('{:.3f}'.format(a))
print('{:.3f}'.format(b))
