# Найти среднее арифметическое для выборки:
#  77, 79, 67, 95, 87, 91, 98, 100, 104, 105
# Найти медиану
# Найти интерквартильное расстояние

import numpy as np

z = np.array([77, 79, 67, 95, 87, 91, 98, 100, 104, 105])
z.sort()
n = len(z)
k1 = 25
k3 = 75
# Медиана и квартили q1, m, q3 зависят от k и n. Необходимо найти целые значения j1, j2, j3 для формулы
q1 = n * k1 / 100 
j1 = int(q1)
j2 = int(n / 2)
q3 = n * k3 / 100
j3 = int(q3)

def median (n, j):
    if n % 2 == 0:
        return (z[j - 1] + z[j]) / 2
    else:
        return (z[j])

def quartile(q, j): 
    if q % 1 == 0:
        return (z[j - 1] + z[j]) / 2
    else:
        return (z[j])

interquartile = quartile(q3, j3) - quartile(q1, j1)

print(f'Среднее арифметическое равно {z.mean()}')
print(f'Медиана {median(n, j2)}')
print(f'Инквартильное расстояние равно {interquartile}')
