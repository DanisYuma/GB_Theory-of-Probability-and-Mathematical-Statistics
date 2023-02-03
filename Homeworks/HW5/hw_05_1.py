# Ниже приведены диаметры коронарных артерий после приема нифедипина и плацебо. 
# Позволяют ли приводимые ниже данные утверждать, что нифедипин влияет на диаметр коронарных артерий?
# Выполнить расчеты в Python
# Сделайте расчет в ручную
# Сравните критерий Стьюдента и p-value со значениями, полученными в Python

import numpy as np
from scipy import stats as st

x = np.array([2.5, 2.2, 2.6, 2, 2.1, 1.8, 2.4, 2.3, 2.7, 2.7, 1.9])
y = np.array([2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2])

mean_x = np.mean(x)
mean_y = np.mean(y)
std = np.std(x, ddof=1)
length = len(x)

print(np.mean(x))
print(np.mean(y))
print(np.std(x, ddof=1))
print(len(x))

t = (mean_x - mean_y) / (std / np.sqrt(length))
print(t)