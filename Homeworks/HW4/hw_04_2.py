# О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.

d = 0.2
a = 0.5
# d = (b - a) ** 2 / 12     # d * 12 = (b - a) ** 2     # ((d * 12) ** (1/2) / a) = b

b = ((d * 12) ** (1/2) / a)
m = (b + a) / 2

print('{:.1f}'.format(b))
print('{:.1f}'.format(m))
