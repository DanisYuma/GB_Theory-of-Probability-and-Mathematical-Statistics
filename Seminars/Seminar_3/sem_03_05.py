# Найти среднее арифметическое для выборки:
#  77, 79, 67, 95, 87, 91, 98, 100, 104, 105
# Найти медиану
# Найти интерквартильное расстояние

import numpy as np
# from formula import median

z = np.array([77, 79, 67, 95, 87, 91, 98, 100, 104, 105])
z.sort()
n = len(z)
h = int(n / 2)

def median (n, h):
    if n % 2 == 0:
        return (z[h - 1] + z[h]) / 2
    else:
        return (z[h])

print(z.mean())
print(median(n, h))

# if n % 2 == 0:
#     a = (z[h - 1] + z[h]) / 2
# else:
#     a = (z[h])

# print(z)
# print(n)
# print(a)
